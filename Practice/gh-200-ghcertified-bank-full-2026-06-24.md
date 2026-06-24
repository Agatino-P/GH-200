# GH-200 — GHCertified Practice Bank (Actions / GH-200)

**Captured:** 2026-06-24 10:41 UTC
**Source:** `github.com/FidelusAleksander/ghcertified` → `questions/en/actions/` (branch `main`, depth-1 clone)
**Folder URL:** https://github.com/FidelusAleksander/ghcertified/tree/main/questions/en/actions
**License:** GPL-3.0 (community-contributed, open source)
**Count:** 178 questions (41 multi-select, 137 single-answer)

> **Accuracy caveat (protocol §4 / §10):** answers below are the *contributor-marked* keys from the repo — the same key the live ghcertified.com site scores against. They are **not** verified against `docs.github.com`. Per protocol, treat any "correct" answer skeptically and verify against official GitHub docs before internalizing it, especially for the reworded Domain 4/5 objectives. The per-question `Docs:` link is the contributor's reference, not proof the marked answer is current.
> **Questions with no source docs link:** Q009, Q052, Q072.
> **Answer letters (A/B/C…)** were assigned by this capture in the source file's option order; the source itself has no letters, only `[x]`/`[ ]` checkboxes.

---

## Q001

Which statement is correct regarding passing permissions to reusable workflows?

- A. The `GITHUB_TOKEN` permissions passed from the caller workflow can be only downgraded by the called workflow.
- B. The `GITHUB_TOKEN` permissions passed from the caller workflow can be only elevated by the called workflow.
- C. The `GITHUB_TOKEN` permissions passed from the caller workflow can be both downgraded and elevated by the called workflow.
- D. The `GITHUB_TOKEN` permissions passed from the caller workflow can be neither downgraded or elevated by the called workflow.

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/reusing-workflows#access-and-permissions

---

## Q002

What are the different permission levels you can assign to `GITHUB_TOKEN` in the `permissions` block?

- A. none, write, read
- B. read, write, delete
- C. read, write

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-jobs/assigning-permissions-to-jobs

---

## Q003

You can use `permissions` to modify the `GITHUB_TOKEN` permissions on:

- A. Workflow level
- B. Job level
- C. Step level

**Answer:** A, B  ·  *multi-select (2 correct)*
**Docs:** https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/controlling-permissions-for-github_token

---

## Q004

Are GitHub Actions free for public repositories?

- A. Yes, when using standard GitHub-hosted runners
- B. No, all GitHub Actions usage is billed
- C. Yes, but only for the first 2,000 minutes per month
- D. No, only self-hosted runners are free for public repositories

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/billing/concepts/product-billing/github-actions#how-use-of-github-actions-is-measured

---

## Q005

Which of these is not a valid event that could trigger a workflow?

- A. Cloning the repository
- B. Committing a file to master branch
- C. A branch is created
- D. Adding a label to a pull request

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#about-events-that-trigger-workflows

---

## Q006

Which is true about workflows?

- A. Workflows can run one or multiple jobs at a time
- B. Workflows can be triggered manually, by an event or run on a schedule
- C. Workflows have to be defined in the `.github/workflows` directory
- D. Workflows can only be run on a schedule
- E. Workflow can run only one job at a time
- F. Workflows are written in any of `.yaml`, `.json` or `.toml` formats
  > Workflows can only be defined in `.yaml` format
- G. Workflows can be shared in GitHub Marketplace
  > Actions (not workflows) can be shared in GitHub Marketplace

**Answer:** A, B, C  ·  *multi-select (3 correct)*
**Docs:** https://docs.github.com/en/actions/using-workflows/about-workflows

---

## Q007

Which components are required for a workflow?

- A. One or more events that will trigger the workflow
- B. One or more jobs
- C. Workflow name
- D. Defined branches on which the workflow will run

**Answer:** A, B  ·  *multi-select (2 correct)*
**Docs:** https://docs.github.com/en/actions/using-workflows/about-workflows#workflow-basics

---

## Q008

Which event is triggered by a webhook action from outside of the repository?

- A. repository_dispatch
- B. webhook_dispatch
- C. workflow_dispatch
- D. remote_dispatch
- E. api_dispatch

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows

---

## Q009

Workflows are defined in which format

- A. yaml
- B. toml
- C. json
- D. xml

**Answer:** A  ·  *single*
**Docs:** — (no link in source)

---

## Q010

Where should you store sensitive data such as passwords or certificates that will be used in workflows

- A. secrets
- B. config variables
- C. vault
- D. environment variables

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions

---

## Q011

In a workflow with multiple jobs the default behavior is:

- A. All jobs run in parallel
- B. Jobs run in sequence
- C. Jobs run based on the order they are defined in the workflow file
- D. Only the first job runs, others require manual approval

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/about-workflows#creating-dependent-jobs

---

## Q012

If job B requires job A to be finished you have to:

- A. use the `needs` keyword in job B to create this dependency
- B. use the `needs` keyword in job A to create this dependency
- C. use the `requires` keyword in job B to create this dependency
- D. use the `requires` keyword in job A to create this dependency

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/about-workflows#creating-dependent-jobs

---

## Q013

In a workflow with multiple jobs, if job A fails then:

- A. the jobs that are dependent on job A are skipped
- B. the jobs that are dependent on job A fail
- C. the workflow immediately cancels all other jobs

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-jobs#defining-prerequisite-jobs

---

## Q014

This code will launch 6 different jobs in parallel using the matrix strategy. Can you use the matrix strategy to parallelize entire workflows?

```yaml
jobs:
  example_matrix:
    strategy:
      matrix:
        version: [10, 12, 14]
        os: [ubuntu-latest, windows-latest]
```

- A. Yes
- B. No
- C. Only if the workflows are in the same repository
- D. Only with self-hosted runners

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/reusing-workflows#using-a-matrix-strategy-with-a-reusable-workflow

---

## Q015

Which matrix job definition is syntactically correct?

- A. 
  ```yaml
  jobs:
    example_matrix:
      strategy:
        matrix:
          version: [10, 12, 14]
          os: [ubuntu-latest, windows-latest]
  ```
- B. 
  ```yaml
  jobs:
    example_matrix:
      matrix:
        strategy:
          version: [10, 12, 14]
          os: [ubuntu-latest, windows-latest]
  ```
- C. 
  ```yaml
  jobs:
    example_matrix:
      matrix:
        version: [10, 12, 14]
        os: [ubuntu-latest, windows-latest]
  ```
- D. 
  ```yaml
  jobs:
    matrix:
      version: [10, 12, 14]
      os: [ubuntu-latest, windows-latest]
  ```

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs#using-a-matrix-strategy

---

## Q016

How do you access matrix variables in a matrix strategy job?

- A. Using the `vars` context
- B. Using the `matrix` context
- C. Using the `job` context
- D. Using the `jobs` context

**Answer:** B  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs#using-a-matrix-strategy

---

## Q017

When using the `pull_request` and `pull_request_target` events, how do you configure the workflow to run only when targeting the `prod` branch?

- A. Using `branches` filter
- B. Using `branch` filter
- C. You create the workflow only on `prod` branch
- D. Using glob patterns

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/triggering-a-workflow#using-filters-to-target-specific-branches-for-pull-request-events

---

## Q018

This workflow will run on all pull requests where:

```yaml
on:
  pull_request:
    branches:
      - 'release/**'
      - '!release/**-alpha'
```

- A. the target branch name starts with `release` but does not end with `-alpha`
- B. the target branch name starts with `release`
- C. the source branch name starts with `release` but does not end with `-alpha`
- D. the source branch name starts with `release`

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/triggering-a-workflow#example-including-and-excluding-branches

---

## Q019

Fill in the blank: When using `push` event trigger filters you can use <____> patterns to target multiple branches

- A. glob
- B. regex
- C. scheme
- D. action

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/triggering-a-workflow#using-filters-to-target-specific-branches-or-tags-for-push-events

---

## Q020

Which event allows you to manually trigger a workflow from the GitHub UI?

- A. workflow_dispatch
- B. manual_dispatch
- C. workflow_trigger
- D. manual_trigger

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/manually-running-a-workflow

---

## Q021

What are the possible types of an input variable for a manually triggered workflow?

- A. choice
- B. boolean
- C. string
- D. number
- E. environment
- F. dropdown
- G. select

**Answer:** A, B, C, D, E  ·  *multi-select (5 correct)*
**Docs:** https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#onworkflow_dispatchinputsinput_idtype

---

## Q022

A workflow that has only `workflow_dispatch` event trigger can be triggered using GitHub's REST API

- A. True
- B. False

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onworkflow_dispatchinputs

---

## Q023

To stop a workflow from running temporarily without modifying the source code you should

- A. Use the `Disable workflow` option in GitHub Actions
- B. Remove secrets that are required for this workflow
- C. Delete environment that is required for this workflow
- D. Prevent any new commits to main branch

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/disabling-and-enabling-a-workflow

---

## Q024

What are `activity types` of an event used for ?

- A. Limiting workflow runs to specific activity types using the `types` filter
- B. Checking if the activity comes from an user or a bot
- C. Reacting to new activity on a repository (e.g new contributor)

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#about-events-that-trigger-workflows

---

## Q025

You want to create a reusable workflow `CI` that runs some quality checks, linting and tests on code changes. What event trigger should the `CI` workflow define to allow reusing it in other workflows?

- A. workflow_call
- B. workflow_trigger
  > There is no such event trigger
- C. workflow_dispatch
  > This is used for manual triggers
- D. workflow_run
  > https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#workflow_run

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows

---

## Q026

A reusable workflow named `build` creates zip file artifacts. How do you pass the zip file location to the caller workflow that is calling the `build` workflow?

- A. You define an output on workflow level in the `build` workflow
- B. You define an output on job level in the `build` workflow
- C. In the `build` workflow you write the output into `$GITHUB_OUTPUT` in one of the steps
- D. All outputs are automatically passed to the caller workflows

**Answer:** A, B, C  ·  *multi-select (3 correct)*
**Docs:** https://docs.github.com/en/actions/using-workflows/reusing-workflows#using-outputs-from-a-reusable-workflow

---

## Q027

What are the valid use cases for using **defaults**?

- A. Using defaults.run on workflow level to set default shell (e.g bash) for an entire workflow
- B. Using defaults.run on job level to set default working-directory for all steps in a single job
- C. Using defaults.run on step level to set default shell (e.g bash) for that single step
  > defaults.run can only be set on workflow or job level
- D. Using defaults.env on workflow level to set default environment variables for an entire workflow
  > There is no such thing as defaults.env
- E. Using defaults.env on job level to set default environment variables for all steps in a single job
  > There is no such thing as defaults.env

**Answer:** A, B  ·  *multi-select (2 correct)*
**Docs:** https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#defaults

---

## Q028

How can you ensure that a workflow called `Deploy Prod` is always running at most one at a time?

- A. Use `concurrency` on workflow level
  ```yaml
  concurrency: ${{ github.workflow }}
  ```
- B. Use `queue` on workflow level
  ```yaml
  queue: ${{ github.workflow }}
  ```
- C. Use `order` on workflow level
  ```yaml
  order: ${{ github.workflow }}
  ```
- D. Use `parallel` on workflow level
  ```yaml
  parallel: ${{ github.workflow }}
  ```

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#concurrency

---

## Q029

Your Pull Request analysis workflow uses multiple code analysis tools and takes about 20minutes to fully complete. It is triggered on `pull_request` event with `branches` filter set to `master`. Therefore if a developer pushes multiple commits within few minutes multiple workflows are running in parallel. How can you stop all previous workflow runs and only run the one with latest changes?

- A. Use concurrency with cancel-in-progress
  ```yaml
  concurrency:
    group: ${{ github.workflow }}-${{ github.ref }}
    cancel-in-progress: true
  ```
- B. Use concurrency
  ```yaml
  concurrency:
    group: ${{ github.ref }}
  ```
  > This would queue runs on that github ref. It will not stop previous runs
- C. Use activity types filter
  ```yaml
  on:
    pull_request:
      branches:
        - master
      types: [latest]
  ```
  > There is no such activity type as `latest` for pull_request event
- D. Use cancel-in-progress flag for `pull_request` event
  ```yaml
  on:
    pull_request:
      branches:
        - master
      cancel-in-progress: true
  ```
  > `cancel-in-progress` can only be used inside a `concurrency` block. It is not a valid key for `pull_request`.

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#example-using-concurrency-to-cancel-any-in-progress-job-or-run

---

## Q030

When will job3 run?

```yaml
jobs:
  job1:
  job2:
    needs: job1
  job3:
    if: ${{ always() }}
    needs: [job1, job2]
```

- A. job3 will run after job1 and job2 have completed, regardless of whether they were successful
- B. You cannot use `if: ${{ always() }}` and `needs` together. The workflow will fail on startup.
- C. job3 will run after job1 and job2 have been successfully completed
- D. job3 will run after both job1 and job2 have failed

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#example-not-requiring-successful-dependent-jobs

---

## Q031

What `jobs.job_id.if` conditional will make sure that job `production-deploy` is triggered only on `my-org/my-repo` repository?

```yaml
jobs:
  production-deploy:  
    if: <CONDITION>
    runs-on: ubuntu-latest
    steps:
      ...
```

- A. `if: github.repository == 'my-org/my-repo'`
- B. `if: ${{ github.repository == 'my-org/my-repo' }}`
- C. `if: ${{ github.organization == 'my-org' && github.repository == 'my-repo' }}`
  > https://docs.github.com/en/actions/learn-github-actions/contexts#github-context
- D. `if: ${{ github.org == 'my-org' && github.repository == 'my-repo' }}`
  > https://docs.github.com/en/actions/learn-github-actions/contexts#github-context

**Answer:** A, B  ·  *multi-select (2 correct)*
**Docs:** https://docs.github.com/en/actions/learn-github-actions/contexts#github-context

---

## Q032

What GitHub-hosted runner types are available to use?

- A. Windows
- B. Ubuntu Linux
- C. macOS
- D. Android

**Answer:** A, B, C  ·  *multi-select (3 correct)*
**Docs:** https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#choosing-github-hosted-runners

---

## Q033

Is this statement true? `Not all steps run actions, but all actions run as a step`

- A. True
- B. False
  > Steps can but don't have to run actions (e.g running a run command)

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idsteps

---

## Q034

For any action published in GitHub Marketplace, you can often use it in multiple versions. Which approach is the most stable and secure?

- A. Reference the commit SHA
- B. Reference a version tag
- C. Reference the main branch

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#example-using-versioned-actions

---

## Q035

To prevent a job from failure when one of the steps fails you can include:

- A. `continue-on-error` flag in the failing step
  ```yaml
  steps:
      - uses: my-org/failing-action@v1
        continue-on-error: true
  ```
