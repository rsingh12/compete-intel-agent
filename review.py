"""
review.py — the iteration loop.

Reading a brief and thinking "that was a bit thin" is not iteration. This turns
each week's read into a labelled record, and attributes every failure to the
stage that caused it, because the fix is completely different depending:

  COLLECT  miss -> source registry or normalize() is wrong. Code fix.
  TRIAGE   miss -> the cheap model dropped something real. Prompt/tier fix.
  ANALYST  miss -> it had the facts and drew the wrong conclusion. Prompt fix.

Without that attribution you will spend six weeks tuning the analyst prompt to
fix a problem that was a broken CSS selector.

  python review.py briefs/gcp-brief-2026-07-20.md     # label a brief
  python review.py --report                           # where is it failing
"""

import argparse
import json
import pathlib
import re
import sys
from collections import Counter
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).parent
LABELS = ROOT / "state" / "reviews.jsonl"

VERDICTS = {
    "1": ("keep", "Correct and useful — I would send this to a seller"),
    "2": ("thin", "Right item, analysis too shallow to act on"),
    "3": ("wrong", "Factually wrong or the 'so what' does not follow"),
    "4": ("noise", "Should never have survived triage"),
}

STAGES = {
    "1": "collect",
    "2": "triage",
    "3": "analyst",
}


def items(brief: str) -> list[tuple[str, str]]:
    """Split a brief into (section, item) pairs."""
    out, section = [], "?"
    for line in brief.splitlines():
        if line.startswith("## "):
            section = line[3:].strip()
        elif re.match(r"\s*[-*]\s+\S", line) and len(line) > 40:
            out.append((section, line.strip("-* ").strip()))
    return out


def label(path: pathlib.Path) -> None:
    brief = path.read_text()
    rows = items(brief)
    if not rows:
        sys.exit(f"No labelable items found in {path}")

    print(f"\n{len(rows)} items in {path.name}. 1=keep 2=thin 3=wrong 4=noise "
          f"s=skip q=quit\n")
    records = []
    for i, (section, text) in enumerate(rows, 1):
        print(f"\n[{i}/{len(rows)}] ({section})\n  {text[:400]}")
        v = input("  verdict> ").strip().lower()
        if v == "q":
            break
        if v not in VERDICTS:
            continue
        verdict = VERDICTS[v][0]
        stage = ""
        if verdict in ("wrong", "noise", "thin"):
            print("  blame: 1=collect 2=triage 3=analyst")
            stage = STAGES.get(input("  stage> ").strip(), "")
        note = input("  note (optional)> ").strip()
        records.append({
            "brief": path.name,
            "section": section,
            "item": text,
            "verdict": verdict,
            "stage": stage,
            "note": note,
            "labelled_at": datetime.now(timezone.utc).isoformat(),
        })

    # The recall question. Everything above measures what the pipeline
    # produced. This measures what it failed to produce, which is the failure
    # mode you cannot see by reading the output.
    print("\nWhat did Google do this week that this brief missed?")
    print("(one per line, blank to finish — leave empty if nothing)")
    while (miss := input("  missed> ").strip()):
        print("  blame: 1=collect 2=triage 3=analyst")
        records.append({
            "brief": path.name,
            "section": "MISSED",
            "item": miss,
            "verdict": "missed",
            "stage": STAGES.get(input("  stage> ").strip(), ""),
            "note": "",
            "labelled_at": datetime.now(timezone.utc).isoformat(),
        })

    LABELS.parent.mkdir(exist_ok=True)
    with LABELS.open("a") as f:
        for r in records:
            f.write(json.dumps(r) + "\n")
    print(f"\nWrote {len(records)} labels to {LABELS}")


def report() -> None:
    if not LABELS.exists():
        sys.exit("No reviews yet.")
    rows = [json.loads(l) for l in LABELS.read_text().splitlines() if l.strip()]
    by_brief = sorted({r["brief"] for r in rows})

    print(f"\n{len(rows)} labels across {len(by_brief)} briefs\n")

    print("Signal quality by brief (keep-rate):")
    for b in by_brief:
        rs = [r for r in rows if r["brief"] == b and r["verdict"] != "missed"]
        if not rs:
            continue
        keep = sum(r["verdict"] == "keep" for r in rs)
        bar = "#" * round(20 * keep / len(rs))
        print(f"  {b:<28} {keep:>2}/{len(rs):<3} {bar}")

    print("\nFailures by stage — fix the tallest bar, not the loudest one:")
    blame = Counter(r["stage"] for r in rows
                    if r["verdict"] != "keep" and r["stage"])
    for stage, n in blame.most_common():
        print(f"  {stage:<10} {n:>3}  {'#' * n}")

    print("\nFailure mix:")
    for v, n in Counter(r["verdict"] for r in rows).most_common():
        print(f"  {v:<10} {n:>3}")

    misses = [r for r in rows if r["verdict"] == "missed"]
    if misses:
        print(f"\nRecall gaps ({len(misses)}) — these matter more than precision.")
        print("A brief full of true-but-minor items still loses you the deal")
        print("if it missed the price cut.")
        for r in misses[-8:]:
            print(f"  [{r['stage'] or '?':<8}] {r['item'][:90]}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("brief", nargs="?")
    ap.add_argument("--report", action="store_true")
    a = ap.parse_args()
    if a.report:
        report()
    elif a.brief:
        label(pathlib.Path(a.brief))
    else:
        ap.print_help()
