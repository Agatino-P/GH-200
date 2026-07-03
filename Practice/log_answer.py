#!/usr/bin/env python3
"""Grade one committed answer against a session manifest and log it.

The manifest written by make_session.py is the only source of the correct
letters, frozen at generation time; the grade is pure letter-set equality in
the shuffled frame. The bank's original letters therefore can never be glued
onto the learner's letters (the 2026-06-28 inversion bug).

This script's output is the reveal: the presenter learns the verdict and the
correct letters only from here, after the learner has committed.

Usage:
    log_answer.py --session ID --qid Qnnn --answer B[,C] [--force]
    log_answer.py --session ID --qid Qnnn --void "reason"
    log_answer.py --session ID --qid Qnnn --set-bucket a|b|c|d [--note "..."] [--force]
"""

import argparse
import datetime
import json
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from quiz_log import SCOREABLE, read_records

DEFAULT_ATTEMPTS = os.path.join(SCRIPT_DIR, "attempts.jsonl")
DEFAULT_SESSIONS = os.path.join(SCRIPT_DIR, "sessions")


def now_ts():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_manifest(sessions_dir, session_id):
    path = os.path.join(sessions_dir, session_id, "manifest.json")
    if not os.path.exists(path):
        sys.exit(f"no manifest for session {session_id!r}: {path}")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def parse_letters(raw, n_options, qid):
    letters = [s.strip().upper() for s in raw.split(",") if s.strip()]
    if not letters:
        sys.exit(f"{qid}: empty answer")
    if len(set(letters)) != len(letters):
        sys.exit(f"{qid}: duplicate letters in answer {raw!r}")
    valid = [chr(ord("A") + k) for k in range(n_options)]
    bad = [x for x in letters if x not in valid]
    if bad:
        sys.exit(f"{qid}: letter(s) {', '.join(bad)} out of range A-{valid[-1]}")
    return letters


def existing_attempts(attempts_path, session_id, qid):
    if not os.path.exists(attempts_path):
        return []
    return [r for r in read_records(attempts_path)
            if r["session"] == session_id and r["qid"] == qid and not r.get("amend")]


def append_record(attempts_path, rec):
    with open(attempts_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def original_frame(entry, shuffled_letters):
    new_to_old = {v: k for k, v in entry["map_old_to_new"].items()}
    return sorted(new_to_old[x] for x in shuffled_letters)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--session", required=True)
    ap.add_argument("--qid", required=True)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--answer", help="committed letters, e.g. B or B,C")
    mode.add_argument("--void", metavar="REASON", help="log ungraded (presenter mishap)")
    mode.add_argument("--set-bucket", choices=list("abcd"),
                      help="amend the miss triage bucket after the reveal")
    ap.add_argument("--note", help="free-text note (with --set-bucket or --answer)")
    ap.add_argument("--force", action="store_true",
                    help="supersede an existing attempt / amend a correct one")
    ap.add_argument("--attempts", default=DEFAULT_ATTEMPTS)
    ap.add_argument("--sessions-dir", default=DEFAULT_SESSIONS)
    args = ap.parse_args()

    if not re.fullmatch(r"Q\d+", args.qid):
        sys.exit("--qid expects the form Qnnn")

    manifest = load_manifest(args.sessions_dir, args.session)
    entry = next((q for q in manifest["questions"] if q["qid"] == args.qid), None)
    if entry is None:
        sys.exit(f"{args.qid} is not part of session {args.session}")

    prior = existing_attempts(args.attempts, args.session, args.qid)

    if args.set_bucket:
        if not prior:
            sys.exit(f"{args.qid}: no attempt logged in {args.session} to amend")
        if prior[-1]["result"] not in SCOREABLE:
            sys.exit(f"{args.qid}: last attempt is {prior[-1]['result']!r}, not gradeable")
        if prior[-1]["result"] == "correct" and not args.force:
            sys.exit(f"{args.qid}: last attempt was correct — bucket triage is for "
                     "misses (--force to override)")
        append_record(args.attempts, {
            "ts": now_ts(), "session": args.session, "qid": args.qid,
            "amend": True, "bucket": args.set_bucket, "note": args.note,
        })
        print(f"{args.qid}: bucket ({args.set_bucket}) recorded")
        return

    if prior and not args.force:
        sys.exit(f"{args.qid}: already logged in session {args.session} "
                 f"(result: {prior[-1]['result']}) — refuse duplicate (--force to supersede)")

    base = {
        "ts": now_ts(), "session": args.session, "qid": args.qid,
        "map_old_to_new": entry["map_old_to_new"],
        "correct": entry["correct"],
        "bucket": None, "bucket_raw": None, "note": args.note,
    }

    if args.void is not None:
        base.update({"given": [], "result": "void",
                     "note": args.void if args.note is None else f"{args.void} — {args.note}"})
        append_record(args.attempts, base)
        print(f"{args.qid}: VOID — {args.void}")
        return

    given = parse_letters(args.answer, entry["n_options"], args.qid)
    if entry["type"] == "single" and len(given) != 1:
        sys.exit(f"{args.qid} is single-answer; got {len(given)} letters — re-ask, "
                 "don't guess the intent")
    result = "correct" if set(given) == set(entry["correct"]) else "incorrect"
    base.update({"given": given, "result": result})
    append_record(args.attempts, base)

    correct_str = ", ".join(entry["correct"])
    orig_str = ", ".join(original_frame(entry, entry["correct"]))
    verdict = "CORRECT" if result == "correct" else "INCORRECT"
    print(f"{args.qid}: {verdict} — given {', '.join(given)}; "
          f"correct {correct_str} (original frame: {orig_str})")
    if result == "incorrect":
        print(f"{args.qid}: triage the miss, then: log_answer.py --session "
              f"{args.session} --qid {args.qid} --set-bucket a|b|c|d [--note ...]")


if __name__ == "__main__":
    main()
