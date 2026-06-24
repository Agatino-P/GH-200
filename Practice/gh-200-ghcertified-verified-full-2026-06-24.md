# GH-200 — GHCertified Bank, Verified — FULL (Q001–Q179)

**Last updated: 2026-06-24 16:20 UTC**
**Source bank:** `gh-200-ghcertified-bank-full-2026-06-24.md` (FidelusAleksander/ghcertified, captured 2026-06-24 10:41 UTC)
**Coverage:** all **178** questions (Q001–Q179; the source bank skips Q157). Consolidated from the 7 per-block verified files.

> **Quizzing reminder (protocol §4.10):** this bank's correct option(s) sit first (~67% bare `A`, ~89% A-inclusive). The `Marked` column below keeps the **original** letters so it stays diffable against the raw bank — **shuffle option order before quizzing** so position carries no signal.

---

## What "verified" means here (read once)

Per practice protocol §4.6, the raw bank's answers are **contributor-marked keys**, not checked against `docs.github.com`. Each verdict below uses a **two-tier method**, and is honest about which tier it rests on:

- **Settled** — verdict rests on stable, well-established GitHub Actions behaviour. No live doc fetch (and none needed). High-confidence, not infallible.
- **🔎 Live-checked** — version-sensitive or genuinely uncertain; verified against current `docs.github.com` (or official changelog) during the 2026-06-24 pass, with the finding noted.
- **⚠ unchecked-currency** — could plausibly have moved since the Jan-2026 cutoff and was **not** separately fetched; trust but re-check if it matters.

This is **not** a live fetch per question — it's settled knowledge + spot-checks on the items that warranted them.

### Legend
| Symbol | Meaning |
|---|---|
| ✓ | Marked answer is correct |
| ✗ | Marked answer is wrong (real answer in note) |
| ⚑ | Correct but flagged — loose wording, trap, or caveat |
| 🔎 | Live-checked this pass |
| ⚠ | Unchecked currency — verify if it matters |

---

## Overall result

| Metric | Count |
|---|---|
| Questions verified | **178** (Q001–Q179, Q157 absent) |
| Marked answer **correct** (✓) | **178** |
| Marked answer **wrong** (✗) | **0** |
| Correct-but-flagged (⚑) | 12 |
| Live-checked this pass (🔎) | 5 |
| Off-syllabus / bucket (d) | 0 |

**Bottom line:** every contributor-marked answer holds up. Zero wrong keys across the whole bank — unusually clean for an unofficial source. The 12 ⚑ flags are loose wording or traps worth knowing, not errors. **This bank is trustworthy and current for GH-200; safe to drill once shuffled.**

### Per-block breakdown
| Block | Range | Qs | ✓ | ✗ | ⚑ | 🔎 |
|---|---|---|---|---|---|---|
| 1 | Q001–Q025 | 25 | 25 | 0 | 2 (Q014, Q018) | 1 (Q021) |
| 2 | Q026–Q050 | 25 | 25 | 0 | 3 (Q043, Q044, Q048) | 1 (Q044) |
| 3 | Q051–Q075 | 25 | 25 | 0 | 2 (Q061, Q066) | 2 (Q069, Q070) |
| 4 | Q076–Q100 | 25 | 25 | 0 | 1 (Q082) | 1 (Q076) |
| 5 | Q101–Q125 | 25 | 25 | 0 | 1 (Q116) | 0 |
| 6 | Q126–Q150 | 25 | 25 | 0 | 1 (Q134) | 0 |
| 7 | Q151–Q179 | 28 | 28 | 0 | 2 (Q174, Q178) | 0 |

### Items live-checked & locked (no re-verify needed)
- **Q021** — `workflow_dispatch` input types = string, choice, boolean, **number**, environment (5). (`workflow_call` = boolean/number/string only.)
- **Q044** — cross-run artifact download needs `actions/download-artifact` + `github-token` (`actions: read`) + `run-id`; "elevate permissions" is the docs' own phrasing.
- **Q069 / Q070** — download run logs = `GET …/runs/{run_id}/logs`; create/update repo secret = `PUT …/actions/secrets/{name}`.
- **Q076** — max **50** unique reusable workflows per file (was 20); nesting depth now **10** levels (was 4).

---

## Verdicts (all 178)

