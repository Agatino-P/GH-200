# Where custom-action metadata lives

*Saved 2026-07-04 during session `2026-07-04-a`.*

**Hard rule:** every custom action — Docker, JavaScript, or composite — needs a metadata file named `action.yml` (or `action.yaml`), placed **at the root of the action's own directory**. That file is always required (public or private, shared or local); without it there is no action. What matters is the *directory*, not which repository it sits in.

Three legitimate homes for that directory:

1. **Its own dedicated repo** — `action.yml` at the repo root. The published/shareable layout, referenced as `owner/repo@ref`.
2. **A subdirectory of any repo** — e.g. `.github/actions/my-action/action.yml`, referenced locally as `./.github/actions/my-action`. Lives in the same repo as the workflow that calls it. Composite actions commonly live here.
3. **A public repo referenced from anywhere** — same as (1), just consumed by other repos.

An action does **not** need its own repository. A composite action (like any type) just needs a folder containing `action.yml`; that folder can sit right next to the workflow that uses it.
