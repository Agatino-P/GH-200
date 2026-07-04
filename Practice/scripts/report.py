#!/usr/bin/env python3
"""Aggregate attempts.jsonl into a markdown progress report.

Sections: per-session scores (raw + adjusted per protocol §4.17, vs the 77%
readiness target), questions failed most recently, exclusion preview for
make_session.py --exclude-recent-correct, and the full per-question history.

Usage:
    report.py [--attempts PATH] [-o report.md]      # default: stdout
"""

import argparse
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.dirname(SCRIPT_DIR)  # Practice/ — attempts.jsonl lives here
sys.path.insert(0, SCRIPT_DIR)

from quiz_log import SCOREABLE, history_by_qid, load_attempts, recently_correct

DEFAULT_ATTEMPTS = os.path.join(DATA_DIR, "attempts.jsonl")
TARGET = 0.77
MARK = {"correct": "✓", "incorrect": "✗", "void": "V", "gap": "G", "excluded": "E"}


def pct(num, den):
    return f"{100 * num / den:.0f}%" if den else "—"


def qnum(qid):
    return int(qid[1:])


def session_rows(attempts):
    sessions = {}
    order = []
    for a in attempts:
        if a["session"] not in sessions:
            order.append(a["session"])
        sessions.setdefault(a["session"], []).append(a)

    rows = []
    for sid in order:
        recs = sessions[sid]
        scored = [r for r in recs if r["result"] in SCOREABLE]
        raw = sum(1 for r in scored if r["result"] == "correct")
        misses = [r for r in scored if r["result"] == "incorrect"]
        buckets = {}
        for r in misses:
            key = r["bucket"] or "?"
            buckets[key] = buckets.get(key, 0) + 1
        bd = sum(1 for r in misses if r["bucket"] in ("b", "d"))
        denom = len(scored) - bd
        date = min(r["ts"] for r in recs)[:10]
        bucket_str = " ".join(f"({k})×{buckets[k]}" for k in sorted(buckets)) or "—"
        adj = raw / denom if denom else 0
        rows.append((sid, date, len(recs), len(scored), f"{raw}/{len(scored)}",
                     pct(raw, len(scored)), f"{raw}/{denom}", pct(raw, denom),
                     "✅" if adj >= TARGET else "❌", bucket_str))
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--attempts", default=DEFAULT_ATTEMPTS)
    ap.add_argument("-o", "--output", help="write report to file (default stdout)")
    ap.add_argument("--exclude-recent-correct", type=int, default=2, metavar="N",
                    help="N used for the exclusion preview (default 2)")
    args = ap.parse_args()

    attempts = load_attempts(args.attempts)
    if not attempts:
        sys.exit(f"no attempts in {args.attempts}")
    history = history_by_qid(attempts)
    qids = sorted(history, key=qnum)

    out = ["# GH-200 practice report", ""]

    out += ["## Sessions", "",
            "| Session | Date | Drawn | Scored | Raw | Raw % | Adjusted | Adj % "
            f"| ≥{TARGET:.0%} | Miss buckets |",
            "|---|---|---|---|---|---|---|---|---|---|"]
    rows = session_rows(attempts)
    for row in rows:
        out.append("| " + " | ".join(str(x) for x in row) + " |")
    out.append("")

    failed = []
    for qid in qids:
        scoreable = [a for a in history[qid] if a["result"] in SCOREABLE]
        if scoreable and scoreable[-1]["result"] == "incorrect":
            last = scoreable[-1]
            failed.append((qid, last["session"], last["bucket"] or "?"))
    out += [f"## Failed on last attempt — {len(failed)} questions", ""]
    if failed:
        for bucket in "abcd?":
            group = [q for q, _, b in failed if b == bucket]
            if group:
                out.append(f"- bucket ({bucket}): {', '.join(group)}")
    else:
        out.append("- none")
    out.append("")

    n = args.exclude_recent_correct
    eligible = [qid for qid in qids if recently_correct(history[qid], n)]
    latest = rows[-1][0]
    drawn_latest = [qnum(a["qid"]) for a in attempts if a["session"] == latest]
    out += [f"## Next session", "",
            f"- excluded by `--exclude-recent-correct {n}`: {len(eligible)} "
            f"of {len(qids)} questions"
            + (f" ({', '.join(eligible)})" if 0 < len(eligible) <= 40 else ""),
            f"- latest session `{latest}` drew up to Q{max(drawn_latest):03d} "
            f"(candidate for `--after`)", ""]

    out += ["## Per-question history", "",
            "| Q | History | Last | Session | Bucket |", "|---|---|---|---|---|"]
    for qid in qids:
        hist = history[qid]
        marks = "".join(MARK[a["result"]] for a in hist)
        last = hist[-1]
        out.append(f"| {qid} | {marks} | {last['result']} | {last['session']} "
                   f"| {last['bucket'] or ''} |")
    out.append("")

    text = "\n".join(out)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"wrote {args.output}")
    else:
        print(text)


if __name__ == "__main__":
    main()
