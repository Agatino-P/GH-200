# GH-200 — Combined Topic Recaps (All 14 Topics)

*Assembled 2026-06-24 20:18 UTC from repo `Agatino-P/gh-200` @ `0f2dd86`, folder `Study material/`. Each section is the per-topic recap reproduced verbatim, headings nested one level under the section title; content not edited. The condensed cheat for any topic is `GH-200_Cheat_<code>_...` (or the combined cheat-sheet file).*

## Contents


**Domain 1 — Author & maintain workflows**
- [Topic 1A — Triggers, Permissions, Inputs & Reusable Workflows](#topic-1a--triggers-permissions-inputs--reusable-workflows)
- [Topic 1B — Contexts, Expressions & Secret Leakage](#topic-1b--contexts-expressions--secret-leakage)
- [Topic 1C — Matrix Strategy In Depth](#topic-1c--matrix-strategy-in-depth)
- [Topic 1D — YAML Anchors, Aliases & Merge Keys](#topic-1d--yaml-anchors-aliases--merge-keys)
- [Topic 1E — Outputs, Summaries & Retention](#topic-1e--outputs-summaries--retention)

**Domain 2 — Troubleshoot**
- [Topic 2A — Troubleshooting Matrix Runs](#topic-2a--troubleshooting-matrix-runs)

**Domain 3 — Consume workflows & actions**
- [Topic 3A — Immutable Releases & Version Pinning](#topic-3a--immutable-releases--version-pinning)

**Domain 4 — Author & maintain actions / runners**
- [Topic 4A — Runner Networking & Access Boundaries](#topic-4a--runner-networking--access-boundaries)
- [Topic 4B — Runner Images & Toolcache](#topic-4b--runner-images--toolcache)
- [Topic 4C — Configuration Variables & Secrets/Variables REST API](#topic-4c--configuration-variables--secretsvariables-rest-api)

**Domain 5 — Secure & optimize**
- [Topic 5A — Untrusted Input & Token Hardening](#topic-5a--untrusted-input--token-hardening)
- [Topic 5B — OIDC Keyless Cloud Auth](#topic-5b--oidc-keyless-cloud-auth)
- [Topic 5C — Action Enforcement Policies & Build Provenance](#topic-5c--action-enforcement-policies--build-provenance)
- [Topic 5D — Optimizing Workflows & Managing Retention](#topic-5d--optimizing-workflows--managing-retention)


---

## Topic 1A — Triggers, Permissions, Inputs & Reusable Workflows

*Source: `GH-200_Topic_1A_-_Triggers_Permissions_Inputs_Reusable_Workflows.md`*

*Personalized recap. Covers Domain 1 gap objectives **1.2** (scope/permissions/events) and **1.3**
(`workflow_dispatch` inputs + `workflow_call` inputs/secrets). Facts verified against live GitHub
docs, June 2026. Quiz outcomes from this session are noted per bit, with a "weak spots" section at the end.*

---

### Bit 1 — Event categories & choosing a trigger  ·  *(quiz: 5/5)*

Every workflow starts with `on:`. Four families of triggers:

1. **Repository / webhook events** — `push`, `pull_request`, `issues`, `release`, `create`, `delete`, `fork`, … (delivered via GitHub's webhook system, hence "webhook" ≈ "repository" events).
2. **Scheduled** — `schedule:` + `cron` (UTC). Runs on the **default branch**; **minimum interval 5 minutes**; best-effort (can be **delayed under load** — avoid the top of the hour).
3. **Manual / external** — `workflow_dispatch` (internal: Run-workflow button, `gh workflow run`, API; supports typed `inputs`) and `repository_dispatch` (external system POSTs to the dispatches REST endpoint with a custom `event_type`).
4. **Workflow-triggered** — `workflow_call` (reusable workflows) and `workflow_run` (fires after another workflow finishes).

**Narrowing repository events:** activity `types:`, `branches:` / `branches-ignore:`, `paths:` / `paths-ignore:`, `tags:`. Note `tags:` applies to `push`, not `pull_request`.

```yaml
on:
  push:
    branches: [main]
    paths: ['src/**']
  pull_request:
    types: [opened, synchronize]
  schedule:
    - cron: '0 6 * * 1'   # 06:00 UTC Mondays
  workflow_dispatch:
```

---

### Bit 2 — `permissions`: workflow vs job scope, least-privilege default  ·  *(quiz: 5/5)*

`permissions:` sets what the automatic **`GITHUB_TOKEN`** may do. That token is **generated per job and expires when the job completes** — ephemeral and scoped, used to authenticate API calls back to the repo.

- **Two levels:** top-level `permissions:` (applies to all jobs) and `jobs.<id>.permissions:` (overrides for that job).
- **Job-level REPLACES, not merges** — and **any scope you don't list is set to `none`.** A `permissions` block is a fresh allow-list, not an add-on to the default.
- **Shorthands:** `read-all`, `write-all`, `{}` (strip everything to `none`).
- **Default is read-only** for new repos/orgs/enterprises (`contents` + `packages` read). It's an admin setting (Settings → Actions → General → "Workflow permissions"); **repo inherits from org, org from enterprise.**
- **Fork PRs:** token is read-only by design unless an admin enabled "Send write tokens to workflows from pull requests."
- **Failure tell:** `403: Resource not accessible by integration` = the token lacks the needed scope → add it to `permissions:`.

```yaml
permissions:
  contents: read          # workflow-wide default
jobs:
  triage:
    runs-on: ubuntu-latest
    permissions:          # replaces for this job → contents is now NONE here
      issues: write
      pull-requests: write
    steps:
      - uses: actions/stale@v9
```

---

### Bit 3 — `workflow_dispatch` typed inputs  ·  *(quiz: 4/5)*

**Five types (current docs):** `string`, `boolean`, `choice`, `number`, `environment`.
*(Historically `number` was excluded; the current official docs list it. Older practice questions may use the four-type legacy list.)*

**Properties:** `description` (optional here), `required`, `default`, `type`, `options` (choice only).
- `string` is the default if `type` is omitted.
- `choice` **requires `options:`**; `default` must be one of them.
- `boolean` → checkbox.
- `environment` → dropdown of configured environments. **But `type: environment` is only a picker** — protection rules and environment-scoped secrets apply **only when a job uses `environment:`** with that value, not from the input itself.

**Accessing values — the gotcha:**
- `${{ inputs.<name> }}` = modern, **typed** context. A boolean works directly: `if: ${{ inputs.flag }}`.
- `${{ github.event.inputs.<name> }}` = legacy, **always a string**. `"false"` is a non-empty string → **truthy**, so `if: ${{ github.event.inputs.flag }}` runs even when set to false.

**Limits:** up to **10 top-level inputs**; max payload **65,535 characters**. CLI: `gh workflow run x.yml -f key=value`.

> **Quiz miss (Q1):** "Which property is required for a `choice` input?" → **`options`**, not `description`.
> Keeper: `description` is required in a custom action's **`action.yml`**, but **not** on `workflow_dispatch` inputs.

---

### Bit 4 — Reusable workflows (`workflow_call`)  ·  *(quiz: 4/5)*

Defined with `on: workflow_call:` declaring `inputs`, `secrets`, (and optionally `outputs`).

- **Input types: `string`, `number`, `boolean` only** — **no `choice`, no `environment`** (those are dispatch-only).
- **`type` is REQUIRED** for `workflow_call` inputs (contrast: optional on dispatch).
- Implicit defaults if none set: `false` (boolean), `0` (number), `""` (string).

**Calling it** — at the **job level**, with a ref:
```yaml
jobs:
  call-deploy:
    uses: my-org/shared/.github/workflows/deploy.yml@v1   # ref required (@v1, @main, @sha)
    with:                       # inputs channel
      environment: production
      dry-run: false
    secrets:                    # secrets channel (separate!)
      deploy-token: ${{ secrets.PROD_TOKEN }}
    # or: secrets: inherit
```

- `secrets: inherit` passes **all** caller secrets (**org + repo level**), and **only works within the same org/enterprise.**
- **Trap #1:** `with:` and `secrets:` are separate channels. You **cannot** reference `secrets.*` inside the caller's `with:` — it's a **parse-time error**. Route secrets through `secrets:`.
- **Trap #2:** environment secrets can't be passed via `workflow_call`; instead set `environment:` on the reusable workflow's job.
- **Nesting** is allowed; **permissions can only be maintained or reduced down the chain — never elevated.** *(Exact nesting-depth / connected-workflow numeric limits not re-verified this session.)*

---

### Your weak spots from the quizzes — focus revision here
1. **Input-type lists by trigger** (missed in both Bit 3 and Bit 4). Lock it: **dispatch = string/boolean/choice/number/environment**; **call = string/number/boolean**; `type` **optional** on dispatch (defaults `string`) but **required** on call.
2. **`options` is the choice-only requirement** — not `description`.
3. **Reusable-workflow invocation = job-level `uses:` with a ref** (you had to scroll back for this — worth over-learning).

### Sources (verified live, June 2026)
- Controlling permissions for `GITHUB_TOKEN` — docs.github.com/en/actions/.../controlling-permissions-for-github_token
- Managing GitHub Actions settings for a repository / for an organization — docs.github.com
- "Updating the default GITHUB_TOKEN permissions to read-only" — github.blog/changelog (2023)
- Workflow syntax (`workflow_dispatch` & `workflow_call` inputs) — docs.github.com/.../workflow-syntax-for-github-actions
- Reuse workflows — docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows


---

## Topic 1B — Contexts, Expressions & Secret Leakage

*Source: `GH-200_Topic_1B_-_Contexts_Expressions_Secret_Leakage.md`*

*Personalized recap. Covers Domain 1 gap objectives **1.10** (contexts, esp. `vars`) and **1.11**
(expressions `${{ }}`: static/parse-time vs runtime; secret-leakage prevention). Facts verified
against live GitHub docs, June 2026. Quiz outcomes noted per bit, with a "weak spots" section at the end.*

---

### Bit 1 — Context families; `env` vs `vars` vs `secrets`  ·  *(quiz: 5/5)*

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

#### The three that get confused

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

#### Matrix primer (you'd seen it, now anchored — full depth is Topic 1C)

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

### Bit 2 — `${{ }}` evaluation: setup-time vs runtime  ·  *(quiz: 5/5)*

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
step-level if:                        github, needs, matrix, steps, runner, vars  (NO secrets)
step-level run: / with: / env         full set incl. secrets
   [CORRECTION 2026-06-25] secrets are NOT usable in if: (job OR step) -> "Unrecognized
   named-value: secrets". To gate on a secret: map to job env: then if: ${{ env.X != '' }}.
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

### Bit 3 — Preventing secret leakage in logs & expressions  ·  *(quiz: 5/5)*

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

#### Passing secrets around — the correct channels

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

### Your weak spots from the quizzes — focus revision here
Topic 1B was a clean sweep: **5/5, 5/5, 5/5.** No learner weak spots to flag.

Instead, the one *concept* to keep sharp (because it's exam-likely and subtle):
- **Masking is best-effort, not exhaustive.** It catches the raw secret + common encodings (Base64),
  but **not** arbitrary transforms, structured/JSON secrets, or `base64(secret+suffix)`. The defensive
  habit: register derived sensitive values with `::add-mask::`, and never store structured data as a
  secret.

### Sources (verified live, June 2026)
- Contexts (incl. `vars`, context availability) — docs.github.com/en/actions/.../contexts
- Variables (`vars`, org/repo/env precedence) — docs.github.com/en/actions/.../variables
- Defining outputs for jobs (matrix overwrite behavior) — docs.github.com/.../defining-outputs-for-jobs
- Evaluate expressions / `fromJSON` — docs.github.com/en/actions/.../evaluate-expressions-in-workflows-and-actions
- Security hardening for GitHub Actions (script injection, `::add-mask::`) — docs.github.com/en/actions/.../security-hardening-for-github-actions


---

## Topic 1C — Matrix Strategy In Depth

*Source: `GH-200_Topic_1C_-_Matrix_Strategy_In_Depth.md`*

*Personalized recap. Covers Domain 1 objective **1.8** (matrix strategy: cross-product, `include`/`exclude`,
failure & concurrency control, dynamic matrices, **runner images**). Facts verified against live GitHub docs,
June 2026. Quiz outcomes per bit noted; weak-spots section at the end.*

---

### Where everything lives (read this first)

The bits across 1B/1C touched keys at different levels; here is the single map so it's never ambiguous:

```
workflow
├─ name:                          WORKFLOW level
├─ on:                            WORKFLOW level
└─ jobs:                          WORKFLOW level
   └─ <job_id>:                   one JOB
      ├─ runs-on:                 JOB level
      ├─ continue-on-error:       JOB level   (ALSO valid per step — see below)
      ├─ needs:                   JOB level
      ├─ strategy:                JOB level
      │  ├─ matrix:               under strategy
      │  ├─ fail-fast:            under strategy   (matrix-wide policy)
      │  └─ max-parallel:         under strategy   (matrix-wide policy)
      └─ steps:                   JOB level
         └─ - <step>:
              └─ continue-on-error:   STEP level
```

Key distinctions to memorize:

```
matrix / fail-fast / max-parallel  -> ONLY under strategy:
continue-on-error                  -> on a JOB, OR on a STEP (NOT under strategy:)
runs-on / needs                    -> JOB level
```

---

### Bit 1 — Cross-product, `exclude`, `include`  ·  *(quiz: 5/5)*

**Resolution order (the whole key):**

```
1. EXPAND   cross-product of all axes -> base combinations
2. EXCLUDE  remove base combos matching an exclude entry
3. INCLUDE  evaluated AFTER exclude -> can even re-add an excluded combo
```

**exclude** — removes any base combo matching *all* keys in the entry. A partial entry removes a whole
slice. Entries do **not** accept arrays — one scalar set per list item.

```yaml
strategy:
  matrix:
    version: [10, 12, 14]
    os: [ubuntu-latest, windows-latest]   # 6 base combos
    exclude:
      - version: 14
        os: windows-latest                # -> 5 jobs
```

**include** — two behaviors depending on whether the entry's matrix keys match an existing combo:

```
keys MATCH an existing combo   -> AUGMENT it (add the extra keys)
keys DON'T match any combo     -> create a NEW combo
original axis values           -> NEVER overwritten
include-added keys             -> CAN be overwritten by a later include
```

```yaml
include:
  - version: 16
    os: ubuntu-latest    # {16, ubuntu} isn't a base combo -> NEW combo (test 16 only on ubuntu)
  - version: 12
    os: ubuntu-latest
    npm: 6               # {12, ubuntu} exists -> AUGMENT (adds npm:6)
```

**include-only** (no base axes) = an explicit hand-picked combo list:

```yaml
strategy:
  matrix:
    include:
      - version: 12
        os: ubuntu-latest
      - version: 14
        os: windows-latest   # exactly 2 jobs, no cross-product
```

> The full canonical docs example (`fruit`/`animal`/`color`/`shape`, 5 include entries → 6 jobs) is
> fiddly because include entries are evaluated against the *original* combos, not combos created by
> *earlier* includes. For GH-200, internalize the augment-vs-new-combo rule above; don't memorize the trace.

---

### Bit 2 — `fail-fast`, `max-parallel`, `continue-on-error`  ·  *(quiz: 5/5)*

**`fail-fast` — default `true`.** First matrix combo counted as a failure → GitHub cancels all
in-progress and queued combos. Set `false` for full reports / debugging / cross-platform runs.

**`max-parallel`** — caps how many combos run simultaneously (default = as many as runner/account
limits allow). It caps a **count**, not an "axis". Specific sizing numbers are judgement, not exam facts.

**`continue-on-error`** — on a JOB or a STEP. When `true`, that unit's failure doesn't fail the run.

#### The interaction (exam-worthy)

```
fail-fast fires ONLY on a combo COUNTED as a failure.
continue-on-error: true  -> that combo's failure is NOT counted.
=> a continue-on-error combo can fail WITHOUT cancelling its siblings and WITHOUT failing the run.
```

Idiomatic carve-out (per-combo, via a matrix axis):

```yaml
strategy:
  fail-fast: true
  matrix:
    version: [9, 10, 11]
    experimental: [false]
    include:
      - version: 12
        experimental: true        # allowed to fail
runs-on: ubuntu-latest
continue-on-error: ${{ matrix.experimental }}   # NOT a flat true
```

```
fail-fast: true + continue-on-error: true (FLAT)        -> pointless (fail-fast inert)
fail-fast: true + continue-on-error: ${{ matrix.x }}    -> meaningful (carve-out for some combos)
```

#### ⚠️ Swallow vs preserve — the gotcha

```
continue-on-error  -> SWALLOWS the failure: run not failed, AND downstream needs: sees SUCCESS.
fail-fast: false   -> PRESERVES the failure: doesn't cancel siblings, but failure still counts
                      (downstream needs: is blocked).
```

So "let all combos finish but still treat a failure as a failure" = **`fail-fast: false`**, NOT
`continue-on-error`.

#### Complete annotated example (every key, with its level)

```yaml
name: CI                          # WORKFLOW
on: [push]                        # WORKFLOW
jobs:                             # WORKFLOW
  test:                           # JOB id
    runs-on: ${{ matrix.os }}     # JOB
    continue-on-error: ${{ matrix.experimental }}   # JOB (swallow failure for experimental combos)
    strategy:                     # JOB
      fail-fast: false            #   under strategy (don't cancel siblings)
      max-parallel: 3             #   under strategy (<=3 at once)
      matrix:                     #   under strategy
        os: [ubuntu-latest, windows-latest]
        version: [18, 20]
        experimental: [false]
        include:
          - os: ubuntu-latest
            version: 22
            experimental: true    # one allowed-to-fail combo
    steps:                        # JOB
      - uses: actions/checkout@v4
      - name: Flaky optional check
        continue-on-error: true   # STEP (this single step may fail without failing the job)
        run: ./maybe-flaky.sh
      - name: Real test
        run: ./test.sh "${{ matrix.version }}"

  deploy:                         # second JOB
    needs: test                   # waits for the WHOLE test matrix (one graph node)
    runs-on: ubuntu-latest
    steps:
      - run: ./deploy.sh
```

---

### Bit 3 — Dynamic matrices via `fromJSON`  ·  *(quiz: 5/5)*

**Why:** matrix is expanded at **setup**, before any step runs — so you can't build it from a same-job
step output. Instead, a **prior job** emits the combinations as a JSON string output; a downstream job
(`needs:` it) feeds that JSON into its matrix with `fromJSON`. (`fromJSON` is a real built-in.)

```yaml
jobs:
  generate:
    runs-on: ubuntu-latest
    outputs:
      matrix: ${{ steps.set.outputs.matrix }}     # step output -> JOB output
    steps:
      - id: set
        run: echo 'matrix={"version":[10,12,14]}' >> "$GITHUB_OUTPUT"
  build:
    needs: generate                               # MANDATORY — no needs:, no output
    runs-on: ubuntu-latest
    strategy:
      matrix: ${{ fromJSON(needs.generate.outputs.matrix) }}
    steps:
      - run: echo "${{ matrix.version }}"
```

A JSON **object** assigned to `matrix` turns each property into an axis. The three shapes — producer
JSON first, then the consumer YAML:

**Shape 1 — whole matrix from a JSON object** (properties become axes → cross-product)

```json
{ "version": [10, 12], "os": ["ubuntu-latest", "windows-latest"] }
```

```yaml
strategy:
  matrix: ${{ fromJSON(needs.gen.outputs.m) }}      # 2 x 2 = 4 jobs
```

**Shape 2 — one axis from a JSON array** (only that axis is dynamic)

```json
["ubuntu-latest", "windows-latest"]
```

```yaml
strategy:
  matrix:
    os: ${{ fromJSON(needs.gen.outputs.oslist) }}
    version: [18, 20]                               # 2 x 2 = 4 jobs
```

**Shape 3 — an `include` list from a JSON array** (explicit hand-picked combos)

```json
[ { "version": 10, "os": "ubuntu-latest" }, { "version": 14, "os": "windows-latest" } ]
```

```yaml
strategy:
  matrix:
    include: ${{ fromJSON(needs.gen.outputs.combos) }}   # exactly 2 jobs
```

Mental grouping:

```
object -> whole matrix (keys = axes, cross-product)
array  -> feeds ONE thing: a single axis OR the include list
```

**Gotchas:**

```
- needs: is mandatory.
- The output is a STRING; fromJSON parses it. Malformed JSON -> matrix fails to expand.
- Build JSON on ONE line (e.g. jq -c) — a job output is a single-line string.
- Empty array -> ZERO jobs (job skipped, not failed). Guard with a has_changes output + if: if needed.
```

> **Exam-scope note:** the *concept* (matrix fixed at setup → feed from a prior job's JSON output via
> `needs:` + `fromJSON`) is fair game for 1.8. How heavily GH-200 drills the producer/`jq` machinery
> specifically is **not confirmed** — the official guide lists matrix strategy broadly. Know the
> pattern + shapes at recognition level; don't over-invest in hand-writing `jq`. Calibrate vs practice exams.

---

### Bit 4 — Runner images & the `-latest` moving target  ·  *(quiz: 5/5)*  ·  verified live June 2026

**Core concept:** `ubuntu-latest` / `windows-latest` / `macos-latest` are **floating labels**, not fixed
environments. GitHub re-points them to newer OS images over time; the migration is **gradual (~1–2
months)**, so a workflow on a `-latest` label can land on a different OS version month-to-month.

```
-latest label        -> auto-updates, convenient, NON-deterministic over time
pinned version label -> reproducible; you choose when to upgrade
   e.g. ubuntu-24.04, ubuntu-22.04, windows-2025, windows-2022, macos-15
```

**Current mappings (snapshot June 2026 — these DRIFT, verify live when it matters):**

```
ubuntu-latest   -> Ubuntu 24.04         (22.04 -> 24.04 default migration completed Jan 17 2025)
windows-latest  -> Windows Server 2025  (also addressable as windows-2025)
macos-latest    -> macOS 15, Arm64      (gotcha: -latest is now Apple-silicon)
```

**The deprecation the study guide flags — Ubuntu 20.04:**

```
20.04 image: deprecation began 2025-02-01, fully unsupported by 2025-04-01.
=> As of mid-2026 it is GONE. A workflow pinned to ubuntu-20.04 FAILS (image not found).
```

**Key nuance (exam trap):** pinning protects against *silent migration*, **not** against *deprecation*.
A pinned old label still dies when GitHub retires the image — pinning buys reproducibility + a chosen
upgrade schedule, not immortality.

**Newer context (likely beyond the Jan-2026 exam — don't memorize, just don't be surprised):**

```
- Ubuntu 26.04 exists as PUBLIC PREVIEW (label ubuntu-26.04), not the default.
- windows-latest / windows-2025 migrating to "Windows Server 2025 with Visual Studio 2026"
  as default (rollout June 8–15 2026). OS stays Server 2025; the toolset changes.
```

**Connects to:** 1.8 (matrix `os` axis) · 4.6 (preinstalled software / toolcache — deeper there) ·
5.6 (same reproducibility logic as pinning actions to SHAs).

---

### Your weak spots from the quizzes — focus revision here
Topic 1C was a clean sweep: **5/5, 5/5, 5/5, 5/5.** No standing learner weak spots.

Concepts to keep sharp (subtle + exam-likely):
1. **Resolution order = expand → exclude → include** (include last; can re-add excluded combos). One
   blog online states this backwards — it's wrong.
2. **Swallow vs preserve:** `continue-on-error` hides a failure (downstream sees success);
   `fail-fast: false` keeps the failure but spares the siblings.
3. **Matrix is fixed at setup** → dynamic matrices require a *prior* job + `needs:` + `fromJSON`, never
   a same-job step output.
4. **Pinning ≠ immortality:** a pinned runner label (e.g. `ubuntu-20.04`) still fails once the image is
   deprecated. Pinning stops *silent migration*, not *deprecation*.

### Sources (verified live, June 2026)
- Workflow syntax — matrix / `include` / `exclude` / `fail-fast` / `max-parallel` — docs.github.com/.../workflow-syntax-for-github-actions
- Running variations of jobs in a workflow (matrix) — docs.github.com/en/actions/.../running-variations-of-jobs-in-a-workflow
- Evaluate expressions / `fromJSON` (returning a JSON object) — docs.github.com/en/actions/.../expressions
- `continue-on-error` × `fail-fast` interaction — corroborated across community discussions + vendor guides (Octopus/Codefresh, copdips)


---

## Topic 1D — YAML Anchors, Aliases & Merge Keys

*Source: `GH-200_Topic_1D_-_YAML_Anchors_Aliases_Merge_Keys.md`*

*Personalized recap. Covers Domain 1 objective **1.9** (YAML anchors `&`, aliases `*`, merge keys `<<`),
which also serves Domain 2 objective **2.3** (reading/expanding anchored YAML when analyzing a workflow).
Facts verified against live GitHub docs + changelog, June 2026. Quiz outcomes per bit noted; weak-spots
section at the end.*

---

### The one-line summary (read this first)

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

### Bit 1 — Anchors `&` and aliases `*`  ·  *(quiz: 5/5)*

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

### Bit 2 — Merge keys `<<`  ·  *(quiz: 4/4)*

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

### Q&A outcomes / things the learner pushed on

- **"How can an unsupported feature be quizzed / be worth quizzing?"** — Resolved: on a
  recognition-based exam, *non-support is the question*. The item type is "spot the mistake" /
  "which is valid" / "what's the correct fallback," not free recall. A `<<: *base` config is a
  distractor designed to catch people who assume full YAML support carries over.
- Confirmed the learner can discriminate supported vs unsupported cleanly (Bit 2 quiz 4/4, including
  the True/False trap "anchors imply merge keys" → False).

---

### Exam-weight uncertainty (calibrate against practice exams)

- Anchor support is so new (Sept 2025) relative to the **Jan 2026 exam reword** that I **cannot verify
  how heavily, or in what form, GH-200 tests it.** Best *inference* (not a confirmed fact): the exam
  leans toward the *reading/analysis* style (objective 2.3) — "read this anchored config, what does it
  produce" and "spot the invalid `<<`." Treat weight as unknown until practice-exam data exists.

---

### Weak-spots / watch-list for review

- Don't let "GitHub supports YAML anchors" drift into "GitHub supports all YAML reuse features." It's
  `&`/`*` **only**; `<<` is out.
- Remember the **define-before-use** ordering rule — an alias above its anchor errors.
- When a scenario needs *base + per-job overrides*, the answer is **composite action / reusable
  workflow**, never a merge key.


---

## Topic 1E — Outputs, Summaries & Retention

*Source: `GH-200_Topic_1E_-_Outputs_Summaries_Retention.md`*

*Personalized recap. Covers Domain 1 objectives **1.14** (job summaries), **1.16** (caching/artifacts +
retention via REST API; overlaps **5.9**), and **1.12** (VS Code editor tooling). All current-state facts
(retention numbers, REST endpoints, extension limits) verified live against official GitHub docs, June 2026.
Quiz outcomes per bit noted; weak-spots at the end.*

---

### Bit 1 — Job summaries via `GITHUB_STEP_SUMMARY`  ·  *(quiz: effectively 5/5)*

**What it is.** `GITHUB_STEP_SUMMARY` is an **environment file** — the variable holds a *file path*, not a
value. Append GitHub-Flavored Markdown to that file and GitHub renders it on the workflow **run summary
page**. Purpose: surface readable output (test tables, build reports, links) so people don't dig through logs.

**Writing to it.** `>>` appends (a newline is auto-added per append); `>` overwrites/clears the **current
step's** buffer. PowerShell uses `$env:GITHUB_STEP_SUMMARY`.

```yaml
steps:
  - name: Write summary
    run: |
      echo "## Test Results" >> $GITHUB_STEP_SUMMARY
      echo "| Suite | Passed | Failed |" >> $GITHUB_STEP_SUMMARY
      echo "|-------|--------|--------|" >> $GITHUB_STEP_SUMMARY
      echo "| Unit  | 142    | 0      |" >> $GITHUB_STEP_SUMMARY
```

**Step isolation — the keeper (flagged to cheat sheet):**

```
- GITHUB_STEP_SUMMARY is a SEPARATE file PER STEP. Steps are isolated.
- `>>` appends to the CURRENT step's file; `>` overwrites ONLY the current step's buffer.
- `>` can NEVER wipe another step's summary. At job end all step files are grouped into one job summary.
- Across jobs: job summaries are ordered by JOB COMPLETION TIME (not definition order).
- (Trap: assuming `>` in a later step clears the whole job summary — it doesn't.)
```

Isolation is enforced so malformed Markdown from one step can't break rendering for the others.

**The number to memorize — 1 MiB per step (verified).** Each step's summary is capped at 1 MiB; exceeding
it **aborts the summary upload** for that step (real error: "supports content up to a size of 1024k") —
it fails rather than silently truncating.

**What renders.** Full GFM: tables, task lists, Mermaid, alert blocks (`> [!NOTE]`, `> [!CAUTION]`). Some
HTML works (`<details>`), but a `<details>` opened in one step and closed in another won't wrap as expected
(step isolation breaks the tag) — keep a `<details>` block inside one step's write.

**Don't confuse the four environment-file siblings** (all written with `>>`, different purposes):

```
GITHUB_STEP_SUMMARY -> Markdown for HUMANS, shown on the run summary page
GITHUB_OUTPUT       -> step OUTPUT for machines (read via steps.<id>.outputs.*)
GITHUB_ENV          -> env var for LATER STEPS in the same job ($NAME)
::warning:: / ::error:: (annotations) -> inline highlights, not rich content
```

Caution: the summary is **user-facing output** — don't write sensitive data into it. (Whether secret-masking
covers the summary file the same way it covers logs is **unverified** — treat it as exposed.)

---

### Bit 2 — Caching vs artifacts; retention via REST API  ·  *(quiz: effectively 5/5)*

#### Artifacts vs cache — opposite purposes

```
ARTIFACTS  -> persist a run's OUTPUTS: share between jobs, download from UI/API,
              inspect after the run. Reliable & retained. upload-artifact / download-artifact.
CACHE      -> SPEED optimization: restore deps/intermediate files across runs by KEY.
              Best-effort, can be EVICTED, NOT guaranteed. actions/cache.
```

Decision rule: need the file reliably / hand an output to another job or human → **artifact**. Just avoiding
re-download/re-build of dependencies → **cache**.

Anti-patterns the exam likes:
- Cache used to **pass build output between jobs** → unreliable (can miss/evict). Use an artifact.
- Artifacts used as a **dependency cache** → slow, burns retention storage. Use the cache.

Cross-job data, pick by payload type:

```
small STRING / metadata       -> job output  (needs.<job>.outputs.X)
FILE / binary / build output  -> ARTIFACT    (upload -> download)
(cache is NOT a cross-job transfer mechanism — best-effort, can miss)
```

#### Retention numbers (verified) — two DIFFERENT sets, easy to confuse

```
ARTIFACTS/LOGS retention: default 90d | public ≤ 90 | private/internal ≤ 400
CACHE retention:          default  7d | public ≤ 90 | private/internal ≤ 365
CACHE size cap:           10 GB / repo default, LRU eviction over the limit
```

Per-artifact override with `retention-days:` (capped by repo/org/enterprise policy). Customizing retention
applies only to **new** artifacts/logs, not retroactively.

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: build-output
    path: dist/
    retention-days: 7      # shorter than the 90-day default
```

**Versions:** `actions/upload-artifact@v4` / `download-artifact@v4` are current; **v3 was deprecated and
stopped working** — a v3-pinned workflow fails today. (v4 behavioral change, stated from general knowledge,
not re-verified: artifact names must be unique within a run — re-uploading the same name errors.)

#### Retention via REST API (verified endpoints)

The documented way to *manage* retention programmatically is **list + delete** (e.g. a scheduled cleanup job):

```
GET    /repos/{owner}/{repo}/actions/artifacts                    # list repo artifacts
GET    /repos/{owner}/{repo}/actions/runs/{run_id}/artifacts      # list a run's artifacts
GET    /repos/{owner}/{repo}/actions/artifacts/{artifact_id}      # get one
DELETE /repos/{owner}/{repo}/actions/artifacts/{artifact_id}      # delete one  <- the workhorse
GET    /repos/{owner}/{repo}/actions/artifacts/{artifact_id}/{archive_format}   # download
```

Download endpoint specifics (verified): returns a redirect URL that **expires after 1 minute** (look for
`Location:` in the response header), and `archive_format` must be `zip`.

**Two honesty flags (carried forward):**
1. I could **not** find an official REST endpoint to *set* default retention-days at repo level. A
   third-party guide floated `PUT /repos/{owner}/{repo}/actions/retention`, but it does **not** appear in
   GitHub's official REST reference — treat as **unverified / likely not official**. The verified API path
   to "enforce retention" is list-then-delete; default-retention *configuration* is a UI / org-policy
   setting, not (as far as I can confirm) a REST call.
2. A **cache** REST API also exists (list caches, delete by key or id, get usage), but only the **artifact**
   endpoints above were verified this session — confirm exact cache paths before relying on them.

---

### Bit 3 (short) — VS Code GitHub Actions extension  ·  *(quiz: 3/3)*

**What it is.** Official extension `GitHub.vscode-github-actions`, now maintained by GitHub (began as a
community project; the old community extension auto-upgrades to it; uses the official Actions schema).
Not the same as the third-party "GitHub Local Actions" extension, which runs workflows locally via the
`act` CLI.

**Two capability areas:**

```
1. AUTHORING workflow YAML
   - syntax highlighting (workflows + expressions)
   - validation + code completion against the official schema
   - SMART validation: detects bad references between jobs/steps (not just static schema),
     and validates/completes against the actual event payload from your `on:` triggers
   - inline docs for schema, expression functions, event payloads

2. MANAGING / MONITORING runs (without leaving the editor)
   - view runs, cancel, re-run, trigger workflow_dispatch workflows
   - drill runs -> jobs -> steps, view logs
```

**Setup:** install from Marketplace → sign in with GitHub + allow access → open a repo → Actions icon in
the left nav.

**Limitations (verified — likely the exam's "what it can't do"):**
- **No remote repositories**, including **github.dev** and **vscode.dev** — use a locally cloned repo.
- GitHub Enterprise Server support is an **experimental, unsupported beta** (`use-enterprise` setting).

---

### Exam-weight notes (calibrate against practice exams)

- Job summaries (1.14) and retention-via-REST-API (1.16/5.9) are **new/thin** objectives from the Jan 2026
  reword — likely tested at recognition level ("what does this do", "which file/endpoint"). Weight unverified.
- The VS Code extension (1.12) is almost certainly **low-weight recognition** — don't over-invest here
  relative to the expressions/YAML topics. Weight unverified.

---

### Weak-spots / watch-list for review

- **Two retention number sets are different** — artifacts default 90 (private max 400); cache default 7
  (private max 365). Don't merge them.
- `>` only clears the **current step's** summary; it can't reach other steps. At job end everything groups.
- For cross-job transfer: **files → artifact, strings → job output**; cache is best-effort, not a transfer tool.
- The `PUT .../actions/retention` endpoint is **unverified** — don't cite it as fact on the exam; the
  reliable REST retention story is **list + `DELETE` artifacts**.


---

## Topic 2A — Troubleshooting Matrix Runs

*Source: `GH-200_Topic_2A_-_Troubleshooting_Matrix_Runs.md`*

*Personalized recap. Covers Domain 2 objective **2.4** (correlate matrix jobs↔axes, analyze variant
failures, rerun individual matrix jobs); cross-refs Topic 1C (matrix mechanics, `fail-fast`). Domain 2's
other gap (2.3, reading YAML anchors) was already covered in Topic 1D. All current-state facts (rerun
scopes/surfaces, REST endpoints, the attempt-archiving behavior) verified live against official GitHub
docs/changelog, June 2026. Quiz outcomes per bit noted; weak-spots at the end.*

---

### Bit 1 — Reading matrix job names & analyzing variant failures  ·  *(quiz: 5/5)*

**Auto-naming convention.** Each matrix combination becomes its own job, labeled:

```
<job_name> (value1, value2, ...)
```

Values appear in the **order the matrix keys are declared**, comma-separated. Example:

```yaml
jobs:
  build:                       # <job_id>
    runs-on: ubuntu-latest
    strategy:
      matrix:
        arch: [x64, arm64]     # declared first
        node: [18, 20]         # declared second
    steps:
      - run: echo build
```

→ the `arch=arm64, node=18` leg is labeled `build (arm64, 18)` — `arch` value first because `arch` is
declared first. **Correlating a label back to axes = the core 2.4 skill**, and it depends entirely on
declaration order; you usually need the YAML in hand to decode a bare label like `(arm64, 18)`.

**Custom label via `name:` (a JOB-LEVEL attribute).** `name:` lives at `jobs.<job_id>.name`, a sibling of
`runs-on`/`strategy`/`steps` — NOT inside `strategy` or `matrix`. It's evaluated per combination, so it can
interpolate the `matrix` context:

```yaml
jobs:
  test:
    name: test ${{ matrix.os }} / ruby-${{ matrix.ruby }}   # jobs.test.name — overrides the auto-label
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest]
        ruby: ["3.0", "3.1"]
    steps:
      - uses: actions/checkout@v4
      - run: echo "ruby ${{ matrix.ruby }} on ${{ matrix.os }}"
```

`name:` exists on any job (matrix or not); what's special in the matrix case is only that the `matrix`
context is available to interpolate. Omit it and you get the auto-label `test (ubuntu-latest, 3.0)` etc.

**The key troubleshooting insight — cancelled ≠ failed (the `fail-fast` trap).** With the default
`fail-fast: true`, if one matrix job fails, all other in-progress and queued legs are **cancelled**. So a
failed run often shows *one* genuinely failed variant plus several **cancelled** ones:

```
- The variant that actually FAILED is the culprit. Cancelled legs are fail-fast collateral.
- A cancelled leg's true result is UNKNOWN — it might have passed.
- To see every variant's real pass/fail, set fail-fast: false and re-run → each leg runs to completion.
```

`fail-fast: false` is the standard move for "is this failure specific to one combination or broad?"

**Two smaller facts:**
- GitHub does **not** guarantee the order matrix jobs run/finish in — decode results from the label, never from timing.
- Inside a job: `matrix` context = current combination; `strategy.job-index` = zero-based position in the matrix.

---

### Bit 2 — Rerunning failed work  ·  *(quiz: 4/4 + correct reasoning on an ambiguous item)*

**Three rerun scopes** (since the March 2022 partial-rerun feature). Each matrix leg is its own job, so a
**single matrix variant can be rerun** on its own:

```
Re-run all jobs      -> the whole run again
Re-run failed jobs   -> only failed jobs + their downstream dependents   [documented behavior]
Re-run a single job  -> one specific job (e.g. one matrix leg)
```

**Three surfaces:**

*UI* — "Re-run jobs" dropdown (all / failed), per-job hover re-run icon, or from the logs view.

*CLI* (`gh run rerun`):
```bash
gh run rerun <RUN_ID>            # re-run all
gh run rerun <RUN_ID> --failed   # re-run only failed jobs
gh run rerun --job <JOB_ID>      # re-run one specific job
# --debug on any of these enables step debug logging for the re-run
```

*REST API:*
```
POST /repos/{owner}/{repo}/actions/runs/{run_id}/rerun                # all
POST /repos/{owner}/{repo}/actions/runs/{run_id}/rerun-failed-jobs    # failed
POST /repos/{owner}/{repo}/actions/jobs/{job_id}/rerun                # single job
```

**Re-runs create a new ATTEMPT** — they don't overwrite the old run. New-run jobs appear alongside previous
ones, an attempt-navigation dropdown moves between attempts, the re-run reuses the original commit SHA, and
the partial-rerun confirmation lists every job that will run (including downstream dependents).
*(Whether a re-run always re-reads the latest workflow-file version vs the original attempt's version is not
precisely verified — flagged.)*

**KEEPER GOTCHA — single-job API reruns archive the prior attempt.** Re-running one job via
`POST .../actions/jobs/{job_id}/rerun` spins up a **new attempt**; the remaining failed jobs then belong to
the **previous (archived) attempt**, so individually re-running a second old failure returns
**HTTP 403 "Only jobs from the current attempt can be re-run."**

```
- There is NO endpoint to re-run a chosen SUBSET of jobs in one call.
- Options: rerun-failed-jobs (ALL failures) OR one single job at a time.
- After ONE single-job rerun, the OTHER old failures can't be picked off individually (403, archived attempt).
  -> To retry several specific legs: use rerun-failed-jobs, or re-run them before a new attempt archives them.
```

---

### Q&A outcomes / things the learner pushed on

- **Floating snippet challenged.** The learner correctly called out a `name:` snippet shown without context.
  Resolution captured above: `name:` is `jobs.<job_id>.name`, a job-level sibling of `runs-on`/`strategy`/
  `steps`, evaluated per matrix combination. (Going forward, YAML snippets show full nesting.)
- **Quiz Q2 ambiguity (documented behavior vs bug).** The learner flagged that "what does Re-run failed jobs
  run?" was ambiguous after I'd emphasized a bug. Clean separation:
  - **Documented/intended (exam answer):** failed jobs **+ their downstream dependents**.
  - **Edge bug (not the rule):** with *matrixed reusable workflows*, downstream dependents inside the
    reusable workflow have been observed not to restart. Know it as a "why didn't my dependent rerun?"
    troubleshooting note, not as the general behavior.

---

### Exam-weight notes (calibrate against practice exams)

- 2.4 is a 🟡 partial gap; matrix basics were course-covered, so the *new* surface here is **reading
  labels/axis correlation**, the **fail-fast cancelled-vs-failed** reading, and **rerun granularity**.
  Likely recognition-level ("which combination failed", "cheapest way to retry one leg", "what does
  rerun-failed include"). Weight unverified.

---

### Weak-spots / watch-list for review

- Decode matrix labels by **declaration order**, never by finish order (run order isn't guaranteed).
- In a fail-fast run, **cancelled legs are collateral, not failures** — the culprit is the one that failed;
  use `fail-fast: false` to get a clean per-variant map.
- **Single-job API rerun archives the attempt** → can't then individually rerun the other old failures
  (403); no subset-rerun endpoint. Use `rerun-failed-jobs` for several at once.
- `name:` is a job attribute (`jobs.<job_id>.name`), not part of `strategy`/`matrix`.


---

## Topic 3A — Immutable Releases & Version Pinning

*Source: `GH-200_Topic_3A_-_Immutable_Releases_and_Version_Pinning.md`*

*Recap note. Objective **3.2** (immutable actions rollout + registry-source implications + version pinning). Standalone Domain 3 topic; the **enforcement** side (org rulesets, required SHA pinning, blocking disallowed actions) is deliberately deferred to **5.6**. Paired cheat file: `GH-200_Cheat_3A_-_Immutable_Releases_and_Version_Pinning.md`.*

*Verified live (June 2026) against GitHub Docs + Changelog. Items I could not confirm are flagged ⚠️ rather than asserted.*

---

### Bit 1 — Immutable releases: what it locks, how it's enabled

#### The problem it solves
By default a **Git tag is movable** and **release assets are editable**. So a compromised maintainer account — or a careless maintainer — can re-point `v1.2.0` to a different commit, or swap an uploaded binary, *after* you've already pinned to it. You'd run different code under the same reference and never notice. Immutable releases removes that attack surface.

#### What it is
A **repository setting**, also settable at the **organization** level, and toggleable via **REST API**. It is a **GitHub Releases** supply-chain feature — *not* actions-specific — but action authors enable it on their action's repo. When on, **every new release is immutable**.

> Key framing: it's a **setting**, not a workflow-YAML key. There is no `immutable: true` in `.github/workflows`. (Spot-the-mistake bait.)

#### What gets locked once a release is immutable
- **Assets** — files attached to the release can't be added, modified, or deleted.
- **The Git tag** — locked to its specific commit; can't be moved or deleted while the release exists. *(This is the lock that actually defeats the re-pointing attack — easy to forget alongside the asset lock.)*
- **Resurrection protection** — if you delete the immutable release you may delete the tag, but you **cannot reuse that tag name** afterward — even in a freshly recreated repo of the same name.

#### Attestation
Creating an immutable release **auto-generates a signed release attestation** (a verifiable record of the release tag, commit SHA, and assets). Format = **Sigstore bundle**. Verify with:

```
gh release verify <tag>
gh release verify-asset <tag> <asset>
```

#### Two behaviors worth memorizing
- **Disabling immutability later does NOT un-freeze** releases created while it was on — those stay immutable.
- Publishing locks everything immediately, so the recommended authoring flow is: **create as draft → attach all assets → publish**.

#### Tie to action versioning (the lever into Bit 2)
Immutability attaches to the **release**, not to a bare tag. So if an author *wants* a movable tag — e.g. keeping `v1` floating to the newest `v1.x` — the docs are explicit: **don't create a release for it**, just push/move the bare tag.

That single authoring choice ("no release = movable") is exactly what leaves a floating tag **unprotected for the consumer**. Same coin, two sides.

```yaml
# Author side: a release published from this workflow is immutable
# ONLY IF the repo/org has immutable releases enabled.
on:
  release:
    types: [published]
# the enable/disable toggle lives in repo/org settings or the REST API,
# NOT in workflow YAML.
```

#### ⚠️ Honesty flag — the OCI / ghcr.io publishing path
Objective 3.2 mentions "registry-source implications." There is a concept of publishing an action as an **OCI artifact to GitHub Packages / `ghcr.io`**, consumed by SemVer. **Status is conflicting and unconfirmed:** a roadmap card labels "Immutable Actions" GA, but the first-party `actions/publish-immutable-action` README *currently* still states it is **not ready for public use** and uploads won't work until fully released. Treated here as **NOT confirmed usable** — mechanics not drilled. **Calibrate its exam weight against practice exams.**

#### ⚠️ Do not confuse with — immutable *subject claims* (OIDC)
A separate feature, "**immutable subject claims**," changes the **OIDC token subject format** (auto-enforced for new repos from ~July 15 2026). It is unrelated to immutable releases. Belongs to **OIDC (objective 5.5)**, not here.

---

### Bit 2 — The version-pinning spectrum (consumer side)

When you write `uses: owner/action@REF`, the `REF` decides how much can change under you. Least → most resistant to silent change:

```yaml
uses: owner/act@main          # branch    — moves on EVERY push          (worst)
uses: owner/act@v4            # major tag — floats to latest v4.x
uses: owner/act@v4.1.0        # version tag — specific, but still a movable pointer
uses: owner/act@<40-char-sha> # full commit SHA — content-addressed       (best)
```

#### Why the ordering
- A **branch** ref changes on every push, with no version signal — most dangerous.
- A **tag** (`v4` or `v4.1.0`) is just a **movable pointer to a commit**. It can be re-pointed by the maintainer or an attacker. `v4` is *designed* to float (newest `v4.x`), so it's looser than `v4.1.0`, but **both are mutable pointers in principle**.
- A **full 40-char commit SHA** is **content-addressed**: it names an exact tree and **can't be re-pointed** (changing content changes the SHA). Guarantees byte-for-byte the same action every run. GitHub's standard recommendation for third-party actions.

#### Full vs short SHA
Use the **full 40-character** SHA. Short SHAs are ambiguous and are not accepted where full-SHA pinning is expected. *(Enforcement details — org policy that can require full-SHA pinning — are in 5.6.)*

#### Trade-offs of SHA pinning (so it's not treated as free)
- Loss of readability — `a1b2c3…` doesn't tell you it's "v4.1.0 with the fix."
- You stop auto-receiving patch updates — you bump the SHA yourself, typically via Dependabot.
- ⚠️ **Unverified caveat:** a claim circulates that SHA-pinning can interfere with Dependabot's vulnerability **alerting** on actions. Confirmed: Dependabot can *update* SHA-pinned actions (and annotates the version in a comment). **Not confirmed:** the alerting nuance — verify before relying on it.

#### Where immutable releases changes the calculus
A reference to a tag that **is** a published **immutable** release (e.g. `@v4.1.0` where that release was published with immutability on) is **locked** — nearly as trustworthy as a SHA, while staying human-readable. **But mind the gaps:**
- It only helps for tags that are **immutable releases** — see the two-level trap below.
- A floating **`@v4`** is movable **as long as no immutable release is published on it** — and authors deliberately keep it that way (no release ⇒ free to advance to newest `v4.x`). Nothing about the *name* `v4` decides this; an author *could* publish an immutable release on `v4`, but then it stops floating.
- It depends on the **author** having enabled the setting; the consumer doesn't control it.

#### ⭐ The two-level trap (a release is NOT automatically immutable)
This is the highest-value exam trap in the topic. Two independent questions, and you must clear **both** before a tag ref is locked:

1. **Is the tag even a release?** A bare tag (no release object) is just a movable pointer.
2. **Is that release _immutable_?** Publishing a release does **NOT** make it immutable. Immutability applies **only if the repo/org had immutable releases enabled at publish time.** A release published while the setting was off — or an older pre-existing release — is **fully mutable** (assets and tag still changeable).

So a tag can be in three states:
- bare tag (no release) → **movable**
- **mutable** release (setting was off) → **still movable**
- **immutable** release (setting was on) → **locked**

The trap a student falls for: "it's a Release on a clean `v3.4.0` tag → locked." **Wrong.** A Release ≠ an immutable Release. The version string and even the *existence of a release* tell you nothing about the lock — only the **immutable** status does.

#### How a consumer actually checks (verified)
- **Release page:** an immutable release shows an **"Immutable" label below the title**. No label ⇒ not immutable.
- **REST API:** `GET /repos/{owner}/{repo}/releases/tags/{TAG}` → the release object has an explicit **`immutable` boolean**. A **404** means there's no release on that tag at all (bare tag).
- **CLI:** `gh release verify <tag>` confirms a release exists **and is immutable** (it loads the auto-generated signed attestation; immutable releases have one, others don't).
- *Honest caveat:* GitHub has an **open docs issue** asking for a proper "how to tell if a release is immutable, as a user" guide — so this check is real but under-documented today.

#### ⭐ The "better safe than sorry" rule
You shouldn't have to audit each action's release setup. A **full commit SHA is immutable by construction** (content-addressed) — independent of whether the author made a release, enabled immutability, or later toggled it off. **When in doubt, pin the SHA and you never have to check any of the above.**

#### Practical ranking
`branch` (worst) → `@v4` floating major → `@v4.1.0` plain tag → **`@v4.1.0` immutable-release tag ≈ `@<full-sha>`** (best; readable-vs-opaque is the tiebreaker).

#### Forward pointer
*Requiring* SHA pinning or blocking disallowed actions org-wide (rulesets / Actions policy) = enforcement → **taught in 5.6**, not here.

---

### Q&A outcomes (what the quizzes surfaced)

**Bit 1 quiz — 4/5.** Misses/keepers:
- The one miss was forgetting that immutability locks **two** things: **assets AND the tag**. The tag-lock (tag pinned to its commit, can't move/delete while the release exists) is the part that actually stops the re-pointing attack. **Keeper:** *immutable release = assets locked + tag locked (+ name unreusable after deletion + auto-attestation).*
- Confirmed cold: movable tag ⇒ don't create a release; disabling never un-freezes; draft→attach→publish; no `immutable:` YAML key (it's a setting).

**Bit 2 quiz — 3/5.** Both misses were the **same misconception**, so it's the headline keeper:
- Treating "immutable releases enabled on the repo" as "**every tag** on that repo is locked." It is **per-release, not per-repo-wide-tag**. `@main` and a floating `@v4` (no release behind them) stay **mutable** even on an immutable-releases repo; only `@v4.1.0`-as-a-published-immutable-release is locked; a full SHA is always pinned regardless of any setting.
- **Don't get fooled by the semver tag alone:** `@v3.4.0` looking precise does *not* make it safe — the same string can be a bare movable tag, a *mutable* release, or a *published immutable* release. Safety comes from the **immutable status** (or a full SHA), never from how specific the version string looks.
- **A release is NOT automatically immutable** (the two-level trap): clearing "is it a release?" is not enough — you must also clear "is that release *immutable*?" Publishing while the setting was off (or an older release) leaves it mutable. This is the single highest-value trap in the topic.
- Short-SHA point reasoned out from first principles (good) rather than memorized.

---

### Cross-references
- **Bit 1 ↔ Bit 2:** "no release = movable tag" is the author's feature *and* the consumer's hazard — the same fact appears in both bits.
- **→ 5.6:** SHA-pinning enforcement, org Actions policy / rulesets, blocking disallowed actions, full-SHA requirement specifics.
- **→ 5.5:** OIDC — and the *different* "immutable subject claims" feature (keep separate).
- **↔ 1.10 / Topic 1B:** version pinning was foreshadowed alongside the contexts material.

### Open / to-calibrate against practice exams
1. Exam weight of the **OCI/ghcr publishing** path (status unconfirmed).
2. The **Dependabot SHA-pinning alerting** caveat (unverified).
3. Whether the exam phrases this as "immutable **actions**" vs "immutable **releases**."


---

## Topic 4A — Runner Networking & Access Boundaries

*Source: `GH-200_Topic_4A_-_Runner_Networking_and_Access_Boundaries.md`*

**Domain 4 (Enterprise, highest weight 20–25%) · Objective 4.4 — IP allow lists & runner networking.**
Verified live against official GitHub docs (Enterprise Cloud) on 2026-06-22. This area is current-state and still evolving; re-verify specifics near exam time.

Cheat file companion: `GH-200_Cheat_4A_-_Runner_Networking_and_Access_Boundaries.md`.

---

### The master distinction (carry this into every 4A question)

Two problems look alike but are solved by different tools. Crossing them is the trap that caught both quiz misses.

- **Egress identity** — *"What source IP does my runner present?"* What an **IP allow list** (and any target firewall) cares about. Fix = make the runner's IP **predictable**: self-hosted runners, or **static-IP larger runners**.
- **Private reachability** — *"How does my runner reach a resource with no public endpoint?"* (DB, Artifactory, on-prem API). Fix = put the runner **onto/into** your network: **Azure VNET**, **WireGuard overlay**, or **API gateway + OIDC**.

A static IP does **not** grant private reachability; a VNET does **not** (by default) give you an allow-listable egress IP.

---

### Bit 1 — IP allow lists

#### What it is and where it lives
- Restricts access to your **private** resources to approved source IPs. **Public resources stay reachable.**
- **GitHub Enterprise Cloud only.** A plain Free/Team org can't use it.
- Configured **org-level** (Settings → Security → **Authentication security → IP allow list**) or **enterprise-level** (inherited by all member orgs).
  - Org owners can add their own entries but **cannot edit** inherited enterprise entries; enterprise owners **cannot manage** org-added entries.
- Entries use **CIDR notation** (single IP or range).

#### Role-blind → lockout risk
Applies to **everyone**, including enterprise/org owners, repo admins, and outside collaborators. Best practice: keep **more than one owner** so a bad entry doesn't lock everyone out. (Caching means add/remove can take a few minutes to take effect.)

#### Trap — adding entries ≠ enforcing (two distinct actions)

```
1. Add IP/CIDR entries to the list.
2. Tick "Enable IP allow list"   ← only THIS starts enforcing.
```

A full list with the toggle **off** restricts nothing.

#### The two toggles that actually exist (corrected the plan's wording)
The §7d plan mistakenly called one "the enable-for-Actions toggle." **There is no Actions toggle.** The two real controls under "IP allow list":

1. **Enable IP allow list** — the enforcement switch.
2. **Enable IP allow list configuration for installed GitHub Apps** — auto-imports IP ranges that installed GitHub Apps *declare* for themselves. Notably, these App IPs are added **irrespective of whether the allow list is currently enabled**.

Actions traffic is gated **solely by the runner's IP** — there is no "let Actions through" button. That's the whole reason the hosted-runner conflict exists.

#### The hosted-runner conflict (headline of Bit 1)
Standard GitHub-hosted runners (`ubuntu-latest`, etc.) run on **Azure** and share the **Azure datacenter IP ranges** — which are **huge, shared across all GitHub customers, and rotate (the published list updates weekly)**. Allow-listing them is impractical *and* weakens the control (you'd trust every other tenant's runners).

- Older (GHES) framing, stated absolutely: with an IP allow list you **cannot** use GitHub-hosted runners; must use self-hosted (a standard runner's `actions/checkout` returns **403**).
- Current **GHEC** resolution: you *can* combine an allow list with Actions, but only with runners whose IPs you control —
  - **self-hosted runners** (add their egress IPs), or
  - **GitHub-hosted *larger* runners with the static-IP feature** (add the fixed range).
  - Then **add the runner's IP/range to the allow list**.

#### Non-obvious carve-outs (likely distractors)
- **Dependabot** is a first-party GitHub App — its repository access is **exempt** from the allow list.
- **GitHub Apps using server-to-server installation tokens** are **not currently restricted** by the allow list.
- Configuring an **org** IP allow list makes **GitHub Codespaces unusable** for that org's repos.
- A **Pages** site built by a *custom* Actions workflow needs an allow-list rule for its build runner (default-workflow builds don't).

---

### Bit 2 — Static-IP larger runners & private networking

#### Path 1 — Static IP larger runners (the allow-list workaround)
Solves **egress identity**. Enterprise Cloud, opt-in: a **fixed IP range** is assigned to larger-runner instances, which you add to your allow list — explicitly usable **in conjunction with** the IP allow list to run hosted Actions and IP allow-listing at the same time. Modern instances get **two ranges** in different geographies (also lets concurrency scale **beyond the old 500 limit**).

Why not just allow-list standard runners? The runner reference says it directly: too many ever-changing ranges; **use larger runners with a static IP range, or self-hosted runners** instead.

#### Path 2 — Azure VNET private networking (main private-reachability path)
Solves **private reachability** via **VNET injection**:

> The runner's **NIC is deployed into your Azure subnet**, while the **runner VM stays in GitHub-owned infrastructure**.

Because the NIC sits in your subnet, your VNET policies apply to the runner: **NSG outbound rules**, plus access to on-prem / other-cloud via **ExpressRoute or VPN**.

- **Benefits:** private connectivity without opening internet ports; full outbound-policy control; network-log monitoring of all runner traffic.
- **Supported runners:** **2–64 vCPU Ubuntu and Windows** larger runners.
- **Setup order:** configure **Azure resources first** (subnet + NSG via the provided `.bicep`), then create a **network configuration** in GitHub and associate it to a **runner group**; all runners in that group then use the VNET.
- **Subnet sizing:** make available IPs exceed **max job concurrency** (docs suggest ~30% buffer; one GitHub Learn page says 20% — learn the *principle*, not the exact %).

#### Paths 3 & 4 — non-Azure options (lighter weight)
For private reachability without Azure, both are **patterns you build** and work with **standard runners** too (they don't depend on GitHub networking config):
- **API gateway + OIDC** — workflow authenticates to a service outside Actions using an OIDC token.
- **WireGuard overlay** — run WireGuard on both the runner and a host in your private network to form an overlay (no separate gateway infra).

#### Headline trap — Static IP ⊕ Azure VNET are mutually exclusive
- VNET runners use **dynamic IPs** (the default); you **cannot** also assign the static-IP feature to them.
- Worse for allow-listing: with VNET on **Azure default outbound access**, egress IPs are **unpredictable** and **cannot** be added to the IP allow list. You'd need a **stable outbound IP (NAT gateway)** to make VNET egress allow-listable.
- **macOS larger runners** support **neither** Azure VNET **nor** static IPs.

---

### Quiz outcomes (exam-style)

- **Bit 1 — 4/5.** Miss: the toggle-name item — selected *"...for GitHub Actions runners"*; correct is *"Enable IP allow list configuration for installed GitHub Apps."* There is **no Actions toggle**. Resolved.
- **Bit 2 — 4/5.** Miss: marked **static IP** as a workable fix for giving a **standard** runner **private reachability**; wrong on two counts — static IP is a larger-runner/GHEC feature (scope), and it solves egress identity, **not** reachability (wrong problem). Resolved.

**Pattern:** both misses sat at the **conceptual boundary**, not the facts — *egress identity vs private reachability*, and *what each tool is for*. That distinction is the lead keeper.

---

### Honesty / freshness flags
1. **GHES vs GHEC tension:** the "hosted runners are wholly incompatible with an allow list" line comes from an **Enterprise Server** page; current **Enterprise Cloud** docs supersede it with the *larger-runners + static IP* exception. Treat GHEC as authoritative for GH-200, but the exam may lean on the older absolute framing.
2. **"Artifacts are exempt from the allow list"** — seen only as a **community claim**, **not** confirmed in official docs. Don't treat as exam-grade.
3. **Evolving:** runner NICs are moving to a GitHub **service subscription** (assigned IPs from your subnet); **VNET failover** (secondary, possibly cross-region subnet, manual switch) is **public preview**. Could change.
4. **Org vs enterprise level for VNET config:** concept page says org owners on **Team** can configure at org level; enterprise doc says initial Azure setup must be at **enterprise** level with orgs enabled by policy. Different scopes — don't over-specify the level unless the scenario names the plan.


---

## Topic 4B — Runner Images & Toolcache

*Source: `GH-200_Topic_4B_-_Runner_Images_and_Toolcache.md`*

**Domain 4 (Enterprise, highest weight 20–25%) · Objective 4.6 — runner images, tool-cache, custom images, self-hosted customization.**
Verified live against official GitHub Docs + the `actions/runner-images` `ubuntu-24.04` README on 2026-06-22. This area is current-state and still evolving (custom images GA'd ~April 2026); re-verify specifics near exam time.

Cheat file companion: `GH-200_Cheat_4B_-_Runner_Images_and_Toolcache.md`.

---

### Bit 1 — Runner images & the tool-cache

#### Mental model: three sources + one store

- **Source 1 — preinstalled (baked into the image)**, two layers:
  - (a) ordinary **system-wide** software on `PATH` (git, docker, a default Node/Python, apt packages);
  - (b) **Cached Tools** — extra runtime *versions* staged into the tool-cache (on `ubuntu-24.04`: Go, Node.js, Python, PyPy, Ruby).
- **Source 2 — `setup-*` actions** (run during the job).
- **Source 3 — your own installs** (`apt-get` / `brew` / `pip` / manual download).
- **The store — the tool-cache (`_work/_tool`)**: filled by Source 1b and Source 2; **ignored** by Source 3.

Key structural point: the tool-cache is the **shelf**, not a third source. "Preinstalled" and "`setup-*`" put things *on* the shelf; direct installs don't.

#### Table 1 — sources & where the tool-cache sits

| Thing | Role | Lives where | Filled by | `setup-*` sees it? |
|---|---|---|---|---|
| Preinstalled — system-wide (git, docker, default Node/Python, apt pkgs) | ready-to-use OS/app software | normal paths (`/usr/bin`, …) | image build | No |
| Preinstalled — Cached Tools (Go, Node.js, Python, PyPy, Ruby) | extra runtime *versions* | tool-cache (`_work/_tool`) | image build | Yes |
| tool-cache (the shelf) | storage, **not** a source | `_work/_tool` | preinstall + `setup-*` misses | it **is** the shelf |
| `setup-*` (setup-node / setup-python / …) | the picker | — (reads/writes the shelf) | — | — |
| Your installs (`apt-get` / `pip` / `brew` / manual) | runtime additions | normal paths | you, mid-job | No |

#### Table 2 — available right away / fast installable / persisted

| Source | Speed | Persist across jobs — HOSTED | Persist across jobs — SELF-HOSTED |
|---|---|---|---|
| Preinstalled (system-wide + Cached Tools) | instant, ~0 cost | re-provided fresh each job (new VM) | yes, while on the machine |
| `setup-*` → version **is** preinstalled/cached | instant (PATH switch) | switch re-runs each job (cheap) | cached version stays |
| `setup-*` → version **not** preinstalled | one-time download | **NOT** persisted; re-downloads each job unless `actions/cache` | persisted in tool-cache → later jobs hit |
| Your manual install (`apt-get`/`pip`/`brew`) | installer speed | not persisted | persists (and risks drift) |

#### The two different "caches" (the fuzzy part)

| Cache | Holds | Filled by | On HOSTED runners |
|---|---|---|---|
| tool-cache (`_work/_tool`) | tool/runtime **binaries** | preinstall + `setup-*` | per-VM — wiped each job (gives **speed**, not persistence) |
| `actions/cache` (Topic 1E) | your **dependencies** (npm/pip/…) | you, via the action | GitHub-side cache service — **survives** across jobs |

**Persistence cut:** HOSTED = fresh VM every job (tool-cache does not persist). SELF-HOSTED = same machine reused (`_work/_tool` survives → `setup-*` downloads stick for later jobs).

#### How `setup-*` behaves
- Requested version already on the shelf (common hosted case) → just prepend to `PATH`. Near-zero cost.
- Not there → the `setup-LANGUAGE` action downloads the binary into the tool-cache, then activates it (needs internet).

#### Where to find the exact image software
Workflow log → expand **Set up job → Runner Image →** the "Included Software" link = the precise manifest for that run. The image set is maintained in `actions/runner-images` and refreshed ~weekly (rollout takes a few days). Don't assume a tool/version is present — pin with `setup-*` + explicit version.

#### Q&A outcomes (Bit 1)
- **The apt-get vs `setup-python` trap:** a direct `apt-get install python3.12` is **invisible** to `setup-python`. setup-python does its normal thing regardless — uses a cached 3.12 if present, otherwise downloads it into the tool-cache. The apt result never enters the picture. (No need to memorize per-image version lists; the point is that direct installs don't touch the tool-cache.)
- Clarified that "preinstalled" is **two layers**, not one (system-wide + Cached Tools), confirmed against the `ubuntu-24.04` README's separate `Installed Software` and `Cached Tools` sections.

---

### Bit 2 — Custom images (larger runners) & self-hosted customization

Spectrum of *how much you bake ahead of time*: install-at-runtime (Bit 1) → **custom image** → **self-hosted fully-custom VM**.

#### A) Custom images — for GitHub-hosted *larger* runners
Start from a GitHub-curated base image and build your own VM image with tools, dependencies, certificates, binaries, and prepulled container images already in place — a "pre-warmed" runner.

- **Headline limit:** custom images work **only on larger runners → GitHub Team or GitHub Enterprise Cloud**. Not standard runners, not Free. GA'd ~April 2026 (public preview from Oct 2025).
- **Three steps:** (1) set up an **image-generation runner**; (2) **generate** the image with the `snapshot` keyword; (3) **install/use** — assign to a runner group and point `runs-on` at it.
- **Platform/size rules:** the image-generation runner's platform must match the target image (**Linux x64, Linux ARM64, or Windows x64**); run the resulting image on a runner of the **same size or larger**.
- **`snapshot` — two syntaxes:**

  String form (name only; GitHub versions it entirely):
  ```yaml
  jobs:
    build:
      runs-on: my-image-generation-runner
      snapshot: my-custom-image      # captures the VM after the LAST step succeeds
      steps:
        - run: ./install-deps.sh
  ```
  Mapping form (name **and** optional major version):
  ```yaml
  jobs:
    build:
      runs-on: my-image-generation-runner
      snapshot:
        image-name: my-custom-image
        version: 1                   # MAJOR only; minor auto-increments, no patch
      steps:
        - run: ./install-deps.sh
  ```
- **Success-only:** a new image version is created **only when the job completes successfully**. A failed/incomplete run produces no new version.
- **Stays GitHub's, not yours:** still runs on GitHub infra; the image lives in the org's Actions settings under **"Custom images,"** *not* in your own container registry (`ghcr.io`); not reusable across other CI providers; not a general-purpose VM pipeline.
- **Billing/governance:** jobs billed at the larger-runner per-minute rate; **storage billed separately** through Actions storage; each successful snapshot = a new version, so frequent rebuilds + retained old versions grow storage fast; enterprise owners manage access and set **retention policies** in Actions policy settings. Regenerating ~weekly is recommended (patches/updates) → another artifact to manage.
- **Security best practices:** dedicated runner groups for image generation; **don't share runner groups between production and dev/test** (dev/test access ⇒ injection path into prod images); images can be built from **any branch**, so write access alone can trigger generation → least privilege. Permissions: org/enterprise owner, CI/CD Admin role, or equivalent fine-grained perms.

#### B) Self-hosted — full customization (the other end)
You own the machine, so you customize everything: full OS image (e.g. Packer/AMIs), **any distro**, persistent tool-cache, pre/post-job hooks. Cost: you own maintenance, patching, security, drift. GitHub explicitly points you to self-hosted (or Docker) for non-Ubuntu Linux distros, since hosted Linux is Ubuntu-only.

#### C) Where each is allowed
```
runtime install   → any runner, ephemeral, re-done every job
custom image      → LARGER hosted runners only (Team/GHEC), pre-warmed, GitHub-managed
self-hosted VM    → total control + total responsibility, any distro
```

#### Q&A outcomes (Bit 2)
- **Mapping-form correction:** my first example showed only the string form. The mapping form is the one that lets you set the version (`image-name:` + `version:`); that `version` is the **major** segment, with the minor auto-incrementing per snapshot and no patch versions.

---

### Quiz outcomes
- **Bit 1:** Q2–Q5 correct (4/4). Q1 wasn't scored as a miss — it was a fair push on a loosely-worded item; the underlying concept (direct installs invisible to `setup-*`) landed.
- **Bit 2:** 5/5. Cleanly rejected the distractors that (C) custom images make you own OS patching like self-hosted [false] and (E) custom images are reusable on other CI providers [false].

### Honesty flags (carried from teaching)
- **Tool-cache path/env var:** the documented default is `_work/_tool`; the hosted-Ubuntu path (commonly cited as `/opt/hostedtoolcache`) and the `RUNNER_TOOL_CACHE` env-var name were **not** re-verified this session.
- **Custom images GA timing:** GA'd ~April 2026 (preview from Oct 2025). Pre-GA write-ups describe it as preview and may be stale; some limits/UI could still shift.
- **Retention numbers:** the *existence* of a retention policy is solid; a community report cites a **60-day default / 90-day maximum**, but those exact numbers were **not** found in official docs this session — treat as unverified.
- **Pre/post-job hook env-var names** (`ACTIONS_RUNNER_HOOK_JOB_STARTED` / `_COMPLETED`) come from a community blog this session, not re-verified against official docs.

### Cross-refs
- `actions/cache` (dependency cache) ↔ Topic 1E (caching vs artifacts + retention).
- Larger runners ↔ Topic 4A (static-IP larger runners, Azure VNET, runner groups).
- Next: Topic 4C — configuration variables (`vars`) hierarchy + managing secrets/variables via REST API (4.7, 4.8).


---

## Topic 4C — Configuration Variables & Secrets/Variables REST API

*Source: `GH-200_Topic_4C_-_Variables_and_Secrets_REST_API.md`*

**Domain 4 (Enterprise, highest weight 20–25%) · Objectives 4.7 (variables) + 4.8 (programmatic secrets/variables).**
Verified live against official GitHub Docs (Variables reference, Contexts reference, REST API for Actions secrets, Encrypting secrets for the REST API, Secrets concept) on 2026-06-22. Current-state; re-verify near exam time.

Cheat file companion: `GH-200_Cheat_4C_-_Variables_and_Secrets_REST_API.md`.

---

### Bit 1 — Configuration variables (`vars`)

Non-secret, **plaintext** config values, defined once and reused, read via the `vars` context. Three levels: **organization, repository, environment**. Secrets are the encrypted sibling (Bit 2).

#### Precedence — most specific wins
Docs phrase it "the variable at the lowest level takes precedence":
```
environment  >  repository  >  organization
```
Same name at multiple levels → the closest-to-the-job level wins.

#### ★ Env-level timing trap
Environment-level variables only become available on the runner **after the job starts executing**, so they do **not** overwrite values in the `env` and `vars` contexts during the **pre-job processing** phase (the part GitHub evaluates before dispatching to a runner). A var consumed in an early-evaluated spot (e.g. `runs-on`) won't pick up the env-level override.

#### ★ Reusable-workflow trap
For a called (reusable) workflow, the variables used come from the **caller's** repository. The called workflow's **own** repo variables are **not** made available to it.

#### Limits (GitHub.com / GHEC)
- 48 KB per individual variable
- 1,000 org · 500 per repo · 100 per environment
- **Combined org+repo total: 256 KB per workflow run.** Past that, only the org variables under the cap are served (after repo variables, sorted alphabetically). **Environment variables do not count toward the 256 KB** → push overflow config into environments.
- *(Version note: GHES uses a 10 MB combined limit instead of 256 KB.)*

#### `vars` context
A name→value map of org/repo/env configuration variables, usable in expressions — including early-evaluated places like `runs-on`, `name`, `if`, `environment`:
```yaml
jobs:
  build:
    if: ${{ vars.DEPLOY_ENABLED == 'true' }}
    runs-on: ${{ vars.RUNNER }}
    environment: ${{ vars.ENV_STAGE }}
```

#### Org access policy
An org-level variable (or secret) can be scoped by repository access: **all repos / private repos only / a selected list**.

#### vars vs secrets (4.7 headline)
Variables are **plaintext** — visible in settings, **not** masked in logs — for non-sensitive config. Secrets are **encrypted + masked**. Same three-level structure; never put sensitive data in a variable.

#### Naming
`vars.NAME` dereference requires a name starting with a letter or `_`, containing only alphanumerics / `-` / `_`. (Stricter variable-*creation* rules — no spaces, can't start with a number, `GITHUB_` prefix forbidden, case-insensitive — are the standard documented rules; not re-pulled verbatim this session.)

#### Q&A outcomes (Bit 1) — 5/5
Confirmed: precedence (env wins), env-timing trap (env var can't feed `runs-on`), the 256 KB combined / env-excluded rule, reusable-workflow var sourcing (caller's repo), org access scoping. Flagged keepers: env-timing trap, reusable-workflow trap, 256 KB-combined/env-excluded.

---

### Bit 2 — Managing secrets & variables via REST API

Headline contrast (4.8): **variables = plaintext CRUD; secrets = encrypt-before-send.**

#### Variables — plain CRUD, value readable
Standard REST on `/actions/variables` (no encryption):
- repo: `POST/GET /repos/{owner}/{repo}/actions/variables`, `GET/PATCH/DELETE …/variables/{name}`
- org: `/orgs/{org}/actions/variables` (+ repository-access scoping)
- env: `/repos/{owner}/{repo}/environments/{env}/variables`
- A `GET` on a variable **returns its value** in plaintext.

#### Secrets — three-step encrypt-first dance
1. **GET the public key** for the target scope:
   ```bash
   GET /repos/{owner}/{repo}/actions/secrets/public-key
   # → { "key_id": "...", "key": "<base64 public key>" }
   ```
2. **Encrypt** the plaintext with that key using a **libsodium sealed box** (`crypto_box_seal`), then Base64-encode.
3. **PUT** the secret with ciphertext + key id:
   ```bash
   PUT /repos/{owner}/{repo}/actions/secrets/{name}
   { "encrypted_value": "<base64 sealed box>", "key_id": "..." }
   ```
   Org-level adds `"visibility"` + `"selected_repository_ids"` (IDs, not names).

#### Why client-side encryption
The sealed box is created **before the value reaches GitHub** (same for UI and API), so the plaintext never lands in GitHub's request/exception logs; GitHub decrypts server-side only to inject it into the runtime. TLS protects transit; the sealed box adds defence against accidental logging *inside* GitHub.

#### What a sealed box is (background, not a memorize-item)
libsodium public-key encryption where only the **recipient** (GitHub) has a key pair. Each call generates a throwaway **ephemeral** key pair, derives a shared key against GitHub's public key, encrypts, prepends the ephemeral public key, and discards the ephemeral private key → only GitHub can decrypt; it's "anonymous" (sender not cryptographically identified — your API token already proves who you are). Per-language wrappers: PyNaCl `SealedBox`, RbNaCl `Boxes::Sealed`, Sodium.Core `SealedPublicKeyBox`, JS `crypto_box_seal`.

#### ★ The big API contrast (trap)
- **`GET` a secret never returns its value** — metadata only (name, timestamps). Values can't be read back via API (even an admin can't exfiltrate stored secret values this way).
- **`GET` a variable returns the value.**

#### Scopes
repo/environment secret endpoints need collaborator access (classic token `repo` scope); org secret endpoints need `admin:org`.

#### gh CLI shortcut
`gh secret set NAME` runs the whole dance (fetch public key → seal → PUT); `gh variable set NAME` for plaintext. (Stated from knowledge; CLI docs not re-pulled this session.)

#### Q&A outcomes (Bit 2) — 5/5
Confirmed: create-secret order (GET key → encrypt → PUT), secret-vs-variable GET behaviour, secrets unreadable via API, client-side-encryption rationale, org `selected` visibility with repo IDs.

---

### Honesty flags (carried from teaching)
- **256 KB combined limit** is GitHub.com/GHEC; **GHES = 10 MB** — version-specific.
- **Variable naming creation rules** (no spaces, no leading digit, `GITHUB_` prefix forbidden, case-insensitive) stated as standard rules, not re-pulled verbatim this session.
- **Variables REST endpoints** (`/actions/variables` paths, PATCH-to-update, GET-returns-value) stated from the parallel API structure; the *secrets* API page was verified live, the *variables* API page was not re-pulled this turn.
- **gh CLI** commands stated from knowledge, not re-pulled this session.
- Current-state only: older docs reference `tweetsodium`; current is libsodium — taught current only.

### Cross-refs
- `vars`/`secrets`/`env` contexts & `${{ }}` setup-time vs runtime evaluation ↔ Topic 1B.
- Secret masking (raw + common encodings incl. Base64) ↔ Topic 1B.
- Environments & deployment protection ↔ Domain 5 (5.7 required reviewers).
- Next domain: Domain 5 — security/optimize (script injection, `GITHUB_TOKEN` vs PAT, OIDC, SHA pinning/immutable enforcement, required reviewers, artifact attestations/SLSA, optimization).


---

## Topic 5A — Untrusted Input & Token Hardening

*Source: `GH-200_Topic_5A_-_Untrusted_Input_and_Token_Hardening.md`*

**Domain 5 (Secure & optimize, 10–15% weight) · Objectives 5.3 (script injection) + 5.4 (`GITHUB_TOKEN` vs PAT).**
Verified live against official GitHub Docs (Script injections concept page, Security hardening guide / Enterprise Cloud, Automatic token authentication, `GITHUB_TOKEN` concept page, Managing your personal access tokens) on 2026-06-23. Current-state; re-verify near exam time.

Cheat file companion: `GH-200_Cheat_5A_-_Untrusted_Input_and_Token_Hardening.md`.

---

### Bit 1 — Script injection (5.3)

#### The core mechanism (this *is* the topic)
A step's `run:` block is **not** handed to the shell directly. GitHub first **builds a temporary shell script**, substituting every `${{ }}` expression into the script *text* at **template/parse time** — before the shell starts. Only then is the generated script executed.

Consequence: if an untrusted value is interpolated straight into `run:`, the attacker's text becomes **part of the script source**, not data the script reads. That is the injection. (Same parse-time-vs-runtime split as Topic 1B — here it's the security fallout.)

#### Vulnerable pattern
```yaml
- name: Check title
  run: |
    title="${{ github.event.issue.title }}"
    echo "$title"
```
An issue title containing shell metacharacters is spliced into the generated script and executed.

#### Why quoting in the YAML does NOT save you
The substitution happens at template-build time, before the shell exists. The quotes you typed are just more script text the attacker can close and break out of. Even a branch/ref name suffices: `zzz";echo${IFS}"hello";#` is a valid Git ref and is enough to break out and inject.

#### Preferred fix — intermediate environment variable
```yaml
- name: Check title
  env:
    TITLE: ${{ github.event.issue.title }}
  run: |
    echo "$TITLE"
```
Why safe: the value is placed into the **process environment** as a data value and read at **runtime** via `$TITLE`. It never becomes part of the generated script's source, so the shell treats it as a string, not commands.

> **Critical sub-point (the "half-fix"):** setting an `env:` var is pointless if you then read it back as an expression — `${{ env.TITLE }}` — instead of as a real shell variable `$TITLE`. `${{ env.TITLE }}` is still an expression, so it's substituted into the script source at template time, exactly like the original vuln. The whole protection is "the shell reads it at runtime," so reference it the shell way (`$VAR` / `"$VAR"`).

#### Alternative safe shape — pass as an action argument
```yaml
- uses: org/title-checker@v3
  with:
    title: ${{ github.event.issue.title }}
```
Not vulnerable: the value is passed to the action as an argument, not used to generate a shell script.

#### Defense-in-depth (supporting, not the primary fix)
- Least-privilege `permissions:` so a successful injection has a weak `GITHUB_TOKEN` to abuse.
- Input validation.
- Prefer vetted / SHA-pinned actions.
- CodeQL (ExpressionInjection query) and OpenSSF Scorecards to detect injection patterns.
- Double-quoting shell variables avoids word-splitting but is **general shell hygiene**, not the GitHub-specific mitigation. Don't let an exam answer dress it up as *the* fix.

#### Non-obvious untrusted sources (classic distractors)
Not just issue/PR `title` and `body`. Also **branch/ref names** and **email addresses**. Untrusted fields cluster on those ending in `body`, `*_ref` (`head_ref`), `label`, `message`, `name`, `page_name`, `title`. System-generated fields (`pull_request.number`, `run_id`, `sha`) are **not** attacker-controlled.

#### Quiz outcomes (Bit 1)
- **5/5.** Correctly identified the only directly-interpolated `run:` as vulnerable; correctly separated attacker-controlled fields (title, `head_ref`, author email) from system fields (PR number, run_id); confirmed quoting is not a fix; chose the env-var indirection as the primary fix.
- **Keeper that caught the trap:** the half-fix — `env:` var defeated by re-reading it as `${{ env.VAR }}`.

---

### Bit 2 — `GITHUB_TOKEN` vs PAT (5.4)

#### What `GITHUB_TOKEN` actually is
When you enable Actions on a repo, GitHub silently installs a **GitHub App** on it. `GITHUB_TOKEN` is an **installation access token** for that App, minted **fresh per job**. You never create or store it; it appears in the job and is read via `${{ secrets.GITHUB_TOKEN }}` or the `github.token` context (available even if you don't explicitly pass it to an action).

#### Three defining properties (and the PAT contrast)
1. **Ephemeral** — expires when the job finishes (or at its max lifetime). Per-**job**, not per-workflow. A PAT lives until its expiry date (or forever if none set) and works from anywhere.
2. **Repo-scoped** — permissions limited to the repo containing the workflow; it cannot reach other repos. This is the headline reason to escalate to a PAT or App token.
3. **Permission-tunable (least privilege)** — shaped via the `permissions:` key at workflow or job level.

#### The `permissions:` rule (exam-critical)
```yaml
permissions:
  contents: read
  issues: write
```
Naming **any** permission sets **all unspecified permissions to `none`** — with the **sole exception of `metadata`, which always gets read**. Job-level `permissions:` overrides workflow-level for that job. GitHub's recommended default posture is `contents: read` (enough to clone and build).

#### Maximum lifetime depends on runner type
- **GitHub-hosted:** max job time 6 hours → token lives up to **6 hours**.
- **Self-hosted:** max job time is 5 days, **but** because it's an installation access token it can only be refreshed for up to **24 hours**. Jobs running longer than 24h must switch to a PAT or other auth. (Don't conflate the 5-day job ceiling with the token's 24h refresh cap.)

#### The recursion guard (favorite trap — mind the wording)
A push or PR made **with `GITHUB_TOKEN`** does **not trigger** a new workflow run. Precise mechanics: the **commit still lands** in the repo; the event is suppressed **at the trigger stage** — no run is created, queued, or skipped; nothing downstream fires. Purpose: prevent recursive/infinite workflow runs.

This is **`GITHUB_TOKEN`-specific**. If you *need* downstream workflows to fire, authenticate the push/PR with a **PAT or a GitHub App installation token** instead — then the events trigger normally. So the same swap that grants cross-repo reach also lifts the recursion guard: one mechanism, two consequences.

#### PATs — two flavors, when each fits
- **Fine-grained PAT (recommended):** restrictable to specific repositories, with fine-grained permissions.
- **PAT (classic):** broad — can access every repository the owning user can access.
- Defining weakness of *any* PAT: tied to a **user account** (carries that user's reach) and **long-lived**. GitHub's guidance: prefer the built-in `GITHUB_TOKEN`; if you need more, prefer a **GitHub App** installation token (short-lived, not user-bound) over a PAT.

#### Decision frame
Default to **`GITHUB_TOKEN`** → need cross-repo, or need to trigger downstream workflows → prefer a **GitHub App** token → use a **PAT** (fine-grained > classic, with expiry) only when an App is impractical.

#### Quiz outcomes (combined 5A quiz)
- **5/5.** Identified `GITHUB_TOKEN` as a per-job App installation token (not user-bound); applied the "name one → others `none`, metadata read" rule; got the recursion guard right including run-vs-trigger and the PAT/App escape hatch; chose the 24h self-hosted refresh cap over the 5-day red herring.
- **Crossover question nailed:** for "read untrusted PR title in `run:` AND push a commit that should trigger CI," chose env-var-read-as-`$TITLE` **plus** a PAT/App token — and rejected the sabotage option that re-broke the injection fix via `${{ env.TITLE }}`.

---

### Cross-references
- 5.3 ↔ Topic 1B (expression evaluation: static/parse-time vs runtime; untrusted `${{ }}`).
- 5.4 ↔ Topic 4C (secrets/variables, `permissions`) and ↔ Topic 5B next (OIDC as the keyless alternative to long-lived PAT secrets).

### Honesty / verification flags
- The full list of `permissions:` scopes (`actions`, `checks`, `contents`, `deployments`, `issues`, `packages`, `pull-requests`, `repository-projects`, `security-events`, `statuses`, plus `metadata`) is stated from a GitHub changelog + community sources; the **`metadata`-always-read** rule and the **unspecified→`none`** rule are confirmed in docs/community. The canonical current permissions-reference table was not re-pulled line-by-line this session — verify exact scope names if an item hinges on one.
- Lifetime figures (6h hosted, 24h self-hosted refresh) are from the current `GITHUB_TOKEN` concept page.
- "Default to `contents: read`" is GitHub's stated good practice, not a hard requirement.


---

## Topic 5B — OIDC Keyless Cloud Auth

*Source: `GH-200_Topic_5B_-_OIDC_Keyless_Cloud_Auth.md`*

**Domain 5 (Secure & optimize, 10–15% weight) · Objective 5.5 (OIDC federation to cloud providers).**
Verified live against official GitHub Docs (OpenID Connect concept page, OpenID Connect reference, Configuring OIDC in cloud providers / AWS / Azure / GCP, Using OIDC with reusable workflows) on 2026-06-23. Current-state; re-verify near exam time.

Cheat file companion: `GH-200_Cheat_5B_-_OIDC_Keyless_Cloud_Auth.md`.

---

### Bit 1 — Concept & flow (5.5)

#### The problem OIDC solves
A workflow that deploys to AWS/Azure/GCP needs to authenticate. The old way: create a cloud credential, **duplicate it** into GitHub as a long-lived secret, and present it every run. That static secret is the liability — it sits in GitHub indefinitely, must be rotated by hand, and if leaked it's valid until someone revokes it.

#### The OIDC alternative — keyless
Instead of storing a cloud credential, the workflow proves *who it is* at runtime and gets a **short-lived** token back. Nothing long-lived **of the cloud's** is stored in GitHub. (Authentication still happens — but with ephemeral, GitHub-provisioned tokens, not a secret you keep. "Keyless" means no key *you own and store*, not "no auth.")

#### Two tokens — keep them straight (the crux)
- **Token A — the request token** (`ACTIONS_ID_TOKEN_REQUEST_TOKEN`): GitHub injects it into the runner for the job (gated by `id-token: write`). Its only job is to authenticate the call *to GitHub's own OIDC endpoint* to mint Token B. GitHub is both ends of that exchange; **the cloud never sees Token A.** Ephemeral, per-job, never stored. Same family of machinery as `GITHUB_TOKEN`.
- **Token B — the OIDC JWT**: what GitHub mints and signs, and what actually gets sent to the cloud. It is an **identity assertion** — it carries claims (repo, ref, environment, actor…) but **no permissions**.

Mental model: Token A authenticates you *to GitHub*; Token B authenticates GitHub's *assertion about you* to the cloud.

#### The flow — end to end
1. GitHub dispatches the job and injects **Token A** into the runner (requires `id-token: write`).
2. The job uses Token A to call GitHub's OIDC provider at `https://token.actions.githubusercontent.com` → GitHub signs and returns **Token B**, a JWT unique to that job.
3. The job sends **Token B** to the cloud (via the cloud's login action).
4. The cloud validates Token B (see validation order below), then returns a **short-lived access token scoped to that job**, carrying the assumed role's permissions.

The clean summary: GitHub never sees your cloud credentials; the cloud never sees any GitHub secret — the only thing crossing the wall is a signed, scoped, short-lived JWT.

#### How the cloud accepts the JWT — asymmetric crypto, no shared secret
GitHub signs the JWT with its **private** key (RS256). The cloud verifies it with GitHub's **public** keys, published at the issuer's JWKS endpoint (discoverable via `https://token.actions.githubusercontent.com/.well-known/openid-configuration` → `jwks_uri`). Only GitHub's private key could produce a signature that verifies against GitHub's published public key, so a valid signature is cryptographic proof the token is authentically from GitHub and untampered. No password or shared secret ever passes between GitHub and the cloud — that's why it's keyless in both directions.

#### Validation order (issuer → signature → claims)
The cloud can't "check against the public key" until it knows *whose* key set to fetch. Correct sequence:
1. Read the **`iss`** claim ("claims to be GitHub").
2. Confirm `iss` is a **trusted, registered issuer** (the one-time provider registration). If not on the trust list → reject.
3. Fetch **that issuer's** public keys from its JWKS endpoint.
4. **Verify the signature** with those keys.
5. Check **`aud`/`sub`** against the role's trust policy (Bit 2).

The issuer check is **not** redundant with the signature check — they answer different questions. Signature = *"is it real / untampered?"*. Issuer = *"is it from a signer I decided to trust?"*. The issuer step also *selects* which key set to verify against, so it must come first. (Two attacks, two defenses: a forged token claiming `iss: github` fails at signature; a genuinely-signed token from an untrusted IdP fails at the issuer/trust check.)

#### The one YAML change — `id-token: write` (and its trap)
```yaml
permissions:
  id-token: write
  contents: read
```
`id-token: write` does **not** grant write to any resource. It only lets the job **request and use** the OIDC token (mint Token B). Pure identity permission. Missing it is the #1 OIDC failure. (Per the 5A rule, naming this one permission sets all others to `none` except `metadata` — add back `contents: read` if you check out code.)

#### Who controls scope (since the token carries none)
Entirely the **cloud side**: authN (identity) is GitHub's; authZ (access) is the cloud's.
- **Trust policy / condition** = *who* may assume the role (claim matching — Bit 2).
- **Permission policy on the role** = *what* the assumed credentials can do (ordinary cloud IAM, nothing to do with GitHub).

Contrast with `GITHUB_TOKEN`, whose scope is set *inside* GitHub via `permissions:` because the resource being accessed *is* GitHub. With OIDC, the resource is the cloud's, so the cloud owns authZ; GitHub's only scope-side levers are whether the token is minted (`id-token: write`) and what identity claims it carries.

#### Mechanics
Normally done by the cloud's official login action — `aws-actions/configure-aws-credentials`, `azure/login`, `google-github-actions/auth`. No official action? Fetch the JWT manually via the runner env vars `ACTIONS_ID_TOKEN_REQUEST_URL` + `ACTIONS_ID_TOKEN_REQUEST_TOKEN` (the toolkit's `getIDToken()` helper wraps exactly that).

Minimal AWS example (the action handles steps 1–4):
```yaml
permissions:
  id-token: write
  contents: read
steps:
  - uses: aws-actions/configure-aws-credentials@<sha>
    with:
      role-to-assume: arn:aws:iam::123456789012:role/my-deploy-role
      aws-region: us-east-1
```

---

### Bit 2 — Trust config & claims (5.5)

Step 4 in detail: once the signature proves the token is from GitHub, **the claims decide whether *this specific workflow* may assume the role.** Two claims do almost all the work — `sub` and `aud`.

#### The `sub` (subject) claim — the main gate
Default format, a concatenation of metadata:
```
repo:<owner>/<repo>:<ref-type>:<ref>
```
Common forms:
```
repo:octo-org/octo-repo:ref:refs/heads/main       # a branch
repo:octo-org/octo-repo:ref:refs/tags/v1.2.3       # a tag
repo:octo-org/octo-repo:environment:production     # a job referencing an environment
repo:octo-org/octo-repo:pull_request               # a pull_request-triggered job
```

#### `sub` precedence — environment > pull_request > branch/tag
The ref/tag form appears only if the job references no environment **and** wasn't PR-triggered. Resolution order:
- Job references an **environment** → `:environment:NAME`, **regardless of trigger** (including PR). Always wins.
- No environment, **PR-triggered** → `:pull_request`.
- No environment, not a PR → `:ref:refs/heads/<branch>` or `:ref:refs/tags/<tag>`.

There is **no composite `pull_request + environment` form** — the environment form replaces the others. Most common "it worked until I added an environment" failure: a condition written for `:ref:refs/heads/main` stops matching the moment the job declares an environment.

The **`pull_request` sub is stable and has no PR number** (the PR ref lives in `ref`/`job_workflow_ref`, not `sub`), so conditioning on `:pull_request` trusts **every** PR, including forks.

#### The `aud` (audience) claim — secondary condition
Defaults to the owner URL (e.g. `https://github.com/octo-org`). Cloud login actions override it to the cloud's expected value (AWS `sts.amazonaws.com`). Condition on **both** `aud` and `sub`.

#### Writing the condition (AWS shape)
```json
"Condition": {
  "StringEquals": {
    "token.actions.githubusercontent.com:aud": "sts.amazonaws.com",
    "token.actions.githubusercontent.com:sub": "repo:octo-org/octo-repo:ref:refs/heads/main"
  }
}
```
Azure = **federated credential** (issuer + subject match); GCP = **workload identity pool** attribute conditions. Different syntax, identical concept.

#### The four classic misconfigurations
1. **`aud` only, no `sub`** — opens the role to all of GitHub.com. No scenario where correct.
2. **`repo:org/*` wildcard (under a wildcard-evaluating operator)** — whole org, incl. forks landing in the org, dependabot branches, new repos by any member.
3. **Wildcard value under `StringEquals`** — `StringEquals` does not evaluate `*`; `:ref:refs/heads/release/*` matches a branch *literally named* `release/*`. Use `StringLike` when the value contains a wildcard.
4. **Production trust on `pull_request`** — PR workflows run with the PR author's token; anyone who can open a PR (incl. external contributors on public repos) runs under that trust.

#### `StringEquals` vs `StringLike` cuts both ways (refined point)
Under `StringEquals`, `*` is **literal** → a wildcard pattern matches *nothing* → the role is assumable by no one. That's a **fail-closed / too-restrictive bug, not an exposure.** The danger appears only under `StringLike`, where `*` expands and a loose pattern can grant the whole org. So "wildcard in the sub condition" is genuinely *unsafe* only when the operator evaluates wildcards. Distinguish **too-restrictive (broken)** from **too-permissive (exposure)** — they fail in opposite directions, and the `StringEquals→StringLike` "fix" is exactly the move that can flip a fail-closed bug into a real hole.

#### Recommended pattern — scope to an environment (plus the consequence)
`repo:org/repo:environment:production` is the cleanest production pattern: the `sub` is **stable across all triggers**, and you can layer GitHub **environment protection rules** on top.

But mind the precedence interaction: a **PR-triggered job that references `production`** also produces `sub: ...:environment:production`, so its token **would match** a `:environment:production` cloud condition. The real defense is **not** the cloud condition — it's the **environment protection rules**, which run GitHub-side *before* the job executes. If `production` is protected (deploy restricted to `main`, required reviewers, etc.), a PR-triggered job can't enter the environment, so it never gets a token with that `sub` to begin with.

**Pairing rule:** `:environment:NAME` in a cloud trust policy is only as safe as the protection rules on that environment. Scope-to-environment and environment-protection-rules are a **pair** — neither does the job alone. A production environment with no protection rules + a trust condition on `:environment:production` is exactly the hole.

#### Going more granular — customizing claims
- **Customize the `sub` template** via REST API (`PUT .../actions/oidc/customization/sub` with `include_claim_keys`) to fold in `actor`, `event_name`, `workflow`, `job_workflow_ref`, etc.
- Condition directly on standalone claims: `repository_id`, `repository_visibility`, `repo_property_*` (repository custom properties → attribute-based access control).
- For **reusable workflows**, the `job_workflow_ref` claim identifies the *called* workflow — how you scope trust to a shared central workflow.

#### ⚠ Current-state flag: immutable subject claims
GitHub is moving to an **immutable `sub` format** adding owner ID and repo ID, to satisfy the OIDC rule that subjects must be unique and never reassigned (closing a namespace-recycling hole where a recycled org/repo name could reproduce an old `sub`):
```
Previous:  repo:octo-org/octo-repo:ref:refs/heads/main
Immutable: repo:octo-org@123456/octo-repo@456789:ref:refs/heads/main
```
The `@` separator is used because `@` can't appear in usernames or repo names. Per docs: repositories created after **2026-07-15** use this format by default; older repos keep the previous format unless they opt in (org/repo OIDC settings UI or REST API); renames/transfers after that date also migrate. **Not available on GitHub Enterprise Server.**

Honesty notes: (a) that date sits just ahead of "today" (2026-06-23), so whether the exam reflects it depends on when the question bank was written — the durable point is that the format *can* differ and **your trust policy must match the format the repo actually uses.** (b) "Immutable subject claims" is a **different feature** from "immutable releases/actions" (Topic 3A) — same adjective, unrelated mechanism. Don't conflate them.

---

### Quiz outcomes
- **Bit 1 quiz: 5/5.** Clean on identity-vs-permissions, `id-token: write` trap, JWT acceptance via public-key crypto + one-time provider registration, scope living cloud-side, and the two-token distinction. One refinement surfaced and resolved: JWT validation is **issuer → signature → claims**, and the issuer check is not redundant with the signature (it selects the key set and confirms a trusted signer).
- **Bit 2 / combined 5B quiz: effectively 6/6.** Correct on `sub` precedence (environment wins), the environment-protection pairing as the real PR gate, validation order, token roles, and immutable claims. The "which configs are unsafe" item exposed the refined point that `StringEquals`+wildcard fails *closed* (too restrictive), not open — recognition of all four misconfig patterns was correct; the strict "genuinely unsafe = too permissive" reading is A (aud-only) and E (pull_request).

### Cross-references
- 5B ↔ 5A (`permissions:` / `id-token: write` follows the "name one → others none except metadata" rule; OIDC is the keyless alternative to the long-lived-PAT-secret pattern).
- 5B ↔ environment protection rules (5.1, already course-covered) — the GitHub-side gate that makes environment-scoped trust safe.
- Immutable subject claims ↔ NOT the same as immutable releases (3A).

### Honesty / verification flags
- RS256, the `jwks_uri`, and the `.well-known/openid-configuration` shape are confirmed against GitHub's live discovery document.
- AWS trust-policy condition syntax (`token.actions.githubusercontent.com:sub`/`:aud`) is current and verified; Azure (federated credentials) and GCP (workload identity pools) achieve the same gate with different syntax — concept identical, exact syntax not re-pulled per provider this session.
- Immutable-subject-claims rollout date (2026-07-15) is from the current OIDC reference; treat as imminent/forward-dated relative to study time.
- AWS short-lived credential default (~1 hour, configurable up to 12h) is provider-/config-dependent — verify a specific figure before relying on it.


---

## Topic 5C — Action Enforcement Policies & Build Provenance

*Source: `GH-200_Topic_5C_-_Action_Enforcement_Policies_and_Build_Provenance.md`*

**Domain 5 (Secure & Optimize). Objectives: 5.6 action-usage enforcement + light 5.7 (pinning/immutable enforcement) + 5.8 (artifact attestations / provenance / SLSA).**
Verified live against `docs.github.com` (Enterprise Cloud) and the GH-200 study guide (skills measured Jan 2026), session date 2026-06-23.

> Companion cheat file: `GH-200_Cheat_5C_-_Action_Enforcement_Policies_and_Build_Provenance.md`
> Boundary reminder: Topic 3A taught *what* pinning/immutability are and *why* to pin. Topic 5C is the **enforcement machinery** (Bit 1) and the **provenance proof** (Bit 2) — not a re-teach of 3A concepts.

---

### Bit 1 — Enforcing safe action consumption

These controls make safe consumption *mandatory* for everyone in a repo/org/enterprise, rather than relying on each developer to choose well.

#### Where the controls live (same block, three signposts)

| Level | How to get there | Section label once there |
|---|---|---|
| Repository | Settings → Actions → General | "Actions permissions" |
| Organization | Settings → Actions → General | "Policies" |
| Enterprise | Policies (top nav) → Actions | "Policies" |

**Override direction (the load-bearing cross-tier fact):** enterprise → organization → repository. A lower level can only *tighten*, never loosen, a policy set above it. A `!` carve-out in an allow list is "partially override" in the sense of subtracting an exception — both entries coexist; block wins on overlap.

#### Lever 1 — "Actions permissions" policy (the allow/deny list)

Four mutually-exclusive options:

| Option | Allows | Note |
|---|---|---|
| Allow all actions and reusable workflows | Anything, any author | Default |
| Allow `<owner>` actions and reusable workflows | *Local only* | **Blocks GitHub's own actions** — `actions/checkout` becomes inaccessible |
| Allow `<owner>`, and select non-`<owner>` | Local + sub-toggles below | Only tier that unlocks finer control |
| Disable | Nothing runs | — |

Sub-toggles under the "select" tier:

| Sub-toggle | Effect |
|---|---|
| Allow actions created by GitHub | Everything in the `actions` and `github` orgs (this restores `actions/checkout`) |
| Allow Marketplace actions by verified creators | Any action with the verified-creator badge |
| Allow or block specified actions and reusable workflows | Explicit list — **max 1000 entries** |

List syntax (same `@ref` grammar as `uses:`):

```
actions/checkout@v4      # exact ref
monalisa/*               # all repos under an owner
monalisa/my-action@*     # any ref of one action
*, !evil-org/*           # allow all, block one owner
```

- `!` entries are denies layered over allows; **block wins on overlap**.
- **Local actions (`uses: ./path`) are never restricted by any policy** — the list only governs remote refs.
- The **verified-creator badge confirms publisher *identity* only** — GitHub verified the org is a genuine partner, not impersonator. It does **not** mean the code was reviewed or audited, and a verified account can itself be compromised. Trusting the toggle = trusting *who* wrote it, not *what the code does*. GitHub's own guidance still says review the source and pin to a SHA even for verified creators.

#### Lever 2 — Require actions to be pinned to a full-length commit SHA

A dedicated checkbox inside the same allowed-actions policy, at repo/org/enterprise. When on, **every action ref must be a full 40-char SHA** — including your own org's actions and GitHub's. This is the *enforcement* of the 3A pinning concept (3A = voluntary; this = compulsory org-wide).

- **★ Reusable workflows are EXEMPT — still referenceable by tag.** The rule applies to `uses:` *actions*, not to `uses: owner/repo/.github/workflows/x.yml@ref`. "Forces reusable workflows onto SHAs too" → false.
- **A SHA pin freezes the action's source tree, not its runtime behavior.** A pinned action can still be mutable underneath via an unpinned Docker base image, an unpinned nested composite action, or a script it `curl`s at runtime. Reproducible *source*, not reproducible *behavior*.

#### Lever 3 — Approval gate for untrusted contributors' workflows

Settings → Actions → General → "Fork pull request workflows" / "Approval for running fork pull request workflows from contributors." This gates on *who triggers*, not on which actions are used.

| Setting | Who must wait for approval |
|---|---|
| First-time contributors who are new to GitHub | Brand-new GitHub accounts only |
| First-time contributors | Anyone with no merged commit/PR in *this* repo |
| All outside collaborators / external contributors | Anyone not a member/owner of the repo or org |

A write-access maintainer approves before the fork-PR workflow runs. **Both the PR author and the triggering actor are checked.** A run awaiting approval for >30 days is auto-deleted.

**★ Exam-wording honesty flag:** the objective says *"required reviewers for unverified actions,"* but **no GitHub feature gates on whether an *action* is verified and demands a reviewer.** The phrase is a loose umbrella over two real, separate features: (a) this contributor-approval gate (keys off *who triggers*), and (b) **environment "Required reviewers"** protection rules (gate a *job* targeting a protected environment — same protection-rule pairing as 5B's OIDC). Recognize both; don't hunt for a literal "unverified-actions reviewer" setting.

#### Backdrop — immutable actions on hosted runners (registry-source shift)

| Aspect | Status |
|---|---|
| Consuming immutable actions | Live/transparent — hosted runners resolve actions as immutable OCI packages from GitHub Packages where one exists, else classic Git-ref resolution. No workflow change needed |
| Download host | `pkg.actions.githubusercontent.com` (under required `*.actions.githubusercontent.com`); publishing uses `ghcr.io` → **4A allow-list tie-in** |
| Publishing your own immutable action | ⚠ **Not confidently GA** — `actions/publish-immutable-action` README still says "not ready for public use," yet a roadmap card is labeled GA. Conflicting signals (flag carried from 3A); verify against a practice exam |

---

### Bit 2 — Artifact attestations & build provenance (5.8)

#### ⚠ Terminology warning — "artifact" is two unrelated features

The exam will not tell you which domain a question belongs to. Read the verbs.

| If the question is about… | "Artifact" means… | Clues |
|---|---|---|
| Moving files between jobs / keeping run outputs (Domain 1, Topic 1E) | a **workflow artifact** | `upload-artifact`, `download-artifact`, "between jobs," "retention," "90 days," "download from the run" |
| Proving where/how a published thing was built (Domain 5, 5.8) | a **build output you publish & someone else consumes** (release binary, container image, package) | `attest`, `attest-build-provenance`, "provenance," "Sigstore," "`gh attestation verify`," "SLSA," "verify before deploy" |

| | Workflow artifact (1E) | Thing an attestation is *about* (5.8) |
|---|---|---|
| Created by | `actions/upload-artifact` | your build step (the file/image) |
| Purpose | hand a file between jobs / retrieve after run | ship a verifiable build output to consumers |
| Stored | Actions artifact service, tied to the **run** | output lives where you publish it; the *attestation* lives in GitHub's attestations API, tied to the **repo** |
| Lifetime | retention-bound (90-day default, 1–400 range — per 1E) | persists with the repo, independent of the run |

They can touch (a build output is sometimes also uploaded as a workflow artifact to move between jobs), but the attestation is about the *published output's provenance*, not the inter-job transfer. Below, "build output" = the 5.8 sense.

#### The problem 5.8 solves

A published build output is linked to the consumer only by *name and location*, not identity. Anyone who can write to a point in the chain (compromised registry creds, hijacked Release asset, poisoned CDN/mirror, typosquat) can swap your file for a malicious one of the same name + version. The version string proves nothing about the bytes. (Distinct from Bit 1: SHA-pinning protects the *action source pulled into* your build; this protects the *build output shipped out of* it.)

#### What an attestation is

A cryptographically signed claim binding a **subject** to a **predicate**, in the **in-toto** format:

- **Subject** = the build output's name + its **SHA-256 digest** (hash of the actual bytes; one byte changed → different digest).
- **Predicate** = build-provenance facts: link to the workflow, repository, organization, environment, commit SHA, triggering event, and other claims from the **OIDC token** used during the build.

5B tie-in: the signing identity comes from OIDC — `id-token: write` exists precisely to mint the identity that signs.

#### Why "swapped in" is *detected* (the real mechanic)

Verification checks three things; the **order matters**:

1. **Bytes (digest lookup).** CLI hashes the file the consumer holds, then fetches the attestation *by that digest*. A swapped file has a different digest → **no attestation exists for those bytes** → fails here, before any signature is examined.
2. **Signature.** Catches a *forged/invalid* attestation that has a matching digest — checked against the Sigstore certificate chain.
3. **Identity.** Confirms the signing cert's claims match the `--owner`/`--repo` you demanded. A validly-signed output from a *different* repo still fails if you demanded yours.

So a **plain file-swap dies at step 1 (bytes)**; the **signature check defends against a forged attestation on a matching digest**. The attestation doesn't block the swap — it makes it detectable before the bytes are used.

#### Generating an attestation

```
permissions:
  id-token: write       # OIDC identity used to sign (keyless)
  contents: read
  attestations: write   # upload the attestation to GitHub
```

```
- name: Generate provenance attestation
  uses: actions/attest@v4
  with:
    subject-path: 'path/to/your/build-output'
```

Container images additionally need `packages: write`.

**⚠ Naming precision:** the historically-named action is **`actions/attest-build-provenance`**; as of its v4 it's a thin **wrapper around `actions/attest`**. Existing workflows can keep using `attest-build-provenance`; new ones should use `actions/attest`. Recognize **both names**. Older GA material shows `attest-build-provenance@v1` vs current `actions/attest@v4` — version drift, not a contradiction.

#### How signing works (keyless, via Sigstore)

Short-lived Sigstore-issued signing certificate; no long-lived key you manage — same keyless philosophy as 5B OIDC.

| Repository type | Sigstore instance | Transparency log? |
|---|---|---|
| Public | Sigstore **Public Good** instance | Yes |
| Private / internal | GitHub's **private** Sigstore instance | **No** — same codebase, no public transparency log, federates only with GitHub Actions |

Signed attestation is uploaded to GitHub's attestations API, associated with the repo, visible in the Actions tab.

#### Verifying

**Generating alone gives no security benefit — the value only materializes on verification.** Done with the GitHub CLI:

```
gh attestation verify path/to/build-output --owner my-org
gh attestation verify path/to/build-output --repo my-org/my-repo
```

Must supply `--owner` (`-o`) *or* `--repo` (`-R`). Specifics:

- **Container images:** point at the image with an `oci://` prefix — `gh attestation verify oci://ghcr.io/my-org/my-image:tag -R my-org/my-repo` (after `docker login ghcr.io`).
- **SBOM attestations:** pass `--predicate-type` explicitly (otherwise it verifies build provenance, not the SBOM).
- **Reusable-workflow signing:** `--signer-repo` points at the repo holding the signing workflow when it differs from the caller; `--signer-workflow` requires a *specific* workflow file did the signing.

**★ Monotonic verification — stated precisely:** verification passes when **at least one attestation satisfies the specific claims you asked to verify** (the identity in `--owner`/`--repo`, plus `--signer-workflow`/`--predicate-type` if supplied) — *not* the vague "at least one attestation passes." Non-matching/junk attestations in the set are **inert**: they can't substitute for your demand and can't veto an attestation that already met it. Monotonic = once it passes, later additions can't flip it to failing (anti-DOS). Corollary: looseness lives in *your query* — `--owner` only proves "someone in the org," so tighten with `--repo`/`--signer-workflow` for a specific builder; and verifying provenance ≠ verifying an SBOM (different predicate).

Why a set can hold multiple attestations for one digest: different predicate types (provenance + SBOM), re-runs/re-publishes of the same bytes, or reusable-workflow signing — plus, maliciously, junk anyone could add.

#### Where SLSA fits

**SLSA** ("Supply-chain Levels for Software Artifacts," said "salsa") is an industry framework (not a GitHub feature) defining graded supply-chain integrity levels. GitHub's provenance predicate *is* in SLSA build-provenance format, so producing these attestations is how you meet SLSA's provenance requirement on GitHub.

Verified claim to hold: **artifact attestations + reusable workflows → SLSA v1.0 Build Level 3** (provenance generated by a hardened, controlled platform — a centrally-managed reusable workflow — rather than by the build about itself).

⚠ Honesty flag: the "reusable workflows → Build L3" statement is straight from the docs (confident). I'm *not* certain of the baseline level a plain attestation reaches, nor the exact requirement wording per level — verify against a practice exam. The objective lists SLSA as an example only ("e.g., SLSA, build metadata") → conceptual familiarity, not reciting the level table.

#### Integrating into deployment verification

Run `gh attestation verify` before a deploy step consumes a build output; proceed only on success → provenance becomes a deploy gate. GitHub also offers a **Kubernetes admission controller** that validates attestations at the cluster so only properly-attested images deploy. (Know it exists; not a deep-dive.)

---

### Quiz outcomes (this session)

**Bit 1 — effectively solid.** Both genuine traps landed: reusable-workflow exemption from SHA enforcement, local-only policy blocking `actions/checkout`, and local-action (`./path`) exemption from the allow list. Misses were *wording*, not concept:
- The `!`-block keeper was reasoned correctly during teaching but dropped on the multiple-choice; reframed as "subtracts an exception, block wins on overlap."
- Marked "required reviewers for unverified actions" as a real setting (the worded trap) — corrected: it's a loose umbrella, not a feature.

**Bit 2 — 4/5.** Clean on: missing `id-token: write` and its signing role; SBOM ≠ provenance (different predicate); the artifact-term collision (correctly classified both scenarios); `--owner` overclaim (owner ≠ workflow; tighten with `--signer-workflow`/`--repo`).
- **The one real miss:** check *order*. A plain **file-swap fails at the digest/bytes lookup** (no attestation exists for those bytes), *before* any signature check. The **signature check** is what defeats a forged/bad attestation on a *matching* digest. → cheat-file keeper.

Learner-driven refinements incorporated: the artifact-collision note (read the verbs, exam won't name the domain); monotonic verification stated as "satisfies the specific claims you asked to verify," not generic "an attestation passes."


---

## Topic 5D — Optimizing Workflows & Managing Retention

*Source: `GH-200_Topic_5D_-_Optimization_and_Retention.md`*

**Domain 5 (Secure & Optimize). Objectives: 5.10 (scaling/optimization strategies) + 5.9 (programmatic retention).**
Verified live against `docs.github.com` (incl. Enterprise Cloud) and GitHub billing/limits reference, session 2026-06-23. Final gap topic of Domain 5.

> Companion cheat file: `GH-200_Cheat_5D_-_Optimization_and_Retention.md`

---

### Bit 1 — The cost & limits model and how to optimize against it

The objective is "recommend strategies" — conceptual. But you recommend against a model: *what you pay for* and *what constrains you*.

#### What you pay for

| Factor | Detail |
|---|---|
| Billable minutes | Only for **GitHub-hosted runners on private repos**. **Public repos and self-hosted runners are free** (no billable minutes). |
| ★ Rounding | Each job rounded **up to the nearest whole minute**. 1s and 59s both bill as 1 min — hurts with many tiny jobs. |
| ★ OS multiplier | **Linux 1× · Windows 2× · macOS 10×.** A 10-min macOS job consumes 100 minutes. Moving to Linux is the biggest single lever. Formula: **billed = round-up(minutes) × OS-multiplier.** |
| Larger runners | Higher per-minute rate scaling with vCPU; **no charge while idle**; static IP adds no cost; included free minutes **can't** be used on them; **not free even for public repos**. |
| Storage | Artifacts + Packages storage billed separately from minutes. |

#### What constrains you

| Limit | Value |
|---|---|
| ★ Job execution time | **6 hours max per job** — killed if exceeded. |
| Concurrency | Capped per plan (Free lowest → Enterprise highest; larger-runner + macOS caps separate). Support can raise on request. |
| Matrix size | A single matrix capped at a max number of job combinations (commonly cited 256). |
| Schedule | `schedule:` no more often than every 5 min; can be delayed/dropped under load. |

⚠ **Confidence split:** the 6-hour limit, OS multipliers, round-up rule, and public/self-hosted=free are confirmed in GitHub docs. Exact per-plan concurrency numbers and the matrix-combination cap are from secondary sources — know they *exist* and scale by plan; verify the figures on a practice exam.

#### Optimization levers — and the critical speed-vs-cost distinction

**★ Parallelization optimizes TIME, not billed minutes — and can increase them.** Billed minutes are *summed across jobs*. 18 min of work as one job = 18 billed min / 18 min wall-clock; split into 3 parallel jobs of 6 min = still 18 billed min but ~6 min wall-clock. Add per-job setup (re-checkout, re-install) + per-job round-up and the split often bills *more*. Parallelism buys latency/throughput, not a cheaper bill.

The genuine **cost** levers:

1. **Run less.** Path filters (skip doc-only changes), branch filters, `if:` conditions.
```
on:
  push:
    paths: ['src/**', 'package.json']
    paths-ignore: ['**/*.md', 'docs/**']   # use ONE of paths/paths-ignore per event
```
2. **Stop wasted in-flight work — the two cheapest wins.**
```
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true      # cancel a run superseded by a new push
```
```
jobs:
  build:
    timeout-minutes: 15          # without it, a hung job runs to the 6h ceiling
```
3. **Cache & reuse.** `actions/cache` keyed on lockfile hash + `restore-keys`; Docker layer cache (`type=gha`); reusable workflows / composite actions. **1E distinction: cache = deps/build-acceleration (7-day default, 10 GB LRU); artifact = results you keep (90-day default).** Different features.
4. **Right-size — bigger isn't automatically cheaper.** 8-core finishing a 20-min build in 12 min = ~4× rate for ~1.67× speed = net more expensive. Pick the knee of the curve; prefer Linux over 2×/10× platforms.
5. **`needs:` as a fast-fail gate (this is where the dependency graph saves *minutes*).** Put cheap checks (lint/unit) in a job the expensive job `needs:`; a failure kills the run before the costly job starts. This is "run less" wearing a dependency-graph costume — *this* saves minutes, not parallelism per se.
6. **Trim storage** (Bit 2): lower `retention-days`, upload only what's needed, compress.

#### Measuring

Org Actions usage metrics show where minutes go. ★ **Keeper trap: usage metrics do NOT apply minute multipliers** — they show *raw* minutes, so a macOS/Windows-heavy org's metric ≠ its bill. Purpose = "where are minutes spent," not "what's the invoice." Use the billing page + spending limits for actual cost.

---

### Bit 2 — Retention & storage management (5.9)

Storage is the other paid axis. Two distinct controls people conflate: the retention **period** (default lifespan for *new* objects) vs **deletion** (removing existing objects). Different mechanisms.

#### The retention period (a setting, not really an API)

| | Artifacts & logs | Caches |
|---|---|---|
| Default | **90 days** | **7 days** |
| Range | **1–400 days** (private/internal/Enterprise); **public capped at 90** | public ≤ 90; private/internal ≤ 365 |
| Set where | Ent/org/repo → Settings → Actions → General → "Artifact and log retention" | same settings area |
| ★ Retroactive? | **No** — applies only to *new* objects, never existing ones | same |
| Hierarchy | Lower level can't exceed the cap set above it | same |

★ **Why the defaults differ (the understanding, not the numbers):** cache is disposable build-acceleration that should churn fast → short 7-day clock + size cap (10 GB default, up to 10,000 GB) with **LRU eviction** when exceeded. Artifacts are results you may retrieve later → long 90-day clock.

Per-artifact override at authoring time (capped by the repo/org max):
```
- uses: actions/upload-artifact@v4
  with:
    name: build-output
    path: dist/
    retention-days: 7         # overrides the 90-day default for this artifact
    compression-level: 6      # 0 (none) – 9 (max); artifacts compressed by default
```

#### Programmatic management — what's actually real (resolves parked 5.9)

**Programmatic DELETION — verified, official:**
```
DELETE /repos/{owner}/{repo}/actions/artifacts/{artifact_id}   # delete one artifact
GET    /repos/{owner}/{repo}/actions/artifacts                 # list to find IDs
DELETE /repos/{owner}/{repo}/actions/runs/{run_id}             # delete a workflow run
```
Often scripted via `actions/github-script` (`github.rest.actions.listArtifactsForRepo` + `deleteArtifact`) or `gh api`. Caches: `gh cache list` / `gh cache delete <id>`.

**⚠ Setting the retention PERIOD via REST — NOT confirmed official.** No documented REST endpoint sets the retention-days value; a `PUT .../actions/retention`-style endpoint is unverified/likely not official (resolves the flag carried since 1E). Setting the period is a **settings/UI** operation + the per-artifact `retention-days` in YAML.

**★ Precise, exam-safe framing of "programmatic retention":**
> = (a) declarative per-artifact `retention-days` in `upload-artifact`, plus (b) programmatic *deletion* via the REST artifacts API / `gh`. It does **not** mean an API that sets the account-wide retention period — that's a setting. Verified path is **list + DELETE**; treat "set the period via REST" as not-confirmed.

#### Operational gotcha

After deleting artifacts/caches, the **storage-quota figure lags** — recalculation can take several hours (commonly 6–24h). A "storage quota exceeded" error does **not** clear instantly after a successful cleanup. Recognize this so you don't assume deletion failed; wait for recalculation and set lower retention going forward.

---

### Quiz outcomes (this session)

**Bit 1 — 5/5** (one item was a typo, not a miss). Solid on: round-up × OS-multiplier (macOS 10×); public-repo standard runners are free regardless of OS; **parallelism cuts wall-clock, not billed minutes** (and can raise them via setup + rounding) — the real minute-saver is **fast-fail `needs:` gating**; `cancel-in-progress` as the cheapest, zero-risk win; usage metrics show **raw** minutes (no multiplier) so dashboard ≠ bill.

**Bit 2 — 5/5** (on substance). Solid on: 90-day artifact vs 7-day cache defaults + override behavior; retention-period change is **not retroactive** (by design, not a bug); **no REST endpoint sets the retention period** — REST does get/list/delete only; cache over size cap → **LRU eviction**; post-deletion **quota recalculation lag** explains a persisting quota error (deletion didn't fail).

**Learner-driven calibration:** quiz format moving to contrasts/scenarios, not recall drills (raw-number recitation has no value for a recognition exam — understand *why* cache=7/artifact=90, don't memorize in isolation).

**Status: Topic 5D complete → Domain 5 gap-complete → Domains 1–5 all done.** Next phase = practice exams (+ settle the long-parked `fromJSON` dynamic-matrix exam-weight question there). A new testing-phase protocol will govern from the next session.
