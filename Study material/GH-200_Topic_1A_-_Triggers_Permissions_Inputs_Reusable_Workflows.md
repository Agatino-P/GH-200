# GH-200 · Topic 1A — Triggers, Permissions, Inputs & Reusable Workflows

*Personalized recap. Covers Domain 1 gap objectives **1.2** (scope/permissions/events) and **1.3**
(`workflow_dispatch` inputs + `workflow_call` inputs/secrets). Facts verified against live GitHub
docs, June 2026. Quiz outcomes from this session are noted per bit, with a "weak spots" section at the end.*

---

## Bit 1 — Event categories & choosing a trigger  ·  *(quiz: 5/5)*

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

## Bit 2 — `permissions`: workflow vs job scope, least-privilege default  ·  *(quiz: 5/5)*

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

## Bit 3 — `workflow_dispatch` typed inputs  ·  *(quiz: 4/5)*

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

## Bit 4 — Reusable workflows (`workflow_call`)  ·  *(quiz: 4/5)*

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

## Your weak spots from the quizzes — focus revision here
1. **Input-type lists by trigger** (missed in both Bit 3 and Bit 4). Lock it: **dispatch = string/boolean/choice/number/environment**; **call = string/number/boolean**; `type` **optional** on dispatch (defaults `string`) but **required** on call.
2. **`options` is the choice-only requirement** — not `description`.
3. **Reusable-workflow invocation = job-level `uses:` with a ref** (you had to scroll back for this — worth over-learning).

## Sources (verified live, June 2026)
- Controlling permissions for `GITHUB_TOKEN` — docs.github.com/en/actions/.../controlling-permissions-for-github_token
- Managing GitHub Actions settings for a repository / for an organization — docs.github.com
- "Updating the default GITHUB_TOKEN permissions to read-only" — github.blog/changelog (2023)
- Workflow syntax (`workflow_dispatch` & `workflow_call` inputs) — docs.github.com/.../workflow-syntax-for-github-actions
- Reuse workflows — docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows
