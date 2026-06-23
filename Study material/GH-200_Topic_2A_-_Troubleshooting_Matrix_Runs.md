# GH-200 · Topic 2A — Troubleshooting Matrix Runs

*Personalized recap. Covers Domain 2 objective **2.4** (correlate matrix jobs↔axes, analyze variant
failures, rerun individual matrix jobs); cross-refs Topic 1C (matrix mechanics, `fail-fast`). Domain 2's
other gap (2.3, reading YAML anchors) was already covered in Topic 1D. All current-state facts (rerun
scopes/surfaces, REST endpoints, the attempt-archiving behavior) verified live against official GitHub
docs/changelog, June 2026. Quiz outcomes per bit noted; weak-spots at the end.*

---

## Bit 1 — Reading matrix job names & analyzing variant failures  ·  *(quiz: 5/5)*

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

## Bit 2 — Rerunning failed work  ·  *(quiz: 4/4 + correct reasoning on an ambiguous item)*

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

## Q&A outcomes / things the learner pushed on

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

## Exam-weight notes (calibrate against practice exams)

- 2.4 is a 🟡 partial gap; matrix basics were course-covered, so the *new* surface here is **reading
  labels/axis correlation**, the **fail-fast cancelled-vs-failed** reading, and **rerun granularity**.
  Likely recognition-level ("which combination failed", "cheapest way to retry one leg", "what does
  rerun-failed include"). Weight unverified.

---

## Weak-spots / watch-list for review

- Decode matrix labels by **declaration order**, never by finish order (run order isn't guaranteed).
- In a fail-fast run, **cancelled legs are collateral, not failures** — the culprit is the one that failed;
  use `fail-fast: false` to get a clean per-variant map.
- **Single-job API rerun archives the attempt** → can't then individually rerun the other old failures
  (403); no subset-rerun endpoint. Use `rerun-failed-jobs` for several at once.
- `name:` is a job attribute (`jobs.<job_id>.name`), not part of `strategy`/`matrix`.
