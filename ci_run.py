"""
GCP competitive-intelligence pipeline for an AWS field team.

Architecture (deliberately three stages, not one big agent):

  1. COLLECT  - deterministic Python. Fetch, normalize, hash, diff. No model.
  2. TRIAGE   - cheap model pass. Is this change material? Tier-aware.
  3. ANALYZE  - Agent SDK subagent. Only sees changes that survived triage.

The split matters. Letting a model do the fetching burns tokens on
unchanged bytes and makes runs non-reproducible. Deterministic diffing means
the same input always produces the same candidate set, which is what lets you
trust a scheduled run you did not watch.

Run:  python ci_run.py --since 7d
"""

import argparse
import asyncio
import hashlib
import json
import pathlib
import re
import sys
from datetime import datetime, timezone

import httpx
import yaml
from claude_agent_sdk import (
    AgentDefinition,
    ClaudeAgentOptions,
    query,
)

ROOT = pathlib.Path(__file__).parent
STATE = ROOT / "state"
BRIEFS = ROOT / "briefs"
MODEL_TRIAGE = "claude-haiku-4-5-20251001"
MODEL_ANALYST = "claude-opus-4-8"


# ---------------------------------------------------------------- 1. COLLECT

def normalize(html: str) -> str:
    """Strip the parts of a page that change on every load.

    Without this, ~40% of your 'changes' are session IDs, timestamps, and
    rotating hero copy. This function is where most of the real engineering
    lives, and it is source-specific in production.
    """
    text = re.sub(r"<script.*?</script>", " ", html, flags=re.S | re.I)
    text = re.sub(r"<style.*?</style>", " ", text, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\b[0-9a-f]{16,}\b", "", text)          # cache-busting hashes
    text = re.sub(r"\d{4}-\d{2}-\d{2}T[\d:.+Z-]+", "", text)  # timestamps
    return re.sub(r"\s+", " ", text).strip()


def fetch(source: dict) -> dict:
    r = httpx.get(source["url"], timeout=30, follow_redirects=True,
                  headers={"User-Agent": "ci-monitor/1.0"})
    r.raise_for_status()
    body = normalize(r.text)
    return {
        "id": source["id"],
        "tier": source["tier"],
        "url": source["url"],
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "sha": hashlib.sha256(body.encode()).hexdigest(),
        "body": body,
    }


def diff_against_state(snap: dict) -> dict | None:
    """Return a change record, or None if nothing moved."""
    path = STATE / f"{snap['id']}.json"
    if not path.exists():
        path.write_text(json.dumps(snap))
        return None                      # first run = baseline, never a finding
    prior = json.loads(path.read_text())
    if prior["sha"] == snap["sha"]:
        return None
    added = _added_segments(prior["body"], snap["body"], snap.get("watch", []))
    path.write_text(json.dumps(snap))
    if not added:
        return None                      # bytes moved, meaning did not
    return {
        "id": snap["id"],
        "tier": snap["tier"],
        "url": snap["url"],
        "prior_seen": prior["fetched_at"],
        "added": added[:60],
    }


def _added_segments(old: str, new: str, watch: list[str]) -> list[str]:
    old_sents = set(re.split(r"(?<=[.!?])\s+", old))
    out = []
    for s in re.split(r"(?<=[.!?])\s+", new):
        if s in old_sents or len(s) < 40:
            continue
        # watch terms boost, but do not gate — novel language matters too
        out.append(s)
    watched = [s for s in out if any(w.lower() in s.lower() for w in watch)]
    return watched + [s for s in out if s not in watched]


# ---------------------------------------------------------------- 2. TRIAGE

TRIAGE_PROMPT = """You are triaging raw diffs from a Google Cloud source for an
AWS competitive intelligence pipeline. For each numbered item, output one line:

<number>|KEEP|<12-word reason>   or   <number>|DROP|<12-word reason>

KEEP only if the change plausibly affects an AWS enterprise deal: pricing,
GA/deprecation, capacity or region availability, contractual terms, a named
customer win, or a capability AWS does not have a public equivalent for.
DROP editorial rewrites, navigation changes, event promos, and restated
existing capabilities. Tier 1 sources get benefit of the doubt; tier 3 must
clear a high bar. Output nothing else."""


async def triage(change: dict) -> dict:
    numbered = "\n".join(f"{i+1}. {s}" for i, s in enumerate(change["added"]))
    verdicts = []
    async for msg in query(
        prompt=f"Source tier {change['tier']} ({change['id']}):\n{numbered}",
        options=ClaudeAgentOptions(
            model=MODEL_TRIAGE,
            system_prompt=TRIAGE_PROMPT,
            allowed_tools=[],            # triage is pure judgment, no tools
            max_turns=1,
        ),
    ):
        for block in getattr(msg, "content", []) or []:
            if getattr(block, "text", None):
                verdicts.append(block.text)
    kept = [
        change["added"][int(m.group(1)) - 1]
        for line in "\n".join(verdicts).splitlines()
        if (m := re.match(r"\s*(\d+)\|KEEP\|", line))
        and int(m.group(1)) <= len(change["added"])
    ]
    return {**change, "added": kept}


# ---------------------------------------------------------------- 3. ANALYZE

async def analyze(changes: list[dict], registry: dict) -> str:
    payload = ROOT / "state" / "_candidates.json"
    payload.write_text(json.dumps(
        {"changes": changes, "battlecard_map": registry["battlecard_map"]},
        indent=2))

    out = []
    async for msg in query(
        prompt=(
            "Read state/_candidates.json and sources/gcp.yaml. Produce this "
            "week's Google Cloud competitive brief for the AWS field team. "
            "Delegate the analysis to the gcp-analyst subagent."
        ),
        options=ClaudeAgentOptions(
            model=MODEL_ANALYST,
            cwd=str(ROOT),
            allowed_tools=["Read", "Grep", "Glob", "Agent"],
            setting_sources=["project"],   # loads agents/ and CLAUDE.md
            agents={
                "gcp-analyst": AgentDefinition(
                    description=("Turns diffed Google Cloud changes into "
                                 "AWS-seller-facing analysis."),
                    prompt=(ROOT / "agents" / "analyst.md").read_text(),
                    tools=["Read", "Grep", "Glob"],
                ),
            },
            max_turns=20,
        ),
    ):
        for block in getattr(msg, "content", []) or []:
            if getattr(block, "text", None):
                out.append(block.text)
    return "\n".join(out)


# ---------------------------------------------------------------- ORCHESTRATE

async def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true",
                    help="collect and diff only; no model calls")
    args = ap.parse_args()

    registry = yaml.safe_load((ROOT / "sources" / "gcp.yaml").read_text())
    STATE.mkdir(exist_ok=True)
    BRIEFS.mkdir(exist_ok=True)

    raw = []
    for src in registry["sources"]:
        try:
            snap = fetch(src) | {"watch": src.get("watch", [])}
        except Exception as e:                     # a dead source is itself signal
            print(f"[fetch-fail] {src['id']}: {e}", file=sys.stderr)
            continue
        if (change := diff_against_state(snap)):
            raw.append(change)

    print(f"[collect] {len(raw)} sources changed of {len(registry['sources'])}")
    if args.dry_run or not raw:
        return 0

    triaged = [c for c in await asyncio.gather(*(triage(c) for c in raw))
               if c["added"]]
    print(f"[triage] {len(triaged)} sources survived")
    if not triaged:
        return 0

    brief = await analyze(triaged, registry)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    path = BRIEFS / f"gcp-brief-{stamp}.md"
    path.write_text(brief)
    print(f"[write] {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
