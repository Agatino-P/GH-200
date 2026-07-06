#!/usr/bin/env python3
"""Print one full question block from a session's questions.md — verbatim.

Guarantees the presenter can never truncate before the `Type:` line: this reads
the block from the `## Qnnn` header through its closing `---` and prints ALL of
it, including options and the single/multi-select Type line. It reads ONLY
questions.md (never manifest.json), so there is no answer-key leak.

Usage:
    present.py --session ID --qid Q042      # print that question's full block
    present.py --session ID --next Q041     # print the block AFTER Q041 (resume)
    present.py --session ID --next          # print the first question in the file
"""

import argparse
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.dirname(SCRIPT_DIR)
DEFAULT_SESSIONS = os.path.join(DATA_DIR, "sessions")

HEADER = re.compile(r"^## (Q\d+)\s*$")


def parse_blocks(path):
    """Return ordered list of (qid, block_text) from a questions.md file."""
    with open(path, encoding="utf-8") as fh:
        lines = fh.readlines()
    blocks = []
    cur_qid = None
    cur = []
    for line in lines:
        m = HEADER.match(line.rstrip("\n"))
        if m:
            if cur_qid is not None:
                blocks.append((cur_qid, "".join(cur).rstrip() + "\n"))
            cur_qid = m.group(1)
            cur = [line]
        elif cur_qid is not None:
            cur.append(line)
    if cur_qid is not None:
        blocks.append((cur_qid, "".join(cur).rstrip() + "\n"))
    return blocks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--session", required=True)
    ap.add_argument("--qid", help="print this exact question id")
    ap.add_argument(
        "--next",
        nargs="?",
        const="",
        help="print the question after this qid (or the first if given no value)",
    )
    ap.add_argument("--sessions-dir", default=DEFAULT_SESSIONS)
    args = ap.parse_args()

    path = os.path.join(args.sessions_dir, args.session, "questions.md")
    if not os.path.exists(path):
        sys.exit(f"no questions.md for session {args.session}: {path}")
    blocks = parse_blocks(path)
    if not blocks:
        sys.exit(f"no question blocks found in {path}")
    order = [qid for qid, _ in blocks]
    by_id = dict(blocks)

    if args.qid:
        target = args.qid
    elif args.next is not None:
        if args.next == "":
            target = order[0]
        else:
            if args.next not in by_id:
                sys.exit(f"{args.next} not in session {args.session}")
            i = order.index(args.next)
            if i + 1 >= len(order):
                sys.exit(f"{args.next} is the last question in {args.session}")
            target = order[i + 1]
    else:
        sys.exit("pass --qid Qnnn or --next [Qnnn]")

    if target not in by_id:
        sys.exit(f"{target} not in session {args.session}")

    block = by_id[target]
    if "**Type:**" not in block:
        # Fail loud: a block without a Type line is exactly the truncation trap.
        sys.stderr.write(f"WARNING: {target} has no **Type:** line in the file!\n")
    print(block, end="")


if __name__ == "__main__":
    main()
