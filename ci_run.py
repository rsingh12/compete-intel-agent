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
import os
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

# Triage is pure judgment on short text with no tools -- the "lower end of
# tasks" the README calls out as ideal for a cheap model. That also makes it
# a fit for a local model on home GPU hardware instead of a paid API call.
# Only reachable from a run on the same LAN as the Ollama host (e.g. the
# systemd timer in deploy/), not from the cloud-hosted scheduled routines.
TRIAGE_BACKEND = os.environ.get("TRIAGE_BACKEND", "claude")   # "claude" | "ollama"
OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://192.168.86.78:11434")
OLLAMA_MODEL_TRIAGE = os.environ.get("OLLAMA_MODEL_TRIAGE", "gpt-oss:20b")

# SEC EDGAR's fair-access policy (sec.gov/os/accessing-edgar-data) rejects
# requests with no identifying User-Agent -- a generic tool name is not
# enough, it 403s the same as no header at all. This one string fixes that
# source outright; it's harmless to send to every other source too.
USER_AGENT = os.environ.get(
    "CI_USER_AGENT", "compete-intel-agent ravinder.dell.singh@gmail.com")

# Fallback for sources that block direct fetches outright (e.g. a site that
# blocks the runner's IP range rather than anything about the request) --
# not a fit for every 403, only ones a header change can't fix. Perplexity
# fetches from its own infrastructure, not this machine's egress path, so it
# can reach a page this machine can't. The trade-off: it returns synthesized
# text, not the raw page, so a diff against a prior *direct* fetch will read
# as "changed" once on the switchover even if nothing moved -- flagged in
# the snapshot so triage/analyst can weight it accordingly.
PERPLEXITY_API_KEY = os.environ.get("PERPLEXITY_API_KEY", "")
PERPLEXITY_MODEL = os.environ.get("PERPLEXITY_MODEL", "sonar")


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


def _fetch_direct(url: str) -> str:
    r = httpx.get(url, timeout=30, follow_redirects=True,
                  headers={"User-Agent": USER_AGENT})
    r.raise_for_status()
    return r.text


def _fetch_via_perplexity(url: str) -> str:
    r = httpx.post(
        "https://api.perplexity.ai/chat/completions",
        headers={"Authorization": f"Bearer {PERPLEXITY_API_KEY}"},
        json={
            "model": PERPLEXITY_MODEL,
            "messages": [{
                "role": "user",
                "content": (
                    f"Fetch the current content at this exact URL: {url}\n"
                    "Return only the page's substantive text, as close to "
                    "verbatim as you can get it. No summary, no commentary, "
                    "no added formatting."
                ),
            }],
        },
        timeout=60,
    )
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]


def fetch(source: dict) -> dict:
    fetch_method = "direct"
    try:
        html = _fetch_direct(source["url"])
    except httpx.HTTPStatusError:
        if not PERPLEXITY_API_KEY:
            raise
        html = _fetch_via_perplexity(source["url"])
        fetch_method = "perplexity_fallback"
        print(f"[fetch-fallback] {source['id']}: direct fetch blocked, used Perplexity",
              file=sys.stderr)
    body = normalize(html)
    return {
        "id": source["id"],
        "tier": source["tier"],
        "url": source["url"],
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "sha": hashlib.sha256(body.encode()).hexdigest(),
        "fetch_method": fetch_method,
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


def _parse_verdicts(text: str, added: list[str]) -> list[str]:
    return [
        added[int(m.group(1)) - 1]
        for line in text.splitlines()
        if (m := re.match(r"\s*(\d+)\|KEEP\|", line))
        and int(m.group(1)) <= len(added)
    ]


async def triage_claude(change: dict) -> dict:
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
    return {**change, "added": _parse_verdicts("\n".join(verdicts), change["added"])}


async def triage_ollama(change: dict) -> dict:
    numbered = "\n".join(f"{i+1}. {s}" for i, s in enumerate(change["added"]))
    async with httpx.AsyncClient(timeout=120) as client:
        r = await client.post(
            f"{OLLAMA_HOST}/api/chat",
            json={
                "model": OLLAMA_MODEL_TRIAGE,
                "messages": [
                    {"role": "system", "content": TRIAGE_PROMPT},
                    {"role": "user",
                     "content": f"Source tier {change['tier']} ({change['id']}):\n{numbered}"},
                ],
                "stream": False,
            },
        )
        r.raise_for_status()
    verdict_text = r.json()["message"]["content"]
    return {**change, "added": _parse_verdicts(verdict_text, change["added"])}


def triage_fn():
    if TRIAGE_BACKEND == "ollama":
        return triage_ollama
    return triage_claude


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
    global TRIAGE_BACKEND
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true",
                    help="collect and diff only; no model calls")
    ap.add_argument("--triage-backend", choices=["claude", "ollama"],
                    default=TRIAGE_BACKEND,
                    help="model backend for triage (default: $TRIAGE_BACKEND or claude)")
    args = ap.parse_args()
    TRIAGE_BACKEND = args.triage_backend

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

    fn = triage_fn()
    triaged = [c for c in await asyncio.gather(*(fn(c) for c in raw))
               if c["added"]]
    print(f"[triage backend={TRIAGE_BACKEND}] {len(triaged)} sources survived")
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
