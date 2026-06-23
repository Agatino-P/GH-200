# GH-200 Cheat — Topic 2A: Troubleshooting Matrix Runs

*Trap-grade keepers only. Full explanation in the matching recap: `GH-200_Topic_2A_-_Troubleshooting_Matrix_Runs.md`.*

### Reading matrix job labels
- Auto-label = `<job_name> (val1, val2, ...)`, values in **matrix-key DECLARATION order**, comma-separated.
- e.g. `matrix: {arch:[x64,arm64], node:[18,20]}` → `arch=arm64,node=18` shows as `build (arm64, 18)`.
- Decode a label using the YAML's key order — NOT by finish order (**run order is not guaranteed**).
- Custom label: `jobs.<job_id>.name` (job attribute, sibling of `runs-on`/`strategy`/`steps`), can use `${{ matrix.* }}`.

### fail-fast: cancelled ≠ failed ⚠️
- Default `fail-fast: true` → one failed leg **cancels** all other in-progress/queued legs.
- Cancelled legs are **collateral**, true result UNKNOWN — the culprit is the leg that actually FAILED.
- `fail-fast: false` + re-run = clean per-variant pass/fail map (is the failure one combo or broad?).

### Rerun scopes & surfaces
- Three scopes: **Re-run all** | **Re-run failed** (failed + downstream dependents) | **Re-run single job** (each matrix leg = its own job).
- UI: "Re-run jobs" dropdown / per-job hover icon / logs view.
- CLI: `gh run rerun <id>` | `gh run rerun <id> --failed` | `gh run rerun --job <job_id>` (`--debug` for debug logging).
- REST: `POST .../runs/{run_id}/rerun` | `.../runs/{run_id}/rerun-failed-jobs` | `.../jobs/{job_id}/rerun`.
- Re-runs create a **new ATTEMPT** (old run preserved; attempt navigation; reuses original SHA).

### KEEPER GOTCHA — single-job API rerun archives the attempt ⚠️
- `POST .../actions/jobs/{job_id}/rerun` creates a NEW attempt → remaining old failures are now in the ARCHIVED attempt.
- Trying to individually rerun a second old failure → **HTTP 403 "Only jobs from the current attempt can be re-run."**
- **No endpoint to rerun a SUBSET** of jobs in one call. Options: `rerun-failed-jobs` (ALL) or one-at-a-time.
- To retry several specific legs: use `rerun-failed-jobs`, or rerun them before a new attempt archives them.

### Edge bug (not the rule)
- Matrixed **reusable** workflows: "Re-run failed jobs" may restart the failed leg but NOT its downstream dependents inside the reusable workflow. (Documented behavior = failed + dependents; this is a reported bug.)