| Q | Marked | Verdict | Tier | Note |
|---|---|---|---|---|
| Q001 | A | ✓ | Settled | Reusable-wf token permissions can only be **downgraded** by the called workflow, never elevated. |
| Q002 | A | ✓ | Settled | `GITHUB_TOKEN` permission values: `none`, `read`, `write`. |
| Q003 | A, B | ✓ | Settled | `permissions` is settable at **workflow** and **job** level — not step level. |
| Q004 | A | ✓ | Settled | Standard GitHub-hosted runners are free for public repos. (Larger runners are billed even on public repos.) |
| Q005 | A | ✓ | Settled | No "clone repo" event exists. Commit/branch-create/PR-label are all real triggers. |
| Q006 | A, B, C | ✓ | Settled | Workflows run 1+ jobs, support manual/event/schedule triggers, and must live in `.github/workflows`. Marketplace shares **actions**, not workflows. |
| Q007 | A, B | ✓ | Settled | Required components: trigger event(s) + one or more jobs. Name and branch list are optional. |
| Q008 | A | ✓ | Settled | `repository_dispatch` = triggered by external webhook / REST API. The other four options are invented. |
| Q009 | A | ✓ | Settled | Workflows are YAML only. (No source link in bank; answer is trivially correct.) |
| Q010 | A | ✓ | Settled | Sensitive data → **secrets** (encrypted). Variables are plaintext. |
| Q011 | A | ✓ | Settled | Multiple jobs run in **parallel** by default (absent `needs`). |
| Q012 | A | ✓ | Settled | `needs` goes in the **dependent** job (job B). `requires` is not a keyword. |
| Q013 | A | ✓ | Settled | When a prerequisite job fails, dependent jobs are **skipped** by default (not marked failed, not a global cancel). |
| Q014 | A | ✓ ⚑ | Settled | "Yes" is correct: you apply a matrix to a job that **calls a reusable workflow** (`strategy.matrix` + `jobs.<id>.uses`). ⚑ Wording "parallelize entire workflows" is loose — the real mechanism is matrix-over-reusable-workflow, not a "workflow matrix" keyword. |
| Q015 | A | ✓ | Settled | Correct nesting is `jobs.<id>.strategy.matrix`. B swaps `strategy`/`matrix`; C and D omit `strategy`. |
| Q016 | B | ✓ | Settled | Matrix values are read via the `matrix` context: `${{ matrix.<key> }}`. |
| Q017 | A | ✓ | Settled | `branches` filter. For `pull_request`, it matches the **base/target** branch. |
| Q018 | A | ✓ ⚑ | Settled | `pull_request` `branches` filter targets the **base (target)** branch → starts with `release/` but not ending `-alpha`. ⚑ Classic trap: target vs source branch. For `pull_request` it is the target. |
| Q019 | A | ✓ | Settled | Push branch/tag filters use **glob** patterns (`*`, `**`, `?`, `!`, etc.), not regex. |
| Q020 | A | ✓ | Settled | `workflow_dispatch` enables the manual "Run workflow" button. |
| Q021 | A, B, C, D, E | ✓ | **🔎 Live-checked** | All five are valid `workflow_dispatch` input types: `string`, `choice`, `boolean`, `number`, `environment` (current `docs.github.com`, workflow-syntax page). ⚠ Note for contrast: `workflow_call` accepts only `boolean`, `number`, `string` (no `choice`/`environment`). *(I initially expected `number` to be invalid here — it was added after an older docs correction; the live check overruled my prior.)* |
| Q022 | A | ✓ | Settled | True — a `workflow_dispatch`-only workflow can be triggered via the "Create a workflow dispatch event" REST endpoint (and `gh workflow run`). Bank's doc anchor is slightly off; answer is correct. |
| Q023 | A | ✓ | Settled | Use the **Disable workflow** option in the Actions UI to pause without code changes. |
| Q024 | A | ✓ | Settled | `activity types` + the `types:` filter limit runs to specific activity types of an event. |
| Q025 | A | ✓ | Settled | A reusable workflow is enabled with the `workflow_call` trigger. `workflow_trigger` doesn't exist; `workflow_dispatch` = manual; `workflow_run` = chain off another workflow. |
| Q026 | A, B, C | ✓ | Settled | Passing an output out of a reusable workflow needs all three layers: step writes to `$GITHUB_OUTPUT` (C), job maps step→job output (B), workflow maps job→workflow output (A). Outputs are **not** auto-passed (D wrong). |
| Q027 | A, B | ✓ | Settled | `defaults.run` is valid at **workflow** and **job** level only (not step). There is no `defaults.env` (D/E invented). |
| Q028 | A | ✓ | Settled | `concurrency: ${{ github.workflow }}` at workflow level ensures at most one run at a time. `queue`/`order`/`parallel` are not keys. |
| Q029 | A | ✓ | Settled | `concurrency` group + `cancel-in-progress: true` cancels older in-progress runs in the same group. `cancel-in-progress` is only valid inside `concurrency`. |
| Q030 | A | ✓ | Settled | `if: ${{ always() }}` + `needs: [job1, job2]` → job3 runs once both upstream jobs finish, regardless of success/failure. `always()` and `needs` are fully compatible. |
| Q031 | A, B | ✓ | Settled | `github.repository` holds `owner/repo`. Both `if: github.repository == '…'` and the `${{ }}`-wrapped form work (`${{ }}` is optional in `if`). `github.organization`/`github.org` are not context fields (C/D wrong). |
| Q032 | A, B, C | ✓ | Settled | GitHub-hosted runners: Windows, Ubuntu Linux, macOS. No Android. |
| Q033 | A | ✓ | Settled | True. A step may run an action (`uses:`) **or** a shell command (`run:`); every action runs inside a step. |
| Q034 | A | ✓ | Settled | Pinning to a full-length **commit SHA** is the most stable+secure reference (immutable; a tag can be moved, a branch is mutable). |
| Q035 | A | ✓ | Settled | `continue-on-error: true` on the step prevents the job from failing when that step fails. `ignore-error` doesn't exist; `failure()`/`always()` are run-conditions, not failure-suppressors. |
| Q036 | A | ✓ | Settled | `strategy.max-parallel: 2` caps concurrent matrix jobs. `strategy.concurrency` is not a key. |
| Q037 | A | ✓ | Settled | `echo "PET=DOG" >> "$GITHUB_OUTPUT"` (name=value). `gh set-output` / `::set-output` are not valid (the latter is deprecated). |
| Q038 | A | ✓ | Settled | A value written to `$GITHUB_ENV` becomes an **env var**, read in later steps as `$action_state`. The `steps.<id>.outputs.*` form (B) would apply only if written to `$GITHUB_OUTPUT`. |
| Q039 | A | ✓ | Settled | Statement is **False** → reusable workflows **can** be nested (called from another reusable workflow), up to 4 levels, with limitations. |
| Q040 | A | ✓ | Settled | `secrets: inherit` passes one level only. A→B inherits; B→C does **not** (B would need its own `secrets: inherit`). So secrets reach B but not C. |
| Q041 | A | ✓ | Settled | Caching = reuse files that **don't change often** (e.g. package deps). Persisting build outputs for later viewing/use = artifacts (C/D). |
| Q042 | A, B | ✓ | Settled | Artifacts = (A) save files to view after a run (test results/logs) **and** (B) pass binaries from a build job to a later deploy job. Reusing rarely-changing deps = caching (C); release notes = releases (D). |
| Q043 | A | ✓ ⚑ | Settled | "Yes" is correct — a branch can restore caches from the **default** branch. ⚑ Precision: cache read scope = current branch + a PR's base branch + the default branch; it is **not** "any branch can read any branch's caches" (B is too broad and wrong). |
| Q044 | B | ✓ | **🔎 Live-checked** | Cross-run/cross-repo download needs `actions/download-artifact` **with a `github-token` (`actions: read`) + `run-id`/`repository`** — by default it's scoped to the current run. The "elevated permissions" wording matches the official README verbatim. |
| Q045 | A | ✓ | Settled | Coverage reports / screenshots → **Artifacts** (outputs to view after the run). |
| Q046 | A | ✓ | Settled | "Single file only" is **False** — `upload-artifact` takes multiple files, directories, and glob patterns. |
| Q047 | A | ✓ | Settled | Upload binaries as artifacts in `build`, download in `deploy`. (Caches are for deps, not for handing build outputs to a deploy job.) |
| Q048 | A | ✓ ⚑ | Settled | Use `needs` in `job2`. ⚑ Trap: `actions/download-artifact` does **not** create a job dependency (B wrong); ordering in the YAML file doesn't either (C wrong). Only `needs` enforces job1→job2. |
| Q049 | A, B, C | ✓ | Settled | Starter workflows: ready-to-use templates (A), GitHub-provided/maintained by category/language/tooling (B), org-customizable (C). They **can** be edited and call reusable workflows; not paid. (Note: GitHub also calls these "workflow templates" — same concept.) |
| Q050 | A, B, C | ✓ | Settled | Secrets **and** config variables can be scoped to: org (all or selected repos), a single repo, and an environment in a repo. Environments aren't shared across repos (D); workflow/job-level scoping applies to *env vars*, not config variables (F/G). |
| Q051 | A | ✓ | Settled | Three action types: **Docker container**, **JavaScript**, **Composite**. "Custom action" is the umbrella term, not a type; Java/Python aren't types. |
| Q052 | A | ✓ | Settled | True — Docker container actions are generally slower (image build/pull latency) than JavaScript actions, which run directly on the runner. (No source link; well-established.) |
| Q053 | A | ✓ | Settled | False — action source does **not** go in `.github/workflows` (that's for workflows). An action lives in its own repo/path with the metadata file at its root. |
| Q054 | A | ✓ | Settled | Metadata goes in **`action.yml`** (or `action.yaml`) at the action's root. The metadata file is **always required**, even for private/unshared actions (D's caveat is wrong). |
| Q055 | A | ✓ | Settled | Re-running a workflow uses the **original** commit SHA + ref → runs commit A's code, not the later fix (commit B). Classic trap: re-run ≠ re-trigger on latest. |
| Q056 | A | ✓ | Settled | **Deployment protection rules** (required reviewers on the environment) gate runs targeting `production`. Branch protection (C) doesn't gate environment deploys. |
| Q057 | A | ✓ | Settled | Each **job** can reference a **single** environment. |
| Q058 | A | ✓ | Settled | **OIDC** is the recommended/safest cloud auth (short-lived tokens, no long-lived stored keys). Maps to studied 5B. |
| Q059 | A | ✓ | Settled | Require approval for fork-triggered runs via the repo/org **fork-run approval setting** (Settings → Actions). Deployment/branch protection don't do this; `fork_pull_request` event is invented (D). |
| Q060 | D | ✓ | Settled | `GITHUB_ACTOR` = the user/app that initiated the run. `GITHUB_USER` doesn't exist. |
| Q061 | A, B, C | ✓ ⚑ | Settled | Default env vars: `GITHUB_REPOSITORY`, `GITHUB_WORKFLOW`, `GITHUB_ACTOR`. ⚑ Trap: `GITHUB_TOKEN` (F) is a **secret**, not a default *environment variable* — you must map it to `env:` yourself; it's correctly excluded. `GITHUB_USER`/`GITHUB_ORGANIZATION` don't exist. |
| Q062 | A | ✓ | Settled | Same-name secret at a **lower** scope wins → a repo-scoped `SomeSecret` overrides the org one (unexpected value). Precedence: environment > repository > organization. (An enterprise-scope dup wouldn't change it, since org is lower.) |
| Q063 | A | ✓ | Settled | `echo "::debug::<message>"` is the correct workflow command for a debug message. |
| Q064 | A | ✓ | Settled | **GitHub Connect** enables GHES to auto-access GitHub.com-hosted actions. `actions-sync` is the manual alternative (C); GHES has **no** access by default (B/D wrong). Domain-5 enterprise. |
| Q065 | A | ✓ | Settled | Self-hosted runner network/connectivity logs live in the **`_diag`** folder on the runner machine. |
| Q066 | A | ✓ ⚑ | Settled | Validate connectivity with a **GitHub-provided script on the runner** — i.e. the runner application's `run.sh`/`config.sh` `--check` connectivity option. ⚑ Wording is generic; the concrete mechanism is the runner's `--check` flag. There's no `network-connectivity.yml` (C) and GitHub doesn't auto-validate on install (D). |
| Q067 | A | ✓ | Settled | `if: ${{ vars.MY_VAR == 'MY_VALUE' }}` — the whole comparison goes **inside** `${{ }}`. B puts `== '…'` outside, leaving a truthy non-empty string. Config vars (unlike secrets) **can** be used in `if`. |
| Q068 | A | ✓ | Settled | Secrets can't be referenced directly in `if:`. Map the secret to a job-level `env:` var, then test `env.my_secret != ''` at step level. |
| Q069 | A | ✓ | **🔎 Live-checked** | Download workflow run logs = **`GET /repos/{owner}/{repo}/actions/runs/{run_id}/logs`** (returns a redirect to the log archive). |
| Q070 | A | ✓ | **🔎 Live-checked** | Create/update a repository secret = **`PUT /repos/{owner}/{repo}/actions/secrets/{secret_name}`**. Docs' own curl uses `-X PUT`; `POST` is not valid for this endpoint. |
| Q071 | A, B | ✓ | Settled | Override an org secret by creating a same-name secret at a **lower** scope: a **repository** secret (A) or **environment** secret (B). Renamed variants (`OVERRIDE_…`, `REPOSITORY_…`) don't override; an enterprise secret (C) is higher scope, so it wouldn't win. |
| Q072 | A, B, C, D | ✓ | Settled | Org-reusable: **Secrets, Configuration Variables, Self-Hosted Runners, Workflow Templates**. Artifacts/Cache are run/repo-scoped; environment variables aren't org-shareable. (No source link; consistent with org-sharing docs.) |
| Q073 | A | ✓ | Settled | **5 jobs.** Base matrix `pet[cat,dog] × color[pink,brown]` = 4. The `include` entry `{color: white, pet: dog}` has an overlapping key (`color`) whose value (`white`) matches no existing combination, so it can't extend one → it's added as a **new** combination. 4 + 1 = 5. (Matrix-`include` counting trap.) |
| Q074 | A | ✓ | Settled | `GITHUB_REPOSITORY` holds the full `owner/repo` name. `GITHUB_REPOSITORY_OWNER` is just the owner. |
| Q075 | A | ✓ | Settled | No — on GitHub-hosted runners, **each job gets a fresh runner instance**; same-machine is never guaranteed (hence artifacts/cache to pass data between jobs). |
| Q076 | E | ✓ | **🔎 Live-checked** | **50** unique reusable workflows max from a single workflow file (includes nested trees). The older cap was 20 — raised to 50. Current docs confirm. |
| Q077 | A | ✓ | Settled | Self-hosted runner = a system you deploy/manage to run Actions jobs. |
| Q078 | C | ✓ | Settled | Workflow → one or more **jobs** → one or more **steps**; each step is an action or a script. (Note: answer is C, not A.) |
| Q079 | C | ✓ | Settled | Scheduled workflows run on the **latest commit of the repository's default branch** — not "main" by name, not a fixed commit. |
| Q080 | A | ✓ | Settled | `defaults.run.working-directory` sets the directory for all `run` steps. |
| Q081 | B, D | ✓ | Settled | Reuse across repos via **workflow templates** (B) and a **reusable workflow in a central repo** (D). Copying files (A) isn't reuse; a reusable action (C) isn't a workflow. |
| Q082 | A | ✓ ⚑ | Settled | `branches` filter is the right answer among the options. ⚑ Precision: branch *filtering* is set at the workflow trigger (`on.<event>.branches`), workflow-level — to gate a single **job** by branch you'd use `if: github.ref == …`. The other options (runs-on/jobs filter, `branch` keyword) are invalid, so A still wins. |
| Q083 | A | ✓ | Settled | `needs` specifies a job's dependencies (prerequisite jobs). |
| Q084 | A | ✓ | Settled | `env` defines environment variables. |
| Q085 | B | ✓ | Settled | `with` supplies input parameters to an action. (Answer B.) |
| Q086 | C | ✓ | Settled | Multiple commands in one step → multiline string with `|`. (Answer C.) |
| Q087 | B | ✓ | Settled | Cache deps with the **`actions/cache`** action. There's no `cache` keyword. (Answer B.) |
| Q088 | A | ✓ | Settled | `matrix` defines multiple job configurations run in parallel. |
| Q089 | A | ✓ | Settled | `concurrency` limits concurrent runs/jobs in a group. (`limit`/`max-jobs`/`parallelism` aren't keys.) |
| Q090 | D | ✓ | Settled | Default job timeout = **360 minutes (6 hours)**. (Corroborated against limits docs this pass.) |
| Q091 | B | ✓ | Settled | `runs-on` selects the runner/OS. (Answer B.) |
| Q092 | A | ✓ | Settled | `actions/setup-node@v4` with `node-version: 20`. The action name is `setup-node` (not `node-setup`) and the input is `node-version`. |
| Q093 | A | ✓ | Settled | `${{ secrets.SECRET_NAME }}` (plural `secrets`). |
| Q094 | C | ✓ | Settled | Default shell on Windows runners = **PowerShell** (since 2019). (Answer C.) |
| Q095 | A, B, C | ✓ | Settled | Self-hosted runners can be added at **repository, organization, enterprise** level — not workflow or step level. |
| Q096 | A | ✓ | Settled | `RUNNER_OS` holds the runner's OS. (`GITHUB_RUNNER_OS` isn't a thing.) |
| Q097 | C | ✓ | Settled | On a cache miss, `actions/cache` automatically saves a new cache (post-step) if the job succeeds. (Answer C.) |
| Q098 | D | ✓ | Settled | Weekday-only schedule → `on: schedule: - cron:` with a day-of-week field. There's no `schedule: weekdays`. (Answer D.) |
| Q099 | C | ✓ | Settled | Secrets > 48 KB: encrypt a file, commit it to the repo, store the **decryption passphrase** as a secret. (Confirmed via secrets docs in Block 3 pass.) |
| Q100 | A | ✓ | Settled | Status-check functions: `success()`, `always()`, `cancelled()`, `failure()`. |
| Q101 | A | ✓ | Settled | Run a step only after a specific step fails: `if: failure() && steps.<id>.outcome == 'failure'`. The `failure()` status function overrides the implicit `success()`. |
| Q102 | A | ✓ | Settled | `github.event` holds the triggering event's webhook payload. |
| Q103 | A | ✓ | Settled | `branches` + `paths` filters are **AND**'d — the workflow runs only when **both** are satisfied. |
| Q104 | A | ✓ | Settled | Treat environment variable names as **case-sensitive** regardless of OS/shell. |
| Q105 | A | ✓ | Settled | A job referencing an environment **won't start until all** the environment's protection rules pass. |
| Q106 | A | ✓ | Settled | `restore-keys` = ordered fallback keys to try on a cache miss (partial-match restore). |
| Q107 | A | ✓ | Settled | `ACTIONS_STEP_DEBUG=true` enables **step** debug logging. (`ACTIONS_RUNNER_DEBUG` is the runner one — see Q139.) |
| Q108 | A | ✓ | Settled | Valid `check_run` config: `types: [rerequested, completed]`. (`started`/`closed`/`filter` aren't valid here; note `types`, not `type`.) |
| Q109 | A | ✓ | Settled | `timeout-minutes` on a step limits that **step's** runtime. (On a job it limits the job — see Q090.) |
| Q110 | A | ✓ | Settled | Org workflow templates live in a `workflow-templates` directory inside the org's **`.github`** repository. |
| Q111 | A | ✓ | Settled | `issue_comment` fires when a comment is created on an issue (or PR). |
| Q112 | A | ✓ | Settled | **Write** access is required to delete workflow-run log files. |
| Q113 | A | ✓ | Settled | `if: github.repository == 'octo/my-prod-repo'` on a run in `octo/my-dev-repo` → condition false → job **skipped**. |
| Q114 | A | ✓ | Settled | Access matrix values via the `matrix` context: `matrix.version`, `matrix.os`. |
| Q115 | A | ✓ | Settled | **Write** access is required to re-run workflows. |
| Q116 | A | ✓ ⚑ | Settled | "After completion, regardless of age" is the marked answer. ⚑ The bank's own note flags a doc discrepancy (docs have at times implied a 14-day wait); observed behaviour is that completed runs can be deleted immediately. Confident in the answer; logged as a mild doc-currency caveat (not separately fetched). |
| Q117 | A | ✓ | Settled | **Repository administrators** can be allowed to bypass deployment protection rules (the "Allow administrators to bypass" option). |
| Q118 | A | ✓ | Settled | Skip a run via commit message / PR title keywords: `[skip ci]`, `[ci skip]`, `[no ci]`, `[skip actions]`, `[actions skip]`. |
| Q119 | A | ✓ | Settled | A container action has `runs.using: 'docker'` in `action.yml`. |
| Q120 | A | ✓ | Settled | Cleanup script in a container action = `post-entrypoint: 'cleanup.sh'`. |
| Q121 | A, B, C | ✓ | Settled | Default vars: set by GitHub, not in the workflow (A); most have a corresponding context property (B); the `CI` default value can currently be overwritten but that's not guaranteed (C). You can't create new defaults via a `GITHUB_` prefix (D); not all defaults are `GITHUB_`-prefixed, e.g. `RUNNER_OS`/`CI` (E); defaults aren't in the `env` context (F). |
| Q122 | A, B, C | ✓ | Settled | Custom variable scopes: workflow (`env` top-level), job (`jobs.<id>.env`), step (`jobs.<id>.steps[*].env`). `jobs.env`/`custom.env`/`environment.<id>.env` are invalid. |
| Q123 | A | ✓ | Settled | To `actions/checkout` a **different private repo**, pass a token: `token: ${{ secrets.MY_ACCESS_TOKEN }}`. The default `GITHUB_TOKEN` is scoped to the current repo only. |
| Q124 | B | ✓ | Settled | **5 jobs.** Base os[ubuntu,windows]×node[14,16] = 4; `include {macos-latest, node:18}` adds a new combo (+1); `include {ubuntu-latest, node:14}` matches an existing combo → no new job. 4 + 1 = 5. (Answer B.) |
| Q125 | A, B, C | ✓ | Settled | Environment variables can be defined at workflow, job, and step level — not "action level." |
| Q126 | A | ✓ | Settled | Reference an upstream job's output: `${{ needs.job1.outputs.output1 }}` (requires `needs: job1`). |
| Q127 | A | ✓ | Settled | Persist an env var for later steps: `echo "API_VERSION=2.1" >> "$GITHUB_ENV"`. (`set-env` is deprecated; `$GITHUB_OUTPUT` is for outputs.) |
| Q128 | A, C | ✓ | Settled | A workflow fires on reopened PRs if `types: [reopened]` is set (A) **or** if no activity types are set (C) — defaults are `opened`, `synchronize`, `reopened`. |
| Q129 | C | ✓ | Settled | **False** — `GITHUB_TOKEN` is scoped to the workflow's own repo; checking out another repo needs a PAT or installation token. (Answer C.) |
| Q130 | B, C, E | ✓ | Settled | Workflow-level `outputs` belong only to reusable workflows (B); a reusable workflow can have both workflow- and job-level outputs (C); workflow-level structure uses `value: ${{ jobs.<job>.outputs.<name> }}` (E). Job-level outputs are `name: ${{ steps… }}` with no nested `value:` (D wrong). |
| Q131 | A, C, D, G | ✓ | Settled | Composite actions: referenced by the folder holding `action.yml` (A), called as a step (C). Reusable workflows: called at job level not step (D), and can use a different runner type while composite inherits the caller's runner (G). Reusable workflows have no `action.yml` (B wrong); only reusable workflows use a `secrets` block (E wrong); both accept inputs (F wrong). |
| Q132 | A, B, E | ✓ | Settled | GHES can't reach GitHub.com/Marketplace actions by default (A); `actions-sync` is the manual tool for moving GitHub.com actions to GHES (B); GHES is self-hosted vs GHEC hosted by GitHub (E). GHES has no GitHub-hosted runners (C wrong); GitHub Connect is automatic, not manual-per-action (D wrong). |
| Q133 | A, B, D | ✓ | Settled | SHA-pinning is more secure (A), immutable vs mutable tags (B), guaranteed same code (D). Tags are *more* convenient not less (C wrong); SHAs make auditing easier not harder (E wrong). |
| Q134 | A | ✓ ⚑ | Settled | Run custom inline JS via the **`actions/github-script`** action. ⚑ Note: `github-script` is a real action but sits at the edge of GH-200's objectives (it was the off-syllabus item in MS-Learn Attempt-1 Q22). The answer is factually correct; just don't over-weight github-script as a core objective. |
| Q135 | A | ✓ | Settled | Forked-repo runs don't receive the base repo's secrets (except `GITHUB_TOKEN`), so a workflow referencing a secret fails. |
| Q136 | A | ✓ | Settled | Keep other matrix jobs running after one fails: `strategy.fail-fast: false` (default is `true`). `fail-fast` is at `strategy` level, not under `matrix`. |
| Q137 | A | ✓ | Settled | **5 jobs** — this is the canonical GitHub-docs `include` example. Includes with only new keys (`comment-color`, `error-color`) attach to all base combos; `{os: ubuntu-latest, comment-color: blue}` overwrites comment-color on the ubuntu combos; `{os: macos-latest, comment-color: yellow}` adds one new job. 4 (base) + 1 = 5. |
| Q138 | A | ✓ | Settled | Run after another workflow completes → `workflow_run`. |
| Q139 | A, B | ✓ | Settled | Runner diagnostic logging: set `ACTIONS_RUNNER_DEBUG=true` (secret/variable) (A), or re-run with "Enable debug logging" (B). |
| Q140 | A | ✓ | Settled | `if: startsWith(inputs.branch-name, 'smoke-test')`. Built-in functions use `fn(arg1, arg2)` form — no method chaining (B wrong); `branches` isn't valid under `workflow_call` (C wrong); shell-style conditionals aren't valid in `if:` (D wrong). |
| Q141 | A | ✓ | Settled | `hashFiles('**/lockfile')` in a cache key makes the key change when dependencies change, keeping the cache fresh. |
| Q142 | A, B, C | ✓ | Settled | Installation access tokens are short-lived and need a GitHub App (A); `GITHUB_TOKEN` is itself an installation access token (B); `actions/create-github-app-token` mints one usable immediately (C). |
| Q143 | A | ✓ | Settled | Lower artifact retention org-wide via the org's Actions settings "Artifact and log retention" value. |
| Q144 | A | ✓ | Settled | Per-workflow/per-artifact retention via the `retention-days` input on `actions/upload-artifact`. |
| Q145 | A, B, C | ✓ | Settled | Download an artifact via `actions/download-artifact` (A), the Actions UI (B), or the REST "Download an artifact" endpoint (C). |
| Q146 | A, B | ✓ | Settled | `pull_request` + unmerged → `github.ref` = `refs/pull/<n>/merge` (A); merged → `refs/heads/<base>` (B). |
| Q147 | A | ✓ | Settled | Keep a decoded (base64) secret out of logs with the `add-mask` workflow command — auto-redaction isn't guaranteed for transformed secrets. (Matches the base64-masking nuance.) |
| Q148 | A | ✓ | Settled | `push` event → `github.ref` is the fully-formed ref of the pushed branch/tag. |
| Q149 | A | ✓ | Settled | Writing to `$GITHUB_STEP_SUMMARY` appends Markdown to the run's **job summary**. |
| Q150 | A | ✓ | Settled | View the full triggering payload by printing the `github.event` object in a step. |
| Q151 | A | ✓ | Settled | Use **job outputs** to pass data between jobs — a value written to `$GITHUB_ENV` only persists within the job that set it. |
| Q152 | A | ✓ | Settled | A self-hosted runner's tool cache starts **empty** and must be populated (unlike GitHub-hosted runners, which ship pre-installed tools). |
| Q153 | A, B | ✓ | Settled | Events that can run a workflow **not** on the default branch: `push` (A) and `pull_request` (B, when the workflow's branch is the PR target). `repository_dispatch`/`star`/`issues`/`issue_comment` only use the default-branch workflow. |
| Q154 | A | ✓ | Settled | Build a Docker container action when you need a **consistent runtime + specific dependencies** baked in. (Docker actions are higher-overhead and Linux-only — not low-overhead, not fast on Win/macOS.) |
| Q155 | A | ✓ | Settled | A `schedule` workflow on a feature branch won't fire — the file must be on the **default branch** to be scheduled. |
| Q156 | A, B, C | ✓ | Settled | Delete artifacts via the UI per-artifact (A), by deleting the run (B), or via the "Delete an artifact" REST endpoint (C). No `actions/delete-artifact` action (D); not via SSH (E); retention can't be set to 0 days (F). |
| Q158 | A | ✓ | Settled | Trigger on a **merged** PR: `pull_request` `types: [closed]` **plus** `if: github.event.pull_request.merged == true`. There is no `merged` activity type. |
| Q159 | A, B, C | ✓ | Settled | `pull_request` runs in the merge-commit context, `pull_request_target` in the base repo's default-branch context (A); `pull_request` won't run on a merge-conflicting PR (B, no merge ref); both default to `opened/synchronize/reopened` (C). The fork-secret danger is `pull_request_target`'s, not `pull_request`'s (D wrong). |
| Q160 | A, B | ✓ | Settled | Use OIDC to avoid long-lived stored cloud secrets (A) and to use short-lived tokens (B). OIDC is recommended, not required (C wrong); you still set up trust policies (D wrong). |
| Q161 | A | ✓ | Settled | OIDC flow: the job requests an **OIDC token from GitHub's OIDC provider** → the cloud provider validates it → returns a short-lived **cloud-access token**. (Order: OIDC token first, then cloud token.) |
| Q162 | A, B | ✓ | Settled | Min files to publish a Docker container action: `action.yml` (A), and a `Dockerfile` **only if** the image is built during the run (B). No Dockerfile when referencing a registry image (`docker://…`); README recommended not required. |
| Q163 | A, B, C | ✓ | Settled | Private npm package for an org: publish to **GitHub Packages** (A), use a token with `write:packages` (B), talk to the `https://npm.pkg.github.com` registry (C). `admin:packages` is only for deletes (E); `registry_package` event isn't needed to *publish* (D/F). |
| Q164 | A, B | ✓ | Settled | `if:` is available at **job** and **step** level — not workflow/environment/org level. |
| Q165 | A, B, C | ✓ | Settled | `repository_dispatch`: external system **POSTs** to the GitHub API to create the event (A); the workflow listens for that created event (B); `on.repository_dispatch.types` maps to the request's `event_type` (C). It's POST not PUT (D); the workflow-dispatch endpoint is different (E); the key is `types` not `event_types` (F). |
| Q166 | A, B, C | ✓ | Settled | `actions/github-script` for short inline scripts (A) and a pre-authenticated GitHub API client (B); a full JavaScript action for a reusable cross-repo action (C). |
| Q167 | A | ✓ | Settled | Deleting a workflow file does **not** delete its runs or artifacts — they persist until the run itself is deleted, so the artifact is recoverable. |
| Q168 | A, B, C | ✓ | Settled | Required `action.yml` keys: `name`, `description`, `runs`. (`author`, `inputs`, `outputs` are optional.) |
| Q169 | A | ✓ | Settled | For an org with IP restrictions, add the self-hosted runners' IP addresses to the org's **IP allow list**. |
| Q170 | A | ✓ | Settled | `runs-on: [self-hosted, nes, linux]` requires a runner with **all** those labels (labels are cumulative/AND). GitHub-hosted runners can't take custom labels. |
| Q171 | A, B, C | ✓ | Settled | Re-run rationale: re-run only failed jobs vs a new run doing all (A); same commit SHA + git ref context (B); option to enable extra debug logging (C). `GITHUB_TRIGGERING_ACTOR` *does* update on re-run (D wrong); `GITHUB_ACTOR` does *not* change (E wrong). |
| Q172 | A | ✓ | Settled | Restrict a subset of self-hosted runners to certain repos via a **runner group** with repo access configured in the group settings. Labels don't restrict access (B/C). |
| Q173 | A | ✓ | Settled | Shared private-network Node env + node-locking software → **organization-level self-hosted runners** (GitHub-hosted runners are ephemeral and don't suit node-locking). |
| Q174 | A | ✓ ⚑ | Settled | Error: the reusable workflow declares workflow-level `permissions: contents: write`, but the caller job grants only `contents: read`. Nested-workflow token permissions can only be **same or more restrictive**, so requesting more makes the workflow invalid. ⚑ Nuance: this is an elevation→failure case (not a silent downgrade); ties directly to Q001's "downgrade-only" rule. |
| Q175 | A | ✓ | Settled | Without `actions/checkout`, repo files aren't on the runner, so `./scripts/scaffold-doc.py` isn't found and won't run — `chmod`/`setup-python` don't fix the missing checkout. |
| Q176 | A | ✓ | Settled | "Every commit" + "programmatic weekly failsafe" → `push` + `schedule`. (`workflow_dispatch` is manual, not programmatic; `weekly` isn't an event.) |
| Q177 | A | ✓ | Settled | Midnight Mon & Fri → `cron: '0 0 * * 1,5'` (min 0, hour 0, day-of-week 1,5). Day-of-week must be numeric; `workflow_schedule` isn't a trigger. |
| Q178 | A, B | ✓ ⚑ | Settled | Environment required reviewers: only **one** listed reviewer must approve (A); you can **prevent self-review** (B). ⚑ Nuance worth knowing: "all must approve" is false (C) — only one approval is needed; to force unanimity you'd need a custom deployment protection rule via a GitHub App. Teams *and* users can be reviewers (E false); reviewers need at least **read** access (F false). *(Several precise feature facts here — high confidence, not separately fetched; flag if a question contradicts.)* |
| Q179 | A, B | ✓ | Settled | Trust signals for a Marketplace action: a **Verified Creator** badge (A) and a thorough README (B). Brief `action.yml`, low stars, and a long-stale repo are the opposite of trust signals. |

---

## Traps, corrections & tracked doubts (consolidated)

### Correction logged during verification
- **Reusable-workflow nesting = 10 levels, not 4.** An early note (Block 2 / Q039) said "4 levels"; current docs say **up to ten**. The Q039 answer was unaffected. Companion limits: **50** unique reusable workflows per file (was 20), **256** matrix combinations, **360-min (6-h)** default job timeout, artifact/log default retention **90 days** (range 1–90).

### High-value traps (most worth drilling)
- **Answer-position bias** — un-shuffled, picking `A` scores ~89% while testing nothing. Always shuffle.
- **Matrix-`include` counting** (Q073, Q124, Q137) — include with only-new-keys attaches to all base combos; an include whose matrix-key value matches no base combo spawns a **new** job; one that matches extends in place. Tested 3×.
- **Re-run uses the ORIGINAL commit SHA + git ref** (Q055, Q133, Q171) — re-run ≠ re-trigger on latest code.
- **`GITHUB_TOKEN` is repo-scoped** (Q123, Q129) — can't check out another repo; needs a PAT/installation token. It's also a **secret, not a default env var** (Q061), yet it **is** an installation access token (Q142).
- **`workflow_dispatch` (5 input types incl. `number`/`choice`/`environment`) vs `workflow_call` (3: boolean/number/string)** (Q021).
- **PR branch filters match the TARGET/base branch** (Q017, Q018); `pull_request` runs in merge-commit context, `pull_request_target` in the base default-branch context — the fork-secret danger is `pull_request_target`'s (Q159).
- **Secret precedence: environment > repository > organization (> enterprise)** — most-specific wins (Q062, Q071).
- **`needs` is the only job-ordering mechanism** (Q048) — `download-artifact` and YAML file order do not create dependencies.
- **Nested-workflow permissions can only be same/more restrictive** (Q001, Q174) — a called workflow requesting more than the caller grants is an error, not a silent cap.
- **OIDC flow order** (Q161) — job requests OIDC token from GitHub first → cloud validates → cloud returns a short-lived access token.
- **Runner labels are cumulative for matching but don't restrict access** (Q170, Q172) — use runner **groups** to limit which repos can use runners.
- **Step vs runner debug** (Q107/Q139) — `ACTIONS_STEP_DEBUG` vs `ACTIONS_RUNNER_DEBUG`.
- **`add-mask` for transformed secrets** (Q147) — auto-masking isn't guaranteed for decoded/transformed values.

### Edge-of-syllabus (correct answers, low priority)
- **`actions/github-script`** (Q134, Q166) — a real action and the correct answer to "run custom inline JS," but it sits at the edge of GH-200's objectives (it was the off-syllabus item in MS-Learn Attempt-1 Q22). Don't over-weight it.

### Residual mild doubts (high-confidence, NOT separately fetched — check first if a quiz bites)
- **Q116** — deleting a workflow run "regardless of age": the bank's own note flags a historical 14-day doc statement; observed behaviour is immediate deletion.
- **Q174** — reusable-workflow permission elevation producing an *error* (vs a silent downgrade).
- **Q178** — environment required-reviewer specifics (only one of the listed reviewers must approve; self-review can be prevented; teams allowed; reviewers need read access).
- **Q066** — "GitHub-provided script" for runner connectivity = the runner's `--check` option (loosely worded but correct).

---

*Provenance: consolidated 2026-06-24 from `gh-200-ghcertified-verified-q001-q025` … `q151-q179`. The seven per-block files remain the diff-against-raw-bank source of record; this file is the single drill/reference copy.*
