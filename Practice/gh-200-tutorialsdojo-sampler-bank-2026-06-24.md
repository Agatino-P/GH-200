# GH-200 — Tutorials Dojo FREE Sampler (raw capture)

**Source:** Tutorials Dojo "FREE GH-200 GitHub Actions Practice Exams – Sampler" (Review Mode export).
**URL:** `https://portal.tutorialsdojo.com/product/free-gh-200-github-actions-practice-exams-sampler/`
**Captured:** 2026-06-24 16:23 UTC · **Count:** 30 questions
**Last updated: 2026-06-24 16:23 UTC**

> Raw capture only — options are transcribed in the order they appeared in this export, lettered A–D for reference. **Option order carries no signal** (TD randomises per session; this is one snapshot), and the §4.10 shuffle rule still applies when drilling. Marked answers are exactly what TD's Review Mode states under "Hence, the correct answer is…". Verdicts/enrichment live in the companion file `gh-200-tutorialsdojo-sampler-verified-2026-06-24.md`.
> TD cites `docs.github.com` references per question; URLs in the PDF were line-wrapped/truncated, so they are **not** reproduced here (see the verified file for doc anchors confirmed by topic).

---

### Q1 · Author and Manage Workflows
Which organizational level supports registering self-hosted runners in GitHub? **(Select THREE.)**
- A. Team
- B. Enterprise
- C. Repository
- D. Organization
- E. Workflow
- F. Project

**Marked correct:** B, C, D — Repository, Organization, Enterprise.

---

### Q2 · Consume and Troubleshoot Workflows
A script needs to retrieve workflow execution logs via the GitHub REST API. Which endpoint downloads workflow run logs?
- A. `DELETE /repos/:owner/:repo/actions/runs/:run_id/logs`
- B. `GET /repos/:owner/:repo/actions/runs/:run_id/logs`
- C. `GET /repos/:owner/:repo/actions/runs/:run_id` (run, not logs)
- D. `POST /repos/:owner/:repo/actions/runs/:run_id/logs`

**Marked correct:** B — `GET …/actions/runs/:run_id/logs`.

---

### Q3 · Manage GitHub Actions for the Enterprise
If an organization mandates the use of local actions exclusively, what is the recommended way to provide these actions?
- A. Hosted in a repository maintained by an external entity.
- B. Distributed through the GitHub Marketplace.
- C. Via internal repositories within the organization's namespace.
- D. Via repositories that belong to the organization.

**Marked correct:** D — via repositories that belong to the organization.

---

### Q4 · Author and Manage Workflows
Which method outputs a debug message in your GitHub Actions workflow?
- A. `echo "::debug::Set variable myVariable to true"`
- B. `echo "::warning::Set variable myVariable to true"`
- C. `echo "::add-mask::Set variable myVariable to true"`
- D. `echo "Debug: myVariable set to true" >> $GITHUB_STEP_SUMMARY`

**Marked correct:** A — `echo "::debug::…"`.

---

### Q5 · Author and Maintain Actions
A locally developed JavaScript action needs real execution results observed in GitHub Actions before publishing publicly. Which method should be used to test it?
- A. Create a simple workflow that runs only the custom JavaScript action.
- B. Schedule the action to run automatically and confirm execution using repository logs.
- C. Add the action to a workflow that includes GitHub's JavaScript debugging tools.
- D. Run the action's JavaScript file locally using Node.js with simulated inputs.

**Marked correct:** A — create a simple workflow that runs only the action.

---

### Q6 · Manage GitHub Actions for the Enterprise
Which role is required to create and manage organization-level encrypted secrets while controlling repository access policies?
- A. Workflow contributor
- B. Organization Member
- C. Organization owner
- D. Repository administrator

**Marked correct:** C — Organization owner.

---

### Q7 · Consume and Troubleshoot Workflows
Which action saves build outputs as an artifact retrievable after the run finishes?
- A. `actions/stale`
- B. `actions/setup-node`
- C. `actions/upload-artifact`
- D. `actions/download-artifact`

**Marked correct:** C — `actions/upload-artifact`.

---

### Q8 · Author and Manage Workflows
Which directory path stores and is used to discover workflows for GitHub Actions?
- A. `.github/pipelines/workflows`
- B. `.github/workflows`
- C. `.github/config/workflows`
- D. `.github/actions/workflows`

**Marked correct:** B — `.github/workflows`.

---

### Q9 · Author and Maintain Actions
Which component should be implemented to package a series of workflow steps into a single reusable custom action?
- A. Reusable workflow
- B. JavaScript action
- C. Composite action
- D. Workflow template