- B. `ignore-error` flag in the failing step
  ```yaml
  steps:
      - uses: my-org/failing-action@v1
        ignore-error: true
  ```
- C. `failure()` conditional in the failing step
  ```yaml
  steps:
      - uses: my-org/failing-action@v1
        if: failure()
  ```
- D. `always()` conditional in the failing step
  ```yaml
  steps:
      - uses: my-org/failing-action@v1
        if: always()
  ```

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepscontinue-on-error

---

## Q036

You defined a matrix job `example_matrix`. How can you limit the matrix to run a maximum of 2 jobs at a time?

```yaml
jobs:
  example_matrix:
    strategy:
      matrix:
        version: [10, 12, 14]
        os: [ubuntu-latest, windows-latest]
```

- A. Set `jobs.example_matrix.strategy.max-parallel` to 2
- B. Set `jobs.example_matrix.strategy.concurrency` to 2
- C. Use GitHub's REST API to check if the job count is lesser than 2
- D. It's not possible, a matrix will always run all of the jobs in parallel if there are runners available

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstrategymax-parallel

---

## Q037

Which of these is a proper way of setting an output parameter `PET` with a value of `DOG` in a `step`.

- A. `echo "PET=DOG" >> "$GITHUB_OUTPUT"`
- B. `echo "DOG=PET" >> "$GITHUB_OUTPUT"`
- C. `gh set-output "DOG=PET"`
- D. `gh set-output "PET=DOG"`

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter

---

## Q038

Which of these is a way of using `action_state` in `step_two`?

```yaml
steps:
  - name: Set the value
    id: step_one
    run: |
      echo "action_state=yellow" >> "$GITHUB_ENV"
  - name: Use the value
    id: step_two
    run: ?
```

- A. `run: echo "$action_state"`
- B. `run: echo "${{ steps.step_one.outputs.action_state }}"`
  > That would be the case if `action_state` was written to `$GITHUB_OUTPUT`
- C. `run: echo "$steps.step_one.outputs.action_state"`
- D. `run: echo "${{ action_state }}"`

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#example-of-writing-an-environment-variable-to-github_env

---

## Q039

Is this statement true? `Workflows can be reused, but a reusable workflow cannot call another reusable workflow.`

- A. False
- B. True
  > Reusable workflows can be nested, but there are limitations https://docs.github.com/en/actions/using-workflows/reusing-workflows#limitations

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/reusing-workflows#nesting-reusable-workflows

---

## Q040

In the following example, `workflow A` passes all of its secrets to `workflow B`, by using the inherit keyword. Then `workflow B` calls `workflow C`. Which statement regarding `secrets` is true for that example?

```yaml
jobs:
  workflowA-calls-workflowB:
    uses: octo-org/example-repo/.github/workflows/B.yml@main
    secrets: inherit
```

```yaml
jobs:
  workflowB-calls-workflowC:
    uses: different-org/example-repo/.github/workflows/C.yml@main
```

- A. All secrets available to `workflow A` will be also available to `workflow B`, but not to `workflow C`
- B. All secrets from `octo-org` organization and `octo-org/example-repo` repository will be available to `workflow B`, but not to `workflow C`
  > Not all secrets from `octo-org` organization have to be made available to `octo-org/example-repo`.
- C. All secrets available to `workflow A` will be also available to `workflow B` and `workflow C`
  > `Workflow B` would need to add `secrets: inherit` when calling `workflow C`
- D. Only repository and environment secrets available to `workflow A` will be available to `workflow B`, but not to `workflow C`. Organization scoped secrets cannot be inherited

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/reusing-workflows#passing-secrets-to-nested-workflows

---

## Q041

When should you use `caching`?

- A. When you want to reuse files that don't change often between jobs or workflow runs, such as build dependencies from a package management system.
- B. When you want to reuse files that do change often between jobs or workflow runs, such as build dependencies from a package management system.
- C. When you want to save files produced by a job to view after a workflow run has ended, such as built binaries or build logs.
  > Artifacts should be used for that https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts
- D. When you want to save binaries produced by a build job to use in a subsequent deploy job to deploy a new version of an application
  > Artifacts should be used for that https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows#comparing-artifacts-and-dependency-caching

---

## Q042

When should you use `artifacts`?

- A. Use artifacts to save files produced by a job to view after a workflow run has ended, such as test results or build logs.
- B. Use artifacts to save binaries produced by a build job to use in a subsequent deploy job to deploy a new version of an application
- C. Use artifacts to reuse files that don't change often between jobs or workflow runs, such as build dependencies from a package management system.
  > Caching should be used for that https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows#comparing-artifacts-and-dependency-caching
- D. Use artifacts to create new versions of your application together with release notes, mentions and/or contributors
  > That's a use case for releases, not artifacts

**Answer:** A, B  ·  *multi-select (2 correct)*
**Docs:** https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts#about-workflow-artifacts

---

## Q043

If a workflow runs on a `feature-a` branch, can it restore `caches` created in the default `main` branch?

- A. Yes, all branches can restore caches created on the default branch
- B. Yes, all caches can be accessed by workflows on any branch within the same repository
- C. No, caches can only be restored from the same branch
- D. Yes but only if no files were changed on `feature-a` branch

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows#restrictions-for-accessing-a-cache

---

## Q044

To access an `artifact` that was created in another, previously triggered workflow run you can:

- A. You cannot access `artifacts` that were created in a different workflow run
- B. Use the `actions/download-artifact` action with elevated permissions.
- C. Use the `actions/upload-artifact` action.
- D. Use the `actions/download-artifact` action and make sure the artifact is not expired

**Answer:** B  ·  *single*
**Docs:** https://github.com/actions/download-artifact?tab=readme-ov-file#download-artifacts-from-other-workflow-runs-or-repositories

---

## Q045

What should you use to store coverage reports or screenshots generated during a workflow that runs automated testing for a repository?

- A. Artifacts
- B. Caches
- C. Packages
  > https://docs.github.com/en/packages/learn-github-packages/introduction-to-github-packages
- D. Releases
  > https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts#comparing-artifacts-and-dependency-caching

---

## Q046

You can only upload a single file at a time when using `actions/upload-artifact` action

- A. False
- B. True
- C. Only directories can be uploaded, not individual files

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts#uploading-build-and-test-artifacts

---

## Q047

In job `deploy`, if you want to access binaries (containing your application) that were created in job `build` you should

- A. upload the binaries as artifacts in `build` and download them in `deploy`
- B. upload the binaries as artifacts in `deploy` and download them in `build`
- C. cache the binaries in `build` and read the files from cache in `deploy`
- D. cache the binaries in `deploy` and read the files from cache in `build`

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts#comparing-artifacts-and-dependency-caching

---

## Q048

A job called `job2` is using artifacts created in `job1`. Therefore it's important to make sure `job1` finishes before `job2` starts looking for the artifacts. How should you create that dependency?

- A. create this dependency using the `needs` keyword in `job2`
- B. this dependency is created implicitly when using `actions/download-artifact` to download artifact from `job1`
- C. create this dependency by defining `job2` after `job1` in the workflow's `.yaml` definition
- D. create this dependency using the `concurrency` keyword in `job2`

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idneeds

---

## Q049

Which is true about `Starter Workflows` ?

- A. They allow users to leverage ready-to-use (or requiring minimal changes) workflow templates
- B. GitHub provides and maintains starter workflows for different categories, languages and tooling
- C. Your organization can create custom starter workflows for users in your organization
- D. Starter workflows cannot call reusable workflows
- E. Starter workflows are a paid GitHub feature
- F. Starter workflows are provided ready-to-use and cannot be modified or enhanced
  > https://docs.github.com/en/actions/using-workflows/using-starter-workflows#using-starter-workflows

**Answer:** A, B, C  ·  *multi-select (3 correct)*
**Docs:** https://docs.github.com/en/actions/using-workflows/creating-starter-workflows-for-your-organization

---

## Q050

Secrets and configuration variables can be scoped to:

- A. The entire organization, or selected repositories in an organization
- B. A single repository
- C. An environment in a repository
- D. An environment shared across multiple repositories
  > Environments cannot be shared across repositories
- E. Multiple repositories that do not share an organization/enterprise
- F. A specific workflow in a repository
  > Environment variables can be scoped to a workflow, configuration variables cannot
- G. A specific job in a workflow
  > Environment variables can be scoped to a workflow, configuration variables cannot

**Answer:** A, B, C  ·  *multi-select (3 correct)*
**Docs:** https://docs.github.com/en/actions/using-workflows/sharing-workflows-secrets-and-runners-with-your-organization#sharing-secrets-and-variables-within-an-organization

---

## Q051

What are the three types of Actions?

- A. `Docker container actions`, `JavaScript Actions`, `Composite Actions`
- B. `Python Actions`, `JavaScript Actions`, `Custom Actions`
- C. `Docker container Actions`, `JavaScript Actions`, `Custom Actions`
- D. `Docker container actions`, `Java Actions`, `Composite Actions`

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/creating-actions/about-custom-actions#types-of-actions

---

## Q052

Is this statement true? `Docker container actions are usually slower than JavaScript actions`

> Docker container actions are slower than JavaScript actions

- A. True
- B. False
  > Because of the latency to build and retrieve the container, Docker container actions are slower than JavaScript actions.

**Answer:** A  ·  *single*
**Docs:** — (no link in source)

---

## Q053

When creating a custom GitHub Action you have to store the source code in `.github/workflows` directory

- A. False
- B. True
  > That is true for `workflows`, not for `actions`
- C. Only if the action is reusable
- D. Only for Docker container actions

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/creating-actions/about-custom-actions#choosing-a-location-for-your-action

---

## Q054

When creating custom GitHub Actions - in what file does all the action `metadata` have to be defined?

Metadata examples: name, description, outputs or required inputs

- A. In the `action.yml` or `action.yaml` file in the action repository
- B. In the repository `README` file
  > While it's good practice to do that, it's not a requirement for the action to work
- C. It's edited in GitHub Marketplace UI when published for sharing
- D. In the `action.yml` or `action.yaml` file in the action repository, but it is not required if the action is not meant to be shared and used by the public
  > All actions require the metadata file.

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/creating-actions/metadata-syntax-for-github-actions

---

## Q055

A workflow was initially run on `commit A` and failed. You fixed the workflow with the subsequent `commit B`. When you re-run that workflow it will run with code from which commit?

- A. It will run with code from `commit A`
- B. It will run with code from `commit B`
  > Re-running a workflow uses the same commit SHA and Git ref of the original event that triggered the workflow run.
- C. You cannot re-run workflows in GitHub Actions. You have to trigger a new workflow which will run with latest changes
- D. It will trigger two workflows, one with code from `commit A` and one with code from `commit B`

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/managing-workflow-runs/re-running-workflows-and-jobs#about-re-running-workflows-and-jobs

---

## Q056

How can you require manual approvals by a maintainer if the workflow run is targeting the `production` environment?

- A. Using deployment protection rules
- B. Setting the required reviewers in the `production` workflow
- C. Using branch protection rules
- D. Manual approvals are not supported by GitHub Actions

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments#deployment-protection-rules

---

## Q057

Which is true about environments?

- A. Each job in a workflow can reference a single environment.
- B. Each workflow can reference a single environment.
- C. Each job in a workflow can reference a maximum of two environments.
- D. Each workflow can reference a maximum of two environments.

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/concepts/workflows-and-actions/deployment-environments

---

## Q058

When using GitHub Actions to access resources in one of the cloud providers (such as AWS, Azure or GCP) the safest and recommended way to authenticate is

