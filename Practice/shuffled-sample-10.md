## Q001

Which statement is correct regarding passing permissions to reusable workflows?

- A. The `GITHUB_TOKEN` permissions passed from the caller workflow can be both downgraded and elevated by the called workflow.
- B. The `GITHUB_TOKEN` permissions passed from the caller workflow can be only elevated by the called workflow.
- C. The `GITHUB_TOKEN` permissions passed from the caller workflow can be neither downgraded or elevated by the called workflow.
- D. The `GITHUB_TOKEN` permissions passed from the caller workflow can be only downgraded by the called workflow.

**Answer:** D  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/reusing-workflows#access-and-permissions

> **✅ Verified 2026-07-02** — Confirmed current on `docs.github.com` (Reuse workflows; Reusing workflow configurations). A caller's `GITHUB_TOKEN` permissions can only be **downgraded** (never elevated) by the called workflow; in nested chains they can only be maintained or reduced. Marked answer **A** stands.

---

## Q002

What are the different permission levels you can assign to `GITHUB_TOKEN` in the `permissions` block?

- A. read, write, delete
- B. read, write
- C. none, write, read

**Answer:** C  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-jobs/assigning-permissions-to-jobs

---

## Q003

You can use `permissions` to modify the `GITHUB_TOKEN` permissions on:

- A. Job level
- B. Step level
- C. Workflow level

**Answer:** A, C  ·  *multi-select (2 correct)*
**Docs:** https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/controlling-permissions-for-github_token

---

## Q004

Are GitHub Actions free for public repositories?

- A. No, only self-hosted runners are free for public repositories
- B. No, all GitHub Actions usage is billed
- C. Yes, but only for the first 2,000 minutes per month
- D. Yes, when using standard GitHub-hosted runners

**Answer:** D  ·  *single*
**Docs:** https://docs.github.com/en/billing/concepts/product-billing/github-actions#how-use-of-github-actions-is-measured

> **✅ Verified 2026-07-02** — Confirmed current on `docs.github.com` (GitHub Actions billing): usage is free for **standard** GitHub-hosted runners in public repositories (and for self-hosted runners). Marked answer **A** stands. Caveat that makes A correct: *larger* runners are always billed, even in public repos — so "free" holds only for **standard** runners. The Jan 1 2026 pricing changes (hosted-runner rate cuts + a $0.002/min platform charge) do **not** affect public-repo standard-runner usage; it remains free.

---

## Q005

Which of these is not a valid event that could trigger a workflow?

- A. Committing a file to master branch
- B. A branch is created
- C. Adding a label to a pull request
- D. Cloning the repository

**Answer:** D  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#about-events-that-trigger-workflows

---

## Q006

Which is true about workflows?

- A. Workflows are written in any of `.yaml`, `.json` or `.toml` formats
  > Workflows can only be defined in `.yaml` format
- B. Workflows can only be run on a schedule
- C. Workflows have to be defined in the `.github/workflows` directory
- D. Workflows can run one or multiple jobs at a time
- E. Workflow can run only one job at a time
- F. Workflows can be shared in GitHub Marketplace
  > Actions (not workflows) can be shared in GitHub Marketplace
- G. Workflows can be triggered manually, by an event or run on a schedule

**Answer:** C, D, G  ·  *multi-select (3 correct)*
**Docs:** https://docs.github.com/en/actions/using-workflows/about-workflows

---

## Q007

Which components are required for a workflow?

- A. Workflow name
- B. One or more jobs
- C. One or more events that will trigger the workflow
- D. Defined branches on which the workflow will run

**Answer:** B, C  ·  *multi-select (2 correct)*
**Docs:** https://docs.github.com/en/actions/using-workflows/about-workflows#workflow-basics

---

## Q008

Which event is triggered by a webhook action from outside of the repository?

- A. webhook_dispatch
- B. remote_dispatch
- C. repository_dispatch
- D. workflow_dispatch
- E. api_dispatch

**Answer:** C  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows

---

## Q009

Workflows are defined in which format

- A. yaml
- B. json
- C. toml
- D. xml

**Answer:** A  ·  *single*
**Docs:** — (no link in source)

---

## Q010

Where should you store sensitive data such as passwords or certificates that will be used in workflows

- A. vault
- B. environment variables
- C. secrets
- D. config variables

**Answer:** C  ·  *single*
**Docs:** https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions

---
