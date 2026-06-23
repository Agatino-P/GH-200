# GH-200 · Topic 1E — Outputs, Summaries & Retention

*Personalized recap. Covers Domain 1 objectives **1.14** (job summaries), **1.16** (caching/artifacts +
retention via REST API; overlaps **5.9**), and **1.12** (VS Code editor tooling). All current-state facts
(retention numbers, REST endpoints, extension limits) verified live against official GitHub docs, June 2026.
Quiz outcomes per bit noted; weak-spots at the end.*

---

## Bit 1 — Job summaries via `GITHUB_STEP_SUMMARY`  ·  *(quiz: effectively 5/5)*

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

## Bit 2 — Caching vs artifacts; retention via REST API  ·  *(quiz: effectively 5/5)*

### Artifacts vs cache — opposite purposes

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

### Retention numbers (verified) — two DIFFERENT sets, easy to confuse

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

### Retention via REST API (verified endpoints)

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

## Bit 3 (short) — VS Code GitHub Actions extension  ·  *(quiz: 3/3)*

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

## Exam-weight notes (calibrate against practice exams)

- Job summaries (1.14) and retention-via-REST-API (1.16/5.9) are **new/thin** objectives from the Jan 2026
  reword — likely tested at recognition level ("what does this do", "which file/endpoint"). Weight unverified.
- The VS Code extension (1.12) is almost certainly **low-weight recognition** — don't over-invest here
  relative to the expressions/YAML topics. Weight unverified.

---

## Weak-spots / watch-list for review

- **Two retention number sets are different** — artifacts default 90 (private max 400); cache default 7
  (private max 365). Don't merge them.
- `>` only clears the **current step's** summary; it can't reach other steps. At job end everything groups.
- For cross-job transfer: **files → artifact, strings → job output**; cache is best-effort, not a transfer tool.
- The `PUT .../actions/retention` endpoint is **unverified** — don't cite it as fact on the exam; the
  reliable REST retention story is **list + `DELETE` artifacts**.
