# Default environment variables: `env` context vs `github` context

**The `env` context holds only variables you define with `env:`** in the workflow (at workflow, job, or step level). It does **not** contain GitHub's default environment variables.

**Default environment variables** (e.g. `GITHUB_SHA`, `GITHUB_REF`, `RUNNER_OS`) are available two ways:

- as **real shell environment variables** inside a `run:` step — `$GITHUB_SHA`, `$GITHUB_REF`;
- via a **corresponding property on the `github` (or `runner`) context** in `${{ }}` expressions — `github.sha`, `github.ref`, `runner.os`.

So in an expression you write `${{ github.sha }}`, **not** `${{ env.GITHUB_SHA }}`.

**Related facts:**

- Most default environment variables have a matching context property (that's the `github` context, not `env`).
- Default variables are set by GitHub, not declared in the workflow.
- Not all default variables use the `GITHUB_` prefix — there are also `RUNNER_*` and `CI`.
- You cannot create new default variables; the `GITHUB_` prefix is reserved.
- The `CI` default can currently be overwritten, but that is not guaranteed to remain possible.