- A. Using OIDC
- B. Using Vault
- C. Storing access keys in `secrets`
  > Using long lasting access keys is not recommended in case of any security leaks or attacks such as [script injection](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions#understanding-the-risk-of-script-injections)
- D. Storing access keys in `variables`
  > No sensitive values should be stored in `variables`

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect

---

## Q059

Your open-source publicly available repository contains a workflow with a `pull_request` event trigger. How can you require approvals for workflow runs triggered from forks of your repository?

- A. Setup required approvals for fork runs in the repository
- B. Setup deployment protection rules for the repository
  > Deployment protection rules are used for protecting environments
- C. Setup branch protection rules for the repository
- D. The workflow will not trigger for forks if using `pull_request` event. If you want to do that you should use `fork_pull_request` event trigger with `require-approval` flag.

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/managing-workflow-runs/approving-workflow-runs-from-public-forks#about-workflow-runs-from-public-forks

---

## Q060

Which of the following default environment variables contains the name of the person or app that initiated the workflow run?

- A. `GITHUB_USER`
- B. `GITHUB_REPOSITORY`
- C. `GITHUB_WORKFLOW`
- D. `GITHUB_ACTOR`

**Answer:** D  ·  *single*
**Docs:** https://docs.github.com/en/actions/reference/environment-variables#default-environment-variables

---

## Q061

Which of the following are default environment variables in GitHub Actions?

- A. `GITHUB_REPOSITORY`
- B. `GITHUB_WORKFLOW`
- C. `GITHUB_ACTOR`
- D. `GITHUB_USER`
- E. `GITHUB_ORGANIZATION`
- F. `GITHUB_TOKEN`

**Answer:** A, B, C  ·  *multi-select (3 correct)*
**Docs:** https://docs.github.com/en/actions/reference/workflows-and-actions/variables#default-environment-variables

---

## Q062

Your organization defines a secret `SomeSecret`, however when you reference that secret in a workflow using `${{ secrets.SomeSecret }}` it provides a different value than expected. What may be the reason for that?

- A. The secret `SomeSecret` is also declared in repository scope
- B. The secret `SomeSecret` is also declared in enterprise scope
  > If a secret with the same name exists at multiple levels, the secret at the lowest level takes precedence.
- C. `${{ secrets.SomeSecret }}` expression is only used for repository scoped secrets
- D. You need to use the GitHub API to access organization scoped secrets

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#naming-your-secrets

---

## Q063

Which is a correct way to print a debug message?

- A. `echo "::debug::Watch out here!"`
- B. `echo ":debug:Watch out here!"`
- C. `echo "::debug::message=Watch out here!"`
- D. `echo "Watch out here!" >> $GITHUB_DEBUG`

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#example-setting-a-debug-message

---

## Q064

How can organizations which are using GitHub Enterprise Server enable automatic syncing of third party GitHub Actions hosted on GitHub.com to their GitHub Enterprise Server instance?

- A. Using GitHub Connect
  > When enabled, GitHub Connect will be used to automatically establish a secure connection between a GitHub Enterprise Server (GHES) instance and a GitHub Enterprise Cloud (GHEC) account (GHEC is hosted on GitHub.com). The GHEC account serves as a trusted (authenticated) identity GitHub.com uses to authorize the GHES instance to access GitHub.com-hosted actions.   
- B. GitHub Enterprise Server has access to all GitHub.com Actions by default
  > GitHub Actions on GitHub Enterprise Server is designed to work in environments without full internet access. By default, workflows cannot use actions from GitHub.com and GitHub Marketplace.
- C. Using actions-sync tool
  > While actions-sync can be used to sync individual action repositories from GitHub.com to an enterprise, this is a manual approach. See the [documentation](https://docs.github.com/en/enterprise-server@3.17/admin/github-actions/managing-access-to-actions-from-githubcom/manually-syncing-actions-from-githubcom#about-the-actions-sync-tool) for more details.
- D. GitHub Enterprise Server (GHES) cannot use GitHub.com Actions because of its on-premise nature and no internet access.
  > While workflows located on a GHES instance cannot use GitHub.com Actions nor GitHub Marketplace actions by default, this can be rectified via the use of GitHub Connect or actions-sync. 

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/enterprise-server@3.17/admin/github-actions/managing-access-to-actions-from-githubcom/enabling-automatic-access-to-githubcom-actions-using-github-connect

---

## Q065

Where can you find network connectivity logs for a GitHub self-hosted-runner?

- A. In the `_diag` folder directly on the runner machine
- B. On GitHub.com on that specific Runner's page
- C. In the job run logs of a job that ran on that Runner
- D. In the job run logs of a job that ran on that Runner with debug logging enabled

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/monitoring-and-troubleshooting-self-hosted-runners#checking-self-hosted-runner-network-connectivity

---

## Q066

How can you validate that your GitHub self-hosted-runner can access all required GitHub services?

- A. Using a GitHub provided script on the runner machine
- B. By trying to access the runner machine by `ssh` to validate the network connectivity
- C. By using the predefined GitHub Actions workflow `network-connectivity.yml`
- D. GitHub will validate the network connectivity automatically when the runner application is installed on the runner machine

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/monitoring-and-troubleshooting-self-hosted-runners#checking-self-hosted-runner-network-connectivity

---

## Q067

Which is the correct way of triggering a job only if configuration variable `MY_VAR` has the value of `MY_VALUE`?

- A. By creating the following conditional on job level
  ```yaml
  my-job:
    if: ${{ vars.MY_VAR == 'MY_VALUE' }}
  ```
- B. By creating the following conditional on job level
  ```yaml
  my-job:
    if: ${{ vars.MY_VAR }} == 'MY_VALUE'
  ```
  > Incorrect, only `vars.MY_VAR` is evaluated inside `${{ }}`; this yields text like `some_value == 'MY_VALUE'`, and GitHub treats that non-empty string as truthy instead of performing the comparison
  > See https://docs.github.com/en/actions/reference/workflows-and-actions/expressions#literals
- C. It's not possible because configuration variables cannot be used in `if` conditionals
  > That is true for `secrets` but not for configuration variables
- D. It's not possible because configuration variables cannot be used in job level `if` conditionals
  > That is true for `secrets` but not for configuration variables

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/learn-github-actions/contexts#example-usage-of-the-vars-context

---

## Q068

To run a `step` only if the secret `MY_SECRET` has been set, you can:

- A. Set the secret `MY_SECRET` as a job level environment variable, then reference that environment variable to conditionally run that step
  ```yaml
  my-job:
    runs-on: ubuntu-latest
    env:
      my_secret: ${{ secrets.MY_SECRET }}
    steps:
      - if: ${{ env.my_secret != '' }}
  ```
- B. By creating the following conditional on job level
  ```yaml
  my-job:
    runs-on: ubuntu-latest
    if: ${{ secrets.MY_SECRET == '' }}
  ```
  > secrets cannot be directly referenced in if: conditionals
- C. By creating the following conditional on step level
  ```yaml
  my-job:
    runs-on: ubuntu-latest
    steps:
      - if: ${{ secrets.MY_SECRET == '' }}
  ```
  > secrets cannot be directly referenced in if: conditionals
- D. By creating the following conditional on step level
  ```yaml
  my-job:
    runs-on: ubuntu-latest
    steps:
      - if: ${{ secrets.MY_SECRET }}
  ```
  > secrets cannot be directly referenced in if: conditionals

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#example-using-secrets

---

## Q069

How can you use the GitHub API to download workflow run logs?

- A. `GET /repos/{owner}/{repo}/actions/runs/{run_id}/logs`
- B. `POST /repos/{owner}/{repo}/actions/runs/{run_id}/logs`
- C. `HEAD /repos/{owner}/{repo}/actions/runs/{run_id}/logs`
- D. `PUT /repos/{owner}/{repo}/actions/runs/{run_id}/logs`

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/rest/actions/workflow-runs?apiVersion=2022-11-28#download-workflow-run-logs

---

## Q070

How can you use the GitHub API to create or update a repository secret?

- A. `PUT /repos/{owner}/{repo}/actions/secrets/{secret_name}`
- B. `POST /repos/{owner}/{repo}/actions/secrets/{secret_name}`
  > `POST` is not valid for this endpoint. Only `PUT` can create or update repository secrets.
- C. `HEAD /repos/{owner}/{repo}/actions/secrets/{secret_name}`
- D. `GET /repos/{owner}/{repo}/actions/secrets/{secret_name}`

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/rest/actions/secrets?create-or-update-a-repository-secret=&apiVersion=2022-11-28#create-or-update-a-repository-secret

---

## Q071

How can you override an organization-level GitHub Secret `API_KEY` with a different value when working within a repository?

- A. By creating a repository secret with the same name `API_KEY`
- B. By creating a environment secret with the same name `API_KEY`
- C. By creating a enterprise secret with the same name `API_KEY`
- D. By creating a enterprise secret with the name `OVERRIDE_API_KEY`
- E. By creating a repository secret with the name `OVERRIDE_API_KEY`
- F. By creating a environment secret with the name `OVERRIDE_API_KEY`
- G. By creating a repository secret with the name `REPOSITORY_API_KEY`
- H. By creating a environment secret with the name `ENVIRONMENT_API_KEY`

**Answer:** A, B  ·  *multi-select (2 correct)*
**Docs:** https://docs.github.com/en/actions/reference/security/secrets

---

## Q072

What components can be reused within a GitHub Organization?

- A. Secrets
- B. Configuration Variables
- C. Self Hosted Runners
- D. Workflow Templates
- E. Artifacts
  > Artifacts are used to preserve data after a job has completed and/or share that data with another job within the same workflow. 
- F. Cache
  > Cache can be reused across workflows within one repository
- G. Environment Variables
  > Environment variables can be scoped to a step, job or a workflow. They cannot be shared across workflows/repositories or organizations

**Answer:** A, B, C, D  ·  *multi-select (4 correct)*
**Docs:** — (no link in source)

---

## Q073

How many jobs will be executed in the following workflow?

```yaml
jobs:
  matrix-job:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        pet: [cat, dog]
        color: [pink, brown]
        include:
          - color: white
            pet: dog
    steps:
      - run: echo "Hello ${{ matrix.color }} ${{ matrix.pet }}"
```

- A. 5
- B. 4
- C. 6
- D. 7

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs#using-a-matrix-strategy

---

## Q074

Which of the following default environment variables contains the full name (e.g `octocat/hello-world`) of the repository where the workflow is running?

- A. `GITHUB_REPOSITORY`
- B. `GITHUB_REPOSITORY_ID`
- C. `GITHUB_REPOSITORY_OWNER`
- D. `GITHUB_REPOSITORY_OWNER_ID`

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/reference/environment-variables#default-environment-variables

---

## Q075

In a workflow that has multiple jobs, all running on GitHub-hosted runners, is it true that all jobs are guaranteed to run on the same runner machine?

- A. No
- B. Yes
  > Each job runs in a fresh instance of a runner image specified by runs-on
- C. Only if they run in parallel
  > Each job runs in a fresh instance of a runner image specified by runs-on
- D. Only if they use the same `runs-on` label
  > Each job runs in a fresh instance of a runner image specified by runs-on

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-jobs/choosing-the-runner-for-a-job#choosing-github-hosted-runners

---

## Q076

What's the maximum amount of reusable workflows that can be called from a single workflow file?

- A. 20
- B. 5
- C. 1
- D. 10
- E. 50

**Answer:** E  ·  *single*
**Docs:** https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations#limitations-of-reusable-workflows

---

## Q077

What is a self-hosted runner?

- A. A self-hosted runner is a system that you deploy and manage to execute jobs from GitHub Actions on GitHub.com
- B. A self-hosted runner is a system to upload code to a private server
- C. A self-hosted runner is a system to be able to create workloads automatically
- D. A self-hosted runner is a system to manage pull requests from users of the organization

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners

---

## Q078

Which of the following is a correct statement about GitHub Workflows and Actions?

- A. Each action is composed of one or more workflows which is composed of one or more jobs, and each job is composed of one or more steps
- B. Each workflow is composed of one or more actions which is composed of one or more jobs, and each job is composed of one or more steps
- C. Each workflow is composed of one or more jobs which is composed of one or more steps, and each step is an action or a script
- D. Each action is composed of one or more jobs which is composed of one or more steps, and each step is a workflow

**Answer:** C  ·  *single*
**Docs:** https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions

---

## Q079

On which commit and branch do scheduled workflows run in GitHub Actions?

- A. Scheduled workflows run on the specific commit on last modified branch.
  > incorrect, both specific commit and on last modified branch
- B. Scheduled workflows run on the specific commit on the main branch.
  > incorrect, both specific commit and main branch
- C. Scheduled workflows run on the latest commit on the repository default branch.
- D. Scheduled workflows run on the latest commit on the main branch.
  > latest commit is correct but the main branch is not

**Answer:** C  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule

---

## Q080

What is the correct syntax for setting the directory for all `run` commands in a workflow?

- A. set `working-directory` under `defaults.run`
  ```yaml
  defaults:
    run:
      shell: bash
      working-directory: ./scripts
  ```
- B. set `directory` under `defaults.run`
  ```yaml
  defaults:
    run:
      shell: bash
      directory: ./scripts
  ```
- C. set `working-directory` under `job`
  ```yaml
  defaults:
    run:
      shell: bash
  job:
    working-directory: ./scripts
  ```
- D. set `directory` under `job`
  ```yaml
  defaults:
    run:
      shell: bash
  job:
    directory: ./scripts
  ```

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#defaultsrunworking-directory

---

## Q081

How can you reuse a defined workflow in multiple repositories?

- A. By copying the workflow file to each repository
- B. By using workflow templates
- C. By creating a reusable action
- D. By defining the workflow in a central repository

**Answer:** B, D  ·  *multi-select (2 correct)*
**Docs:** https://docs.github.com/en/actions/using-workflows/creating-starter-workflows-for-your-organization

---

## Q082

How can you ensure a job runs only on a specific branch?

- A. By using the branches filter
- B. By using the runs-on filter
- C. By using the jobs filter
- D. By using the branch keyword

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#using-filters

---

## Q083

What does the `needs` keyword do in a GitHub Actions workflow?

- A. Specifies the dependencies of a job
- B. Defines environment variables
- C. Sets up the environment
- D. Triggers a job based on an event

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idneeds

---

## Q084

Which keyword allows you to define environment variables in a GitHub Actions workflow?

- A. env
- B. vars
- C. secrets
- D. config

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idenv

---

## Q085

What is the purpose of the `with` keyword in a GitHub Actions workflow?

- A. To define environment variables
- B. To specify input parameters for an action
- C. To set up dependencies
- D. To trigger another workflow

**Answer:** B  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepswith

---

## Q086

Which of the following GitHub Actions syntax is used to run multiple commands in a single step?

- A. Using && to chain commands
- B. Defining commands in an array
- C. Using a multiline string with |
- D. Separating commands with a semicolon ;

**Answer:** C  ·  *single*
**Docs:** https://docs.github.com/en/enterprise-cloud@latest/actions/using-workflows/workflow-commands-for-github-actions#example-of-a-multiline-string

---

## Q087

How can you cache dependencies to speed up workflow execution?

- A. Using the cache keyword
- B. Using the actions/cache action
- C. By storing them in the repository
- D. By using the store keyword

**Answer:** B  ·  *single*
**Docs:** https://docs.github.com/en/enterprise-cloud@latest/actions/using-workflows/caching-dependencies-to-speed-up-workflows#about-caching-workflow-dependencies

---

## Q088

What does the `matrix` keyword do in a GitHub Actions workflow?

- A. Allows defining multiple job configurations to run in parallel
- B. Sets environment variables for the job
- C. Triggers workflows based on a schedule
- D. Defines secrets for the workflow

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/enterprise-cloud@latest/actions/using-jobs/using-a-matrix-for-your-jobs

---

## Q089

Which of the following can be used to limit the number of concurrent jobs running in a GitHub Actions workflow?

- A. concurrency
- B. limit
- C. max-jobs
- D. parallelism

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/enterprise-cloud@latest/actions/using-jobs/using-concurrency

---

## Q090

What is the default timeout for a GitHub Actions job?

- A. 30 minutes
- B. 60 minutes
- C. 120 minutes
- D. 360 minutes

**Answer:** D  ·  *single*
**Docs:** https://docs.github.com/en/actions/reference/limits#existing-system-limits

---

## Q091

How can you specify the operating system for a job in GitHub Actions?

- A. Using the os keyword
- B. Using the runs-on keyword
- C. Using the platform keyword
- D. Using the env keyword

**Answer:** B  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idruns-on

---

## Q092

In a GitHub Actions workflow, how do you specify a specific version of Node.js to use in a job?

- A. 
  ```yaml
  uses: actions/setup-node@v4
  with:
    node-version: 20
  ```
- B. 
  ```yaml
  uses: actions/node-setup@v4
  with:
    node-version: 20
  ```
- C. 
  ```yaml
  uses: setup-node@v4
  with:
    version: 20
  ```
- D. 
  ```yaml
  uses: setup-node@v4
  with:
    node: 20
  ```

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-nodejs#specifying-the-nodejs-version

---

## Q093

How do you reference a secret stored in GitHub Secrets in a workflow?

- A. ${{ secrets.SECRET_NAME }}
- B. ${{ secret.SECRET_NAME }}
- C. ${{ env.SECRET_NAME }}
- D. ${{ config.SECRET_NAME }}

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#using-secrets-in-a-workflow

---

## Q094

What is the default shell used by GitHub Actions on Windows runners?

- A. bash
- B. sh
- C. powershell
- D. cmd

**Answer:** C  ·  *single*
**Docs:** https://github.blog/changelog/2019-10-17-github-actions-default-shell-on-windows-runners-is-changing-to-powershell/

---

## Q095

Which of the following statements are true about adding a self-hosted runner in GitHub Actions?

- A. You can add a self-hosted runner to a repository
- B. You can add a self-hosted runner to an organization
- C. You can add a self-hosted runner to an enterprise
- D. You can add a self-hosted runner to a workflow
  > You can't add to workflow level
- E. You can add a self-hosted runner to a step
  > You can't add to step level

**Answer:** A, B, C  ·  *multi-select (3 correct)*
**Docs:** https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners#adding-a-self-hosted-runner-to-a-repository

---

## Q096

Select the default environment variable that contains the operating system of the runner executing the job

- A. `RUNNER_OS`
- B. `GITHUB_RUNNER_OS`
- C. `RUNNER_ARCH`
- D. `RUNNER_NAME`

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/learn-github-actions/variables#default-environment-variables

---

## Q097

How does the `actions/cache` action in GitHub Actions handle a cache miss?

- A. by requiring manual intervention to create a new cache
- B. by searching for a cache in other repositories
- C. by automatically creating a new cache if the job is completed successfully
- D. by terminating the workflow if a cache miss occurs

**Answer:** C  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows#managing-caches

---

## Q098

How can you specify the schedule of a GitHub actions workflow to run on weekdays only?

- A. add a condition in the workflow YAML for weekdays
- B. it is not possible in GitHub actions
- C. use the on: schedule: weekdays event trigger
- D. use the on: schedule: cron event trigger

**Answer:** D  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule

---

## Q099

What is the recommended approach for storing secrets larger than 48 KB?

- A. avoid storing large secrets entirely to ensure security
- B. secrets larger than 48 KB cannot be stored
- C. encrypt and store secrets in the repository but keep the decryption passphrase as a secret
- D. store large secrets directly as repository secrets to avoid limitations

**Answer:** C  ·  *single*
**Docs:** https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#limits-for-secrets

---

## Q100

Select status check functions in GitHub Actions

- A. `success()`, `always()`, `cancelled()` and `failure()`
- B. `completed()`, `always()`, `cancelled()` and `failure()`
- C. `status()`, `always()`, `cancelled()` and `failure()`
- D. `state()`, `always()`, `cancelled()` and `failure()`

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/learn-github-actions/expressions#status-check-functions

---

## Q101

How do you ensure that `Upload Failure test report` step is executed only if `Run Tests` step fails?

- A. 
  ```yaml
  - name: Run Tests
    id: run-tests
    run: npm run test
  - name: Upload Failure test report
    if: failure() && steps.run-tests.outcome == 'failure'
    uses: actions/upload-artifact@v3
    with:
      name: test-report
      path: test-reports.html
  ```
  > `failure()` overrides the default `success()` status check so the step can run after a failure, and the outcome check targets the specific step.
- B. 
  ```yaml
  - name: Run Tests
    id: run-tests
    run: npm run test
  - name: Upload Failure test report
    if: always()
    uses: actions/upload-artifact@v3
    with:
      name: test-report
      path: test-reports.html
  ```
  > `always()` works but runs the step even on cancellation, which is broader than needed.
- C. 
  ```yaml
  - name: Run Tests
    id: run-tests
    run: npm run test
  - name: Upload Failure test report
    if: steps.run-tests.outcome == 'failure'
    uses: actions/upload-artifact@v3
    with:
      name: test-report
      path: test-reports.html
  ```
  > Without a status check function like `failure()`, the implicit `success()` is applied, so this step is skipped after a failure even though the outcome check is correct.
- D. 
  ```yaml
  - name: Run Tests
    id: run-tests
    run: npm run test
  - name: Upload Failure test report
    uses: actions/upload-artifact@v3
    with:
      name: test-report
      path: test-reports.html
  ```
  > No `if` condition at all — this step only runs when all previous steps succeed (the default behavior).

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/learn-github-actions/expressions#status-check-functions

---

## Q102

Which context holds information about the event that triggered a workflow run?

- A. `github.event`
- B. `github.repository`
- C. `github.job`
- D. `jobs.<job_id>.result`

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/triggering-a-workflow#using-event-information

---

## Q103

In GitHub Actions, if you define both branches and paths filter, what is the effect on the workflow execution?

- A. the workflow will only run when both `branches` and `paths` are satisfied
- B. the workflow will run when either `branches` or `paths` are satisfied, but will only apply the matching filter
- C. the workflow will run when either `branches` or `paths` are satisfied
- D. the workflow will not run when both `branches` and `paths` are satisfied

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onpull_requestpull_request_targetbranchesbranches-ignore

---

## Q104

What is the recommended practice for treating environment variables in GitHub Actions, regardless of the operating system and shell used?

- A. treat environment variables as case-sensitive
- B. use only uppercase letters for environment variable names
- C. ignore case sensitivity as GitHub Actions handles it automatically
- D. depend on the behavior of the operating system in use

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions#setting-an-environment-variable

---

## Q105

Which of the following statements accurately describes the behavior of workflow jobs referencing an environment's protection rules?

- A. workflow jobs won't start until all the environment's protection rules pass
- B. workflow jobs will start immediately and protection rules are evaluated during execution
- C. workflow jobs will start if at least one protection rule passes
- D. workflow jobs will fail if protection rules are configured

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment

---

## Q106

What is the purpose of the `restore-keys` parameter in `actions/cache` in GitHub Actions?

- A. provide alternative keys to use in case of a cache miss
- B. indicate whether a cache hit occurred
- C. specify the location of the cached files
- D. enable cross-OS cache functionality

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows#managing-caches

---

## Q107

Which variable would you set to `true` in order to enable step debug logging?

- A. `ACTIONS_STEP_DEBUG`
- B. `ACTIONS_JOB_DEBUG`
- C. `ACTIONS_RUNNER_DEBUG`
- D. `ACTIONS_WORKFLOW_DEBUG`

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/enabling-debug-logging

---

## Q108

Which configuration is appropriate for triggering a workflow to run on webhook events related to check_run actions?

- A. 
  ```yaml
  on:
      check_run:
          types: [rerequested, completed]
  ```
- B. 
  ```yaml
  on:
      check_run:
          types: [started]
  ```
- C. 
  ```yaml
  on:
      check_run:
          type: [closed]
  ```
- D. 
  ```yaml
  on:
      check_run:
          filter: [requested]
  ```

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#check_run

---

## Q109

What is the purpose of the `timeout-minutes` keyword in a step?

- A. it limits the execution time for individual step
- B. it defines the time interval for individual commands within a step
- C. it sets the timeout for waiting on external events before proceeding to the next step
- D. it specifies the maximum duration a job is allowed to run

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepstimeout-minutes

---

## Q110

Dave is creating a templated workflow for his organization. Where must Dave store the workflow files and associated metadata files for the templated workflow?

- A. inside a directory named `workflow-templates` within a repository named `.github`
- B. inside a directory named `workflow-templates` within the current repository
- C. inside a directory named `.github/org-templates`
- D. inside a directory named `.github/workflow-templates`

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/creating-starter-workflows-for-your-organization

---

## Q111

Dave wants to be notified when a comment is created on an issue within a GitHub repository. Which event trigger should be used within the workflow configuration?

- A. `issue_comment`
- B. `issues.comment`
- C. `issues`
- D. `comment`

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#issue_comment

---

## Q112

What level of access is required on a GitHub repository in order to delete log files from workflow runs?

- A. write 
- B. read
- C. admin
- D. owner

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/using-workflow-run-logs

---

## Q113

What is true about the following workflow configuration if triggered against the `octo/my-dev-repo` repository?

```yaml
name: deploy-workflow
on: [push]
jobs:
    production-deploy:
        if: github.repository == 'octo/my-prod-repo'
        runs-on: ubuntu-latest
        steps:
            - uses: actions/checkout@v4
            - uses: actions/setup-node@v4
              with:
                  node-version: '14'
            - run: npm install -g bats
```

- A. the `production-deploy` job will be marked as skipped
- B. the `production-deploy` job will error
- C. the `production-deploy` job will execute three steps
- D. the `production-deploy` job will run if the `node-version` is `14`

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-jobs/using-conditions-to-control-job-execution

---

## Q114

How can you access the current values of variables in a matrix within a job in the example below:

```yaml
jobs:
    example_matrix:
        strategy:
            matrix:
                version: [10, 12, 14]
                os: [ubuntu-latest, windows-latest]
```

- A. reference variables through the `matrix` context with syntax like`matrix.version` and `matrix.os`
- B. by using the `matrix.property` syntax
- C. by using the `context` keyword within the job configuration
- D. by accessing the variables directly with the syntax `version` and `os`

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs#using-a-matrix-strategy

---

## Q115

What level of permission is required to re-run the workflows

- A. write 
- B. read
- C. admin
- D. owner

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/managing-workflow-runs/re-running-workflows-and-jobs

---

## Q116

When can you delete workflow runs?

- A. After the workflow run has completed, regardless of its age.
  > At the time of writing, the documentation states that the workflow needs to be 14 days old before it can be deleted.
  > However, that is not the case, and workflow runs can be deleted immediately after completion, regardless of their age.
- B. After the workflow run has completed and at least 30 days have passed.
- C. Workflow runs can be deleted at any time, regardless of their status or age.
- D. Workflow runs cannot be deleted, but they can be archived.

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/how-tos/manage-workflow-runs/delete-a-workflow-run

---

## Q117

Who can bypass configured deployment protection rules to force deployment (by default)

- A. Repository administrators
- B. Anyone with repository write permission
- C. Anyone with repository read permission

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment#allow-administrators-to-bypass-configured-protection-rules

---

## Q118

How can you skip the following workflow run when you commit or create a PR?

```yaml
name: Build
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    name: Extract artifact version
...
```

- A. By including any one of the following keywords in the commit message or in the title of the pull-request
  ```yaml
  [skip ci]
  [ci skip]
  [no ci]
  [skip actions]
  [actions skip]
  ```
- B. Provide `SKIP_WORKFLOW` in the commit message
- C. The above workflow will run in every event of push or pull request in every case

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/managing-workflow-runs/skipping-workflow-runs

---

## Q119

How can you determine if an action is a container action by looking at its action.yml file?

- A. `runs.using` has `docker` as value
- B. `runs.using` has `container` as value
- C. `runs.using` has `Dockerfile` as value
- D. `runs.main` has `container` as value

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/creating-actions/metadata-syntax-for-github-actions#runs-for-docker-container-actions

---

## Q120

What is the correct syntax for specifying a cleanup script in a container action?

- A. 
  ```yaml
  runs:
    using: 'docker'
    image: 'Dockerfile'
    entrypoint: 'entrypoint.sh'
    post-entrypoint: 'cleanup.sh'
  ```
- B. 
  ```yaml
  runs:
    using: 'docker'
    image: 'Dockerfile'
    entrypoint: 'entrypoint.sh'
    post: 'cleanup.sh'
  ```
- C. 
  ```yaml
  runs:
    using: 'docker'
    image: 'Dockerfile'
    entrypoint: 'entrypoint.sh'
    after: 'cleanup.sh'
  ```
- D. 
  ```yaml
  runs:
    using: 'docker'
    image: 'Dockerfile'
    entrypoint: 'entrypoint.sh'
    after-entrypoint: 'cleanup.sh'
  ```
- E. 
  ```yaml
  runs:
    using: 'docker'
    image: 'Dockerfile'
    entrypoint: 'entrypoint.sh'
    cleanup: 'cleanup.sh'
  ```

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/creating-actions/metadata-syntax-for-github-actions#runspost-entrypoint

---

## Q121

What’s true about default variables?

- A. Default environment variables are set by GitHub and not defined in a workflow
- B. Most of the default environment variables have a corresponding context property
- C. Currently, the value of the default CI environment variable can be overwritten, but it's not guaranteed this will always be possible
- D. You can add a new default environment variable adding the prefix “GITHUB_” to it
- E. Default environment variables always have the prefix “GITHUB_”
- F. Default environment variables can be accessed using the env context

**Answer:** A, B, C  ·  *multi-select (3 correct)*
**Docs:** https://docs.github.com/en/actions/reference/workflows-and-actions/variables

---

## Q122

What are the scopes defined for custom variables in a workflow?

- A. The entire workflow, by using `env` at the top level of the workflow file
- B. The contents of a job within a workflow, by using `jobs.<job_id>.env`
- C. A specific step within a job, by using `jobs.<job_id>.steps[*].env`
- D. All the jobs within a workflow, by using `jobs.env`
- E. The entire workflow, by using `custom.env` at the top level of the workflow file
- F. A specific environment in the repository, by using `environment.<environment_id>.env` at the top level of the workflow file

**Answer:** A, B, C  ·  *multi-select (3 correct)*
**Docs:** https://docs.github.com/en/actions/learn-github-actions/variables#defining-environment-variables-for-a-single-workflow

---

## Q123

What must be added to `actions/checkout` if `my-org/my-private-repo` is a private repository differing from the one containing the current workflow?

```yaml
name: deploy-workflow
on: [push]
jobs:
    my-job:
        runs-on: ubuntu-latest
        steps:
          - name: "Checkout GitHub Action"
            uses: actions/checkout@v4
            with:
               repository: my-org/my-private-repo
               path: ./.github/actions/my-org/my-private-repo
```

- A. Create a GitHub secret `MY_ACCESS_TOKEN`
  ```yaml
  with:
      repository: my-org/my-private-repo
      path: ./.github/actions/my-org/my-private-repo
      token: ${{ secrets.MY_ACCESS_TOKEN }}
  ```
- B. Create an input `MY_ACCESS_TOKEN`
  ```yaml
  with:
      repository: my-org/my-private-repo
      path: ./.github/actions/my-org/my-private-repo
      token: ${{ MY_ACCESS_TOKEN }}
  ```
- C. The environmental variable `GITHUB_TOKEN`
  ```yaml
  with:
      repository: my-org/my-private-repo
      path: ./.github/actions/my-org/my-private-repo
      token: $GITHUB_TOKEN
  ```
- D. Leave as is since access tokens will be passed automatically
  ```yaml
  with:
      repository: my-org/my-private-repo
      path: ./.github/actions/my-org/my-private-repo
  ```

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#example-using-an-action-inside-a-different-private-repository-than-the-workflow

---

## Q124

Given the following configuration, how many jobs will GitHub Actions run when this matrix is evaluated?

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    node: [14, 16]
    include:
      - os: macos-latest
        node: 18
      - os: ubuntu-latest
        node: 14
```

- A. 4 jobs
- B. 5 jobs
- C. 6 jobs
- D. 7 jobs
- E. No jobs will run because the syntax is invalid.

**Answer:** B  ·  *single*
**Docs:** https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/running-variations-of-jobs-in-a-workflow#expanding-or-adding-matrix-configurations

---

## Q125

At what levels can environment variables be defined ?

- A. Workflow level
- B. Job level
- C. Step level
- D. Action level

**Answer:** A, B, C  ·  *multi-select (3 correct)*
**Docs:** https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/store-information-in-variables

---

## Q126

How should a dependent job reference the `output1` value produced by a job named `job1` earlier in the same workflow?

- A. `${{needs.job1.outputs.output1}}`
- B. `${{job1.outputs.output1}}`
- C. `${{needs.job1.output1}}`
- D. `${{depends.job1.output1}}`

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/passing-information-between-jobs

---

## Q127

Which workflow command syntax correctly sets an environment variable named 'API_VERSION' with the value '2.1' for subsequent steps in a GitHub Actions job?

- A. `echo "API_VERSION=2.1" >> "$GITHUB_ENV"`
- B. `echo "API_VERSION=2.1" >> "$GITHUB_OUTPUT"`
- C. `export API_VERSION=2.1 >> "$GITHUB_ENV"`
- D. `set-env name=API_VERSION value=2.1`

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-environment-variable

---

## Q128

A workflow is triggered when pull requests are reopened. Why might this be the cause?

- A. `types: [reopened]` is defined under the `pull_request` event. 
- B. Branch protection rules were improperly configured.
  > Branch protection rules do not determine when a workflow fires.
- C. No activity types are defined under the `pull_request` event.
  > If no activity types are explicitly defined, the `pull_request` event will fire off on opened PRs (`opened`), PRs whose source branch has been updated since the PR was opened (`synchronize`), or reopened PRs (`reopened`).
- D. `on: schedule` was configured with `pull_requests: [reopened]`
  > `schedule` is used to fire workflows at certain times, not repository-based activity.

**Answer:** A, C  ·  *multi-select (2 correct)*
**Docs:** https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#pull_request

---

## Q129

`GITHUB_TOKEN` can be used to check out any repository.

- A. True
- B. Only with elevated permissions
- C. False
  > `GITHUB_TOKEN`'s permissions are scoped to the repository that contains the workflow that was triggered. 
  > To check out another repository, other methods token must be used, such as a personal access token (PAT) or installation access token

**Answer:** C  ·  *single*
**Docs:** https://docs.github.com/en/actions/concepts/security/github_token#about-the-github_token

---

## Q130

Which of the following are true regarding workflow-level vs. job-level outputs blocks?

- A. Job-level `outputs` blocks should only be used in caller workflows, not reusable workflows.
  > Reusable workflows can have both job-level and workflow-level `outputs` blocks.
- B. A workflow-level `outputs` block should only be used in reusable workflows, not caller workflows.
  > A "workflow-level" `outputs` block refers to an `outputs` block that is a direct child of `workflow_call` in reusable workflows. In non-reusable workflows, `outputs` blocks should only be present at job-level.
- C. A reusable workflow can have both workflow-level and job-level `outputs` blocks.
  > If setting an output in a reusable workflow and passing that same output to a caller workflow is desired, both a workflow-level and a job-level `outputs` block must be used. 
  > See the documentation for more details https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows#using-outputs-from-a-reusable-workflow
- D. A job-level `outputs` block must have the following structure:
  ```
  outputs:
      <output-name>
          value: ${{ steps.<step-name>.outputs.<output-name> }}
  ```
  > A job-level `outputs` block uses an un-nested structure of `key=value` pairs. See the official documentation (https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#example-defining-outputs-for-a-job) for more details.
- E. A workflow-level `outputs` block must have the following structure:
  ```
  outputs:
      <output-name>
          value: ${{ jobs.<job-name>.outputs.<output-name> }}
  ```
  > A workflow-level `outputs` block must follow the above structure. A `value` key is always required. An optional `description` key can also be used (not seen in the above example). 
  > See the documentation for more details -  https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows#using-outputs-from-a-reusable-workflow

**Answer:** B, C, E  ·  *multi-select (3 correct)*
**Docs:** https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#example-defining-outputs-for-a-job

---

## Q131

Which of the following are true regarding calling reusable workflows versus calling composite actions?

- A. Composite actions are called via referencing the folder that contains their `action.yml` file.
  > As an action, composite actions must contain the brunt of their logic within an `action.yml` file. To call the composite action, point to where its `action.yml` is located (this includes the root. ex. to call a composite action that is located at the root of the same repository as the caller workflow, the syntax `uses: ./` would be used).
- B. Reusable workflows are called via referencing the folder that contains their `action.yml` file.
  > Reusable workflows are regular `.yml` or `.yaml` files that are stored in `.github/workflows`. They do not have an `action.yml` file.
- C. Composite actions must be called as a step within a job
  > Composite actions (as with any other action) are called from within a step of a workflow job--in other words, you do not need a specific workflow job just to caller a composite action. 
- D. Reusable workflows must be called on workflow job level (not from step-level).
  > Steps within a workflow job cannot call a reusable workflow. A reusable workflow must be called by an individual job within the caller workflow. This can result in one or more jobs running in the caller workflow (said jobs can be seen in workflow runs in the Github Actions UI). 
- E. Secrets can be passed to both reusable workflows and calling composite actions via the `uses.secrets` block.
  > Only reusable workflows can be called using the `secrets` block. To pass secrets to a composite action, workarounds must be used (such as passing the secret as an input)
- F. Only reusable workflows can accept inputs.
  > Both reusable workflows and composite inputs can accept inputs. 
- G. Reusable workflows can use a different runner type than the caller workflow, while composite actions cannot. 
  > Reusable workflows have jobs like any other workflow, and those jobs can specify different runner type via the `jobs.runs-on` key. Composite actions inherit the runner environment of their calling workflow job.

**Answer:** A, C, D, G  ·  *multi-select (4 correct)*
**Docs:** https://docs.github.com/en/actions/concepts/workflows-and-actions/reusing-workflow-configurations#key-differences-between-reusable-workflows-and-composite-actions

---

## Q132

Which of the following are true regarding GitHub Enterprise Server (GHES)?

- A. GHES workflows cannot access GitHub.com nor GitHub Marketplace actions by default. 
- B. `actions/actions-sync` is primarily devoted to moving GitHub.com actions to a GHES instance.
  > Syncing Actions from GitHub.com is mainly accomplished either via GitHub Connect or `actions-sync`. The `actions/actions-sync` tool is a [manual way](https://docs.github.com/en/enterprise-server/admin/managing-github-actions-for-your-enterprise/managing-access-to-actions-from-githubcom/manually-syncing-actions-from-githubcom) to perform this process. 
- C. GHES is allowed to use enhanced versions of GitHub-hosted runners.
  > GHES does not have access to GitHub-hosted runners at all. This is seen in the [`actions/actions-sync` documentation](https://docs.github.com/en/enterprise-server/admin/managing-github-actions-for-your-enterprise/managing-access-to-actions-from-githubcom/manually-syncing-actions-from-githubcom)
- D. Using GitHub Connect, users can follow a manual process to access GitHub.com actions. This process must be done once per desired action.
  > GitHub Connect allows automatic access to GitHub.com actions. Users must follow a setup process, but this generally only needs to be done once. See the [GitHub Connect documentation](https://docs.github.com/en/enterprise-server/admin/managing-github-actions-for-your-enterprise/managing-access-to-actions-from-githubcom/enabling-automatic-access-to-githubcom-actions-using-github-connect#enabling-automatic-access-to-public-githubcom-actions) for more details.
- E. GitHub Enterprise Server instances are self-hosted, compared to GitHub Enterprise Cloud (GHEC) which is hosted and managed by GitHub.
  > [GitHub Enterprise Server](https://docs.github.com/en/enterprise-server/admin/overview/about-github-enterprise-server) is a self-hosted version of the GitHub platform. [GitHub Enterprise Cloud](https://docs.github.com/en/enterprise-cloud@latest/admin/overview/about-github-enterprise-cloud) instances are hosted on a dedicated subdomain of GHE.com. All GHE.com subdomains are hosted by GitHub.

**Answer:** A, B, E  ·  *multi-select (3 correct)*
**Docs:** https://docs.github.com/en/enterprise-server/admin/overview/about-github-enterprise-server

---

## Q133

Why use a commit SHA versus a tag to pin an action?

- A. Commit SHAs are more secure
  > Commit SHAs are more secure because they are currently the only way to use an action as an immutable release
- B. Commit SHAs are immutable, whereas tags have the potential to be changed
  > [Tags](https://git-scm.com/book/en/v2/Git-Basics-Tagging) are pointed to specific commits. Their reference can be changed, which is not always obvious. Tag-related vulnerabilities can be mitigated by enabling [immutable releases](https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases), but a commit SHA will always point to the same commit and is immutable.
  > Re-running a workflow uses the same commit SHA and Git ref of the original event that triggered the workflow run.
- C. Commit SHAs are more convenient to use as opposed to tags
  > While more secure, tags are generally easier to use.
- D. Commit SHAs are guaranteed to point to the exact same code every time, tags are not
- E. Commit SHAs are more difficult to trace in an audit, making it difficult for bad actors to determine how an action's code factors in overall processes.
  > Commit SHAs always point to the same commit. When pinning an action to a SHA, the SHA is explicitly referenced, meaning you can find the corresponding commit in the action's repository. These factors make auditing easier.
  > Tags can have their references changed, and this is not always obvious. This can result in confusing scenarios when the tag points to a new commit, because the code referencing the action does not appear to have changed. Thus, in audit scenarios, you will have to figure out what commit the tag was pointing to and what it is currently pointed to.

**Answer:** A, B, D  ·  *multi-select (3 correct)*
**Docs:** https://docs.github.com/en/actions/reference/security/secure-use#using-third-party-actions

---

## Q134

How do you run custom JavaScript scripts directly in a GitHub Actions workflow?

- A. Via the `actions/github-script` action
  > `actions/github-script` allows you to write and leverage inline JavaScript to make API calls and access workflow context. To use `actions/github-script`, you call it like any other action as seen in the [documentation](https://github.com/actions/github-script) 
- B. By enabling the 'Allow custom JavaScript scripts' configuration in the Actions settings of a repository
  > There is no 'Allow custom JavaScript scripts' configuration in the Actions settings of a repository.
- C. By enabling the 'Allow custom JavaScript scripts' configuration in the Actions settings of an organization
  > There is no 'Allow custom JavaScript scripts' configuration in the Actions settings of a repository. While you may have to enable settings like 'Allow actions created by Github' in an organization's Action settings to use official Github Actions, this is not only related to `actions/github-script`. 
- D. Write the contents of a script block to the `GITHUB_SCRIPT` environmental variable
  > `GITHUB_SCRIPT` is not a default Github Actions environmental variable. A list of default environmental variables can be found in the [documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/variables)
- E. In a JavaScript Action, set the `using` key to `'github-script'`
  > JavaScript Actions must have their `using` key set to `node*` where `*` is a supported version of Node.js.  Generally, JavaScript Actions do not have a need for `actions/github-script`.

**Answer:** A  ·  *single*
**Docs:** https://github.com/marketplace/actions/github-script

---

## Q135

You have forked a repository to enhance a workflow that uses a secret to access a third-party application. You trigger the workflow before editing its code to get a baseline result, but find that the workflow fails. Why would this occur?

- A. Forked repositories do not inherit secrets from the original repository  
  > As a security measure, (except for `GITHUB_TOKEN`) secrets are not passed to the runner when a workflow is triggered from a forked repository. This will result in the workflow failing if it references a secret from the original repository.
- B. When inheriting the secret from the original repository, there was an error during the fork that resulted in a malformed, invalid secret
  > Except for `GITHUB_TOKEN`, secrets are not passed to the runner when a workflow is triggered from a forked repository. Thus, no such malformation could occur.
- C. The inherited secret had a size larger than 48 KB
  > Except for `GITHUB_TOKEN`, secrets are not passed to the runner when a workflow is triggered from a forked repository. Thus, size is not a factor to consider.
- D. Forked repositories only inherit repository secrets, so the secret being used in the workflow must have been an organizational or environment secret.
  > Except for `GITHUB_TOKEN`, secrets are not passed to the runner when a workflow is triggered from a forked repository. This applies to all types of secrets (repository, environment, and organizational).

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets?tool=webui#using-secrets-in-a-workflow

---

## Q136

You have a workflow that uses the matrix below. If a job in the matrix fails, how can you ensure other in-progress and queued jobs in the matrix are not cancelled?

```yaml
jobs:
  deploy:
    strategy:
      matrix:
        version: ["1", "1.2", "1.3"]
        os: [ubuntu-latest, windows-latest]
```

- A. Set `jobs.<job_id>.strategy.fail-fast` to `false`
  > `jobs.<job_id>.strategy.fail-fast` is set to `true` by default, meaning if one matrix job fails, other in-progress and queued matrix jobs will be cancelled. You must explicitly set `fail-fast` to `false` to avoid this behavior. 
- B. Nothing needs to be done, since `jobs.<job_id>.strategy.fail-fast` has a default setting of `false`
  > `jobs.<job_id>.strategy.fail-fast` is set to `true` by default.
- C. Set `jobs.<job_id>.strategy.matrix.fail-fast` to `false`
  > This is incorrect, `fail-fast` is at `strategy` level, not `matrix` level. If you set `fail-fast` at `matrix` level, it would function as part of the [job configuration](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/run-job-variations#adding-a-matrix-strategy-to-your-workflow-job) and not effect the cancellation/continuation of other matrix jobs.
- D. Nothing needs to be done, since `jobs.<job_id>.strategy.matrix.fail-fast` has a default setting of `false`
  > This is incorrect, `fail-fast` is at `strategy` level, not `matrix` level. 
- E. There is no way to enforce this behavior, it cannot be worked around.

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_idstrategyfail-fast

---

## Q137

How many jobs will run in the following matrix?

```yaml
jobs:
  test_deploy:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
        version: [1, 2]
        include:
            - comment-color: "green"
            - error-color: "red"
            - os: "ubuntu-latest"
              comment-color: "blue"
            - os: "macos-latest"
              comment-color: "yellow"
```

- A. 5
  > This matrix produces 5 jobs with the following matrix combinations:
  > `os:ubuntu-latest,version:1,comment-color:blue,error-color:red` 
  > `os:ubuntu-latest,version:2,comment-color:blue,error-color:red` 
  > `os:windows-latest,version:1,comment-color:green,error-color:red` 
  > `os:windows-latest,version:2,comment-color:green,error-color:red` 
  > `os:macos-latest,comment-color:yellow` 
  > An `include` key NOT defined in `strategy.matrix` can be added to a job configuration if it does not overwrite the configuration. `include` keys already present in `strategy.matrix` will create a new job if they have a new value. 
- B. 6
- C. 7
- D. 10

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/run-job-variations#expanding-or-adding-matrix-configurations

---

## Q138

You want to create a workflow `Post-Deploy` that performs post-deploy related activity. What event trigger should the `Post-Deploy` workflow use so it runs automatically after a specified workflow is completed?

- A. `workflow_run`
  > `workflow_run` allows you to trigger a workflow once other specified workflows have completed (regardless of success). Note that while this question specifically asks about completed workflows, `workflow_run` can also be oriented to trigger a workflow when other specified workflows have been triggered or started processing on a runner
- B. `workflow_trigger`
  > There is no such event trigger
- C. `workflow_dispatch`
  > `workflow_dispatch` is used for manually triggering a workflow. See [the documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#workflow_dispatch) for more info.
- D. `workflow_call`
  > `workflow_call` is used so a workflow can be called from other workflows or actions. See [the documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#workflow_call) for more info.

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#workflow_run

---

## Q139

In what ways can you enable runner diagnostic logging?

- A. Setting a secret or variable named `ACTIONS_RUNNER_DEBUG` to `true`
  > Note: `ACTIONS_RUNNER_DEBUG` can be set as a secret or variable at organization-level or repository-level.
- B. Re-running a workflow with `Enable debug logging enabled`
- C. By adding a `ACTIONS_RUNNER_DEBUG` top-level folder to the workflow's repository
- D. By adding a `runner-diagnostic-logs` subfolder to the `_diag` directory of the self-hosted runner being used
  > `runner-diagnostic-logs` is the name of the folder Github generates when `ACTIONS_RUNNER_DEBUG` is enabled. To avoid potential confusion, a folder with this name should not be created anywhere else. 
- E. Renaming the `_diag` directory of a self-hosted runner to `runner-diagnostic-logs`
  > Renaming the `_diag` directory should never be done as this can potentially effect logging activities.

**Answer:** A, B  ·  *multi-select (2 correct)*
**Docs:** https://docs.github.com/en/actions/how-tos/monitor-workflows/enable-debug-logging#enabling-runner-diagnostic-logging

---

## Q140

You are writing a reusable workflow which has `branch-name` as an input. How can you conditionally run a step in that workflow if the branch name begins with 'smoke-test'?

- A. Use the built-in `startsWith` method in combination with `jobs.<job_id>.steps[*].if`
  ```yaml
      if: startsWith(inputs.branch-name, 'smoke-test')
  ```
- B. Use the built-in `startsWith` method in combination with `jobs.<job_id>.steps[*].if`
  ```yaml
      if: inputs.branch-name.startsWith('smoke-test')
  ``` 
  > You cannot use method chaining with Github Actions built-in methods. Almost all built-in methods are written in the style of `methodName(arg1,arg2,...)` 
- C. Use the `branches` filter under `workflow_call`
  ```yaml
  on:
    workflow_call:
      branches:
          - 'smoke-test/**'
  ```
  > `branches` filter is not available for `workflow_call` event trigger. Furthermore, workflow event triggers can't be used to control whether a step runs or not
- D. Use shell conditionals in combination with `jobs.<job_id>.steps[*].if`
  ```yaml
      if: [[ "${{inputs.branch-name}}" == "smoke-test"* ]]
  ```
  > Only supported Github Actions contexts and expressions can be used in `jobs.<job_id>.steps[*].if` conditionals. 

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/reference/workflows-and-actions/expressions#startswith

---

## Q141

Why might you use `hashFiles` when utilizing `actions/cache`?

```yaml
  - uses: actions/cache@v5
    with:
      path: ~/.npm
      key: ${{ runner.os }}-build-${{ env.cache-name }}-${{ hashFiles('**/package-lock.json') }}
```

- A. If a cache key contains the dependencies file wrapped in `hashFiles`, the key changes when the dependencies file is updated, which helps keep it up to date.
  > `hashFiles` is a built-in Github function that creates a hash of the specified path. Using it to compose a cache key causes the hash to be regenerated, which in turn updates the cache key. The official [Dependency Caching Reference](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching#example-using-the-cache-action) documentation shows how to use `hashFiles` as part of a cache key.
- B. `hashFiles` is required for compatibility with Windows runners.
- C. When using `hashFiles` as part of a cache key, if there is a cache miss, `hashFiles` gives additional debug info.  
- D. When using `hashFiles` as part of a cache key, an additional step will be generated in the caller workflow. This workflow step prints the value of the SHA-256 hash of the cache key for reference purposes.  
  > Creating a hash of the cache key would not be useful in most situations.

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/reference/workflows-and-actions/expressions#hashfiles

---

## Q142

Which of the following answers is correct regarding installation access tokens?

- A. Installation access tokens are short-lived tokens ideal for automation activities, but require setting up a Github App.
- B. `GITHUB_TOKEN` is a type of installation access token.
  > `GITHUB_TOKEN` is a GitHub App installation access token that is automatically generated for every workflow run. See the  [documentation](https://docs.github.com/en/actions/concepts/security/github_token) for additional details.
- C. The `actions/create-github-app-token` can be called within workflows to create an installation access token available for immediate use. 
- D. The `actions/create-github-app-token` can be called within workflows to create an installation access token, but the installation access token can only be used in future runs of the workflow.
  > Once created, an installation access can be used immediately. See the [official page for this action](https://github.com/actions/create-github-app-token) for additional details.
- E. Installation access tokens cannot be configured to act on behalf of their associated Github App. 
  > Installation access tokens are often configured to act on behalf of their associated Github App. This can aid in auditing automated activity.

**Answer:** A, B, C  ·  *multi-select (3 correct)*
**Docs:** https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app-installation#using-an-installation-access-token-to-authenticate-as-an-app-installation

---

## Q143

Your organization wants to lower the retention period for stored artifacts, citing storage concerns. How can this be done at an organizational level?

- A. By navigating to the organization's Actions settings and editing the value of the "Artifact and log retention" setting
- B. By using self-hosted runners, creating a `.github/retention-policy.yml` file, and specifying the value of the `artifact-retention-period` key 
  > Customizing artifact retention periods is not limited to self-hosted runners.  
- C. This cannot be done at an organizational level. All workflows that utilize `actions/upload-artifact` must use the required `retention-days` input.
  > While the `retention-days` input can be used to customize the retention period for individual artifacts created by a workflow, this is inappropriate if trying to apply an organizational level blanket policy. Furthermore, the `retention-days` input is [optional, not required](https://github.com/actions/upload-artifact#inputs).
- D. This cannot be done: artifacts are strictly stored for 90 days across all systems implementing Github Actions. 
  > The default retention period for artifacts is 90 days. It is possible to change this value in all systems implementing Github Actions. 

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/organizations/managing-organization-settings/configuring-the-retention-period-for-github-actions-artifacts-and-logs-in-your-organization

---

## Q144

How can you change the retention period for artifacts generated by a certain workflow?

- A. By utilizing the `retention-days` input in `actions/upload-artifact` 
- B. By utilizing the `retention-days` input in `actions/download-artifact`
  > `actions/download-artifact` is used to download artifacts. Thus, it has no say in how long an uploaded artifact should be retained for. Additionally, `retention-days` is not an input for this action. See [the documentation](https://github.com/actions/download-artifact#inputs) for more details. 
- C. In the workflow's repository, navigate to the Actions settings and editing the value of the "Artifact and log retention" setting for the workflow listed.
  > While you can edit the ["Artifact and log retention" setting](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#configuring-the-retention-period-for-github-actions-artifacts-and-logs-in-your-repository) in a repository, this applies to all workflows within that repository, not an individual workflow. This setting does not list out individual workflows.
- D. By navigating to the organization's Actions settings and editing the value of the "Artifact and log retention" setting
  > While you can edit the ["Artifact and log retention" setting](https://docs.github.com/en/organizations/managing-organization-settings/configuring-the-retention-period-for-github-actions-artifacts-and-logs-in-your-organization) in an organization, this applies to all workflows within that an organization, not an individual workflow. 

**Answer:** A  ·  *single*
**Docs:** https://github.com/actions/upload-artifact#inputs

---

## Q145

In what ways can you download an artifact?

- A. By using the `actions/download-artifact` action in a workflow 
- B. By downloading artifacts from the Github Actions UI workflow run
  > Using the UI allows you a hands-on approach to downloading artifacts. See the [documentation](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/download-workflow-artifacts) for more details.
- C. By using a specific GitHub API endpoint
  > The Github API has a "Download an artifact" endpoint. See the [documentation](https://docs.github.com/en/rest/actions/artifacts?apiVersion=2026-03-10#download-an-artifact) for more details.
- D. By using the `actions/upload-artifact` action in a workflow
  > `actions/upload-artifact` is used to upload artifacts, not download them 
- E. By remotely accessing self-hosted runners via SSH and accessing the `.github/artifacts` directory
  > Artifacts are generally stored using GitHub infrastructure, not runners. There is one exception: when using GitHub Enterprise Server (GHES), artifacts and other data generated by workflow runs are stored on external blob storage. See the [documentation](https://docs.github.com/en/enterprise-server/admin/managing-github-actions-for-your-enterprise/getting-started-with-github-actions-for-your-enterprise/getting-started-with-github-actions-for-github-enterprise-server#external-storage-requirements) for more details regarding GHES storage. 

**Answer:** A, B, C  ·  *multi-select (3 correct)*
**Docs:** https://github.com/actions/upload-artifact#inputs

---

## Q146

Which statements are true regarding `github.ref` when the workflow is triggered by a `pull_request` event?

- A. In pull requests that have not been merged, `github.ref` refers to the fully-formed ref of the pull request merge branch/tag 
  > For example, if the (opened) pull request's number was #123, `github.ref` would be `refs/pull/123/merge`. For more information about refs, see the official [Git documentation](https://git-scm.com/book/en/Git-Internals-Git-References).
- B. In pull requests that have been merged, `github.ref` refers to the fully-formed ref of the branch that was merged into.
  > For example, if you were merging something into the `main` branch, `github.ref` would be `ref/heads/main` after the pull request was merged.
- C. In pull requests (regardless of merge status), `github.ref` refers to the pull request number 
  > For the `pull_request` event, the value of `github.ref` varies depending on whether the pull request was merged. This value will always be a ref, not the pull request number.
- D. In pull requests (regardless of merge status), `github.ref` is the SHA of the last merge commit on the `GITHUB_REF` branch.
  > `github.sha` is what points to the latest SHA on the merge branch (ex. `refs/pull/PULL_REQUEST_NUMBER/merge`).  Refer to the [events documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#pull_request) for more details (search for `GITHUB_SHA`).
- E. In pull requests that have not been merged, `github.ref` is the fully-formed ref of the pull request title. 
  > Refs are not formed from pull request titles. `github.event.pull_request.title` is what contains the pull request title. See the [documentation](https://docs.github.com/en/webhooks/webhook-events-and-payloads#pull_request) for more details.
- F. In pull requests that have been merged, `github.ref` is the type of fully-formed ref that triggered the workflow run. The value will either be `branch`, `tag`, or `null` (if the ref was not fully-formed).
  > `github.ref_type` is the value of the ref type that triggered the workflow run. It can only contain `branch` or `tag`; `null` is not a valid value. Refer to the document link in this question for more details.

**Answer:** A, B  ·  *multi-select (2 correct)*
**Docs:** https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#github-context

---

## Q147

You have a base-64 encoded secret that you decode in a GitHub Actions workflow. How can you make sure the decoded secret does not show up in the workflow log accidentally?

- A. Using `add-mask` workflow command in jobs where the decoded secret may be utilized.
  > Using `add-mask` will redact values Github Actions does not detect as a secret. This needs to be done once per value, per job that utilizes the decoded secret.
- B. Nothing needs to be done since Github Actions infrastructure automatically redacts decoded secrets.
  > It is not guaranteed that Github Actions will be able to automatically detect and redact transformed secrets per the [documentation](https://docs.github.com/en/actions/reference/security/secure-use#use-secrets-for-sensitive-information).  
- C. Avoiding the usage of print statements that contain the decoded secret, since this is the only way the decoded secret could appear in the workflow log
  > While avoiding print statements that contain decoded secrets is recommended, decoded secrets may appear elsewhere in the workflow log, such as in messages relating to API calls.
- D. Using the built-in `maskSecret` function to redact the decoded secret in instances where it may be utilized.
  > `maskSecret` is not a built-in function provided by Github Actions.

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands#masking-a-value-in-a-log

---

## Q148

Which statement is true regarding `github.ref` when the workflow is triggered by a push event?

- A. In push events, `github.ref` is the fully-formed ref of the branch or tag ref that was pushed. 
  > For more information about refs, see the official [Git documentation](https://git-scm.com/book/en/Git-Internals-Git-References).
- B. In push events, `github.ref` is the message of the commit that triggered the workflow.
  >  `github.event.head_commit.message` is what contains the latest commit message. See the [documentation](https://docs.github.com/en/webhooks/webhook-events-and-payloads#push) for more details.
- C. In push events, `github.ref` is SHA of the commit that triggered the workflow.
  > `github.sha` is what points to the commit SHA. Refer to the [events documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows) and the document link in this question for more details.
- D. In push events, `github.ref` is the description of the commit that triggered the workflow.
- E. In push events, `github.ref` is the type of fully-formed ref that triggered the workflow run. The value will either be `branch`, `tag`, or `null` (if the ref was not fully-formed).
  > `github.ref_type` is the value of the ref type that triggered the workflow run. It can only contain `branch` or `tag`; `null` is not a valid value. See the document link in this question for more details.

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#github-context

---

## Q149

What does writing to `GITHUB_STEP_SUMMARY` do?

```yaml
- name: "Write results of test suite"
  run: |
    echo "The results of the testing suite are:" >> $GITHUB_STEP_SUMMARY
```

- A. Adds this line to the job summary
  > Writing to `GITHUB_STEP_SUMMARY` adds to the job summary, which can be used as a streamlined version of a workflow log.
- B. Adds this line as a subtitle to the step name in the GitHub Actions UI
- C. Adds this line to the built-in artifact `github-steps-summary.md`
- D. Prints this line as a step-level debug message
  > To print a debug message in a step, you must use the `::debug::` syntax. See the "Setting a debug message" section in the linked documentation.

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands#adding-a-job-summary

---

## Q150

Dorothea is troubleshooting a workflow triggered by a push event and is interested in seeing details about the webhook. How can she view the entire payload of the webhook that triggered the workflow?

- A. Printing the contents of the `github.event` object in a step
  > `github.event` will show the full event webhook payload. This payload varies upon the type of event. See the [Webhook events and payloads](https://docs.github.com/en/webhooks/webhook-events-and-payloads) for more details.
- B. Checking the "Show event webhook payload" checkbox under the workflow run options.
- C. Setting a secret or variable named `SHOW_EVENT_PAYLOAD` to `true`
- D. Navigating to the "Webhooks" section of the repository settings 
  > The "Webhooks" section in repository settings will only show details for custom webhooks, not standard event webhooks like `push`. 

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#github-context

---

## Q151

Which should you use when passing information between jobs: job outputs or `GITHUB_ENV`?

- A. Job outputs, because the value of environmental variables set via writing to `GITHUB_ENV` only applies to the current job.
  > While `env` can be set at workflow-level (meaning its variables can be referenced by multiple jobs), this does not mean changing the value of the environmental variable persists beyond the job that changed it.
- B. `GITHUB_ENV`, because job outputs can only be set and referenced within the same job.
- C. Job outputs, because they are simpler to set up
  > Setting up and referencing job outputs is more complicated than utilizing `GITHUB_ENV`. For example, job outputs require setting up an `outputs` block, adding an `id` to a step, and using `needs` to indicate dependencies.
- D. `GITHUB_ENV`, because using it to set environmental variables puts significantly less strain on the runner, reducing workflow runtime.

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-variables#passing-values-between-steps-and-jobs-in-a-workflow

---

## Q152

Fill in the blank: When using self-hosted runners, the tool cache ___

- A. starts off empty and must be populated in order to save tools between runs
  > Tool caches allow you to to cache different versions of tools, which enables faster self-hosted runner activity. Without tool caches, self-hosted runners that use `actions/setup-*` will take longer to execute.
- B. starts off the same as GitHub-hosted runners in that it is pre-populated with certain tools
  > While GitHub-hosted runners do come with certain tools pre-installed, this is not the case for self-hosted runners
- C. starts with the same tools GitHub-hosted runners do, as well as a selected assortment of custom tools to enhance self-hosted runner management
- D. cannot be populated

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/enterprise-server/admin/managing-github-actions-for-your-enterprise/managing-access-to-actions-from-githubcom/setting-up-the-tool-cache-on-self-hosted-runners-without-internet-access

---

## Q153

Which of the following events can trigger a workflow that has not been merged to the default branch?

- A. `push`
- B. `pull_request`
  > To trigger a workflow via `pull_request` the branch containing the workflow must be the target branch of the pull request.
- C. `repository_dispatch`
- D. `star`
- E. `issues`
- F. `issue_comment`

**Answer:** A, B  ·  *multi-select (2 correct)*
**Docs:** https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#pull_request

---

## Q154

When would you build a Docker container action to share in the GitHub Actions marketplace?

- A. Docker container actions ensure a consistent runtime environment and specific dependencies without users needing to handle these aspects themselves
- B. Docker container actions are an out-of-the-box, low-overhead action
  > Docker container actions are not considered to be low-overhead as they require the use of an image (pre-built or specified by the `Dockerfile`), an entrypoint script, and possibly pre and post-entrypoint logic. 
- C. Docker container actions have fast startup speed on Windows and macOS runners
  > Docker containers can only be executed on Linux OS runners (`ubuntu-latest` for GitHub-hosted runners). They also take longer compared to JavaScript and composite actions.
- D. Docker container actions are a bundle of steps within other workflows that run within the context of the calling workflow/action
  > A "reusable bundle of steps" describes a composite action, not a Docker container action
- E. Docker container actions allow you to utilize Docker without requiring an `action.yml` file
  > All actions, regardless of type, must use an `action.yml` file

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/concepts/workflows-and-actions/custom-actions#docker-container-actions

---

## Q155

Marianne has a feature branch that contains her new workflow file, which is set to be triggered at 2 AM every day, using the syntax seen below. However, the next day, the workflow does not trigger. Why might this be the case?

```yaml
on:
    schedule:
        cron:
            "0 2 * * *"
```

- A. The workflow file must exist on the default branch in order to be triggered by the `schedule` event
- B. The `cron` syntax is not scheduled correctly
  > `"0 2 * * *"` in CRON syntax means "fire off every day at 2 AM." Even if the schedule was set up incorrectly, the workflow would still not be triggered since it is not present on the default branch.
- C. `schedule` cannot be the only event in the workflow. It must be paired with a repository-based event, such as `push`
- D. The `@daily` syntax was not used
  > Non-standard CRON syntax like `@daily` is not supported by GitHub Actions. 
- E. The private repository containing the workflow has not had any repository activity in greater than 60 days, automatically disabling the workflow.
  >  This automatic disabling activity only occurs in public repositories, not private repositories.

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule

---

## Q156

In what ways can you delete workflow artifacts?

- A. By using the Github Actions UI to navigate to a workflow run and delete the artifacts individually
- B. By using the Github Actions UI to delete the workflow run that generated the artifacts
  > Deleting a workflow run also deletes the artifacts associated with the run. 
- C. By using a specific GitHub API endpoint
  > The Github API has a "Delete an artifact" endpoint. See the [documentation](https://docs.github.com/en/rest/actions/artifacts?apiVersion=2026-03-10#delete-an-artifact) for more details.
- D. By using the `actions/delete-artifact` action in a workflow 
- E. By remotely accessing self-hosted runners via SSH, navigating to the `.github/artifacts` directory, and deleting the selected artifacts
  > Artifacts are generally stored using GitHub infrastructure, not runners. 
- F. By setting the artifact retention period to 0 days
  > Artifact retention periods cannot be set to 0 days. See the [documentation](https://docs.github.com/en/organizations/managing-organization-settings/configuring-the-retention-period-for-github-actions-artifacts-and-logs-in-your-organization) for more information.

**Answer:** A, B, C  ·  *multi-select (3 correct)*
**Docs:** https://docs.github.com/en/actions/how-tos/manage-workflow-runs/remove-workflow-artifacts

---

## Q158

Petra is building a workflow whose sole job is named `post-merge`. How can she set up the job to be triggered upon a merged pull request?

- A.  Specify the `pull_request` activity type as `closed`, and use a job-level conditional to check if `github.event.pull_request.merged` is true
  ```yaml
  on:
      pull_request:
          types: [closed]
  jobs:
      post-merge:
          if: github.event.pull_request.merged == true
  ``` 
  > To trigger a workflow job when a pull request is merged, you must specify both the activity type of the pull request in `on:` and set a job-level conditional.
- B.  Specify the `pull_request` activity type as `merged`, and use a job-level conditional to check if `github.event.pull_request.merged` is true
  ```yaml
  on:
      pull_request:
          types: [merged]
  jobs:
      post-merge:
          if: github.event.pull_request.merged == true
  ``` 
  > The `pull_request` event does not have a `merged` activity type. See the "pull_request" section of the linked documentation to see the valid activity types for `pull_request`
- C.  Specify the `pull_request` activity type as `merged` (no need for a job-level conditional)
  ```yaml
  on:
      pull_request:
          types: [merged]
  jobs:
      post-merge:
  ``` 
  > The `pull_request` event does not have a `merged` activity type.
- D. Specify the the `pull_request` activity type as `closed` (no need for a job-level conditional)
  ```yaml
  on:
      pull_request:
          types: [closed]
  jobs:
      post-merge:
  ``` 
  > Pull requests can be closed without being merged. If you do not use a corresponding job-level conditional that checks whether the PR was merged, then the job will fire any time a PR is closed, not just when merging occurred.
- E.  Specify the the `pull_request` activity type as `closed` and use a job-level conditional to check if `github.ref` is equal to the merge branch of the pull request.
  ```yaml
  on:
      pull_request:
          types: [closed]
  jobs:
      post-merge: 
          if: ${{ github.ref == github.event.pull_request.base.ref }}
  ``` 
  > After after a pull request has been merged, `github.ref` will be the *fully-formed ref* of the merge branch (ex. `refs/heads/main`), not simply the merge branch (ex. `main`). 

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#running-your-pull_request-workflow-when-a-pull-request-merges

---

## Q159

Which of the following are true when comparing the pull_request and pull_request_target events?

- A. The `pull_request` event runs within the context of the merge commit, while `pull_request_target` runs in the context of the default branch of the base repository.
  > For more information about merge commits, see the GitHub [documentation](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges). 
- B. Workflows will not run on `pull_request` activity if there is a merge conflict
- C. Both `pull_request` and `pull_request_target` events have default activity types of `opened`, `synchronize`, and `reopened`.
- D. `pull_request` should be used with caution, since PRs from forks will allow the workflow to access all secrets within the repository due to being associated with the default branch.
  > This is true for `pull_request_target`; `pull_request` is not associated with the default branch and thus when triggered by forked PRs, the workflow will have limited access to secrets. See the documentation linked above, specifically the "pull_request_target" section for more information.
- E. Workflows will not run on `pull_request_target` activity if there is a merge conflict
- F. The `pull_request_target` event should be used when you want to run code contained in a PR's changed files, to do things like performing CI checks or running test suites.
  >  `pull_request_target` runs in the context of the default branch of the repository, which can lead to untrusted code being checked out and executed by activity like CI checks or test suites. See the [documentation](https://docs.github.com/en/enterprise-cloud@latest/actions/reference/security/secure-use#mitigating-the-risks-of-untrusted-code-checkout) for more information. 

**Answer:** A, B, C  ·  *multi-select (3 correct)*
**Docs:** https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#pull_request

---

## Q160

Why should you use OIDC when connecting a workflow to cloud providers?

- A. OIDC prevents you from having to keep cloud credentials as long-lived GitHub secrets 
- B. OIDC involves the generation and use of short-lived tokens, which is more secure
- C. Cloud providers require the use of OIDC.
  > OIDC is optional and recommended, but not strictly required.
- D. Using OIDC allows you to circumvent setting up trust policies with cloud providers
  > You must set up trust policies with the cloud provider in order to use OIDC
- E. OIDC generates JSON web tokens (JWTs) that can be used across workflow jobs
  > OIDC infrastructure involves creating JWTs that are unique for each workflow job
- F. Using OIDC within a workflow will automatically save that workflow's logs in cloud storage
  > OIDC is concerned with security when connecting to cloud providers, not storage. Thus, it is not involved in saving workflow logs anywhere.    

**Answer:** A, B  ·  *multi-select (2 correct)*
**Docs:** https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect

---

## Q161

How do workflows integrate with OIDC after a trust relationship has been established?

- A. A workflow job requests an OIDC token from GitHub's OIDC provider. The OIDC token is then validated by the cloud provider, which then provides a cloud-access token so the workflow can access cloud resources.
- B. A workflow job requests an cloud access token from GitHub's cloud access provider. The token is then validated by the cloud provider, which then provides a OIDC token so the workflow can access cloud resources.
  > OIDC tokens are requested first, then a cloud access token is generated. OIDC tokens cannot access cloud resources.
- C. The `on: OIDC_request` event trigger requests a cloud access token from GitHub's cloud access provider. The token is then validated by the cloud provider, which allows the workflow access to cloud resources.
  > There is no `on: OIDC_request` event trigger.
- D. The `on: OIDC_request` event trigger requests an OIDC token from GitHub's OIDC provider. The token is then validated by the cloud provider, which allows the workflow access to cloud resources.
  > There is no `on: OIDC_request` event trigger.
- E. After adding a workflow to the "OIDC-allowed workflows" list in the repository settings, workflows will automatically create OIDC and cloud access tokens on their own behalf. These tokens can then be used immediately in the workflow to interface with cloud providers
  > There is no "OIDC-allowed workflows" setting.  

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/concepts/security/openid-connect#how-oidc-integrates-with-github-actions

---

## Q162

Mercedes wants to publish a Docker container action she has created to the GitHub Actions Marketplace. What files does she need at a minimum to do so?

- A. `action.yml`
  > An `action.yml` file is required for an action to be published to the Marketplace, regardless of type.
- B. A `Dockerfile`, if the image is built as part of the action during the workflow run
  > Docker container actions only require a `Dockerfile` if the image has to be created from scratch and cannot be pulled from an image registry. The value of `runs.image` in `action.yml` must be the path to `Dockerfile`
- C. A `Dockerfile`, if the image is to be referenced from an image registry
  > When referencing an image in an image registry, no `Dockerfile` is needed. The value of the `runs.image` key in  `action.yml` must be prefixed with `docker://` followed by the image name.  See the "runs" and "runs.image" sections in the [documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax#runsimage) for more information. 
- D. `README.md`
  > While a `README.md` file is recommended by GitHub for Actions being published to the Marketplace, it is not a strict requirement.
- E. `.dockerignore`
- F. `CONTRIBUTING.md`

**Answer:** A, B  ·  *multi-select (2 correct)*
**Docs:** https://docs.github.com/en/actions/how-tos/create-and-publish-actions/publish-in-github-marketplace

---

## Q163

Annette needs to write a workflow to publish a custom `npm` package that only members in her private organization will use. What should her workflow include?

- A. Logic to publish to GitHub Packages
  > GitHub Packages is a package registry integrated with GitHub, making it easier to use if your needs are GitHub specific (such as with actions/workflows). GitHub Packages includes the ability to host packages privately.
- B. A token with `write:packages` permissions 
  > Personal access tokens are supported across all GitHub Packages registries. Certain registries also support the use of `GITHUB_TOKEN`. See the [documentation](https://docs.github.com/en/packages/learn-github-packages/about-permissions-for-github-packages#about-scopes-and-permissions-for-package-registries) for more information.  
- C. Communication logic with the corresponding GitHub Packages registry `https://npm.pkg.github.com`
  > Workflows involved with GitHub Packages often involve communication with the corresponding GitHub-hosted package registry, whose URL has the syntax of `https://<package-type>.pkg.github.com`. For an example, see the [npm registry documentation](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-npm-registry).
- D. An `on:registry_package` event with no activity types specified
  > The `on:registry_package` is related to packages, but a workflow does not need this event to publish a package.
- E. A token with `admin:packages` permissions
  > `admin:packages` permissions are only needed when you need to delete a package hosted by GitHub Packages. The principle of least permissions should be followed; in this case, only `write` permissions are needed
- F. An `on:registry_package` event with `types:[published]` 
  > The `on:registry_package` event can be configured to trigger a workflow when a package is published, but a workflow does not need this event to publish a package.

**Answer:** A, B, C  ·  *multi-select (3 correct)*
**Docs:** https://docs.github.com/en/packages/learn-github-packages/publishing-a-package

---

## Q164

At what levels can `if:` be used in workflows?

- A. Job-level
- B. Step-level
- C. Workflow-level
  > `if:` is not present at workflow-level. To conditionally trigger an entire workflow, other methods must be used such as specifying activity types.
- D. Environment-level
- E. Organization-level

**Answer:** A, B  ·  *multi-select (2 correct)*
**Docs:** https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax

---

## Q165

How does `repository_dispatch` enable systems outside of GitHub to trigger a workflow?

- A. The external system makes a POST request to the GitHub API to create a repository dispatch event.
- B. The workflow is triggered by the creation of a repository dispatch event 
  > The result of the "Create a repository dispatch event" is a new `repository_dispatch` event (webhook), which `on.repository_dispatch` listens for. 
- C. The `on.repository_dispatch.types` workflow key corresponds to the `event_type` parameter in the request payload, restricting the workflow to only trigger on relevant external events 
  > `on.repository_dispatch.types` lets you define custom activity types. See the [documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#repository_dispatch) for examples of how `on.repository_dispatch.types` and `event_type` relate to each other.
- D. The external system makes a PUT request to the GitHub API to create a repository dispatch event
  > The proper HTTP method for the "Create a repository dispatch event" is POST.
- E. The workflow is triggered by a POST request to the workflow using the following endpoint `/repos/OWNER/REPO/actions/workflows/<WORKFLOW_ID>/dispatches` 
  > This endpoint corresponds to creating a workflow dispatch event, not a repository dispatch event. Furthermore, the GitHub API is what Actions-related requests should be made to--API calls cannot be made the workflow itself.
- F. The `on.repository_dispatch.event_types` workflow key corresponds to the `event_type` parameter in the request payload, restricting the workflow to only trigger on relevant external events
  > There is no `on.repository_dispatch.event_types` key. The `on.repository_dispatch.types` is used, keeping in line with how other events use `on.<event_name>.types` to filter based on activity.

**Answer:** A, B, C  ·  *multi-select (3 correct)*
**Docs:** https://docs.github.com/en/rest/repos/repos?apiVersion=2026-03-10#create-a-repository-dispatch-event

---

## Q166

JavaScript actions and `actions/github-script` both use JavaScript. Why should you use `actions/github-script` versus creating your own JavaScript action?

- A. `actions/github-script` should be used for short inline scripts
- B. `actions/github-script` should be used when you want to use a pre-authenticated client to interact with the GitHub API.
- C. JavaScript actions should be used when you want a custom reusable action to be used across repositories 
- D. JavaScript actions should be used for short inline scripts
- E. `actions/github-script` should be used when you need to utilize a fine-tuned Node.js environment with several specific dependencies
  > While you can install modules for `actions/github-script` to use before calling it, if several dependencies are needed, this results in several steps in the workflow. `actions/github-script` also does not allow you to change the Node.js version; you are bound to the one it defines.
- F. JavaScript actions should be used when you want a low-overhead solution to making GitHub API calls.
  > JavaScript actions are not low-overhead; they require making an `action.yml` file, which in turn must be stored in its own folder or even its own repository, depending on the approach. `actions/github-script` comes with a pre-authenticated client that makes it easy to make GitHub API calls using a JavaScript-based approach.

**Answer:** A, B, C  ·  *multi-select (3 correct)*
**Docs:** https://github.com/actions/github-script

---

## Q167

Hilda needs access to an artifact generated by a recent workflow run, but the workflow file itself has since been deleted. Will she still be able to recover the artifact?

- A. Yes, because deleting a workflow does not automatically delete its runs and generated artifacts
  > Workflow runs and their generated artifacts are not automatically deleted when the corresponding workflow is. You must delete the run itself to delete the artifacts.
- B. No, because deleting a workflow automatically deletes its runs and generated artifacts
- C. Yes, but only if she has administrator privileges
- D. No, because while workflow runs will remain after a workflow is deleted, generated artifacts become corrupted

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/how-tos/manage-workflow-runs/remove-workflow-artifacts#artifacts-from-deleted-workflow-runs

---

## Q168

Which keys are required when making an `action.yml` file?

- A. `name`
- B. `description`
- C. `runs`
- D. `author`
- E. `inputs`
- F. `outputs`

**Answer:** A, B, C  ·  *multi-select (3 correct)*
**Docs:** https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax

---

## Q169

Manuela is setting up self-hosted runners for her organization, which has heavily restricted communication with IP addresses. How can she ensure the self-hosted runners can communicate with GitHub?

- A. Adding the self-hosted runners' IP address(es) to the organization's IP allow list
  > Self-hosted runners communicate with GitHub to perform various activity, as seen in the [documentation](https://docs.github.com/en/enterprise-cloud@latest/actions/reference/runners/self-hosted-runners#communication). To allow this communication, you must add the self-hosted runner's IP address(es) to the IP allow list
- B. Adding the self-hosted runners' operating system to the organization's operating system allow list
- C. Adding the `.ip-exception` file to the top-level of the self-hosted runner's directory structure
- D. Switch to GitHub-hosted standard runners, since self-hosted runners will be blocked if IP allow lists are enabled
- E. Selecting the 'Allow access from self-hosted runners' checkbox in the organization's IP allow list settings

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#using-github-actions-with-an-ip-allow-list

---

## Q170

Observe the values in `runs-on` key as seen in the below workflow job. Which is true regarding how the  the job will run?

```yaml
jobs:
    fire_emblem_deploy:
        name: "Deploy the 'Fire Emblem' application"
        runs-on: [self-hosted,nes,linux]
```

- A. The job will run on a self-hosted runner that has all the labels applied.
- B. The job will run on a self-hosted runner that has any of the labels applied.
  > Runner labels apply cumulatively; a workflow will not run on a runner that only has some of the labels. All of them are needed.
- C. The job will still be able to run on GitHub-hosted runners, since they can have custom labels applied to them
  > GitHub-hosted runners cannot have custom labels applied to them. They must be referenced with the [predefined labels](https://docs.github.com/en/enterprise-cloud@latest/actions/how-tos/write-workflows/choose-where-workflows-run/choose-the-runner-for-a-job#standard-github-hosted-runners-for-public-repositories) they have been assigned.
- D. The job will run on a runner (self-hosted or GitHub-hosted, whichever is first available) with the name `self-hosted,nes,linux`
  > `runs-on` points to runner labels, not names.

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/use-in-a-workflow#using-custom-labels-to-route-jobs

---

## Q171

Why would you re-run a workflow versus generating a new workflow run?

- A. Re-running a workflow lets you re-run failed workflow jobs, as opposed to generating a new run which will run all jobs.
- B. Re-running a workflow means the workflow jobs run in the same context of the commit SHA and git ref of the original event that triggered the job
- C. Re-running a workflow allows you to enable extra debug logging for the selected job(s).
- D. Re-running a workflow ensures `GITHUB_TRIGGERING_ACTOR` remains unchanged, so it is unambiguous as to who originally triggered the workflow
  > Per the [documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#github-context), the value of `GITHUB_TRIGGERING_ACTOR` is updated based on who re-ran the workflow.  
- E. Re-running a workflow ensures `GITHUB_ACTOR` is updated, so it is unambiguous as to who re-ran the workflow
  > Per the [documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#github-context), the value of `GITHUB_ACTOR` is who originally triggered the workflow; it does not change upon re-running a workflow.
- F. Re-running a workflow overwrites the failing job runs, making runs appear more straightforward.
  > Failing job runs remain when a job is re-run. Using the UI, it is easy to toggle between the original job run and subsequent re-runs.  

**Answer:** A, B, C  ·  *multi-select (3 correct)*
**Docs:** https://docs.github.com/en/actions/how-tos/manage-workflow-runs/re-run-workflows-and-jobs

---

## Q172

Ingrid's organization has a subset of self-hosted Linux runners that should only be used by certain repositories. What is the best approach for her to enforce this behavior?

- A. Create a new runner group, add the runners to the group, then select which repositories are allowed access to the group in the group settings.
- B. Create a new runner label, add the labels to the runners, then select which repositories are allowed access to the label in the label settings.
- C. Create a new runner label, add the labels to the runners, then make sure all workflows in the repositories have that label included in their `runs-on` field.
  > Labels do not limit access to runners. Simply adding a label will not work; adding labels to `runs-on` can potentially effect the corresponding workflow from finding a runner to run on.
- D. Create a new runner group, select "Linux" as the OS, and use glob patterns to define which repositories are allowed access in the group settings.  

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/manage-access#changing-which-repositories-can-access-a-runner-group

---

## Q173

An organization has several repositories that share a specialized Node.js environment hosted on a private network. The organization's next objective involves the setup of node-locking software within that network. Which of the following would best suit the organization's needs when it comes to executing workflows?

- A. Self-hosted runners set up at the organization-level
- B. One self-hosted runner per repository, set up at the repository level
  > This would be duplicative and complex to manage. Repositories can reference the same organization-level runner, which is the correct approach in this situation.
- C. GitHub-hosted runners, with all workflows utilizing `actions/setup-node`
  > GitHub-hosted runners are [ephemeral](https://docs.github.com/en/actions/concepts/runners/github-hosted-runners#overview-of-github-hosted-runners), meaning that a new instance of the runner is set up per workflow run. This would not work well with node-locking software, which only allows the software to run on a specified device/VM. Additionally, while GitHub-hosted runners can be set up to access private networks, this is not out-of-the-box functionality.
- D. GitHub-hosted runners set up at the organization-level
  > GitHub-hosted runners cannot be set up in this way.
- E. GitHub-hosted runners, using `runs-on: [node<version>]` (`<version>` being the desired Node version) in all workflows.
  > `[node<version>]` does not point to any GitHub-hosted runner.

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/concepts/runners/self-hosted-runners

---

## Q174

The following workflow that calls a reusable workflows in one of its jobs. The reusable workflow has `permissions` defined at workflow level as seen below. What will be the result of calling the reusable workflow?

```yaml
# caller workflow
on:
    issues:
        types: [opened]
    
    permissions:
        contents: write

    jobs:
        issue_creator:
            permissions:
                contents: read
            uses: ./.github/workflows/issue-creator.yml

# reusable workflow (issue-creator.yml)
on:
    workflow_call:

    permissions:
        contents: write

    jobs:
        create_issue:
            runs-on: ubuntu-latest
            steps: 
                env: GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}    
                - run: gh issue create --title "Issue report" --body "Hello!" --repo $GITHUB_REPOSITORY

```

- A. The reusable workflow will return an error, since the job that called it only has `contents:read` permissions
  > In this scenario the caller workflow is triggered, but its job will not fire. Instead an error will be generated saying the caller workflow file is not valid since the reusable workflow is requesting `contents: write`, but is only allowed `contents: read`.
- B. The reusable workflow will create an issue in the repository titled `"Issue Report"`
  > This would occur if the `issue_creator` job had `contents:write` permissions, which would be the reusable workflow would inherit
- C. The reusable workflow will not be called, since reusable workflows must be in a subfolder of `.github/workflows`
  > All workflows must be located in the `.github/workflows` directory. 
- D. Both the caller and reusable workflow will not get called, because `issues` is not an available trigger for GitHub Actions. 
  > `issues` is a standard event trigger, as seen in the [documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#issues)

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows

---

## Q175

Catherine writes the following workflow job below. What will be the result of the job?

```yaml
jobs:
  doc-generate:
    name: "Generate Scaffold Doc"
    runs-on: ubuntu-latest
    steps:
      
      - name: Setup Python 3.13 
        uses: actions/setup-python@v6
        with:
          python-version: '3.13' 

      - name: Grant Execute Permission to Scaffolding Python Script
        run: chmod +x ./scripts/scaffold-doc.py

      - name: Execute Scaffolding Python Script
        run: python ./scripts/scaffold-doc.py
```

- A. The Python script will not run, because `actions/checkout` is not included in the workflow.
  > `actions/checkout` is necessary to check out the repository's code into the runner's file system. If it is not used, the Python script will not be found and thus not executed.
- B. The Python script will run successfully, because the `chmod` command grants execute permissions to the script.
  > This would be true if `actions/checkout` was used.
- C. The Python script will not run, because `runs-on` does not have a value of `python`.
- D. The Python script will not run, because `actions/python-setup` is not the correct action for setting up Python.
  > Most official actions that set up programming languages use the structure `actions/setup-<language>`. 

**Answer:** A  ·  *single*
**Docs:** https://github.com/actions/checkout

---

## Q176

Judith has a workflow that should be triggered every time a commit is made to the repository. The repository is not always that active, so Judith desires the workflow to programmatically run once a week as a failsafe. What combination of events should she use to enforce this behavior?

- A. `push` and `schedule`
- B. `pull_request` (with `types:[closed]`) and `schedule`
  > Pull requests can closed without being merged, and commits can be made to a repository without a pull request.
- C. `push` and `workflow_dispatch`
  > The word "programmatically" in the question means that the workflow should be triggered in a non-manual way. Having users manually have to trigger a workflow every week is not reliable--it can and should be automated via `schedule` 
- D. `push` and `weekly`
  > `weekly` is not a valid event. Use `schedule` with `cron` syntax to set the workflow to run weekly.
- E. This is not possible: `schedule` cannot be combined with other events

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows

---

## Q177

Your workflow must fire off at 12:00 AM every Monday and Friday. Which of the following snippets correlates to this behavior?

- A. 
  ```yaml
  on:
    schedule:
      - cron: '0 0 * * 1,5'
  ```
  > `cron` syntax has its items defined in order of increasing magnitude, with the exception that the "day(s) of the week" item being the last item. See the [documentation](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/crontab.html#tag_20_25_07) for more information and examples.
- B. 
  ```yaml
  on:
    schedule:
      - cron: '0 12 * * Mon,Fri'
  ```
  > The "day(s) of the week" item must be in numerical format. Additionally, the "minute" and "hour" items point to 12:00 PM, not 12:00 AM.
- C. 
  ```yaml
  on:
    workflow_schedule:
      - cron: '0 0 * * 1,5'
  ```
- D. 
  ```yaml
  on:
    workflow_schedule:
      - cron: '1,5 * * 0 0'
  ```
- E. 
  ```yaml
  on:
    workflow_call:
      - days: [Mon,Fri]
      - times: [00]
  ```

**Answer:** A  ·  *single*
**Docs:** https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule

---

## Q178

You need to ensure that your `prod` environment requires manual approvals before deploys can proceed. Out of the following options, which are true regarding how this is set up?

- A. If you list required reviewers, only one of them needs to approve to continue with the deployment.
- B. You can prevent self-reviews in the event the person who wants to deploy is also a required reviewer.
- C. If you list required reviewers, all of them need to approve to continue with the deployment.
  > Surprisingly only 1 of the required reviewers needs to approve the workflow job. To enforce this behavior, you would need to create a custom deployment protection rule via a GitHub App.
- D. You cannot prevent self-reviews, but you can set up alerts to see who triggered the deployment.
- E. Only individual users can be assigned as required reviewers, not teams.
  > Both individual users and teams can be assigned as required reviewers
- F. Required reviewers need at least `write` access to the repository in order to approve.
  > Required reviewers need at least `read` access

**Answer:** A, B  ·  *multi-select (2 correct)*
**Docs:** https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments#required-reviewers

---

## Q179

You are considering a Marketplace action to utilize in your workflow. What are some aspects you can look for that indicate the action is trustworthy?

- A. A 'Verified Creator' badge on the Marketplace page for the action
- B. The README is thorough in defining the purpose of the action and how it works
- C. The `action.yml` is very brief
- D. The amount of Stars is low on the Marketplace page for the action
- E. The source code for the action has not been updated in a long time, indicating development on that action has finished
  > If the repository containing the action has not been updated in a long time, dependencies and the like may be outdated, presenting potential security risks.

**Answer:** A, B  ·  *multi-select (2 correct)*
**Docs:** https://docs.github.com/en/actions/reference/security/secure-use#using-third-party-actions

---
