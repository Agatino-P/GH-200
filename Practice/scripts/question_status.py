#!/usr/bin/env python3
"""Per-question pass status — classify ONE question's attempt history.

The atomic, independently-runnable unit behind pass_progress.py. Run it on
specific qids to inspect or debug a single question's classification.

Category (from the first two SCOREABLE attempts — i.e. pass 1 then pass 2;
void / gap / skip produce no scoreable record and are ignored):

    both          1st correct, 2nd correct
    first_only    1st correct, 2nd incorrect
    second_only   1st incorrect, 2nd correct
    never         1st incorrect, 2nd incorrect
    once_correct  only one scoreable attempt, and it was correct
    once_wrong    only one scoreable attempt, and it was incorrect
    none          no scoreable attempts (every attempt was void/gap/skip)

`presented_p3` uses the real make_session filter (recently_correct, n=2): a
question is EXCLUDED from the next pass only when its last two scoreable
attempts were both correct; otherwise it is presented again.

Usage:
    question_status.py Q071 Q081        # inspect specific questions
    question_status.py --all            # every qid seen in the log
"""

import argparse
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.dirname(SCRIPT_DIR)  # Practice/
sys.path.insert(0, SCRIPT_DIR)

from quiz_log import load_attempts, history_by_qid, recently_correct, SCOREABLE

DEFAULT_ATTEMPTS = os.path.join(DATA_DIR, "attempts.jsonl")

_PAIR = {
    ("correct", "correct"): "both",
    ("correct", "incorrect"): "first_only",
    ("incorrect", "correct"): "second_only",
    ("incorrect", "incorrect"): "never",
}


def scoreable_results(history):
    """The correct/incorrect results of one question, in chronological order."""
    return [a["result"] for a in history if a["result"] in SCOREABLE]


def classify(history):
    """Map one question's merged attempt list to a category string."""
    s = scoreable_results(history)
    if not s:
        return "none"
    if len(s) == 1:
        return "once_correct" if s[0] == "correct" else "once_wrong"
    return _PAIR[(s[0], s[1])]


def status(qid, history):
    return {
        "qid": qid,
        "scoreable": scoreable_results(history),
        "category": classify(history),
        "presented_p3": not recently_correct(history, 2),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("qids", nargs="*", help="qids to inspect, e.g. Q071 Q081")
    ap.add_argument("--all", action="store_true", help="every qid in the log")
    ap.add_argument("--attempts", default=DEFAULT_ATTEMPTS)
    args = ap.parse_args()

    hist = history_by_qid(load_attempts(args.attempts))
    if args.all:
        qids = sorted(hist)
    elif args.qids:
        qids = args.qids
    else:
        ap.error("give one or more qids, or --all")

    for q in qids:
        st = status(q, hist.get(q, []))
        marks = "".join("C" if r == "correct" else "x" for r in st["scoreable"]) or "-"
        flag = "present" if st["presented_p3"] else "DONE"
        print(f"{q}  {marks:6}  {st['category']:13}  {flag}")


if __name__ == "__main__":
    main()
