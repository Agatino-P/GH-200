# GH-200 · Topic 1D — YAML Anchors, Aliases & Merge Keys

*Personalized recap. Covers Domain 1 objective **1.9** (YAML anchors `&`, aliases `*`, merge keys `<<`),
which also serves Domain 2 objective **2.3** (reading/expanding anchored YAML when analyzing a workflow).
Facts verified against live GitHub docs + changelog, June 2026. Quiz outcomes per bit noted; weak-spots
section at the end.*

---

## The one-line summary (read this first)

GitHub Actions supports **anchors (`&`) and aliases (`*`)**, but **NOT merge keys (`<<`)**.
That asymmetry is the entire topic. Anchors give you *exact duplication within one file*; the
inherit-and-override capability you'd want (merge keys) was deliberately left out.

```
&  anchor   -> SUPPORTED (since 2025-09-18, auto-enabled for all repos)
*  alias    -> SUPPORTED
<< merge key -> NOT SUPPORTED  (the trap)
```

Why care if a feature is *un*supported? Because GH-200 is recognition-based. A config using
`<<: *base` is a textbook "spot the mistake" distractor. The skill tested is **discrimination**:
recognize valid (`&`/`*`) vs invalid (`<<`), and know the correct fallback.

---

## Bit 1 — Anchors `&` and aliases `*`  ·  *(quiz: 5/5)*

**Pure-YAML definition (not GitHub-specific).** An **anchor** `&name` tags a node ("remember this").
An **alias** `*name` drops a *copy* of that tagged node elsewhere in the **same file**. `name` is an
invented label — not a key, no meaning beyond linking the alias to its anchor.

The purpose is eliminating within-file duplication. Minimal example:

```yaml
jobs:
  job1:
    env: &prod_env          # anchor: tag this mapping
      NODE_ENV: production
      LOG_LEVEL: info
    runs-on: ubuntu-latest
    steps:
      - run: echo "deploy"
  job2:
    env: *prod_env          # alias: reuse the tagged mapping
    runs-on: ubuntu-latest
    steps:
      - run: echo "smoke test"
```

`job2`'s `env` expands to exactly the same two variables as `job1`'s. GitHub's docs describe the
aliased version as *equivalent to* writing the YAML out in full without anchors.

**What can be anchored.** Any node type: a scalar, a sequence (e.g. a shared `paths:` list reused
across `push` and `pull_request` triggers), a mapping, or an entire job definition (`test: &base_job`
... `alt-test: *base_job`).

**Mechanics that form the trap surface:**

```
1. ALL-OR-NOTHING   An alias copies the WHOLE node. No partial override with plain aliases.
2. DEFINE BEFORE USE The anchor must appear earlier in the file than any alias to it (top-to-bottom).
3. SAME FILE ONLY   Anchors don't cross files. NOT a substitute for reusable workflows / composite actions.
4. EXPANSION MODEL  Think "alias = the anchored content written out again at expansion time."
```

**Current-state / accuracy note.** Anchor + alias support in workflow files is *recent*: shipped
**2025-09-18**, automatically enabled for all users and repositories. Before that date, anchors in
workflow files were unsupported and errored. Just inside the Jan 2026 knowledge cutoff, so grounded
against the live changelog rather than memory.

---

## Bit 2 — Merge keys `<<`  ·  *(quiz: 4/4)*

**Pure-YAML definition.** A merge key `<<: *anchor` pulls the keys of an anchored *mapping* into the
current mapping **and** lets you **override** individual keys by also writing them out. This is the
"inherit a base, then change one thing" power that plain aliases (Bit 1) lack.

In a parser that supports merge keys, this:

```yaml
base: &base
  retries: 3
  timeout: 30
  region: us-east-1

prod:
  <<: *base
  region: eu-west-1   # override just this one key
```

would resolve `prod` to `retries: 3`, `timeout: 30`, `region: eu-west-1`.

**THE GOTCHA — GitHub Actions does NOT support merge keys.** Anchors/aliases work; `<<` does not.
The official GitHub "Reusing workflow configurations" page documents only `&`/`*` and never mentions
`<<`; independent write-ups confirm merge keys were deliberately excluded ("they shipped half the
feature"). The compositional gap stays unfilled.

```
WANT:  inherit base config + override one key   -> merge key would do this
REALITY (GitHub Actions):  merge key not honored -> the override pattern is unavailable
```

**Honest caveat on the exact failure mode.** The merge semantics definitely do **not** happen. I did
*not* verify whether GitHub's parser hard-errors on `<<` or treats it as a literal key named `<<`.
Either way: treat `<<` in a workflow file as broken/invalid, not as "merge." (Flagged uncertain.)

**Why it matters / the fallback.** The inherit-and-override pattern from GitLab/Azure Pipelines is
unavailable here. For base-config-plus-overrides, fall back to **composite actions** or **reusable
workflows**. Anchors give *exact duplication only*.

**Precision side note** (for empirical verification): merge keys were never part of core YAML 1.2 —
they're a YAML 1.1 optional type — so inconsistent parser support is the norm, not a GitHub-only quirk.

---

## Q&A outcomes / things the learner pushed on

- **"How can an unsupported feature be quizzed / be worth quizzing?"** — Resolved: on a
  recognition-based exam, *non-support is the question*. The item type is "spot the mistake" /
  "which is valid" / "what's the correct fallback," not free recall. A `<<: *base` config is a
  distractor designed to catch people who assume full YAML support carries over.
- Confirmed the learner can discriminate supported vs unsupported cleanly (Bit 2 quiz 4/4, including
  the True/False trap "anchors imply merge keys" → False).

---

## Exam-weight uncertainty (calibrate against practice exams)

- Anchor support is so new (Sept 2025) relative to the **Jan 2026 exam reword** that I **cannot verify
  how heavily, or in what form, GH-200 tests it.** Best *inference* (not a confirmed fact): the exam
  leans toward the *reading/analysis* style (objective 2.3) — "read this anchored config, what does it
  produce" and "spot the invalid `<<`." Treat weight as unknown until practice-exam data exists.

---

## Weak-spots / watch-list for review

- Don't let "GitHub supports YAML anchors" drift into "GitHub supports all YAML reuse features." It's
  `&`/`*` **only**; `<<` is out.
- Remember the **define-before-use** ordering rule — an alias above its anchor errors.
- When a scenario needs *base + per-job overrides*, the answer is **composite action / reusable
  workflow**, never a merge key.
