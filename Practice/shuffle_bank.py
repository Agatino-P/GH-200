#!/usr/bin/env python3
"""Shuffle the answer options of a GH-200 markdown question bank.

The bank format (see gh-200-ghcertified-bank-full-2026-06-24.md):

    ## Q001

    <question stem, may contain fenced code blocks>

    - A. option text
    - B. option text
      <indented continuation lines: code fences, "> note" lines>

    **Answer:** A, B  ·  *multi-select (2 correct)*
    **Docs:** <url>

    > optional verification notes

    ---

For each question the options are shuffled with a seeded RNG, re-lettered
A, B, C, ... in their new order, and the **Answer:** letters are remapped so
they keep pointing at the same option texts. Everything else (stem, Docs,
notes, spacing) is preserved byte-for-byte.

Usage:
    shuffle_bank.py INPUT -o OUTPUT [--seed N] [--limit N]
    shuffle_bank.py INPUT --check          # lossless round-trip self-test
"""

import argparse
import random
import re
import sys

HEADER_RE = re.compile(r"^## (Q\d+)\s*$")
OPTION_RE = re.compile(r"^- ([A-Z])\.(?=\s|$)")
ANSWER_RE = re.compile(r"^(\*\*Answer:\*\*\s*)([A-Z](?:,\s*[A-Z])*)(.*)$")
FENCE_RE = re.compile(r"^\s*```")


class BankError(Exception):
    pass


def split_blocks(text):
    """Split file into (preamble_lines, [question_line_lists]).

    A question block runs from its '## Qnnn' line up to (not including) the
    next '## Qnnn' line. Fence state is tracked so a '## Q' inside a code
    block is never treated as a header.
    """
    lines = text.split("\n")
    starts = []
    in_fence = False
    for i, line in enumerate(lines):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence and HEADER_RE.match(line):
            starts.append(i)
    if not starts:
        raise BankError("no '## Qnnn' headers found")
    preamble = lines[: starts[0]]
    blocks = [lines[s:e] for s, e in zip(starts, starts[1:] + [len(lines)])]
    return preamble, blocks


def parse_block(block):
    """Split one question block into (pre, options, post).

    pre  = lines from header through the last line before the first option
    options = list of (letter, [lines]) — each option's lines incl. continuations
    post = lines from the first blank/answer line after the options to the end
    """
    qid = HEADER_RE.match(block[0]).group(1)

    answer_idx = None
    in_fence = False
    for i, line in enumerate(block):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence and ANSWER_RE.match(line):
            answer_idx = i
            break
    if answer_idx is None:
        raise BankError(f"{qid}: no **Answer:** line found")

    first_opt = None
    in_fence = False
    for i, line in enumerate(block[:answer_idx]):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence and OPTION_RE.match(line):
            first_opt = i
            break
    if first_opt is None:
        raise BankError(f"{qid}: no options found before **Answer:**")

    # Options end at the last non-blank line before the answer line; blank
    # lines in between stay attached to `post` so spacing survives.
    opt_end = answer_idx
    while opt_end > first_opt and block[opt_end - 1].strip() == "":
        opt_end -= 1

    options = []
    current = None
    in_fence = False
    for line in block[first_opt:opt_end]:
        is_fence = bool(FENCE_RE.match(line))
        m = None if in_fence else OPTION_RE.match(line)
        if m:
            current = (m.group(1), [line])
            options.append(current)
        else:
            if current is None:
                raise BankError(f"{qid}: stray line inside options: {line!r}")
            current[1].append(line)
        if is_fence:
            in_fence = not in_fence

    letters = [letter for letter, _ in options]
    expected = [chr(ord("A") + k) for k in range(len(options))]
    if letters != expected:
        raise BankError(f"{qid}: option letters {letters} != {expected}")

    answer_line = block[answer_idx]
    marked = [s.strip() for s in ANSWER_RE.match(answer_line).group(2).split(",")]
    for letter in marked:
        if letter not in letters:
            raise BankError(f"{qid}: answer letter {letter} has no option")

    return {
        "qid": qid,
        "pre": block[:first_opt],
        "options": options,
        "post": block[opt_end:],
        "answer_offset": answer_idx - opt_end,
        "marked": marked,
    }


def render_block(q, order):
    """Rebuild a block with options in `order` (a permutation of indices)."""
    old_to_new = {}
    new_option_lines = []
    for new_idx, old_idx in enumerate(order):
        old_letter, lines = q["options"][old_idx]
        new_letter = chr(ord("A") + new_idx)
        old_to_new[old_letter] = new_letter
        lines = [OPTION_RE.sub(f"- {new_letter}.", lines[0], count=1)] + lines[1:]
        new_option_lines.extend(lines)

    post = list(q["post"])
    m = ANSWER_RE.match(post[q["answer_offset"]])
    new_marked = sorted(old_to_new[letter] for letter in q["marked"])
    post[q["answer_offset"]] = m.group(1) + ", ".join(new_marked) + m.group(3)

    return q["pre"] + new_option_lines + post, old_to_new


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("input")
    ap.add_argument("-o", "--output", help="output file (required unless --check)")
    ap.add_argument("--seed", type=int, default=None, help="RNG seed for reproducibility")
    ap.add_argument("--limit", type=int, default=None, help="only emit the first N questions")
    ap.add_argument("--check", action="store_true",
                    help="identity round-trip: parse + re-render unshuffled, compare to input")
    args = ap.parse_args()

    with open(args.input, encoding="utf-8") as f:
        text = f.read()

    preamble, blocks = split_blocks(text)
    questions = [parse_block(b) for b in blocks]

    if args.check:
        rebuilt = preamble[:]
        for q in questions:
            lines, _ = render_block(q, list(range(len(q["options"]))))
            rebuilt.extend(lines)
        if "\n".join(rebuilt) == text:
            print(f"OK: {len(questions)} questions parsed; "
                  "identity round-trip reproduces the input exactly.")
            return
        sys.exit("FAIL: identity round-trip does not match the input")

    if not args.output:
        ap.error("-o/--output is required unless --check")

    rng = random.Random(args.seed)
    if args.limit is not None:
        questions = questions[: args.limit]

    out_lines = []
    first_letter_counts = {}
    for q in questions:
        n = len(q["options"])
        order = list(range(n))
        rng.shuffle(order)
        lines, old_to_new = render_block(q, order)
        out_lines.extend(lines)
        new_first = sorted(old_to_new[letter] for letter in q["marked"])[0]
        first_letter_counts[new_first] = first_letter_counts.get(new_first, 0) + 1
        print(f"{q['qid']}: {' '.join(f'{o}->{old_to_new[o]}' for o in sorted(old_to_new))}"
              f"  answer {', '.join(q['marked'])} -> "
              f"{', '.join(sorted(old_to_new[x] for x in q['marked']))}", file=sys.stderr)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write("\n".join(out_lines))

    dist = ", ".join(f"{k}:{v}" for k, v in sorted(first_letter_counts.items()))
    print(f"Wrote {len(questions)} questions to {args.output} "
          f"(seed={args.seed}). First-correct-letter distribution: {dist}")


if __name__ == "__main__":
    main()
