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

---

## Decisions agreed (session 2026-07-01)

Resolved before any edit, so a future session can resume without re-litigating:

1. **Structure = Hybrid.** Keep the 5-domain / topic-code backbone (1A–5D); fold each scattered
   keeper into its named topic home; **add new labelled sections** for genuinely homeless clusters
   rather than force-fitting them or inventing a fake "Domain 6." New sections landed as **4D**
   Self-Hosted Runners · **4E** Custom Actions Authoring · **4F** Editions/GHES/GitHub Connect ·
   **4G** Packages & GHCR. GitHub-Apps token ladder folded into **5A** (not its own section).
2. **Trap notation = single leading `⚠️`.** Drop the stacked `⭐ ★ ⊕` symbol systems and heavy bold.
   Keep the high-value inline distinctions: `X ≠ Y`, `❌` on invalid-pattern lines, "distractor",
   and the `TRAPS FIRST` section headers.
3. **Verification breadth = merged/moved facts only** (where drift/contradiction risk is real),
   against live `docs.github.com`. Preserve every existing `⚠ unverified` note as-is — do not mark
   one "resolved" unless a live doc confirms it (then note the confirmation).
4. **Readability conventions (added after first render review):**
   - A spacing-only `<style>` block at the top (line-height + list/heading spacing, no colours so it
     is theme-safe). Honoured by VS Code preview / Typora / PDF; **GitHub.com strips it** (harmless).
   - **No semicolon-joined lists.** A set of parallel items becomes real sub-bullets, never
     `a; b; c` on one line. (Prose clauses and tight two-part contrasts like `>>`/`>` may keep a
     semicolon.) Break wall-of-text bullets into scannable sub-bullets.
   - Tables as real markdown (not space-aligned in code fences); YAML/commands/REST paths stay fenced.

## Execution log — what has been done (2026-07-01)

Branch **`cheatsheet-restructure`** off `main`. Committed (`ca8a64b` restructure + a follow-up commit
for the readability pass). **Not pushed** — owner reviews/pushes. Only the target cheat sheet +
this brief were touched.

- **Three trailing "Drill-Surfaced Keepers" blocks dissolved**; every item routed to one home.
- **Duplicates merged** keeping all nuance: `if:` job/step-only + implicit `success()` (was 3×),
  `github.ref` family, `RUNNER_*`/`GITHUB_*` env vars, reusable-wf limits, env-vs-vars scopes,
  matrix include-counting, re-run actor split, environment scope, secret masking / `::add-mask::`,
  cache/artifact scope, OIDC two-token.
- **One fact reconciliation** (later-corrects-earlier): artifact scope is a **soft** run-default
  (openable via `actions: read` + `run-id` + `repository`); only **cache branch-scope is hard**.
  Merged as the corrected version — **live-doc confirmed**.
- **Live-doc verification passed, nothing failed:** reusable-wf limits (50/nesting 10, no loops),
  token ladder (JWT 10 min / installation 1 h / user OAuth 8 h), `head_ref`/`base_ref` PR-only,
  env required reviewers (≤6 / read suffices / one approval), skip-CI (push+PR only), matrix
  include counting, dispatch endpoints, cache scope isolation, `actions/checkout` v7 fork-blocking
  (effective 2026-06-18), `RUNNER_*` set + `GITHUB_TOKEN`-is-a-secret. The reusable-wf-limits flag
  was upgraded from "re-verify" to "verified 2026-07-01".
- **Notation unified** to leading `⚠️`; `⭐ ★ ⊕` removed. **Wall-of-text bullets and all
  semicolon-joined lists split into sub-bullets.** Two pseudo-table code fences → real tables.
  Stale top-of-file note rewritten (it claimed "verbatim, not edited" + pointed at non-existent
  `GH-200_Topic_*` files). Spacing-only `<style>` block added.
- File went 800 → ~905 lines (growth is list structure + four new sections, net of de-dup).

### Still open — the owner's next pass
- **The prune pass** (deleting now-obvious content) was intentionally **not** started — that is the
  owner's separate step; this restructure only made it safe.
- Optional deeper reflow: the compact two-part semicolon contrasts left in place (`>>`/`>`,
  `{}`/`read-all`, `with:`/`secrets:`) can be split further if wanted.
- Push the branch / open a PR when ready.
