#!/usr/bin/env python3
"""Generate a quiz session: filter the bank by history, shuffle, strip the key.

Reads the master bank, drops questions whose recent attempt history says they
are learned (--exclude-recent-correct), shuffles each survivor's options with
a seeded RNG (reusing shuffle_bank), and writes:

    sessions/<id>/questions.md   re-lettered options; Answer/Docs/hint lines removed
    sessions/<id>/manifest.json  answer key + letter maps, read only by log_answer.py

The correct letters are frozen into the manifest at generation time and appear
nowhere else — not in questions.md, not on stdout — so the presenter never
sees them and grading can only ever compare letters in the shuffled frame.

Usage:
    make_session.py [--limit N] [--after Qnnn] [--seed N] [--id NAME]
                    [--exclude-recent-correct N] [--qids Q001,Q005,...]
                    [--bank PATH] [--attempts PATH] [--sessions-dir PATH]
"""

import argparse
import datetime
import json
import os
import random
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.dirname(SCRIPT_DIR)  # Practice/ — bank, attempts, sessions live here
sys.path.insert(0, SCRIPT_DIR)

from shuffle_bank import ANSWER_RE, FENCE_RE, parse_block, render_block, split_blocks
from quiz_log import history_by_qid, load_attempts, recently_correct

DOCS_RE = re.compile(r"^\*\*Docs:\*\*")
DEFAULT_BANK = os.path.join(DATA_DIR, "gh-200-ghcertified-bank-full-2026-06-24.md")
DEFAULT_ATTEMPTS = os.path.join(DATA_DIR, "attempts.jsonl")
DEFAULT_SESSIONS = os.path.join(DATA_DIR, "sessions")


def type_line(n_correct):
    if n_correct == 1:
        return "**Type:** *single*"
    return f"**Type:** *multi-select ({n_correct} correct)*"


def strip_key(lines, n_correct):
    """Remove every answer-revealing line from one rendered block.

    All '>' blockquote lines outside code fences are annotations that restate
    or explain the answer (option hints, verified notes, even stem-position
    hints like Q052's) — never question content, so they all go.
    """
    out = []
    in_fence = False
    for line in lines:
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        if ANSWER_RE.match(line):
            out.append(type_line(n_correct))
            continue
        if DOCS_RE.match(line):
            continue
        if line.lstrip().startswith(">"):
            continue
        if line.strip() == "" and out and out[-1].strip() == "":
            continue
        out.append(line)
    return out


def assert_no_leak(lines):
    in_fence = False
    for line in lines:
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if ANSWER_RE.match(line) or DOCS_RE.match(line) or line.lstrip().startswith(">"):
            sys.exit(f"leak self-check failed, refusing to write: {line!r}")


def pick_session_id(sessions_dir):
    today = datetime.date.today().isoformat()
    for suffix in "abcdefghijklmnopqrstuvwxyz":
        sid = f"{today}-{suffix}"
        if not os.path.exists(os.path.join(sessions_dir, sid)):
            return sid
    sys.exit(f"no free session id left for {today}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--bank", default=DEFAULT_BANK)
    ap.add_argument("--attempts", default=DEFAULT_ATTEMPTS)
    ap.add_argument("--sessions-dir", default=DEFAULT_SESSIONS)
    ap.add_argument("--exclude-recent-correct", type=int, default=2, metavar="N",
                    help="skip questions whose last N graded attempts were all "
                         "correct (default 2; 0 disables)")
    ap.add_argument("--limit", type=int, help="cap the session at N questions")
    ap.add_argument("--seed", type=int, help="RNG seed (default: random, kept in manifest)")
    ap.add_argument("--after", metavar="Qnnn", help="only questions numbered above this id")
    ap.add_argument("--qids", help="explicit comma-separated ids; overrides all filters")
    ap.add_argument("--id", dest="session_id", help="session id (default: date + free letter)")
    args = ap.parse_args()

    with open(args.bank, encoding="utf-8") as f:
        text = f.read()
    _, blocks = split_blocks(text)
    questions = [parse_block(b) for b in blocks]

    excluded = []
    if args.qids:
        wanted = [s.strip() for s in args.qids.split(",") if s.strip()]
        known = {q["qid"] for q in questions}
        unknown = [w for w in wanted if w not in known]
        if unknown:
            sys.exit(f"unknown qids: {', '.join(unknown)}")
        wanted_set = set(wanted)
        selected = [q for q in questions if q["qid"] in wanted_set]
    else:
        selected = questions
        if args.exclude_recent_correct > 0:
            if os.path.exists(args.attempts):
                history = history_by_qid(load_attempts(args.attempts))
                keep = []
                for q in selected:
                    if recently_correct(history.get(q["qid"], []), args.exclude_recent_correct):
                        excluded.append(q["qid"])
                    else:
                        keep.append(q)
                selected = keep
            else:
                print(f"note: {args.attempts} not found — recent-correct filter skipped",
                      file=sys.stderr)
        if args.after:
            m = re.fullmatch(r"Q(\d+)", args.after)
            if not m:
                sys.exit("--after expects the form Qnnn")
            cut = int(m.group(1))
            selected = [q for q in selected if int(q["qid"][1:]) > cut]
        if args.limit is not None:
            selected = selected[: args.limit]

    if not selected:
        sys.exit("no questions left after filtering — nothing to write")

    seed = args.seed if args.seed is not None else random.SystemRandom().randrange(10**9)
    rng = random.Random(seed)

    session_id = args.session_id or pick_session_id(args.sessions_dir)
    session_dir = os.path.join(args.sessions_dir, session_id)
    if os.path.exists(session_dir):
        sys.exit(f"session dir already exists: {session_dir}")

    today = datetime.date.today().isoformat()
    out_lines = [
        f"# GH-200 practice session {session_id}",
        "",
        f"Generated {today} from `{os.path.basename(args.bank)}` — "
        f"{len(selected)} questions, options shuffled and re-lettered.",
        "Answers withheld: grade each commitment with `log_answer.py` "
        "(see QUIZ-PROTOCOL.md).",
        "",
        "---",
        "",
    ]
    manifest_questions = []
    for q in selected:
        order = list(range(len(q["options"])))
        rng.shuffle(order)
        lines, old_to_new = render_block(q, order)
        out_lines.extend(strip_key(lines, len(q["marked"])))
        manifest_questions.append({
            "qid": q["qid"],
            "n_options": len(q["options"]),
            "type": "single" if len(q["marked"]) == 1 else "multi",
            "n_correct": len(q["marked"]),
            "map_old_to_new": old_to_new,
            "correct": sorted(old_to_new[letter] for letter in q["marked"]),
        })

    assert_no_leak(out_lines)

    manifest = {
        "session": session_id,
        "created": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "bank": os.path.basename(args.bank),
        "seed": seed,
        "selection": {
            "exclude_recent_correct": args.exclude_recent_correct,
            "limit": args.limit,
            "after": args.after,
            "qids": args.qids,
        },
        "questions": manifest_questions,
    }

    os.makedirs(session_dir)
    with open(os.path.join(session_dir, "questions.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(out_lines).rstrip("\n") + "\n")
    with open(os.path.join(session_dir, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
        f.write("\n")

    print(f"session {session_id}: {len(selected)} questions -> "
          f"{os.path.join(session_dir, 'questions.md')}")
    if excluded:
        print(f"excluded {len(excluded)} recently-correct: {', '.join(excluded)}")


if __name__ == "__main__":
    main()
