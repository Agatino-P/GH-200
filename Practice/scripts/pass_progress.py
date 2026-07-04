#!/usr/bin/env python3
"""Aggregate per-question pass status across a qid range.

Collects question_status.classify() over a range of qids and reports how many
fall in each category, plus how many will be PRESENTED vs EXCLUDED on the next
pass (make_session's recently-correct=2 filter). Reuses the per-question logic
in question_status.py so the classification lives in exactly one place.

Usage:
    pass_progress.py                     # Q001 .. highest logged
    pass_progress.py --from 1 --to 150
    pass_progress.py --to 150 --list     # also print the qids in each category
"""

import argparse
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.dirname(SCRIPT_DIR)  # Practice/
sys.path.insert(0, SCRIPT_DIR)

from quiz_log import load_attempts, history_by_qid, recently_correct
from question_status import classify

DEFAULT_ATTEMPTS = os.path.join(DATA_DIR, "attempts.jsonl")

CATS = ["both", "first_only", "second_only", "never",
        "once_correct", "once_wrong", "none"]
LABEL = {
    "both": "both times right",
    "first_only": "right 1st, wrong 2nd",
    "second_only": "wrong 1st, right 2nd",
    "never": "never right (both wrong)",
    "once_correct": "one attempt only, correct",
    "once_wrong": "one attempt only, wrong",
    "none": "no scoreable attempt (all void/skip)",
}


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--from", dest="lo", type=int, default=1)
    ap.add_argument("--to", dest="hi", type=int, default=None)
    ap.add_argument("--list", action="store_true", help="print qids per category")
    ap.add_argument("--attempts", default=DEFAULT_ATTEMPTS)
    args = ap.parse_args()

    hist = history_by_qid(load_attempts(args.attempts))
    hi = args.hi if args.hi is not None else max(int(q[1:]) for q in hist)
    qids = [f"Q{n:03d}" for n in range(args.lo, hi + 1) if f"Q{n:03d}" in hist]

    buckets = {c: [] for c in CATS}
    presented, excluded = [], []
    for q in qids:
        h = hist[q]
        buckets[classify(h)].append(q)
        (excluded if recently_correct(h, 2) else presented).append(q)

    print(f"Range Q{args.lo:03d}-Q{hi:03d}: {len(qids)} questions logged\n")
    for c in CATS:
        if buckets[c]:
            print(f"  {LABEL[c]:36} {len(buckets[c]):3}")
            if args.list:
                print(f"      {', '.join(buckets[c])}")
    print()
    print(f"  PRESENTED next pass (not yet 2-in-a-row correct): {len(presented)}")
    print(f"  EXCLUDED  next pass (done - 2 consecutive correct): {len(excluded)}")
    if args.list:
        print(f"\n  presented: {', '.join(presented)}")


if __name__ == "__main__":
    main()