**Marked correct:** C — Composite action.

---

### Q10 · Consume and Troubleshoot Workflows
Which YAML step configuration correctly makes a step-level environment variable `APP_ENDPOINT` available to a shell command?
- A. `env:` as a list — `- key: APP_ENDPOINT` / `val: appserver01`
- B. `vars:` mapping — `APP_ENDPOINT: appserver01`
- C. `env:` mapping — `APP_ENDPOINT: appserver01`
- D. `with:` mapping — `APP_ENDPOINT: appserver01`

(All four share `- name: Display endpoint` / `run: echo $APP_ENDPOINT`.)

**Marked correct:** C — the `env:` mapping form.

---

### Q11 · Author and Maintain Actions
How can a composite action be identified in a GitHub Actions repository?
- A. The `action.yml` specifies a JavaScript entry point.
- B. The action repository name contains the term "composite".
- C. The `action.yml` metadata file defines `runs.using` with the value `composite`.
- D. The `action.yml` file defines multiple workflow steps using a workflow-style key.

**Marked correct:** C — `runs.using: composite` in `action.yml`.

---

### Q12 · Consume and Troubleshoot Workflows
Which two statements accurately describe caching vs workflow artifacts? **(Select TWO.)**
- A. Cache storage allows files to be retained for up to 30 days when accessed between workflow runs.
- B. Caching is useful for storing files that are reused and rarely change between jobs or workflow runs.
- C. Artifacts provide access to files that were created by a job after the workflow finishes.
- D. Artifacts support retrieving packages from the GitHub Package Registry for workflow use.
- E. Use GitHub Packages integration to distribute and version artifacts as reusable packages across repositories.

**Marked correct:** B, C.

---

### Q13 · Author and Maintain Actions
Which options reflect best practices for publishing GitHub Actions for reliable, predictable referencing? **(Select TWO.)**
- A. Publishing and referencing the action using a semantic version tag.
- B. Pinning the action to a specific commit SHA.
- C. Using the organization name to scope the action reference.
- D. Referencing the action using a moving branch name, such as `main`.
- E. Referencing the action without specifying a version identifier.

**Marked correct:** A, B.

---

### Q14 · Author and Manage Workflows
A single self-hosted runner with Windows x64 and a custom tool setup is available. Which configuration targets this specific runner?
- A. `runs-on: [self-hosted, windows, x64]`
- B. `self-hosted-runner: [windows, x64]`
- C. `runs-on: windows-latest`
- D. `self-hosted-runner: [win-x64]`

**Marked correct:** A — `runs-on: [self-hosted, windows, x64]`.

---

### Q15 · Consume and Troubleshoot Workflows
Which repository access level is the minimum required for downloading workflow artifacts?
- A. Triage
- B. Read
- C. Actions Read
- D. Write

**Marked correct:** B — Read.

---

### Q16 · Consume and Troubleshoot Workflows
Which feature enforces a manual approval gate before a job targeting sensitive resources can continue?
- A. Assigning elevated repository permissions to approvers.
- B. Using CODEOWNERS to require approval before workflow jobs execute.
- C. Configuring required reviewers on a deployment environment.
- D. Restricting workflow execution using branch protection rules.

**Marked correct:** C — required reviewers on a deployment environment.

---

### Q17 · Consume and Troubleshoot Workflows
A deployment workflow must start automatically only after a separate build workflow finishes successfully, without changing the build config. Which trigger should be configured?
- A. `schedule`
- B. `workflow_run`
- C. `workflow_dispatch`
- D. `workflow_call`

**Marked correct:** B — `workflow_run`.

---

### Q18 · Consume and Troubleshoot Workflows
Which duration causes a workflow in the Waiting state to automatically fail?
- A. 25 days
- B. 100 days
- C. 30 days
- D. 60 days

**Marked correct:** C — 30 days.

---

### Q19 · Author and Manage Workflows
Which feature allows a workflow to use a temporary PostgreSQL database during execution?
- A. Use a database service container defined in the workflow.
- B. Provision a managed cloud database and connect using secrets.
- C. Use a self-hosted runner with PostgreSQL installed permanently.
- D. Embed the database inside the application Docker image.

**Marked correct:** A — service container.

---

### Q20 · Author and Manage Workflows
When scheduled workflows execute, which commit and branch are used?
- A. The most recent commit on the repository's default or base branch.
- B. The latest commit and branch where the schedule event initiated the workflow.
- C. The most recent commit on the branch called `schedule`.
- D. The commit and branch defined in the workflow configuration file.

**Marked correct:** A — latest commit on the default/base branch.

