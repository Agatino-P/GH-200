# Downloading artifacts from another workflow run

*Saved 2026-07-04 during session `2026-07-04-a` — reinforcement note for Q044 (answered correctly; clarification requested on the mechanics).*

`actions/download-artifact` (v4) by default only sees artifacts from the **current** workflow run. To pull from a different run you add two things: which run, and a token that can read it.

**Same run (the default, no extras needed):**

```yaml
- uses: actions/download-artifact@v4
  with:
    name: test-results
```

**Different run — add `run-id` and `github-token`:**

```yaml
- uses: actions/download-artifact@v4
  with:
    name: test-results
    run-id: ${{ github.event.workflow_run.id }}   # the "previous run details"
    github-token: ${{ github.token }}              # the "elevated permission"
```

The two pieces:

1. **The run details** — artifacts belong to a specific workflow *run*, so you must name the `run-id`. Where it comes from depends on the scenario: if your workflow is triggered by `workflow_run` (the classic "CI finished → now deploy" chain), it's right there in the event payload as `github.event.workflow_run.id`. Otherwise you look it up — `gh run list`, or the REST API.

2. **The token** — within the same run, the action uses ambient credentials and no token input is needed. Cross-run, the action makes real API calls to the Actions artifacts endpoints, so it needs an explicit `github-token`. For the **same repo**, the job's own `GITHUB_TOKEN` suffices as long as the job's permissions include `actions: read`. For a **different repo** (there's also a `repository:` input), the default token won't do — you need a PAT or GitHub App token with access to that repo.

The non-Actions equivalent is the REST API directly: list a run's artifacts, then download the zip — same auth requirement, which is why "elevated permissions" is the distinguishing phrase in exam options.
