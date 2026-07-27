# compete-intel-agent

A scheduled competitive-intelligence pipeline built on the Claude Agent SDK.
It monitors a competitor's public surfaces on a schedule and produces a weekly
brief written for a specific home-team audience — not a news digest, but
seller-facing analysis that answers "so what for the deal."

The first configured target is **Google Cloud**, written for an **AWS** field
team (`sources/gcp.yaml`). The pipeline itself is competitor-agnostic: point it
at a different registry and battlecard map and it runs unchanged.

Runs unattended. Designed to be iterated on, not just deployed — see
`review.py`.

## Why three stages instead of one agent

Most agent demos hand the model a URL list and a prompt. That works once, in a
recording. It fails on a schedule for three reasons, and each stage here exists
to fix one of them.

**Collection is deterministic Python, not a model.** Pages change on every load
— session tokens, rotating hero copy, build hashes. A model asked "what changed"
will dutifully report all of it. `normalize()` strips the volatile layer before
hashing, so the diff is against meaning rather than bytes. This is unglamorous
and it is where most of the actual work is.

**Triage runs on a cheap model with no tools.** Its only job is to decide what
survives. Running the expensive model over every diff is how a monitoring
pipeline becomes a line item somebody kills. Tier-aware: a pricing page gets the
benefit of the doubt, a marketing blog has to earn its place.

**Analysis runs in an isolated subagent context.** The analyst never sees the
raw scrape — only what survived triage. Context isolation is the point: the
analyst's judgment is not polluted by 4,000 lines of stripped nav markup.

## The part that isn't the plumbing

`sources/gcp.yaml` carries a `battlecard_map`. Every theme Google can move on
maps to the AWS service it pressures. That mapping is the difference between a
news digest and competitive intelligence — it is what lets the brief answer
"so what for the deal" instead of "here is what Google announced."

The analyst prompt (`agents/analyst.md`) enforces two rules that most AI-written
competitive content violates: it separates *what changed* from *what it means*,
and it requires an honest concession alongside every counter-position. A
battlecard that admits nothing is a battlecard the field stops opening.

## Baseline behavior

First run on any source writes state and reports nothing. A monitoring system
that treats its cold start as a hundred urgent findings trains its readers to
ignore it in week one.

## Run

    pip install claude-agent-sdk httpx pyyaml
    python ci_run.py --dry-run     # collect + diff, no model calls
    python ci_run.py

Cron:

    0 6 * * 1 cd /path/gcp-ci && python ci_run.py >> run.log 2>&1

## Extending

- Swap `sources/gcp.yaml` for `azure.yaml`, `oracle.yaml` — the pipeline is
  competitor-agnostic; only the registry and battlecard map change.
- Add an MCP server (Slack, Gmail) to the analyze stage to route the brief.
- Add a `PostToolUse` hook to log every fetch for audit — useful when the brief
  gets challenged and you need to show provenance.
- Triage (the cheap-model stage) can run against a local Ollama endpoint
  instead of Claude Haiku — set `TRIAGE_BACKEND=ollama` (plus `OLLAMA_HOST`
  and `OLLAMA_MODEL_TRIAGE` if not using the defaults in `ci_run.py`) or pass
  `--triage-backend ollama`. Only works for a run on the same LAN as the
  Ollama host; the cloud-scheduled routines can't reach it.
