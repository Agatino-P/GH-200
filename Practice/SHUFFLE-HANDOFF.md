# Handoff — Question-Bank Option Shuffler

**Written:** 2026-07-02
**Purpose:** the GH-200 practice banks in this folder carry the contributor-marked key almost always as option **A** (~89% of the ghcertified bank). These scripts randomize the option order per question — remapping the answer key accordingly — so practice runs don't leak the answer by position. They will later be driven by an automated process that prepares fresh practice sets.

## Files

| File | Role |
|---|---|
| `shuffle_bank.py` | Core engine: parses a bank, shuffles each question's options, re-letters them, remaps the `**Answer:**` line. Also the reusable library (`split_blocks`, `parse_block`, `render_block`). |
| `shuffle_all.py` | Driver for the full-bank case: `shuffle_all.py BANK OUTPUT [--seed N]`. Imports the engine and shuffles all questions one by one, prepending a dated provenance note. |
| `shuffled-sample-10.md` | First test artifact: Q001–Q010 shuffled with seed 42, verified by an independent agent on 2026-07-02 (10/10 PASS). |
| `gh-200-ghcertified-bank-full-shuffled.md` | Full 178-question shuffled bank, seed 20260702, verified on 2026-07-02 (178/178 PASS). |

## Usage

```bash
cd Practice

# Shuffle a whole bank into a new file (input is never modified):
python3 shuffle_all.py gh-200-ghcertified-bank-full-2026-06-24.md my-shuffled-bank.md --seed 7

# Same, but let the script pick (and print) a random seed:
python3 shuffle_all.py gh-200-ghcertified-bank-full-2026-06-24.md my-shuffled-bank.md

# Core engine directly — subset + per-question mapping log on stderr:
python3 shuffle_bank.py gh-200-ghcertified-bank-full-2026-06-24.md -o sample.md --limit 10 --seed 42

# Parser safety check (run after editing a bank or the scripts):
python3 shuffle_bank.py gh-200-ghcertified-bank-full-2026-06-24.md --check
```

- **Seeds** make runs reproducible: same bank + same seed = identical output. `shuffle_all.py` records the seed in the output's provenance note.
- `--check` re-serializes the bank unshuffled and compares byte-for-byte with the input; it proves the parser is lossless for that file. It passes on the full ghcertified bank (178 questions) as of 2026-07-02.
- The **letter-mapping log** (`Q001: A->D B->B ...`) goes to stderr only — output files never reveal where options moved.

## Bank format the parser expects

`## Qnnn` header · stem (may contain fenced code) · options as `- A. text` with optional indented continuation lines (code fences, `> note` lines — these travel with their option) · `**Answer:** <letters>  ·  *<type>*` · `**Docs:** <url>` · optional trailing `>` note paragraphs · `---` separator. Option letters must be consecutive from A. Anything malformed raises a `BankError` naming the question — the script fails loudly rather than emit a corrupted bank.

## Known caveats

1. **Note prose is never rewritten.** Trailing `> **✅ Verified …**` notes (and the bank preamble) may say things like "Marked answer **A** stands" — those letters refer to the *pre-shuffle* order. Only the `**Answer:**` line is remapped. If the future practice-set process should strip these notes, that's a small flag to add.
2. **First-correct-letter distribution still leans A** on the full bank (A:62 of 178 with seed 20260702). This is expected, not a bug: many questions have only 2–3 options, and for multi-selects the stat counts the alphabetically first correct letter. Positional leakage is gone; a perfectly flat histogram is not the goal.
3. **Scripts must stay side by side** — `shuffle_all.py` imports `shuffle_bank` from its own directory.

## Verification history

- 2026-07-02 — 10-question sample (seed 42) verified by an independent agent: stems, option multisets, resolved correct-answer texts, type suffixes, and Docs lines all match; option order changed in 10/10.
- 2026-07-02 — full-bank output (seed 20260702) verified with the same per-question criteria: 178/178 PASS.

## Next step (done 2026-07-03)

Built as the quiz tooling in this directory: `make_session.py` (imports this library to prepare fresh, answer-free question sets), `log_answer.py`, `report.py`. Session recipe: `QUIZ-PROTOCOL.md`.
