# GH-200 · Topic 1C — Matrix Strategy In Depth

*Personalized recap. Covers Domain 1 objective **1.8** (matrix strategy: cross-product, `include`/`exclude`,
failure & concurrency control, dynamic matrices, **runner images**). Facts verified against live GitHub docs,
June 2026. Quiz outcomes per bit noted; weak-spots section at the end.*

---

## Where everything lives (read this first)

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

## Bit 1 — Cross-product, `exclude`, `include`  ·  *(quiz: 5/5)*

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

## Bit 2 — `fail-fast`, `max-parallel`, `continue-on-error`  ·  *(quiz: 5/5)*

**`fail-fast` — default `true`.** First matrix combo counted as a failure → GitHub cancels all
in-progress and queued combos. Set `false` for full reports / debugging / cross-platform runs.

**`max-parallel`** — caps how many combos run simultaneously (default = as many as runner/account
limits allow). It caps a **count**, not an "axis". Specific sizing numbers are judgement, not exam facts.

**`continue-on-error`** — on a JOB or a STEP. When `true`, that unit's failure doesn't fail the run.

### The interaction (exam-worthy)

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

### ⚠️ Swallow vs preserve — the gotcha

```
continue-on-error  -> SWALLOWS the failure: run not failed, AND downstream needs: sees SUCCESS.
fail-fast: false   -> PRESERVES the failure: doesn't cancel siblings, but failure still counts
                      (downstream needs: is blocked).
```

So "let all combos finish but still treat a failure as a failure" = **`fail-fast: false`**, NOT
`continue-on-error`.

### Complete annotated example (every key, with its level)

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

## Bit 3 — Dynamic matrices via `fromJSON`  ·  *(quiz: 5/5)*

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

## Bit 4 — Runner images & the `-latest` moving target  ·  *(quiz: 5/5)*  ·  verified live June 2026

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

## Your weak spots from the quizzes — focus revision here
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

## Sources (verified live, June 2026)
- Workflow syntax — matrix / `include` / `exclude` / `fail-fast` / `max-parallel` — docs.github.com/.../workflow-syntax-for-github-actions
- Running variations of jobs in a workflow (matrix) — docs.github.com/en/actions/.../running-variations-of-jobs-in-a-workflow
- Evaluate expressions / `fromJSON` (returning a JSON object) — docs.github.com/en/actions/.../expressions
- `continue-on-error` × `fail-fast` interaction — corroborated across community discussions + vendor guides (Octopus/Codefresh, copdips)