---

### Q21 · Consume and Troubleshoot Workflows
Which predefined environment variable contains the branch or tag that initiated the current workflow run?
- A. `GITHUB_HEAD_REF`
- B. `GITHUB_REF`
- C. `GITHUB_WORKFLOW`
- D. `GITHUB_BRANCH`

**Marked correct:** B — `GITHUB_REF`.

---

### Q22 · Consume and Troubleshoot Workflows
Which statement accurately describes deleting workflow runs?
- A. Repository admin privileges are required to delete a workflow run.
- B. Runs that have finished execution can be removed.
- C. Runs that are still in progress can be removed.
- D. Deletion is only possible for runs more than 30 days old.

**Marked correct:** B — finished runs can be removed.

---

### Q23 · Consume and Troubleshoot Workflows
Deployments must pause until a specific operations team approves the release. Which actions enforce this? **(Select TWO.)**
- A. Assign the operations team as repository administrators to control production deployments.
- B. Define a Production environment in repository settings and configure the operations team as required reviewers.
- C. Reference the Production environment in the deployment job within the workflow.
- D. Configure branch protection rules to require approvals before workflow execution.
- E. Register the production virtual machines directly within the GitHub Actions environment configuration.

**Marked correct:** B, C.

---

### Q24 · Manage GitHub Actions for the Enterprise
An org wants to reduce duplication by centrally maintaining deployment logic that includes multiple jobs and is reusable by different repositories. Which feature?
- A. Workflow templates used only when creating new workflows.
- B. Reusable workflows referenced using the `workflow_call` trigger.
- C. Composite actions defined in an `action.yml` file.
- D. YAML anchors and aliases within each workflow file.

**Marked correct:** B — reusable workflows (`workflow_call`).

---

### Q25 · Consume and Troubleshoot Workflows
Which syntax correctly references a reusable workflow?
- A. `uses: octo-org/another-repo/.github/workflows/workflow.yml@v1`
- B. `implements: octo-org/another-repo/workflow.yml@v1`
- C. `imports: another-repo/workflow.yml using v1`
- D. `uses: another-repo/.github/workflows/workflow.yml@v1` (no owner)

**Marked correct:** A — full `uses: owner/repo/.github/workflows/file.yml@ref`.

---

### Q26 · (labelled "Author and Maintain Actions" — but see verified file: OFF-SYLLABUS)
You are developing a custom Microsoft Sentinel query to monitor unusual sign-in patterns in Microsoft Entra ID. The results need a time-series chart grouped by daily intervals. Which operator aggregates the sign-in events by day for the time chart?
- A. `makeset`
- B. `bin`
- C. `summarize`
- D. `render`

**Marked correct:** B — `bin`. *(This is a Kusto/KQL question, not GitHub Actions — flagged in the verified file.)*

---

### Q27 · Manage GitHub Actions for the Enterprise
Which scenario accurately represents a valid use case for GitHub Actions environment secrets?
- A. Configuring environment secrets to automatically synchronize from AWS Secrets Manager.
- B. Configuring environment secrets to authenticate GitHub Actions workflows with Microsoft Entra ID.
- C. Restricting environment secret access to individual workflow steps rather than entire jobs.
- D. Implementing required approvals to restrict job access to environment secrets until authorized reviewers grant permission.

**Marked correct:** D — required approvals gate access to environment secrets.

---

### Q28 · Author and Maintain Actions
Which action type provides the simplest method for executing a shell script?
- A. Composite run steps action
- B. JavaScript action
- C. TypeScript action
- D. Docker container action

**Marked correct:** A — composite run steps action.

---

### Q29 · Manage GitHub Actions for the Enterprise
Which approach allows a GitHub repository to authenticate and securely access resources in Azure?
- A. Commit Azure credentials to the repository for access across workflows.
- B. Hardcode Azure service principal credentials in the workflow file.
- C. Authenticate to Azure using a GitHub personal access token (PAT).
- D. Manage Azure service principal credentials using GitHub Secrets.

**Marked correct:** D — manage SP credentials via GitHub Secrets. *(See verified file: correct among the offered options, but OIDC — the current best practice — is not offered.)*

---

### Q30 · Author and Maintain Actions
Which are advantages of GitHub-hosted runners? **(Select TWO.)**
- A. Built-in support for Linux, Windows, and macOS runners managed by GitHub.
- B. Automatic patching and maintenance of both the runner application and its underlying operating system.
- C. Native integration with GitHub Environments for long-lived runner persistence.
- (plus distractor options about self-hosted-style control)

**Marked correct:** A, B.
