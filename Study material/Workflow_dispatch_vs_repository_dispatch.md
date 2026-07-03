# workflow_dispatch vs repository_dispatch

*Saved 2026-07-03 after session `2026-07-03-a` — corrects the mental map "repository_dispatch is the remote equivalent of workflow_dispatch" (it isn't). Related misses: Q022 (×2, bucket c).*

The mental map is understandably wrong because it's *almost* right — and the exam loves that gap. The correction has two parts:

**Part 1: workflow_dispatch is already remote.** That's exactly the Q022 trap. It's triggerable via UI, REST API, and `gh workflow run`. So "remote equivalent" isn't what distinguishes `repository_dispatch` — both are remotely triggerable.

**Part 2: what repository_dispatch actually is.** It's not "trigger a workflow" at all — it's **"send a custom event to the repository."** Think webhook, not run button:

- You call `POST /repos/{owner}/{repo}/dispatches` with an `event_type` string you invent (e.g. `"deploy-approved"`) and an optional free-form JSON `client_payload`.
- You never name a workflow file. **Any and every workflow** in the repo that subscribes to that event fires — possibly several at once:
  ```yaml
  on:
    repository_dispatch:
      types: [deploy-approved]   # omit types: to catch all event_types
  ```
- Inside the run, `github.event.action` holds the event_type and `github.event.client_payload.*` holds your JSON.
- There is **no UI button** for it — API only.
- It **only triggers workflows on the default branch**, always. No ref selection.

## The sharper mental map

| | `workflow_dispatch` | `repository_dispatch` |
|---|---|---|
| Metaphor | "Run **this workflow**" | "Announce an **event to the repo**" |
| Targets | one named workflow | whoever subscribes via `types:` |
| Trigger via | UI + API + CLI | API only |
| Branch/ref | you pick the ref | default branch only |
| Data in | declared, typed `inputs` (validated) | free-form `client_payload` JSON |

The intended audience for `repository_dispatch` is **external systems and cross-repo automation**: your deployment tool, another repo's workflow, or any script that wants to say "something happened, react as you see fit" without knowing which workflows care. One caveat for cross-repo use: the calling side needs a PAT or GitHub App token with repo access — a workflow's own `GITHUB_TOKEN` can't dispatch to a *different* repo.

Two limits recalled but not 100% certain — verify against current docs if they matter for the exam: `client_payload` is capped at approximately 10 top-level properties, and there's a max length on `event_type` (~100 chars).
