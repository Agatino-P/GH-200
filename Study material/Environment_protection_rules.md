# Environment protection rules

Rules configured per environment (Settings → Environments). A job that targets an environment **won't start until all configured protection rules pass** — the rule *types* below are AND'd together.

**Rule types:**

1. **Required reviewers** — a manual approval gate. List up to **6** users/teams. **Only one of the listed reviewers needs to approve** for the job to proceed (not all of them). Reviewers need at least read access; a rejection blocks the deployment.
2. **Wait timer** — a forced delay before the job may run (max ~30 days / 43,200 minutes).
3. **Deployment branch policy** — restricts which branches may deploy to the environment: all branches / protected branches only / selected branch name patterns.
4. **Custom deployment protection rules** — optional, provided by third-party GitHub Apps (advanced).

**Two different "counts" to keep straight:**

- Across rule *types* → **AND**: every configured rule must pass (wait timer elapsed **and** a reviewer approved **and** branch policy allows it).
- *Within* required reviewers → **one approval is enough**.

**Not the same as branch protection rules:** those gate PRs/pushes to a branch and use a *number* of required approvals — a separate mechanism from environment gates.
