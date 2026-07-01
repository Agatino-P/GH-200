<style>
/* Readability tuning — honored by the VS Code preview / Typora / PDF export.
   GitHub.com strips <style> during sanitization, so it has no effect there
   (harmless). Spacing only, no colors → safe on both light and dark themes.
   Affects presentation only; no content is changed. */
li { margin-bottom: 0.35em; line-height: 1.55; }
ul { margin-top: 0.35em; }
li > ul { margin-top: 0.3em; margin-bottom: 0.5em; }
h2 { margin-top: 2em; }
h3 { margin-top: 1.4em; margin-bottom: 0.5em; }
table { margin: 0.7em 0; }
</style>

<!-- Review-tag legend & Todo Tree setup → see REVIEW-TAGS.md -->

# GH-200 — Combined Cheat Sheets

*Consolidated study sheet for GH-200 (GitHub Actions). Restructured 2026-07-01: the three trailing
"Drill-Surfaced Keepers" blocks were dissolved and each item folded into a single topic home;
duplicate statements were merged (keeping every distinction); trap notation was unified to a single
leading ⚠️ marker. Content is faithfully reorganised and de-duplicated, not pruned or re-taught.
Trap/distractor callouts and explicit `X ≠ Y` distinctions are the highest-value content and are
preserved throughout.*

## Contents


