# GH-200 Cheat — Topic 1A: Triggers, Permissions, Inputs, Reusable Workflows

*Trap-grade keepers only. Full explanation in the matching recap: `GH-200_Topic_1A_-_Triggers_Permissions_Inputs_Reusable_Workflows.md`.*

### Triggers
- `workflow_dispatch` = **internal** (UI / `gh` CLI / API; typed inputs). `repository_dispatch` = **external** POST to dispatches endpoint with custom `event_type`.
- `schedule`: **min 5 min**, **default branch only**, best-effort (delayed under load; avoid top-of-hour).
- Narrow events with: `types:`, `branches:`/`branches-ignore:`, `paths:`/`paths-ignore:`, `tags:`. `tags:` is for `push`, not `pull_request`.

### permissions / GITHUB_TOKEN
- Token is **per-job + ephemeral** (expires when the job ends).
- **Job-level `permissions:` REPLACES workflow-level (not merge).** Any **unlisted scope → `none`**.
- `{}` = no access; `read-all` / `write-all` = shortcuts.
- **Default read-only** for new repos/orgs/enterprises (`contents`+`packages` read). **Repo ← org ← enterprise** inheritance.
- **Fork PR token = read-only** unless admin enabled "Send write tokens to workflows from pull requests."
- `403: Resource not accessible by integration` = missing scope → add it to `permissions:`.

### Input types  ⚠️ MEMORIZE THE TWO SETS
- `workflow_dispatch`: **string, boolean, choice, number, environment** (5). `type` **OPTIONAL** (defaults `string`).
- `workflow_call`: **string, number, boolean** (3). `type` **REQUIRED**. **No `choice`, no `environment`.**
- `choice` **requires `options:`**.
- `description`: **required** in `action.yml` inputs; **NOT** required in `workflow_dispatch` inputs.
- `github.event.inputs.*` = **always strings** (`"false"` is truthy!). `inputs.*` = **typed**.
- `type: environment` = **picker only**; protection + env-secrets apply **only when a job sets `environment:`**.
- dispatch limits: **10 inputs max**, **65,535-char** payload.
- `workflow_call` unset defaults: **`false` / `0` / `""`**.

### Reusable workflows (`workflow_call`)
- Called at **JOB level**: `jobs.<id>.uses: owner/repo/.github/workflows/x.yml@REF` (**ref required**).
- `secrets: inherit` = **all** caller secrets (**org + repo**), **same org/enterprise only**.
- **Can't** reference `secrets.*` in caller `with:` (**parse-time error**). `with:` = inputs channel; `secrets:` = secrets channel.
- Environment secrets **not passable** via `workflow_call`; set `environment:` on the reusable job instead.
- Nesting allowed; **permissions only reduce down the chain, never elevate.**
