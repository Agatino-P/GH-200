#!/usr/bin/env python3
"""Shuffle every question of a GH-200 markdown bank into a new file.

Thin driver over shuffle_bank.py: it parses the bank, then shuffles each
question one by one with shuffle_bank's parse/render machinery, and writes
a complete new bank (original preamble + a provenance note + all questions
with shuffled options and remapped answer keys). The input file is never
modified.

Usage:
    shuffle_all.py BANK OUTPUT [--seed N]

If --seed is omitted a random seed is drawn and printed, so any run can be
reproduced later.
"""

import argparse
import datetime
import os
import random
import sys

from shuffle_bank import split_blocks, parse_block, render_block


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("bank", help="input question bank (read-only)")
    ap.add_argument("output", help="file to write the shuffled bank to")
    ap.add_argument("--seed", type=int, default=None,
                    help="RNG seed; omitted = random, printed for reproducibility")
    args = ap.parse_args()

    if os.path.exists(args.output) and os.path.samefile(args.bank, args.output):
        sys.exit("refusing to overwrite the input bank; pass a different output path")

    seed = args.seed if args.seed is not None else random.SystemRandom().randrange(10**9)
    rng = random.Random(seed)

    with open(args.bank, encoding="utf-8") as f:
        text = f.read()
    preamble, blocks = split_blocks(text)

    today = datetime.date.today().isoformat()
    out = list(preamble)
    out.extend([
        f"> **🔀 Shuffled {today}** — option order randomized per question "
        f"(`shuffle_all.py`, seed {seed}) and answer keys remapped accordingly. "
        "Prose notes may still reference pre-shuffle option letters.",
        "",
    ])

    first_letter_counts = {}
    for block in blocks:
        q = parse_block(block)
        order = list(range(len(q["options"])))
        rng.shuffle(order)
        lines, old_to_new = render_block(q, order)
        out.extend(lines)
        new_first = sorted(old_to_new[letter] for letter in q["marked"])[0]
        first_letter_counts[new_first] = first_letter_counts.get(new_first, 0) + 1

    with open(args.output, "w", encoding="utf-8") as f:
        f.write("\n".join(out))

    dist = ", ".join(f"{k}:{v}" for k, v in sorted(first_letter_counts.items()))
    print(f"Wrote {len(blocks)} shuffled questions to {args.output} (seed={seed}).")
    print(f"First-correct-letter distribution: {dist}")


if __name__ == "__main__":
    main()