**Domain 1 — Author & maintain workflows**
- [Topic 1A — Triggers, Permissions, Inputs, Reusable Workflows](#topic-1a--triggers-permissions-inputs-reusable-workflows)
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
- [Topic 4C — Variables & Secrets REST API](#topic-4c--variables--secrets-rest-api)
- [Topic 4D — Self-Hosted Runners](#topic-4d--self-hosted-runners)
- [Topic 4E — Custom Actions Authoring](#topic-4e--custom-actions-authoring)
- [Topic 4F — Editions, GHES & GitHub Connect](#topic-4f--editions-ghes--github-connect)
- [Topic 4G — Packages & GHCR Publishing](#topic-4g--packages--ghcr-publishing)

**Domain 5 — Secure & optimize**
- [Topic 5A — Untrusted Input & Token Hardening](#topic-5a--untrusted-input--token-hardening)
- [Topic 5B — OIDC Keyless Cloud Auth](#topic-5b--oidc-keyless-cloud-auth)
- [Topic 5C — Action Enforcement Policies & Build Provenance](#topic-5c--action-enforcement-policies--build-provenance)
- [Topic 5D — Optimization & Retention](#topic-5d--optimization--retention)


---

## Topic 1A — Triggers, Permissions, Inputs, Reusable Workflows

### Triggers
- `workflow_dispatch` = **internal** (UI / `gh` CLI / API; typed inputs).
- `repository_dispatch` = **external** POST to the dispatches endpoint with a custom `event_type`.
- Dispatch endpoints (both POST):
  - `repository_dispatch` → `/repos/{o}/{r}/dispatches`
  - `workflow_dispatch` → `/repos/{o}/{r}/actions/workflows/<id>/dispatches`
- `schedule`:
  * **min 5 min** spacing
  * **default branch only**
  * best-effort (delayed/dropped under load; avoid top-of-hour)
  * Cron weekdays example: `0 0 * * 1-5`.
  * Runs use the **latest commit on the default branch** (not a fixed/pinned commit).
- `star` event = repo **starred/unstarred** (activity types `created` / `deleted`).
- Narrow events with:
  * `types:` →  ⚠️ **`types:` REPLACES the default set (opened, synchronize, reopened), doesn't extend it.**
    - To keep the defaults *and* add more → re-list them all, e.g.: `types: [opened, synchronize, reopened, labeled]`.
    - Most events default to **all** activity types; `pull_request`/`pull_request_target` are the exception (default = `opened`/`synchronize`/`reopened`).
  * `branches:`/`branches-ignore:`
  * `paths:`/`paths-ignore:`
  * `tags:` → `tags:` is for `push`, **not** `pull_request`.
- `synchronize` (a `pull_request` type) = **new commits pushed to the PR head/source branch** — the activity that re-runs CI on every push to an already-open PR.
- `pull_request` `branches:`/`paths:` filters match the **base (target) branch** (where the PR merges INTO), NOT the source/head branch. `!pattern` excludes; a later negative line removes earlier matches.
- ⚠️ **No `merged` activity type exists.** To run only on a merged PR:
  ```yaml on: 
    pull_request: 
      types: [closed]
       + `if: github.event.pull_request.merged == true`.
  ```
- ⚠️ **Which branch's workflow file runs?**
  - Only **`push` & `pull_request`** run the workflow from the event's (possibly non-default) branch — so only they can fire a not-yet-merged workflow.
  - **All other events** (`schedule`, `repository_dispatch`, `workflow_dispatch`, `star`, `issues`, …) use the **default-branch** version.
- **Skip a run:**
  - Tokens: `[skip ci]`, `[ci skip]`, `[no ci]`, `[skip actions]`, `[actions skip]` (or a `skip-checks: true` trailer).
  - Placed in **any commit message of a push**, or in the **HEAD commit of a PR**.
  - Applies **only** to `push` & `pull_request` (not `pull_request_target`).
  - `ci` tokens = cross-tool convention (Travis/GitLab); `actions` tokens = GitHub-specific.

### permissions / GITHUB_TOKEN
- Token is **per-job + ephemeral** (expires when the job ends).
- ⚠️ **Job-level `permissions:` REPLACES workflow-level (DOES NOT MERGE).** Any **unlisted scope → counts as `none`**.
- `{}` = no access; `read-all` / `write-all` = shortcuts.
- **Default read-only** for new repos/orgs/enterprises (`contents`+`packages` read). **Repo ← org ← enterprise** inheritance.
- **Fork PR token = read-only** unless an admin enabled "Send write tokens to workflows from pull requests."
- `403: Resource not accessible by integration` = missing scope → add it to `permissions:`.

### Input types  ⚠️ MEMORIZE THE TWO SETS
- `workflow_dispatch`: 5 types: **string, boolean, choice, number, environment**. `type` is **OPTIONAL** (defaults `string`).
- `workflow_call`: 3 types: **string, number, boolean** (no `choice`, no `environment`) `type` is **REQUIRED**. 
- `choice` **requires `options:`**
- ⚠️ `description`: **required** in `action.yml` inputs; **NOT** required in `workflow_dispatch` inputs.
- ⚠️ `github.event.inputs.*` = **always strings** (`"false"` is truthy!). `inputs.*` = **typed**. Therefore inputs context is often preferrable.
- `type: environment` = **picker only** (environment-protection mechanics → 5C)
- dispatch limits: **25 inputs max** (raised from 10; verified 2026-06-30 vs docs), **65,535-char** payload.
- When triggered by `workflow_call` unset fallback to defaults: **`false` / `0` / `""`**.

### Reusable workflows (`workflow_call`)
- Called at **JOB level**: `jobs.<id>.uses: owner/repo/.github/workflows/x.yml@REF` (**ref required**).
- `secrets: inherit` = **all** caller secrets (**org + repo**), **same org/enterprise only**.
- ⚠️ **Two separate channels when calling a reusable workflow**
  - `with:` = the **inputs** channel.
  - `secrets:` = the **secrets** channel (or `secrets: inherit`).
  - ❌ Putting a secret in `with:` — i.e. referencing `secrets.*` inside the caller's `with:` — is a **parse-time error**. Pass secrets through `secrets:`.
- Environment secrets **not passable** via `workflow_call`; set `environment:` on the reusable job instead.
- Nesting allowed; **permissions only reduce down the chain, never elevate.**
- **Limits** *(verified 2026-07-01 vs docs)*:
  - **max 50** unique reusable workflows callable per file (raised from 20).
  - **nesting depth 10** levels = top-level caller + 9 (raised from 4).
  - No **loops (cycles)** in the call chain — a reusable workflow can't call itself, directly or indirectly.
- Workflow-level (`workflow_call`) outputs use the **`value:`** key; **job-level outputs do NOT** (`<name>: ${{ steps... }}` directly). See 1E.
- **Reusable workflow vs composite action:
  - Reusable = **job-level** `uses:`, own runner, has a `secrets:` block. 
  - Composite = a **step** in a job, caller's runner, **no** `secrets:` block (secrets arrive as `with:` or directly in env)

---

## Topic 1B — Contexts, Expressions & Secret Leakage

### Context — what the term means HERE
- A **context** = a **read-only bag of runtime data**, read via `${{ }}`
  * Examples: 
    - `github` → event/actor/ref/sha/repo 
    - `needs` → upstream job outputs 
    - `matrix` → this job's axis values 
    - `steps` → id'd step outputs in the **same** job 
    - `runner` → runner machine facts.
- ⚠️ `github.repository` = full **`owner/repo`**; owner alone = `github.repository_owner` (there is **no** `github.org` / `github.organization`).

### env vs vars vs secrets  ⚠️ THE contrast
- `env` = **custom environment variables**, inline in YAML:
  - **auto-exposed as shell `$NAME`**
  - **not masked**
  - Scopes: **workflow / job / step only**
  - Inheritance flows parent→child (innermost wins); **siblings never see each other**
- `vars` = **configuration variables** (UI/API config):
  - **read only via `${{ vars.X }}`**
  - **NOT masked**
  - **must map to `env:` to read it as a shell `$VAR`** (not auto-exposed like `env`)
    - the same map-to-`env:` + quoted `"$VAR"` pattern also **safeguards against script injection** for **untrusted** `${{ }}` values (PR titles, branch names…)
  - Scopes: **enterprise / org / repo / environment** (precedence + limits → 4C)
- `secrets` = UI/API sensitive:
  - **read only via `${{ secrets.X }}`**
  - **auto-masked**
  - **must map to `env:` to read it as a shell `$VAR`** (not auto-exposed like `env`)
    - here that mapping is **access only, NOT an injection fix** — secrets are maintainer-set (trusted), so the risk isn't injection but **leakage** (masking is best-effort)
- ⚠️ **secrets masked / vars NOT masked** ← the whole exam point. A sensitive value in `vars` = leak.
- `env:` blocks **don't self-reference** (one entry can't use another from the same block).
- Env-var **names are case-sensitive** regardless of OS/shell.

### github ref family — by event
- `github.ref`:
  - push (branch) → `refs/heads/<branch>` (**NOT** the SHA — that's `github.sha`)
  - push (tag) → `refs/tags/<tag>`
  - PR (unmerged) → `refs/pull/<n>/merge`
  - PR (merged) → `refs/heads/<base>`
- `github.ref_type` (`branch` / `tag`) is a **different** value from `github.ref`.
- `github.ref_name` = the short ref name; on `pull_request` it is `<n>/merge` (**not checkout-able**) → use `head_ref` for the source branch.
- `github.head_ref` = PR **source/head** branch (short, e.g. `feature-x`).
- `github.base_ref` = PR **base/target** branch (e.g. `main`).
- ⚠️ **Both PR-only — empty string on every non-PR event.**

### Default env vars — `GITHUB_*` vs `RUNNER_*`
- **`GITHUB_*`** = repo/event/workflow data: `GITHUB_WORKFLOW`, `GITHUB_REPOSITORY`, `GITHUB_ACTOR`, `GITHUB_SHA`, `GITHUB_REF`, `GITHUB_RUN_ID`/`_NUMBER`, `GITHUB_JOB`, `GITHUB_EVENT_NAME`, `GITHUB_WORKSPACE`, `GITHUB_API_URL`, …
- **`RUNNER_*`** = runner-machine facts, mirroring the `runner` context (`runner.os` ↔ `RUNNER_OS`): `RUNNER_OS` (Linux/Windows/macOS), `RUNNER_ARCH` (X86/X64/ARM/ARM64), `RUNNER_NAME`, `RUNNER_TEMP`, `RUNNER_TOOL_CACHE`. NOT `GITHUB_RUNNER_OS`.
- ⚠️ **`GITHUB_TOKEN` is NOT a default env var** — it's a secret (`secrets.GITHUB_TOKEN` / `github.token`); map it to `env:` yourself if the shell needs it.

### Matrix (primer; depth = 1C)
- `strategy.matrix` is **per JOB**; runs the job once per **cross-product** combo, **parallel** by default.
- Throttle with **`max-parallel`** (1 = sequential). It caps a **count**, not an "axis." Combo order = don't rely on it.
- `needs: <matrix-job>` waits for **ALL** combos — a matrix job = **one graph node**.
- **Matrix outputs:** all combos write the **same** output names → overwrite (**last wins, unreliable**). Fix: unique names via `matrix` context, e.g. `result_${{ matrix.x }}`.

### Expression evaluation — two phases
- **Setup phase** (before runners): job graph, **matrix expansion**, names, concurrency, `needs`.
- **Execution phase** (on runner): `if:`, `run:`, `with:`, env interpolation, step/job outputs.
- **Context availability by location:** top-of-file = ~nothing · job-level `if:`/`strategy` = `github`/`needs`/`vars` (**NO `steps`, NO `runner`**) · step-level = **everything**.
- ❌ `jobs.x.if: ${{ steps.y.outputs.z }}` fails — `steps` not available at job level.
- Matrix is **fixed at setup** → dynamic matrix = **`fromJSON(needs.<prior>.outputs.list)`**, never from a same-job step. (`fromJSON` = real built-in; full treatment 1C.)

### Status functions & implicit `success()`
- Status-check functions (used in `if:`): `success()` (**implicit default**), `failure()`, `always()`, `cancelled()`, `!cancelled()`. NOT functions: `completed` / `state` / `status`.
- ⚠️ **Every step and job carries an implicit `if: success()`** — even with **no `if:` at all**. It's why a job halts at the first failing step, and why a `needs:` job won't start if its dependency failed. A failing step **does** stop the job by default.
- **`if:` exists at job + step level ONLY** — there is **no workflow-level `if:`**.
- **Scope of the implicit `success()` by level:**
  - **STEP-level** = "no **earlier step in this same job** failed/cancelled."
  - **JOB-level** = "no job in my **`needs:`** failed/cancelled."
- ⚠️ Putting **any** status function (`always()` / `failure()` / `cancelled()` / `!cancelled()`) into an `if:` **removes the default `success()` entirely** — so at job level you must re-add the safety check yourself, e.g. `if: ${{ !cancelled() && needs.build.result == 'success' }}`.
- Run a step only when a specific prior step failed: `if: failure() && steps.<id>.outcome == 'failure'` (a bare `outcome` check alone would be skipped).
- The surrounding `${{ }}` is **optional** in `if:` (`if: success()` == `if: ${{ success() }}`).
- ⚠️ **Secrets are NOT usable in `if:`** (job or step) — validation error. To gate on a secret: map it to a job-level `env:` var, then `if: ${{ env.X != '' }}` (an unset secret → empty string).

### Secret leakage — masking is best-effort
- Masking catches the **raw secret + common encodings (notably Base64)** — so `base64(secret)` IS masked. But **NOT guaranteed**:
  - `echo "${{ secrets.T }}"` → `***`  ·  `echo "${{ secrets.T }}" | base64` → `***` (Base64 handled)  ·  `... | rev` → **CLEAR TEXT** (uncommon transform).
  - Leaks via: **structured/JSON secrets**, splitting/substringing, odd transforms, and the `base64(secret+suffix)` padding edge case.
- ⚠️ A freshly **decoded/derived** value is **not** covered by auto-mask → register it with **`::add-mask::$VALUE`** (real workflow command). Never store structured data (JSON/XML) as a secret.
- **Outputs are NOT a secret channel** — they flow to GitHub + downstream as ordinary data. (A real registered secret in an output *is* redacted on the runner; a self-minted value is not.)
- **Script injection** (also 5A): never interpolate untrusted `${{ }}` (PR title / branch / issue body / commit msg) straight into `run:`. **Bind to `env:`, then use `"$VAR"` quoted.**

### Passing secrets — where & how
- Already a registered secret? → read **`${{ secrets.X }}`** in the later job. Available run-wide; **no passing.**
- Calling a reusable workflow? → hand it over via the **`secrets:`** block (or **`secrets: inherit`**). Separate trust boundary; secrets don't cross automatically.
- A value you generated & must reuse downstream? → **`::add-mask::`** it, OR better: **don't pass the credential** — write the artifact/result it protects, not the secret.


---

## Topic 1C — Matrix Strategy In Depth

### Where keys live ⚠️ (don't confuse levels)
- `matrix` / `fail-fast` / `max-parallel` → **only under `strategy:`**.
- `continue-on-error` → on a **JOB** or a **STEP** (NOT under `strategy:`).
- `runs-on` / `needs` → **JOB** level.

### Resolution order
- **EXPAND → EXCLUDE → INCLUDE.** `include` runs **last** and can **re-add** an excluded combo. (A common blog states this backwards — it's wrong.)
- `exclude`/`include` entries **don't accept arrays** — one scalar set per list item.

### include behavior
- Entry's matrix keys **match** an existing combo → **AUGMENT** (add extra keys).
- Keys **don't match** any combo → **NEW combo**.
- **Original axis values never overwritten**; include-added keys **can** be overwritten by a later include.
- **include-only** (no base axes) = explicit hand-picked combo list.
- **Counting rule:** base = product of the axes; each `include` entry merges into an existing combination **only if it doesn't overwrite an original matrix value**, else it adds a **NEW** combination. Worked example: `2×2` base `+ 1` unmergeable include = **5** jobs.

### fail-fast / max-parallel / continue-on-error
- **`fail-fast` default = `true`** → first failing combo **cancels** all in-progress + queued. Set `false` for full reports.
- `max-parallel` = cap on **simultaneous** combos (default = max allowed). A **count**, not an axis.
- ⚠️ **`concurrency` ≠ `max-parallel`:** `concurrency` limits **concurrent workflow runs** (and can `cancel-in-progress`, see 5D); `max-parallel` throttles **matrix legs within one run**.
- ⚠️ **Swallow vs preserve** (THE distinction):
  - `continue-on-error: true` → **SWALLOWS** failure: run not failed, **downstream `needs:` sees SUCCESS**.
  - `fail-fast: false` → **PRESERVES** failure (still counts, blocks `needs:`), just doesn't cancel siblings.
- ⚠️ `fail-fast: true` + **flat** `continue-on-error: true` = **pointless** (fail-fast inert). Meaningful only as `continue-on-error: ${{ matrix.experimental }}` (per-combo carve-out).

### Dynamic matrix via fromJSON
- Matrix is fixed at **setup** → can't build from a **same-job** step output. Use a **PRIOR job** + `needs:` + `fromJSON`.
- Producer: set a **single-line JSON string** job output (`jq -c`). Consumer: `matrix: ${{ fromJSON(needs.<job>.outputs.<key>) }}`.
- **object** → whole matrix (keys become axes) · **array** → one axis OR the `include` list.
- `needs:` mandatory · malformed JSON → matrix won't expand · **empty array → ZERO jobs** (skipped, not failed).

### Matrix over a whole reusable workflow
- You CAN parallelize an **entire reusable workflow**: put `strategy.matrix` on a job whose body is `jobs.<id>.uses: <reusable-wf>@ref` → runs that whole reusable workflow once per matrix combo. (Matrix itself is still job-scoped; this is the mechanism.)

### Runner images & -latest (verified June 2026; mappings DRIFT)
- `-latest` labels **float** — GitHub migrates them to newer OS gradually (~1–2 months) → **non-deterministic over time**. **Pin** a version label for reproducibility.
- Current: `ubuntu-latest`=**Ubuntu 24.04** · `windows-latest`=**Windows Server 2025** (=`windows-2025`) · `macos-latest`=**macOS 15 Arm64** (gotcha: Apple silicon).
- **Ubuntu 20.04 retired** (unsupported since **2025-04-01**) → `runs-on: ubuntu-20.04` **fails**.
- ⚠️ **Pinning stops silent migration, NOT deprecation** — a pinned old label still dies when the image is retired.
- (Newer, likely post-exam: `ubuntu-26.04` = public preview; `windows-latest` moving to "Server 2025 + VS 2026" toolset, June 2026.)


---

## Topic 1D — YAML Anchors, Aliases & Merge Keys

### Support matrix ⚠️ THE whole topic
- `&` anchor + `*` alias → **SUPPORTED** (shipped **2025-09-18**, auto-enabled all repos). Before that: errored.
- `<<` **merge key → NOT SUPPORTED.** GitHub shipped "half the feature." Official docs document only `&`/`*`.
- ⚠️ Don't generalize: "anchors supported" ≠ "merge keys supported." They are **not** the same feature.

### Anchors / aliases mechanics
- Alias copies the **WHOLE node** — **all-or-nothing**, NO partial override.
- **Define before use** — anchor must appear **above** any alias to it (top-to-bottom). Alias-before-anchor = error.
- **Same file only** — NOT a cross-file/cross-repo reuse tool (that's composite actions / reusable workflows).
- Can anchor any node: scalar, sequence (e.g. shared `paths:` across triggers), mapping, or a whole job.

### Merge keys — the trap
- ⚠️ `<<: *base` in a workflow = **broken/invalid**, not inherit-and-override. (Exact failure mode — hard error vs literal `<<` key — unverified; either way the merge does NOT happen.)
- Want **base + override one key**? → **composite action or reusable workflow.** Anchors = exact duplication only.
- `<<: *base` is a classic **"spot the mistake"** distractor (objective 2.3 reading/analysis).
- Trivia: merge keys are a YAML **1.1** optional type, never in core 1.2 → inconsistent parser support generally.

### Exam weight ⚠️ uncertain
- Feature shipped Sept 2025, exam reworded Jan 2026 → weight/form **not verified**. Likely tested as *read-and-analyze* / *spot-invalid-`<<`* rather than authoring. Calibrate vs practice exams.


---

## Topic 1E — Outputs, Summaries & Retention

### Job summaries — `GITHUB_STEP_SUMMARY`
- It's an **environment FILE** (the variable = a file path). Append **GFM Markdown**; renders as the **job summary** on the run summary page.
- `>>` appends (auto-newline each append); `>` overwrites **the current step's** buffer only.
- ⚠️ **1 MiB per step** limit → exceeding it **aborts** that step's summary (error "1024k"), not silent truncation.
- Renders GFM: tables, Mermaid, alerts (`> [!NOTE]`). `<details>` must stay within ONE step (isolation breaks cross-step tags).

### Job summaries — step isolation
- `GITHUB_STEP_SUMMARY` is a **SEPARATE file PER STEP**. Steps are isolated.
- `>>` appends to the CURRENT step's file; `>` overwrites ONLY the current step's buffer.
- ⚠️ `>` can **NEVER** wipe another step's summary. At job end all step files are grouped into one job summary. (Trap: assuming `>` in a later step clears the whole job summary — it doesn't.)
- Across jobs: summaries ordered by **job completion time**, not definition order.

### The four environment-file siblings (all use `>>`)

| File / command | Purpose | Read back via |
|---|---|---|
| `GITHUB_STEP_SUMMARY` | Markdown for **humans** (run summary page) | — (rendered) |
| `GITHUB_OUTPUT` | step **output** for machines | `steps.<id>.outputs.*` |
| `GITHUB_ENV` | env var for **later steps** | `$NAME` |
| `::warning::` / `::error::` | annotations (inline highlights) | — (not rich content) |

- Cross-step data sharing is **not** a sibling reference: write `$GITHUB_ENV` (for later steps) or step outputs via `$GITHUB_OUTPUT` → `steps.<id>.outputs.X`.

### Artifacts vs cache ⚠️
- **Artifact** = persist a run's OUTPUTS (share between jobs, download, inspect). Reliable & retained.
- **Cache** = SPEED (restore deps across runs by key). **Best-effort, can be EVICTED, NOT guaranteed.**
- Cross-job:
  - FILE/binary → **artifact**
  - small STRING/metadata → **job output** (`needs.<job>.outputs.X`)
  - Cache is NOT a transfer tool.
- Anti-patterns:
  - cache to pass build output between jobs (unreliable)
  - artifacts as a dep cache (slow/costly)

### `actions/cache` mechanics
- `key` = exact key.
- `path` = files to cache.
- **`restore-keys`** = ordered **fallback prefixes** — on an exact-key miss, restore the most recent **partial** match (still reports `cache-hit: false`).
- `enableCrossOsArchive` = cross-OS restore.
- `cache-hit` output = hit/miss.

### Cache vs artifact — access scope
- ⚠️ **Cache scope is a HARD isolation boundary:** a run can read caches from its **own branch + the default branch (+ PR base)**; **sibling branches are isolated**. Default-branch caches are shared to all.
- **Artifact scope defaults to the RUN** — but that's a **SOFT** default, not a wall. With `actions: read` + `run-id` (+ optional `repository`), `download-artifact` v4+ pulls artifacts from **other runs and repos**.
  - *(Reconciles an earlier keeper that called artifact scope a hard "the RUN" boundary — it is the default reach, openable by permissions; only cache's branch scope is hard.)*

### Retention numbers ⚠️ TWO DIFFERENT SETS (easy to confuse)

| | Default | Public cap | Private/internal cap |
|---|---|---|---|
| **Artifacts / logs** | 90 days | ≤ 90 | ≤ 400 (range 1–400) |
| **Cache** | 7 days | ≤ 90 | ≤ 365 |

- **Cache size cap:** 10 GB/repo default, **LRU eviction** over the limit.
- ⚠️ **Understand *why*:** cache = disposable/churns fast + size-capped LRU; artifact = retrievable results. Don't memorize in isolation.
- ⚠️ **A retention-period change is NOT retroactive** — it applies to **NEW objects only**; existing artifacts keep their original lifespan (by design). To reclaim now → delete explicitly.
- Per-artifact override: `retention-days:` on `upload-artifact` (capped by repo/org/enterprise max). `compression-level: 0–9`.
- `upload-artifact@v4` / `download-artifact@v4` current; **v3 deprecated & stopped working**. (v4: artifact names must be unique within a run.)
- **No official `actions/delete-artifact` action** — delete via REST API, delete the run, or the per-artifact UI.

### Retention & deletion via REST API (verified)
```
GET    /repos/{o}/{r}/actions/artifacts                  # list repo artifacts
GET    /repos/{o}/{r}/actions/runs/{run_id}/artifacts    # list a run's artifacts
DELETE /repos/{o}/{r}/actions/artifacts/{artifact_id}    # delete one  <- retention workhorse
GET    /repos/{o}/{r}/actions/artifacts/{id}/{format}    # download (format=zip; URL expires in 1 MIN)
DELETE /repos/{o}/{r}/actions/runs/{run_id}              # delete a whole run
```
- "Enforce retention" programmatically = **`retention-days` (declarative) + list + DELETE on a schedule** (`gh cache delete` for caches).
- ⚠️ **There is NO confirmed REST endpoint to SET the retention period.** `PUT .../actions/retention` is **UNVERIFIED / likely not official** — do NOT trust it. Default-retention config is UI/org-policy. REST does **get / list / delete** only.
- ⚠️ **Quota recalculation lags** (commonly 6–24h). A "storage quota exceeded" error can persist *after* a successful delete — the deletion didn't fail; just wait + lower retention going forward.

### VS Code GitHub Actions extension (`GitHub.vscode-github-actions`)
- Two halves: (1) **authoring** — schema validation + completion, incl. smart checks of job/step references and event-payload validation from `on:`; (2) **run management** — view/cancel/re-run/trigger runs, drill runs→jobs→steps, view logs.
- ⚠️ **No remote repos** — github.dev / vscode.dev unsupported; use a local clone. GHES support = experimental beta.
- NOT the same as "GitHub Local Actions" (third-party, runs workflows locally via `act`).


---

## Topic 2A — Troubleshooting Matrix Runs

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
- Re-runs create a **new ATTEMPT:**
  - old run preserved
  - attempt navigation
  - **reuses the original SHA/ref** (not a fresh checkout of the branch)
- **Re-run actor split:**
  - `github.actor` / `GITHUB_ACTOR` = the **original** triggerer (unchanged on re-run; the re-run uses its privileges).
  - `github.triggering_actor` / `GITHUB_TRIGGERING_ACTOR` = whoever **re-ran** it (changes).
- **Permissions:** re-running workflows **and** deleting logs both require **WRITE**. Download run logs = `GET /repos/{o}/{r}/actions/runs/{run_id}/logs`.

### KEEPER GOTCHA — single-job API rerun archives the attempt ⚠️
- `POST .../actions/jobs/{job_id}/rerun` creates a NEW attempt → remaining old failures are now in the ARCHIVED attempt.
- Trying to individually rerun a second old failure → **HTTP 403 "Only jobs from the current attempt can be re-run."**
- **No endpoint to rerun a SUBSET** of jobs in one call. Options: `rerun-failed-jobs` (ALL) or one-at-a-time.
- To retry several specific legs: use `rerun-failed-jobs`, or rerun them before a new attempt archives them.

### Edge bug (not the rule)
- Matrixed **reusable** workflows: "Re-run failed jobs" may restart the failed leg but NOT its downstream dependents inside the reusable workflow. (Documented behavior = failed + dependents; this is a reported bug.)


---

## Topic 3A — Immutable Releases & Version Pinning

*Objective 3.2. Enforcement specifics → see 5C.*

### ⚠️ HEADLINE TRAP — a Release is NOT automatically immutable
Two independent checks; a tag ref is locked only if **BOTH** pass:
1. **Is it a release at all?** Bare tag (no release) → movable.
2. **Is that release _immutable_?** Publishing a release does **NOT** lock it. Immutable **only if** the repo/org had immutable releases **enabled at publish time**. Setting off (or an older release) → **mutable release = still movable** (assets + tag changeable).

Three states of any tag: **bare tag → movable** · **mutable release → still movable** · **immutable release → locked**.

> ⚠️ **The exam trap:** "it's a Release on a clean `v3.4.0` tag, so it's locked." ❌ WRONG. A Release ≠ an immutable Release. The version string *and even the existence of a release* tell you nothing — only the **immutable** status does.
>
> **Don't get fooled by the semver tag alone** — `@v3.4.0` can be a bare tag, a mutable release, OR an immutable release. Lock comes from the **immutable status** (or a full SHA), never the version text.

### How a consumer checks immutability
- **Release page:** **"Immutable" label** below the title (no label ⇒ not immutable).
- **REST:** `GET /repos/{o}/{r}/releases/tags/{TAG}` → the release object's **`immutable` boolean** (404 ⇒ no release / bare tag).
- **CLI:** `gh release verify <tag>` (succeeds + loads attestation ⇒ immutable).
- *(GitHub's own user-facing "how to check" docs are still an open issue — under-documented.)*

### ⚠️ Better-safe-than-sorry rule
**A full commit SHA is immutable by construction** — no audit of the author's release/setting needed. When in doubt, **pin the SHA**.

### Immutable releases — the lock
- **= assets locked + Git tag locked** (+ tag name unreusable after deletion + auto signed attestation). ← don't drop the **tag** lock.
- It's a **repo/org setting** (UI or REST API) — **NOT** a workflow-YAML key. No `immutable: true` in YAML. (spot-the-mistake)
- **Disabling it later does NOT un-freeze** already-immutable releases.
- Publishing locks instantly → author flow: **draft → attach assets → publish**.
- Attestation = **Sigstore bundle**; verify with `gh release verify` / `gh release verify-asset`.
- Immutability attaches to the **release, not a bare tag** → an author keeps a tag movable by **not creating a release** for it.

### Pinning spectrum (consumer)  — least → most safe
`@main` (branch, worst) → `@v4` (floating major) → `@v4.1.0` (plain version tag) → `@<full 40-char SHA>` (best)
- Tags = **movable pointers**; full SHA = **content-addressed, can't be re-pointed**.
- **Full 40-char SHA** only — short SHAs are ambiguous / not accepted.
- On an immutable-releases repo: best readable option = a version tag `@v4.1.0` **that is itself a published immutable release** ≈ a SHA.
- **`@v4` floating stays movable as long as no immutable release is published on it** (authors keep it release-free so it can advance). The name `v4` decides nothing.

### ⚠️ Flags (uncertain — calibrate vs practice exams)
- **OCI/`ghcr.io` publishing** of actions: status conflicting; first-party publish action README says **not for public use**. Treat as **not confirmed GA**.
- **Dependabot + SHA-pinning alerting** interference: **unverified**. (Updates of SHA-pinned actions = confirmed.)

### ⚠️ Do not confuse
- **Immutable *subject claims*** = an **OIDC token format** change (→ 5B). **Different feature**, not immutable releases.


---

## Topic 4A — Runner Networking & Access Boundaries

*(Domain 4 · 4.4)*

### ⚠️ MASTER DISTINCTION — egress identity vs private reachability
- **Egress identity** = the predictable *source IP* the runner presents → for **IP allow lists** / target firewalls. Tools: **self-hosted** or **static-IP larger runners**.
- **Private reachability** = getting onto/into a network with **no public endpoint** → DB, Artifactory, on-prem API. Tools: **Azure VNET**, **WireGuard**, **API gateway + OIDC**.
- ⚠️ **Don't cross them:** a static IP does NOT grant reachability; a VNET does NOT (by default) give an allow-listable egress IP.

### ⚠️ NO "Actions" toggle on an IP allow list
Only two controls exist:
1. **Enable IP allow list** (enforcement on/off)
2. **Enable IP allow list configuration for installed GitHub Apps** (auto-imports App-declared IPs; happens even if the list isn't enabled)

Actions is gated **purely by the runner's IP**. Distractor bait: *"...for Actions runners"*, *"...for Actions and Pages."*

### ⚠️ Static IP and Azure VNET = mutually exclusive
- VNET runners use **dynamic IPs**; can't also assign a static IP.
- VNET + **Azure default outbound** ⇒ egress IPs **unpredictable**, **not** allow-listable → need **NAT gateway / stable outbound IP**.

### IP allow list — fast facts
- **GHEC only.** Gates **PRIVATE** resources (public stays open).
- ⚠️ **Role-blind** — applies to owners, repo admins, outside collaborators too → **lockout risk**, keep ≥2 owners.
- **Adding entries ≠ enforcing** — must tick *Enable IP allow list*.
- Org-level **or** enterprise-level (enterprise entries inherited; org can add but not edit inherited).
- CIDR notation.

### Hosted-runner conflict
- Standard hosted runners = **wide + shared + weekly-rotating Azure IPs** ⇒ can't practically allow-list (and it weakens control).
- Under an allow list, use **self-hosted** OR **static-IP larger runners**; add the runner IP/range to the list. (Standard runner ⇒ `checkout` 403.)

### Carve-outs / exemptions (distractors)
- **Dependabot** = exempt (first-party App).
- **GitHub App server-to-server installation tokens** = not currently restricted.
- **Codespaces** = unusable for org repos when an org allow list is set.

### Private networking paths
- **Static IP larger runner** → egress identity:
  - fixed range, usable *with* an allow list
  - dual ranges, scales past 500 concurrency
- **Azure VNET** → reachability:
  - **VNET injection** = NIC in your subnet, **VM stays GitHub-side**; inherits NSG / ExpressRoute / VPN.
  - **2–64 vCPU Ubuntu + Windows only.**
  - Setup order = Azure resources first → network config → runner group; size subnet > max concurrency.
- **API gateway + OIDC** and **WireGuard overlay** → reachability, **work with standard runners** (patterns you build).

### OS/size exclusions
- **macOS larger runners** = **no** Azure VNET, **no** static IP.

### ⚠️ Watch-outs (uncertain / evolving — don't over-commit)
- "Artifacts exempt from allow list" = **community claim, unverified**.
- GHES docs say hosted runners wholly incompatible (older/absolute); GHEC adds the static-IP exception.
- VNET NICs moving to a GitHub service subscription; **VNET failover** in public preview.
- Subnet buffer %: docs ~30% vs GitHub Learn 20% — know the *principle* (size > max concurrency), not the number.


---

## Topic 4B — Runner Images & Toolcache

*(Domain 4 · 4.6)*

### ⚠️ Three SOURCES + one STORE (don't make the tool-cache a "source")
- **Preinstalled** (baked) = TWO layers:
  - (a) system-wide on `PATH` (git, docker, default Node/Python, apt pkgs)
  - (b) **Cached Tools** = extra runtime *versions* in the tool-cache (ubuntu-24.04: Go, Node, Python, PyPy, Ruby)
- **`setup-*` actions** (run-time picker).
- **Your installs** (`apt-get`/`pip`/`brew`/manual).
- **tool-cache (`_work/_tool`)** = the SHELF. Filled by preinstall + `setup-*` only. **Direct installs never touch it.**

### ⚠️ Direct installs are INVISIBLE to `setup-*`
`apt-get install python3.12` → `setup-python` does NOT see it. `setup-python` uses a cached version if present, else downloads into the tool-cache. The apt result is irrelevant in all cases.

### ⚠️ HOSTED = speed, not persistence
- Tool-cache on hosted = **per-VM**, wiped every job. Preinstalled versions give *fast starts*, but nothing you download mid-job survives.
- ⚠️ What persists across **hosted** jobs = **`actions/cache`** (deps), a *different* cache — don't confuse the two.
- **SELF-HOSTED** = same machine ⇒ `_work/_tool` survives ⇒ a `setup-*` download sticks for later jobs (manual installs persist too → drift risk). Runner management → 4D.

### Custom images ⚠️
- **LARGER runners ONLY → Team/GHEC.** Not standard runners, not Free. GA ~April 2026 (was preview Oct 2025).
- ⚠️ **Custom image ≠ self-hosted.** Still **GitHub's infra**. The image lives in the org Actions → **"Custom images"** catalog — **NOT** `ghcr.io`, **NOT** your registry. No cross-CI reuse. Not a general VM pipeline.
  - Distractor bait: "pushed to ghcr.io", "reuse on CircleCI", "you patch the OS like self-hosted."

### Custom images — fast facts
- **3 steps:** image-generation runner → generate via `snapshot` → assign to runner group + `runs-on`.
- **Platform match:** gen-runner platform = target (Linux x64 / Linux ARM64 / Windows x64). Run image on **same size or larger**.
- **`snapshot` syntax:**
  - String (`snapshot: name`) = name only, GitHub versions it.
  - Mapping (`image-name:` + `version:`) = name + **major** version; **minor auto-increments, NO patch**.
- **Version created ONLY on job success.** Fail/incomplete ⇒ no new version.
- **Storage billed separately** (Actions storage); each snapshot = new version ⇒ storage grows. Enterprise owners set **retention policy**.
- **Security:**
  - dedicated runner group for image gen
  - **don't share prod with dev/test** (injection)
  - buildable from **any branch** ⇒ write access = trigger ⇒ least privilege

### Find the exact image software
Log → **Set up job → Runner Image → "Included Software"** link. Source = `actions/runner-images`, refreshed ~weekly. Don't assume presence/version — pin `setup-*` + explicit version.

### ⚠️ Unverified (calibrate vs practice exams)
- Hosted tool-cache **path** `/opt/hostedtoolcache` + env var `RUNNER_TOOL_CACHE` — not re-verified (documented default = `_work/_tool`).
- Custom-image **retention 60-day default / 90-day max** — community-reported, not docs-confirmed.
- Hook env-var names `ACTIONS_RUNNER_HOOK_JOB_STARTED`/`_COMPLETED` — from a community blog. (Cleanup-hook keys for *actions* → 4E.)


---

## Topic 4C — Variables & Secrets REST API

*(Domain 4 · 4.7, 4.8)*

### ⚠️ Variable precedence — MOST SPECIFIC wins
`environment > repository > organization`. Docs say "lowest level takes precedence" = closest to the job.

### Scope levels
- Configuration-variable / secret scope levels = **organization / repository / environment**.
- ⚠️ An **environment is repo-scoped** — there is **NO** environment shared across repositories (common distractor).

### ⚠️ Env-level timing trap
Environment-level variables land on the runner **only after the job starts** ⇒ they do **NOT** overwrite `env`/`vars` during **pre-job processing**. So an env-level var can't feed `runs-on` / early-evaluated keys. Distractor bait: "set the runner via an environment variable."

### ⚠️ Reusable-workflow trap
A called (reusable) workflow uses the **CALLER's** repository variables. The called workflow's **own** repo variables are **NOT** available to it.

### ⚠️ 256 KB combined — env excluded
Combined **org+repo** variables = **256 KB / workflow run** (GitHub.com/GHEC; **GHES = 10 MB**).
- Over the cap → only org vars under it served (after repo vars, alphabetical).
- **Environment vars don't count** → push overflow into environments.
- Other per-item limit: **48 KB/var**.
- Count limits: **1000 org / 500 repo / 100 env**.

### ⚠️ Variables = PLAINTEXT, Secrets = ENCRYPTED
Variables: visible in settings, **not masked**, for non-sensitive config. Secrets: libsodium-sealed + masked. Never put sensitive data in a variable.

### Org-level shareable/reusable components
- **Shareable (4):** Secrets · Configuration Variables · Self-Hosted Runners · Workflow Templates.
- **NOT shareable:** Environment Variables (inline `env:`) · Cache · Artifacts (run/repo-scoped).
- ⚠️ Trap = **Configuration Variables (yes)** vs **Environment Variables (no)**.

### Secrets via REST — 3-step encrypt-first
1. **GET** `…/actions/secrets/public-key` → `{ key_id, key }`
2. **Encrypt** plaintext with that key via **libsodium sealed box**, Base64 it
3. **PUT** `…/actions/secrets/{name}` body `{ "encrypted_value", "key_id" }` — **idempotent create-or-update (PUT, not POST)**
- Org adds `"visibility":"selected"` + `"selected_repository_ids":[...]` ← **IDs, not names**.
- Encryption is **client-side, before it reaches GitHub** → plaintext never in GitHub logs; GitHub decrypts server-side at runtime.
- Sealed box = recipient-only (GitHub) anonymous PK encryption; function `crypto_box_seal`. (Concept, not a memorize-item.)

### ⚠️ API read-back contrast (trap)
- **GET a secret = NO value** — metadata only (name/timestamps). Values can **never** be read back via API.
- **GET a variable = returns the value** (plaintext CRUD: `POST`/`GET`/`PATCH`/`DELETE` on `/actions/variables`).

### Scopes (auth)
- repo/env secrets: collaborator access (classic `repo` scope).
- org secrets: `admin:org`.

### gh CLI
- `gh secret set NAME` (does GET-key → seal → PUT for you)
- `gh variable set NAME` (plaintext)

### ⚠️ Unverified / version-specific (calibrate vs practice exams)
- **256 KB** = cloud; **10 MB** = GHES.
- Variable **creation naming rules** (no spaces, no leading digit, no `GITHUB_` prefix, case-insensitive) — standard rules, not re-pulled verbatim.
- **Variables REST endpoints** stated from parallel structure (secrets API verified live; variables API page not re-pulled).
- **gh CLI** commands from knowledge, not re-pulled.


---

## Topic 4D — Self-Hosted Runners

*Registration, groups, labels, security. Runner **images/toolcache** → 4B; **networking** → 4A.*

### What it is
- A machine **you deploy & manage** to run Actions jobs. Full OS/image control, **any distro**, persistent tool-cache, pre/post-job hooks — but you own maintenance/security/drift.
- **Hosted Linux = Ubuntu ONLY.** Other distros ⇒ Docker, or a self-hosted custom VM.

### Registration & scope
- Attach at **repository / organization / enterprise**. Scope meaning:
  - **repo** = single repo
  - **org** = many repos in one org
  - **enterprise** = many orgs
- Validate connectivity with the runner app's `config.sh` / `run.sh --check`; connectivity logs live in the runner's `_diag` folder.

### ⚠️ Groups = access control; Labels = routing (don't merge them)
- **Runner GROUPS = access control** — *which repos/orgs may use these runners*.
  - Org/enterprise only.
  - Every org has a **default** group (unspecified at registration → default).
  - Access policy defaults to **private repos only** (overridable).
- **Labels = routing** — `runs-on` matches **cumulatively (must have ALL labels — AND)**.
  - Auto-applied labels: `self-hosted` + OS (`linux`/`windows`/`macOS`) + arch (`x64`/`ARM`/`ARM64`).
  - Set custom labels at registration via `--labels`. ⚠️ The config script **can't relabel an existing runner** — use UI/REST.

### ⚠️ Security
- **Never use self-hosted on PUBLIC repos** — a fork PR can run arbitrary code on your box.
- Not ephemeral by default → prefer **ephemeral / JIT** runners (one job, then auto-removed) to limit state/secret leakage.

### Routing
- No matching idle runner → the job **stays queued and fails after 24 h**.


---

## Topic 4E — Custom Actions Authoring

*Authoring the actions themselves. Reusable-workflow specifics → 1A.*

### action.yml metadata
- Custom-action metadata always lives in **`action.yml` / `action.yaml`** (required even for a private action).
- **Required keys:** `name` + `description` + `runs`.
- `description` is **required** in `action.yml` inputs (contrast: not required in `workflow_dispatch` inputs — see 1A).

### Composite vs reusable (the distinction)
- **Composite action:**
  - a **step** in a job
  - runs on the **caller's runner**
  - **no `secrets:` block** (secrets arrive as `with:` inputs / env)
- **Reusable workflow:**
  - **job-level** `uses:`
  - its **own runner**
  - **has a `secrets:` block** (details in 1A)

### Cleanup hooks
- **JavaScript action** → `runs.post`.
- **Docker container action** → `runs.post-entrypoint`.
- *(Distinct from self-hosted **runner** hooks `ACTIONS_RUNNER_HOOK_JOB_STARTED`/`_COMPLETED` in 4B.)*

### Checkout
- ⚠️ **No `actions/checkout` ⇒ empty workspace** (repo files absent). Most action/build steps need it first.


---

## Topic 4F — Editions, GHES & GitHub Connect

### Editions
- **GHEC** = GitHub Enterprise Cloud (hosted SaaS).
- **GHES** = GitHub Enterprise Server (self-hosted). No Marketplace by default.

### Getting github.com actions onto GHES
- **GitHub Connect** = **AUTO** access to github.com actions. Needs **outbound** to github.com from **both the instance AND the runners** (no inbound). No outbound ⇒ `actions-sync` only.
- **`actions-sync`** = **MANUAL** copy (air-gapped scenario).
- Neither is enabled by default.
- ⚠️ **Security:** the first use of a github.com action **retires that org/repo namespace locally** (blocks a MITM via a look-alike local repo); a Site admin unretires via Site admin.


---

## Topic 4G — Packages & GHCR Publishing

### Permissions & scopes
- ⚠️ **`GITHUB_TOKEN` default = read-only for packages → add `packages: write`** to push.
- Publishing a package needs **`write:packages`** + registry config + publish logic.
- PAT (classic) package scopes: `read:packages` / `write:packages` / `delete:packages` (+ `repo` for private).

### GHCR behavior
- **Public GHCR images pull anonymously** (other registries need auth even when public).
- **New packages default to private.**
- Repo↔package link: a **workflow push auto-links**; a **CLI push** needs `LABEL org.opencontainers.image.source=<repo-URL>` in the Dockerfile.

### Events
- `registry_package` event only **reacts to** a publish (types `published` / `updated`) — it does not perform the publish.


---

## Topic 5A — Untrusted Input & Token Hardening

*Domain 5 · objectives 5.3 + 5.4. Verified live 2026-06-23.*

### TRAPS FIRST
- ⚠️ **The half-fix.** Moving an untrusted value into an `env:` var is pointless if you then read it back as `${{ env.VAR }}`. That's still an expression → substituted into the script source at template time → still injectable. Read it the shell way: `$VAR` / `"$VAR"`.
- ⚠️ **Quoting ≠ a fix.** `"${{ github.event.* }}"` in a `run:` block is still vulnerable — substitution happens before the shell exists, so quotes are just text to break out of.
- ⚠️ **Double-quoting shell vars** is general hygiene (word-splitting), NOT the GitHub script-injection mitigation. Don't pick it as *the* fix.
- ⚠️ **`permissions:` — name one, lose the rest.** Naming any permission sets all unspecified ones to `none`; **`metadata` always stays read**. Unnamed perms do NOT keep their defaults.
  - **Scope → action map:**
    - label/comment a PR = `pull-requests: write` (issue labels = `issues: write`) — **NOT** `contents`
    - `contents: write` = git-repo writes (push commits, tags, releases) — the high-risk scope in a pwn-request context
    - `packages: write` to publish GHCR (see 4G)
    - `id-token: write` for OIDC
- ⚠️ **Self-hosted lifetime trap.** Job ceiling is 5 days, but `GITHUB_TOKEN` only refreshes up to **24h**. Don't pick "lasts 5 days."
- ⚠️ **Run vs trigger.** A push/PR via `GITHUB_TOKEN` does **not trigger** a new run — the commit still **lands**, the event is suppressed at the trigger stage (no run created/queued/skipped). It's not "rejected" and not "held."
- ⚠️ **System fields aren't untrusted.** `pull_request.number`, `run_id`, `sha` = system-generated, not attacker-controlled. Distractors.

### Bit 1 — Script injection (5.3)
- **Mechanism:** `run:` builds a temp shell script with `${{ }}` substituted in **before execution** → untrusted context becomes script *source*.
- **Fix hierarchy:**
  1. Intermediate `env:` var, read as `"$VAR"` (the preferred inline-script fix).
  2. Pass the value as an action `with:` argument (also safe).
- **Untrusted sources:** issue/PR `title`, `body`, **branch/ref names** (`head_ref`), **email addresses**, `label`, `message`, `name`. Branch-name PoC: `zzz";echo${IFS}"hello";#`.
- **Defense-in-depth:** least-privilege `permissions:`, input validation, vetted/SHA-pinned actions, CodeQL / Scorecards.

### Bit 1b — `pull_request` vs `pull_request_target` (security)
- `pull_request` = **merge-commit context**, **no fork secrets**, blocked by a merge conflict → **SAFE** for running PR code. Fork `pull_request` token is **read-only** (nothing to steal — that's why running fork code is safe).
- ⚠️ `pull_request_target` = **base-branch context**, **full secrets (incl. on fork PRs)**, not blocked by conflict, **auto-runs** (no first-timer approval), runs the **base-branch** workflow (checks out base by default) → **DANGEROUS** for untrusted PR code ("pwn request").
- ⚠️ **The vuln is not the checkout — it's *executing* the checked-out fork code** inside the privileged job that already holds secrets + a write token.
- **Safe pattern** when you must build untrusted code AND use secrets: unprivileged `pull_request` builds → uploads an **artifact** → privileged `workflow_run` consumes it (treat the artifact as **untrusted data**).
- Recency: `actions/checkout` v7 now **blocks** fork head/merge checkout in these privileged events (`allow-unsafe-pr-checkout` opt-out).

### Bit 2 — `GITHUB_TOKEN` vs PAT (5.4)
- **What it is:** a **GitHub App installation token**, minted **per job**, auto-injected, never stored. Read via `secrets.GITHUB_TOKEN` or `github.token`. NOT user-bound (that's why it's safer than a PAT).
- **Three traits:** ephemeral (dies at job end) · repo-scoped (can't reach other repos) · permission-tunable.
- **Lifetime cap:** 6h hosted · self-hosted refreshable only to 24h.
- ⚠️ **Recursion guard:** `GITHUB_TOKEN`-pushed commits/PRs don't trigger downstream runs. Need them to? Use a **PAT or GitHub App token** — the same swap that gives cross-repo reach also lifts the guard.
  - Exceptions:
    - `workflow_dispatch` & `repository_dispatch` **always** create runs even via `GITHUB_TOKEN`.
    - A `GITHUB_TOKEN`-created PR (opened/synchronize/reopened) **does** create runs, but in an **approval-required** state.
    - `workflow_run` fires off another workflow **completing** (a lifecycle event, not a token-emitted one), so it runs normally — the standard way to **chain** off a run the guard would otherwise suppress.
- **PATs:** fine-grained (recommended, repo-restrictable) > classic (every repo the user can access). Flaw = user-bound + long-lived.

### Bit 3 — GitHub Apps & the token-lifetime ladder
- A **GitHub App** authenticates to a repo/org as an *installation* via a short-lived **installation access token** (not tied to any user). `GITHUB_TOKEN` is the special case: the installation token for the App that Actions auto-installs (per-job, repo-scoped).
- For your **own** automation needing cross-repo reach or to trigger downstream workflows: register a GitHub App, install it, and mint a token in-workflow with **`actions/create-github-app-token`** — usable immediately in that run. Prefer it over a PAT (short-lived, not user-bound).
- **Token-lifetime ladder:**
  - private key signs a **JWT** ("as the App") — **10-min max**
  - exchange at `POST /app/installations/{id}/access_tokens` → **installation access token** — **1 h** (the workhorse)
  - optional **user access token** (OAuth, on behalf of a person) — **8 h** + refresh
- App **installation** rate limit **scales** with repos/org users (PAT/OAuth don't).
- **Escalation order:** `GITHUB_TOKEN` → **GitHub App installation token** (cross-repo / short-lived) → **fine-grained PAT** (last resort, set an expiry).


---

## Topic 5B — OIDC Keyless Cloud Auth

*Domain 5 · objective 5.5. Verified live 2026-06-23.*

### TRAPS FIRST
- ⚠️ **`id-token: write` ≠ resource write.** It only lets the job request/use the OIDC token. Missing it = #1 OIDC failure. (Names one permission → all others `none` except `metadata` read.)
- ⚠️ **Two tokens, don't merge them.** `ACTIONS_ID_TOKEN_REQUEST_TOKEN` (request token) authenticates the runner *to GitHub* to mint the JWT — **the cloud never sees it.** Only the **JWT** goes to the cloud. And the cloud returns a **third, separate** short-lived credential — the temp cloud creds are the easily-forgotten half of the round trip.
- ⚠️ **The JWT carries identity, not permissions.** Scope is 100% cloud-side. AuthN = GitHub; authZ = cloud.
- ⚠️ **Validation order = issuer → signature → claims.** Read `iss` → confirm trusted/registered issuer → fetch *that* issuer's public keys → verify signature → check `aud`/`sub`. Issuer check is NOT redundant with signature: it *selects* the key set ("is it a signer I trust?") vs signature ("is it real?").
- ⚠️ **`sub` precedence: environment > pull_request > branch/tag.** A job referencing an environment gets `:environment:NAME` even on a PR trigger. No composite form. A condition for `:ref:refs/heads/main` breaks the moment a job declares an environment.
- ⚠️ **PR job referencing `production` → `sub` matches `:environment:production`.** The cloud condition does NOT stop it — **environment protection rules** (GitHub-side, before token issue) do. Scope-to-environment + protection-rules are a **pair**.
- ⚠️ **`StringEquals` + `*` fails CLOSED.** `*` is literal under `StringEquals` → matches nothing → too-restrictive bug, not exposure. Danger appears under `StringLike` (wildcard expands). Distinguish too-restrictive (broken) from too-permissive (hole).
- ⚠️ **Immutable subject claims ≠ immutable releases (3A).** Same word, unrelated feature.

### Bit 1 — Concept & flow
- **Why:** swap a **long-lived stored cloud secret** for a **short-lived token fetched at runtime**. Nothing durable in GitHub.
- **Flow:** job (with `id-token: write`) → request token mints a **signed JWT** from `https://token.actions.githubusercontent.com` → JWT sent to cloud → cloud validates against its trust policy → returns **short-lived, job-scoped** cloud creds.
- **Acceptance = asymmetric crypto.** GitHub signs with a private key (RS256); cloud verifies with GitHub's **public** keys (JWKS via `.well-known/openid-configuration`). No shared secret. Trust anchored by one-time provider registration (issuer URL).
- **Scope:** trust policy = *who may assume the role*; role permission policy = *what it can do*. GitHub's only levers = `id-token: write` + the identity claims.
- **Mechanics:** the cloud's official login action (`aws-actions/configure-aws-credentials`, `azure/login`, `google-github-actions/auth`), or a manual fetch via `ACTIONS_ID_TOKEN_REQUEST_URL` + `ACTIONS_ID_TOKEN_REQUEST_TOKEN` (`getIDToken()` helper).

### Bit 2 — Trust config & claims
- **`sub` format:** `repo:<owner>/<repo>:<ref-type>:<ref>`. Forms: `ref:refs/heads/<branch>`, `ref:refs/tags/<tag>`, `environment:<name>`, `pull_request`.
- ⚠️ **`pull_request` sub is stable, no PR number** → conditioning on it trusts ALL PRs incl. forks. Never for production.
- **`aud`:** defaults to the owner URL; cloud actions set it (AWS `sts.amazonaws.com`). Condition on `aud` AND `sub`.
- **Cloud mapping (same concept):**
  - **AWS** condition keys: `token.actions.githubusercontent.com:aud` / `:sub`
  - **Azure** = federated credential
  - **GCP** = workload identity pool
- ⚠️ **Four misconfigs:**
  1. `aud`-only = all of GitHub.
  2. `repo:org/*` (wildcard-eval) = whole org incl. forks/dependabot/new repos.
  3. wildcard under `StringEquals` = matches nothing → use `StringLike`.
  4. production on `pull_request` = any PR author incl. forks.
- **Best pattern:** scope to `:environment:NAME` (stable across triggers) **+ environment protection rules** (the actual gate).
- **Granularity:**
  - customize the `sub` template via REST (`include_claim_keys`)
  - condition on `repository_id`, `repository_visibility`, `repo_property_*`
  - `job_workflow_ref` for reusable workflows
- ⚠️ **Immutable subject claims:** repos created after **2026-07-15** default to a `sub` with owner_id + repo_id → `repo:org@123456/repo@456789:...` (anti namespace-recycling). Old repos opt in (settings UI / REST). **Not** on GHES. The trust policy must match the repo's actual format.


---

## Topic 5C — Action Enforcement Policies & Build Provenance

> 5C = **enforcement** (Bit 1) + **provenance proof** (Bit 2). NOT a re-teach of 3A concepts.

### ⚠️ THE BIG ONE — "artifact" is two unrelated features (the exam won't name the domain)

| Verbs in the question | It's… | Domain |
|---|---|---|
| `upload-artifact`/`download-artifact`, "between jobs," "retention," "90 days" | **workflow artifact** | 1 (Topic 1E) |
| `attest`, "provenance," "Sigstore," "`gh attestation verify`," "SLSA," "verify before deploy" | **build output under an attestation** | 5 (5.8) |

Same word, unrelated mechanics. Read the verbs, not the noun.

### Bit 1 — enforcement keepers
- **Override direction:** enterprise → org → repo. A lower level can only **tighten**, never loosen.
- **Section labels differ by scope** (concept identical; recognize, don't memorize):
  - repo = "Actions permissions"
  - org & enterprise = "Policies"
- **Local-only policy blocks GitHub's own actions** → `actions/checkout` becomes inaccessible. Re-enable via "Allow actions created by GitHub."
- **Local actions (`uses: ./path`) are NEVER restricted by the allow/deny list.** Remote refs only.
- **`!` in the allow list** = subtract an exception:
  - both entries coexist; **block wins on overlap**
  - `*, !evil-org/*` = allow all except that owner
  - list capped at **1000 entries**
- **Verified-creator badge = publisher IDENTITY only**, not code review/audit. Verified accounts can be compromised. Still review source + pin SHA.
- ⚠️ **SHA-pinning enforcement applies to ACTIONS only — reusable workflows are EXEMPT (still tag-referenceable).** "Forces reusable workflows onto SHAs too" → FALSE.
- ⚠️ **SHA pin freezes source, not behavior** — a pinned action can still pull an unpinned Docker image / nested composite / `curl`ed script. Reproducible *source*, not *behavior*.
- ⚠️ **"Required reviewers for unverified actions" is NOT a real feature.** It's a loose umbrella over: (a) the fork-PR contributor-approval gate (keys off *who triggers*) + (b) environment "Required reviewers" protection rules (gate a *job* hitting a protected env). No setting inspects action-verified-status and demands a reviewer.
- **Fork-PR approval:**
  - a maintainer (write access) approves before the run
  - **both the PR author AND the triggering actor are checked**
  - a run awaiting approval **>30 days → auto-deleted**
- **Environment required reviewers** (verified vs docs):
  - up to **6** users/teams
  - **at least read** access suffices (NOT write)
  - **one** approval is enough
  - self-review can be prevented
  - teams allowed
- ⚠️ **Environment protection + environment secrets only activate when a job sets `environment:`** — selecting an environment via a `workflow_dispatch` `environment` **input** is just a picker; it does NOT apply protection rules or expose environment secrets.
- **Immutable actions:** **consuming = live/transparent** (OCI packages from GitHub Packages, host `pkg.actions.githubusercontent.com` under `*.actions.githubusercontent.com` → 4A allow-list). **Publishing your own = ⚠️ not confidently GA** (README "not for public use" vs roadmap "GA"). Verify on a practice exam.

### Bit 2 — attestation keepers
- **Attestation = a signed claim binding SUBJECT (name + SHA-256 digest) → PREDICATE (provenance facts) in in-toto format.** Digest = hash of the actual bytes.
- **3 permissions to generate:** `id-token: write` (OIDC signing identity — the 5B tie-in, NOT for deploy), `contents: read`, `attestations: write`. (+ `packages: write` for container images.)
- **Action naming:** `actions/attest-build-provenance` (historic) is, as of v4, a **wrapper around `actions/attest`**. New code → `actions/attest@v4`. **Recognize BOTH names.** `@v1` in old material = drift, not wrong.
- **Keyless signing via Sigstore:** public repo → **Public Good** instance (has a transparency log); private/internal → GitHub **private** Sigstore (no transparency log, federates only with Actions).
- **Generating alone = no security benefit. Value only on verification** (`gh attestation verify`, needs `--owner` OR `--repo`).
  - Container image → `oci://ghcr.io/...` prefix, not a file path.
  - SBOM → must pass `--predicate-type` (else it verifies provenance, not the SBOM).
  - `--signer-workflow` / `--signer-repo` → require a *specific* signing workflow/repo.
  - Verify **prints every policy it evaluated** (pass/fail transparency; Feb-2025 change).
- ⚠️ **CHECK ORDER (Q2 keeper):** verify runs **bytes → signature → identity**.
  - A **plain file-swap fails at step 1 (digest/bytes lookup)** — the swapped bytes hash to a different digest, so **no attestation exists for them**, before any signature is examined.
  - The **signature check** defeats a **forged/invalid attestation that has a matching digest**.
  - The **identity check** rejects a validly-signed output from a *different* owner/repo than you demanded.
  - The exam can split these: "what catches a swapped artifact?" (bytes) vs "what catches a forged attestation?" (signature).
- ⚠️ **MONOTONIC — state it precisely:** verify passes when **≥1 attestation satisfies the SPECIFIC CLAIMS YOU ASKED TO VERIFY** (`--owner`/`--repo` + `--signer-workflow`/`--predicate-type` if given) — NOT the generic "an attestation passes." Junk/non-matching attestations are **inert** (can't substitute, can't veto). Monotonic = once it passes, later additions can't flip it to fail (anti-DOS).
  - **Looseness lives in YOUR query:** `--owner acme` only proves "*someone* in acme signed it," not "`release.yml` did." Tighten with `--repo`/`--signer-workflow`. **Owner ≠ workflow.**
  - Verifying provenance ≠ verifying SBOM (different predicate).
- **SLSA** = "Supply-chain Levels for Software Artifacts" ("salsa"), an industry framework, not a GitHub feature. GitHub provenance is in SLSA build-provenance format. **Attestations + reusable workflows → SLSA v1.0 Build Level 3.** (⚠️ the baseline level of a plain attestation + the exact per-level wording = unverified; the objective lists SLSA as an *example* only.)
- **Deploy gate:** run `gh attestation verify` before consuming a build output; proceed only on pass. A K8s **admission controller** can enforce at the cluster (know it exists).
- **Availability (verified 2026-07-01):**
  - public repos = **all current plans**
  - **private/internal = GHEC only**
  - **NOT on GHES**
  - not on legacy Bronze/Silver/Gold plans


---

## Topic 5D — Optimization & Retention

> 5D = cost/limits/optimization (5.10) + retention/storage (5.9).

### Cost model (Bit 1)
- **Billed = round-up(minutes) × OS-multiplier.** Round each job **UP to the whole minute** (1s and 59s both = 1 min).
- **OS multiplier: Linux 1× · Windows 2× · macOS 10×.** A macOS 10-min job = 100 min. Move to Linux = the biggest lever.
- **Public repos + self-hosted runners = FREE** (no billable minutes). 10× only bites on **private** (or larger runners, never free even on public).
- **Larger runners:**
  - higher rate by vCPU
  - **free while idle**
  - static IP no extra cost
  - included free minutes can't be used on them
- ⚠️ **Job limit = 6 hours** (killed if exceeded). The **default `timeout-minutes` = 360** (i.e. that same 6 h ceiling) — set it lower so a hung job doesn't run to the cap. Concurrency capped per plan (Free→Enterprise). Matrix cap commonly cited **256**. `schedule:` ≥ 5-min spacing, can be delayed/dropped.

### Optimization levers (Bit 1)
- ⚠️ **Parallelization cuts TIME, not billed minutes — and can INCREASE them.** Minutes are summed across jobs; a split adds per-job setup + per-job round-up. Exam answer: "splitting into a parallel matrix reduces wall-clock, NOT billed minutes, and may raise them."
- **Real minute-savers:**
  - path/branch filters + `if:` — run less.
  - `concurrency` + **`cancel-in-progress: true`** — cheapest win; kills runs superseded by a new push.
  - **`timeout-minutes`** — else a hung job runs to the 6h ceiling.
  - right-sizing — bigger ≠ cheaper (4× rate for 1.67× speed = net loss).
  - **`needs:` fast-fail gate** — a cheap lint job gates the expensive job → failure stops the run before costly work = where the dependency graph actually saves minutes.
- **cache vs artifact (1E):** cache = deps/build-accel, **7-day default**, 10 GB LRU; artifact = results, **90-day default**. Don't swap their roles.
- ⚠️ **Usage metrics show RAW minutes (NO multiplier applied)** → the dashboard number ≠ the bill. Metrics = "where minutes go"; the billing page / spending limits = actual cost.

### Retention & storage (Bit 2)
- **Defaults:**
  - artifact/log = **90 days**
  - cache = **7 days**
  - *Understand why:* cache = disposable/churns fast + size-capped LRU; artifact = retrievable results. Don't memorize in isolation.
- **Range:** artifacts **1–400 days** (private/internal/Enterprise); **public capped at 90**. Cache: public ≤ 90, private/internal ≤ 365.
- ⚠️ **A period change is NOT retroactive** — it applies to NEW objects only; old artifacts keep their original lifespan (by design, not a bug). To reclaim now → delete explicitly.
- Per-artifact override: `retention-days:` in `upload-artifact` (capped by repo/org max); `compression-level: 0–9`.
- ⚠️ **Programmatic retention — precise meaning:** = per-artifact `retention-days` (declarative) + programmatic **deletion** via REST/`gh`. There is **NO confirmed REST endpoint to SET the retention period** (`PUT .../actions/retention` unverified/likely not official). REST does **get / list / delete** only. (Full endpoint list → 1E.)
- ⚠️ **Quota recalculation lags** (commonly 6–24h). A "storage quota exceeded" error persists *after* a successful delete — the deletion didn't fail; just wait + lower retention going forward.
