# Task Brief — Restructure the GH-200 Combined Cheat Sheet

**Run in:** Claude Code (VS Code extension), a **new session** on a **fresh clone**.
**Target file:** `Study material/GH-200_Combined_Cheat_Sheets.md` in `Agatino-P/gh-200`.
**Review model:** use **plan mode** (approve the structure before any edit) and the **per-edit diff gate**.
**Do not push** — the owner reviews and commits.

---

## Goal

Make the cheat sheet coherent and readable **without losing any verified fact**. Right now the same concept is scattered across the topic sections *and* several trailing "Drill-Surfaced Keepers" blocks — the file itself flags this (the "Distribute into the topic sections above on the next cleanup pass" note). Consolidate so **each concept has exactly one home**, keep the trap callouts, and leave the result **easy to prune afterward**.

This is a restructure, not a prune and not a rewrite. Faithful reorganisation + de-duplication only.

## Setup

1. Fresh clone: `git clone --depth 1 https://github.com/Agatino-P/gh-200.git`. The `/mnt/project` mirror (if present) is **not** authoritative — ignore it; the repo is canonical.
2. Work on a **branch** (e.g. `cheatsheet-restructure`) or a sibling file. **Never edit in place on `main`.**
3. You have and will need **web access** (see Verify).
4. If a merge is ambiguous, the fuller per-topic sources are in the same folder (`GH-200_Topic_*` / `GH-200_Cheat_*`) — consult them to disambiguate rather than guess.

## Hard rules (non-negotiable)

- **No fact changes during restructure.** Move and merge only. When two entries state the same fact in different words, merge to one — but the merged wording must keep **every distinction either carried**. Never drop a nuance to make a sentence shorter.
- **Verify, don't trust.** Re-check **every consolidated fact against live `docs.github.com`** — not from memory, and not by trusting the existing text (it may have drifted). Distractor notes and offhand asides count as facts and must be verified too. If something fails verification, **surface it in the summary — do not silently "fix" it.**
- **Do not prune.** Deleting "now-obvious" content is the owner's separate pass. Your job is to make that pass **safe**, not to do it.
- **Keep traps visible.** The trap/misconception callouts and the explicit distinction-drawing (`X ≠ Y`, "distractor", "TRAPS FIRST") are the highest-value content — preserve them.
- **No wall-of-text.** Break dense prose blobs back into scannable bullets (the trailing keeper paragraphs are the worst offenders).

## Staged workflow

1. **Plan first (plan mode).** Propose the target structure **and a merge map** (which scattered entries fold into which home, and where each duplicate goes). **No edits until the owner approves the plan.**
2. **Consolidate + de-duplicate.** Apply the approved moves/merges. Faithful only.
3. **Verify.** Each merged/consolidated fact against live docs. Note anything that doesn't check out.
4. **Stop.** Hand back for the owner's prune pass — do not continue into pruning.

## Structure & style

- **One home per concept.** No concept should live in more than one place. Known duplicates to collapse (non-exhaustive — find the rest): `if:` is job+step-only (stated ~3×), `RUNNER_*` vars (~2×), reusable-workflow limits, the implicit `success()` / status-function behaviour, the `github.ref` family.
- **Topic split is no longer sacred.** A coherent, low-redundancy structure beats preserving the exact 14-topic layout. Reorganise around how the material actually clusters.
- **Prunable = low coupling.** Each entry should stand alone so deleting an obvious line never orphans another. Avoid "see above" chains that break when a line is removed.
- **Calm the notation.** Pick **one** emphasis convention for traps (e.g. a single leading marker) and drop the competing symbol systems currently stacked together (`⚠️ ⭐ ★ ❌ → ↔ ←` plus bold plus ALL-CAPS in the same line). Use bold sparingly so the real signal stands out.
- **Markdown hygiene.** Run a linter / use the preview and fix rendering messes. Tables as real markdown (not space-aligned). Fenced code blocks for YAML, commands, and anything with special characters.

## Output & handoff

- Deliver as a branch or sibling file with **reviewable diffs** (that is the whole point of doing this in the extension).
- End with a short **summary**: structure changes, the merge map, and **any fact that failed live-doc verification**.
- **Do not push.** Owner commits.

## Non-goals

- Not a prune, not a re-teach, not a rewrite of correct content.
- Don't touch other repo files (scripts, drill log, protocol, gap plan).
- Don't judge the final length until *after* de-duplication — a large share of the current bulk is the four-places-per-concept problem, which consolidation removes on its own.
