# GH-200 · Topic 1B — Contexts, Expressions & Secret Leakage

*Personalized recap. Covers Domain 1 gap objectives **1.10** (contexts, esp. `vars`) and **1.11**
(expressions `${{ }}`: static/parse-time vs runtime; secret-leakage prevention). Facts verified
against live GitHub docs, June 2026. Quiz outcomes noted per bit, with a "weak spots" section at the end.*

---

## Bit 1 — Context families; `env` vs `vars` vs `secrets`  ·  *(quiz: 5/5)*

A **context** is a **read-only bag of runtime data**, read via `${{ }}`. It is *not* the vague English
"surrounding situation" — it's a named object you index into, and it only holds data that exists at
that moment in the run.

Full set: `github`, `env`, `vars`, `job`, `jobs`, `steps`, `runner`, `secrets`, `strategy`,
`matrix`, `needs`, `inputs`. Worth recognizing:

- `github` — event / actor / ref / sha / repository
- `needs` — outputs of upstream (`needs:`) jobs
- `matrix` — this job's axis values
- `steps` — outputs of id'd steps in the **same** job
- `runner` — `runner.os`, `runner.temp`, `runner.tool_cache`
- `inputs` — the `workflow_dispatch` / `workflow_call` inputs from Topic 1A

### The three that get confused

```
                  env              vars             secrets
Defined where     inline in YAML   GitHub UI/API    GitHub UI/API
                  (env: blocks)    (org/repo/env)   (org/repo/env)
Content           non-sensitive    non-sensitive    sensitive
                                   configuration
Read how          ${{ env.NAME }}  ${{ vars.NAME }} ${{ secrets.NAME }}
                  or shell $NAME   (only)           (only)
Masked in logs?   no               no               yes (auto-masked)
Shell env var?    yes (automatic)  no (must map)    no (must map)
```

**Key behavior:** `vars` and `secrets` are **NOT** auto-exposed as shell environment variables — they
live only inside `${{ }}`. A script doing `echo "$MY_REGION"` for a repo variable gets nothing unless
you map it first:

```yaml
steps:
  - name: deploy
    env:
      MY_REGION: ${{ vars.MY_REGION }}    # map vars  -> env
      API_KEY:   ${{ secrets.API_KEY }}   # map secret -> env
    run: ./deploy.sh "$MY_REGION"         # now $MY_REGION exists in the shell
```

**The "Content" row** is about *what's appropriate*, driven by one fact — only `secrets` are masked:

```
secrets -> sensitive (tokens, keys); stored encrypted; auto-masked
vars    -> non-sensitive CONFIGURATION managed outside YAML, reused across workflows/envs
env     -> non-sensitive, usually local/throwaway, scoped to this workflow/job/step
```

Decision tree: sensitive → `secrets`; reused config managed outside YAML → `vars`; just a value for
this file → `env`.

**Precedence** (both `vars` and `secrets`): **environment > repository > organization.**

**Two gotchas:** (1) never store sensitive data in `vars` — not masked, prints in plaintext;
(2) `env:` blocks don't self-reference (one entry can't be defined from another in the *same* block).

### Matrix primer (you'd seen it, now anchored — full depth is Topic 1C)

`strategy.matrix` lives **on a job** and runs the *same job* once per combination (cross-product of
the axes), in **parallel** by default. `matrix.<axis>` reads the current job's value; commonly fed
into `runs-on:` and steps.

```yaml
strategy:
  matrix:
    version: [16, 18, 20]
    os: [ubuntu-latest, windows-latest]   # 3 x 2 = 6 parallel jobs
runs-on: ${{ matrix.os }}
```

- **Parallelism is a count you cap** with `max-parallel` (e.g. `max-parallel: 1` = sequential) — it is
  **not** an "axis" GitHub steps through. Execution *order* of combinations is not something to rely on.
- A downstream `needs: <matrix-job>` waits for **all** combinations — the matrix job is **one node** in
  the dependency graph regardless of fan-out.
- **Matrix outputs:** all instances write to the **same** output names → they overwrite (**last wins,
  unreliable**). Fix: make names unique per combination via the `matrix` context, e.g.
  `result_${{ matrix.version }}`. For robust per-variant results, real-world pattern is **artifacts**
  (out of GH-200 scope).

---

## Bit 2 — `${{ }}` evaluation: setup-time vs runtime  ·  *(quiz: 5/5)*

GitHub processes a workflow in **two phases**; each key is evaluated **when GitHub needs to consume it.**

```
PHASE 1 — run setup (before any runner does work)
  builds the run: which jobs exist, EXPAND THE MATRIX, names, concurrency,
  the job graph (needs).

PHASE 2 — execution (on the runner, as steps reach)
  if:, run:, with:, env interpolation, step outputs, job outputs.
```

**Core consequence — context availability:** an expression can only read a context whose data already
exists at that phase.

```
WHERE you write it                    WHAT's available
on: / name: (earliest)                almost nothing
job-level if: / strategy              github, needs, vars  (NO steps, NO runner yet)
step-level if: / run: / with: / env   full set (github, needs, matrix, steps, runner, vars, secrets)
```

```yaml
# ❌ fails — steps context not available at job level (no step has run)
jobs:
  deploy:
    if: ${{ steps.check.outputs.ok == 'true' }}

# ✅ works — same data, but read at step level after the step ran
    steps:
      - id: check
        run: echo "ok=true" >> "$GITHUB_OUTPUT"
      - if: ${{ steps.check.outputs.ok == 'true' }}
        run: ./deploy.sh
```

> The exact which-context-where rules are a lookup table in the GitHub docs ("Context availability").
> Principle above + the high-confidence cases are reliable; glance at that table once before the exam.

