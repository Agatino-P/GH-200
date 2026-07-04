#!/usr/bin/env python3
"""Integrity-check a generated session against the master bank.

For every question in a session it confirms:

  * the session's option TEXTS are exactly the bank's option texts
    (order-independent), with the bank's `>` answer-hint annotations stripped
    to mirror what make_session's strip_key removes from questions.md;
  * applying the manifest's old->new letter map to the bank options reproduces
    the session's {letter: text} exactly (so the shuffle didn't drop, add, or
    garble any option);
  * the manifest's `correct` letters equal the bank's marked answers mapped
    through the same map, and n_options / n_correct match.

One text-normalization routine is used for both sides so the comparison can't
be fooled by whitespace or annotation differences.

Exit 0 and "ALL CLEAN" if the session faithfully represents the bank; exit 1
and a per-question problem list otherwise. Run it right after make_session.py.

Usage:
    validate_session.py [SESSION_ID]        # default: newest session dir
    validate_session.py --session 2026-07-04-a
    validate_session.py --bank PATH --sessions-dir PATH SESSION_ID
"""

import argparse
import json
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.dirname(SCRIPT_DIR)  # Practice/ — bank and sessions live here
sys.path.insert(0, SCRIPT_DIR)

from shuffle_bank import split_blocks, parse_block, OPTION_RE, FENCE_RE, HEADER_RE

DEFAULT_BANK = os.path.join(DATA_DIR, "gh-200-ghcertified-bank-full-2026-06-24.md")
DEFAULT_SESSIONS = os.path.join(DATA_DIR, "sessions")


def opt_text(lines):
    """Normalized text of one option: drop the '- X.' prefix, skip fenced-code
    markers and '>' answer-hint annotations (which strip_key removes), and
    collapse whitespace so the two sides compare on content alone."""
    body = [OPTION_RE.sub("", lines[0], count=1)]
    in_fence = False
    for line in lines[1:]:
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence and line.lstrip().startswith(">"):
            continue
        body.append(line)
    return re.sub(r"\s+", " ", " ".join(body)).strip()


def bank_by_qid(bank_path):
    with open(bank_path, encoding="utf-8") as f:
        _, blocks = split_blocks(f.read())
    out = {}
    for b in blocks:
        q = parse_block(b)
        out[q["qid"]] = {
            "opts": {letter: opt_text(ls) for letter, ls in q["options"]},
            "marked": set(q["marked"]),
        }
    return out


def session_options(questions_md):
    """Parse {qid: {letter: text}} from a session questions.md, grouping option
    continuation lines the way parse_block does (fence-aware), stopping each
    option at the Type line / rule / next header."""
    with open(questions_md, encoding="utf-8") as f:
        lines = f.read().split("\n")
    idx = [i for i, l in enumerate(lines) if HEADER_RE.match(l)]
    out = {}
    for a, b in zip(idx, idx[1:] + [len(lines)]):
        qid = HEADER_RE.match(lines[a]).group(1)
        opts, cur, in_fence = {}, None, False
        for line in lines[a:b]:
            is_fence = bool(FENCE_RE.match(line))
            m = None if in_fence else OPTION_RE.match(line)
            if m:
                cur = [line]
                opts[m.group(1)] = cur
            elif cur is not None:
                if not in_fence and (line.startswith("**Type:") or line.startswith("---")
                                     or line.startswith("## ")):
                    cur = None
                else:
                    cur.append(line)
            if is_fence:
                in_fence = not in_fence
        out[qid] = {l: opt_text(ls) for l, ls in opts.items()}
    return out


def newest_session(sessions_dir):
    dirs = [d for d in os.listdir(sessions_dir)
            if os.path.isdir(os.path.join(sessions_dir, d))]
    if not dirs:
        sys.exit(f"no session dirs under {sessions_dir}")
    return sorted(dirs)[-1]


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("session_id", nargs="?", help="session id (default: newest)")
    ap.add_argument("--session", dest="session_flag", help="session id (alt form)")
    ap.add_argument("--bank", default=DEFAULT_BANK)
    ap.add_argument("--sessions-dir", default=DEFAULT_SESSIONS)
    args = ap.parse_args()

    sid = args.session_flag or args.session_id or newest_session(args.sessions_dir)
    sdir = os.path.join(args.sessions_dir, sid)
    if not os.path.isdir(sdir):
        sys.exit(f"no such session dir: {sdir}")

    bank = bank_by_qid(args.bank)
    session = session_options(os.path.join(sdir, "questions.md"))
    with open(os.path.join(sdir, "manifest.json"), encoding="utf-8") as f:
        man = {q["qid"]: q for q in json.load(f)["questions"]}

    problems = []
    for qid in session:
        if qid not in bank:
            problems.append((qid, "MISSING", "not in bank", ""))
            continue
        b, s, mm = bank[qid], session[qid], man[qid]
        m = mm["map_old_to_new"]
        expected = {m[old]: text for old, text in b["opts"].items()}
        if expected != s:
            for letter in sorted(set(expected) | set(s)):
                if expected.get(letter) != s.get(letter):
                    problems.append((qid, letter, expected.get(letter), s.get(letter)))
        exp_correct = sorted(m[l] for l in b["marked"])
        if exp_correct != sorted(mm["correct"]):
            problems.append((qid, "CORRECT", exp_correct, mm["correct"]))
        if mm["n_correct"] != len(b["marked"]) or mm["n_options"] != len(b["opts"]):
            problems.append((qid, "COUNTS",
                             f"bank opts={len(b['opts'])} correct={len(b['marked'])}",
                             f"manifest opts={mm['n_options']} correct={mm['n_correct']}"))

    print(f"session {sid}: {len(session)} questions checked against {os.path.basename(args.bank)}")
    if not problems:
        print("ALL CLEAN — every session question's options + correct answers match the bank exactly.")
        return 0
    print(f"PROBLEMS: {len(problems)}")
    for qid, where, exp, got in problems:
        print(f"  {qid} [{where}]\n    expected: {exp!r}\n    session:  {got!r}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
