# GH-200 Cheat — Topic 1E: Outputs, Summaries & Retention

*Trap-grade keepers only. Full explanation in the matching recap: `GH-200_Topic_1E_-_Outputs_Summaries_Retention.md`.*

### Job summaries — `GITHUB_STEP_SUMMARY`
- It's an **environment FILE** (variable = a file path). Append **GFM Markdown**; renders on the run summary page.
- `>>` appends (auto-newline each append); `>` overwrites **the current step's** buffer only.
- **1 MiB per step** limit → exceeding it **aborts** that step's summary (error "1024k"), not silent truncation.
- Renders GFM: tables, Mermaid, alerts (`> [!NOTE]`). `<details>` must stay within ONE step (isolation breaks cross-step tags).

### Job summaries — step isolation ⚠️ (flagged keeper)
- `GITHUB_STEP_SUMMARY` is a **SEPARATE file PER STEP**. Steps are isolated.
- `>>` appends to the CURRENT step's file; `>` overwrites ONLY the current step's buffer.
- `>` can **NEVER** wipe another step's summary. At job end all step files are grouped into one job summary.
- Across jobs: summaries ordered by **job completion time**, not definition order.
- (Trap: assuming `>` in a later step clears the whole job summary — it doesn't.)

### The four environment-file siblings (all use `>>`)
```
GITHUB_STEP_SUMMARY -> Markdown for HUMANS (run summary page)
GITHUB_OUTPUT       -> step OUTPUT for machines (steps.<id>.outputs.*)
GITHUB_ENV          -> env var for LATER STEPS ($NAME)
::warning:: / ::error:: -> annotations (inline highlights, not rich content)
```

### Artifacts vs cache ⚠️
- **Artifact** = persist a run's OUTPUTS (share between jobs, download, inspect). Reliable & retained.
- **Cache** = SPEED (restore deps across runs by key). **Best-effort, can be EVICTED, NOT guaranteed.**
- Cross-job: FILE/binary → **artifact**; small STRING/metadata → **job output** (`needs.<job>.outputs.X`). Cache is NOT a transfer tool.
- Anti-patterns: cache to pass build output between jobs (unreliable); artifacts as a dep cache (slow/costly).

### Retention numbers ⚠️ TWO DIFFERENT SETS (easy to confuse)
```
ARTIFACTS/LOGS: default 90d | public ≤90 | private/internal ≤400
CACHE:          default  7d | public ≤90 | private/internal ≤365
CACHE size cap: 10 GB/repo default, LRU eviction over limit
```
- Per-artifact override: `retention-days:` on `upload-artifact` (capped by repo/org/enterprise). Applies to NEW artifacts only.
- `upload-artifact@v4` / `download-artifact@v4` current; **v3 deprecated & stopped working**. (v4: artifact names must be unique within a run.)

### Retention via REST API (verified)
```
GET    /repos/{o}/{r}/actions/artifacts                  # list repo artifacts
GET    /repos/{o}/{r}/actions/runs/{run_id}/artifacts    # list a run's artifacts
DELETE /repos/{o}/{r}/actions/artifacts/{artifact_id}    # delete one  <- retention workhorse
GET    /repos/{o}/{r}/actions/artifacts/{id}/{format}    # download (format=zip; URL expires in 1 MIN)
```
- "Enforce retention" programmatically = **list + DELETE** on a schedule.
- ⚠️ `PUT .../actions/retention` is **UNVERIFIED / likely not official** — do NOT trust it. Default-retention config is UI/org-policy.

### VS Code GitHub Actions extension (`GitHub.vscode-github-actions`)
- Two halves: (1) **authoring** — schema validation + completion, incl. smart checks of job/step references and event-payload validation from `on:`; (2) **run management** — view/cancel/re-run/trigger runs, drill runs→jobs→steps, view logs.
- ⚠️ **No remote repos** — github.dev / vscode.dev unsupported; use a local clone. GHES support = experimental beta.
- NOT the same as "GitHub Local Actions" (third-party, runs workflows locally via `act`).