**Matrix is static relative to the run:** it's expanded in Phase 1, so you can't grow/shrink it from a
step in the *same* run. Dynamic matrices come from a **prior job's output** via `fromJSON`:

```yaml
jobs:
  list:
    runs-on: ubuntu-latest
    outputs:
      items: ${{ steps.gen.outputs.items }}   # a JSON array string
    steps:
      - id: gen
        run: echo 'items=["a","b","c"]' >> "$GITHUB_OUTPUT"
  build:
    needs: list
    strategy:
      matrix:
        thing: ${{ fromJSON(needs.list.outputs.items) }}
    runs-on: ubuntu-latest
    steps:
      - run: echo "${{ matrix.thing }}"
```

`fromJSON` is a **real built-in expression function**. *(Note: deferred for proper treatment in Topic
1C / objective 1.8 — and how heavily GH-200 tests dynamic/`fromJSON` matrices specifically is not yet
verified; gauge against practice exams.)*

---

## Bit 3 — Preventing secret leakage in logs & expressions  ·  *(quiz: 5/5)*

`secrets` are auto-masked (raw value → `***`). Bit 3 is about the **holes in that net.**

**Hole 1 — masking is best-effort: exact match PLUS common encodings, but NOT all transforms.**
GitHub redacts the raw secret value **and common encodings such as Base64** — so `base64(secret)` is
normally masked. But it is **not guaranteed**: uncommon transforms slip through, and there's a known
edge case where `base64(secret + suffix)` leaks due to base64 padding.

```
echo "${{ secrets.TOKEN }}"            -> ***          exact match
echo "${{ secrets.TOKEN }}" | base64   -> ***          common encoding — GitHub handles Base64
echo "${{ secrets.TOKEN }}" | rev      -> CLEAR TEXT   not a recognized encoding -> leaks
```

The mental model: masking handles the obvious cases (raw + common encodings) but cannot anticipate
arbitrary transformations. For a derived sensitive value you generate yourself, register it:

```
echo "::add-mask::$DERIVED_VALUE"      # ::add-mask:: is a real workflow command
```

**Hole 2 — structured (JSON) secrets:** only the whole blob was registered; a field you parse out
isn't masked → `::add-mask::` it.

**Hole 3 — outputs are not a secret channel.** Values in `$GITHUB_OUTPUT` flow to GitHub and into
downstream jobs as ordinary data. *(Nuance: an actual registered secret read via `${{ secrets.X }}` is
redacted on the runner before being sent — but a value you minted yourself isn't registered, so that
protection doesn't apply.)* Exam-safe rule: **don't route secrets through outputs.**

**Hole 4 — script injection (the big one, also objective 5.3).** Untrusted input interpolated
directly into `run:` is substituted into the shell command before it runs → a malicious value becomes
executable code. Classic vector: PR title, branch name, issue body, commit message.

```yaml
# ❌ DANGEROUS — a title like  "; cat ~/.ssh/id_rsa; echo "  gets executed
- run: echo "Title: ${{ github.event.pull_request.title }}"

# ✅ SAFE — bind to env:, then quote in the script
- env:
    TITLE: ${{ github.event.pull_request.title }}
  run: echo "Title: $TITLE"
```

### Passing secrets around — the correct channels

You asked exactly where "passing" applies. Confirmed model:

```
Same workflow run (steps & jobs in one file):
  secrets context is available everywhere -> read ${{ secrets.X }} directly. No passing.

Calling a reusable workflow (workflow_call) = separate trust boundary:
  secrets do NOT cross automatically. Hand over via the secrets: block.
    with:    -> feeds called workflow's inputs:
    secrets: -> feeds called workflow's secrets:   (secrets: inherit = all of them)
```

The decision table (also on the cheat sheet):

```
Already a registered secret?  -> read ${{ secrets.X }} in the later job. Available run-wide; no passing.
Calling a reusable workflow?  -> hand it over via the secrets: block (or secrets: inherit).
A value you generated and must reuse downstream?
                              -> ::add-mask:: it, OR better: don't pass the credential at all —
                                 write the artifact/result it protects, not the secret.
```

> **On Q1 (corrected):** `echo "${{ secrets.TOKEN }}" | base64` → **masked (`***`)**, because GitHub
> redacts common encodings like Base64, not just the raw string. Earlier framing of this as a leak was
> wrong — verified live against the security-hardening docs. The genuine leak cases are *uncommon*
> transforms (e.g. `rev`, splitting), structured/JSON secrets, and `base64(secret+suffix)` padding.

---

## Your weak spots from the quizzes — focus revision here
Topic 1B was a clean sweep: **5/5, 5/5, 5/5.** No learner weak spots to flag.

Instead, the one *concept* to keep sharp (because it's exam-likely and subtle):
- **Masking is best-effort, not exhaustive.** It catches the raw secret + common encodings (Base64),
  but **not** arbitrary transforms, structured/JSON secrets, or `base64(secret+suffix)`. The defensive
  habit: register derived sensitive values with `::add-mask::`, and never store structured data as a
  secret.

## Sources (verified live, June 2026)
- Contexts (incl. `vars`, context availability) — docs.github.com/en/actions/.../contexts
- Variables (`vars`, org/repo/env precedence) — docs.github.com/en/actions/.../variables
- Defining outputs for jobs (matrix overwrite behavior) — docs.github.com/.../defining-outputs-for-jobs
- Evaluate expressions / `fromJSON` — docs.github.com/en/actions/.../evaluate-expressions-in-workflows-and-actions
- Security hardening for GitHub Actions (script injection, `::add-mask::`) — docs.github.com/en/actions/.../security-hardening-for-github-actions
