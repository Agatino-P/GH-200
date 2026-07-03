# GH-200 practice session 2026-07-03-a

Generated 2026-07-03 from `gh-200-ghcertified-bank-full-2026-06-24.md` — 178 questions, options shuffled and re-lettered.
Answers withheld: grade each commitment with `log_answer.py` (see QUIZ-PROTOCOL.md).

---

## Q001

Which statement is correct regarding passing permissions to reusable workflows?

- A. The `GITHUB_TOKEN` permissions passed from the caller workflow can be only elevated by the called workflow.
- B. The `GITHUB_TOKEN` permissions passed from the caller workflow can be only downgraded by the called workflow.
- C. The `GITHUB_TOKEN` permissions passed from the caller workflow can be neither downgraded or elevated by the called workflow.
- D. The `GITHUB_TOKEN` permissions passed from the caller workflow can be both downgraded and elevated by the called workflow.

**Type:** *single*

---

## Q002

What are the different permission levels you can assign to `GITHUB_TOKEN` in the `permissions` block?

- A. none, write, read
- B. read, write
- C. read, write, delete

**Type:** *single*

---

## Q003

You can use `permissions` to modify the `GITHUB_TOKEN` permissions on:

- A. Step level
- B. Job level
- C. Workflow level

**Type:** *multi-select (2 correct)*

---

## Q004

Are GitHub Actions free for public repositories?

- A. Yes, when using standard GitHub-hosted runners
- B. No, only self-hosted runners are free for public repositories
- C. Yes, but only for the first 2,000 minutes per month
- D. No, all GitHub Actions usage is billed

**Type:** *single*

---

## Q005

Which of these is not a valid event that could trigger a workflow?

- A. Cloning the repository
- B. Committing a file to master branch
- C. Adding a label to a pull request
- D. A branch is created

**Type:** *single*

---

## Q006

Which is true about workflows?

- A. Workflows can be triggered manually, by an event or run on a schedule
- B. Workflows can be shared in GitHub Marketplace
- C. Workflows can only be run on a schedule
- D. Workflows are written in any of `.yaml`, `.json` or `.toml` formats
- E. Workflows can run one or multiple jobs at a time
- F. Workflows have to be defined in the `.github/workflows` directory
- G. Workflow can run only one job at a time

**Type:** *multi-select (3 correct)*

---

## Q007

Which components are required for a workflow?

- A. Defined branches on which the workflow will run
- B. Workflow name
- C. One or more jobs
- D. One or more events that will trigger the workflow

**Type:** *multi-select (2 correct)*

---

## Q008

Which event is triggered by a webhook action from outside of the repository?

- A. workflow_dispatch
- B. repository_dispatch
- C. remote_dispatch
- D. api_dispatch
- E. webhook_dispatch

**Type:** *single*

---

## Q009

Workflows are defined in which format

- A. yaml
- B. json
- C. toml
- D. xml

**Type:** *single*

---

## Q010

Where should you store sensitive data such as passwords or certificates that will be used in workflows

- A. secrets
- B. config variables
- C. vault
- D. environment variables

**Type:** *single*

---

## Q011

In a workflow with multiple jobs the default behavior is:

- A. All jobs run in parallel
- B. Jobs run in sequence
- C. Jobs run based on the order they are defined in the workflow file
- D. Only the first job runs, others require manual approval

**Type:** *single*

---

## Q012

If job B requires job A to be finished you have to:

- A. use the `requires` keyword in job B to create this dependency
- B. use the `requires` keyword in job A to create this dependency
- C. use the `needs` keyword in job A to create this dependency
- D. use the `needs` keyword in job B to create this dependency

**Type:** *single*

---

## Q013

In a workflow with multiple jobs, if job A fails then:

- A. the jobs that are dependent on job A fail
- B. the workflow immediately cancels all other jobs
- C. the jobs that are dependent on job A are skipped

**Type:** *single*

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

- A. Only with self-hosted runners
- B. Only if the workflows are in the same repository
- C. No
- D. Yes

**Type:** *single*

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
    matrix:
      version: [10, 12, 14]
      os: [ubuntu-latest, windows-latest]
  ```
- C. 
  ```yaml
  jobs:
    example_matrix:
      matrix:
        strategy:
          version: [10, 12, 14]
          os: [ubuntu-latest, windows-latest]
  ```
- D. 
  ```yaml
  jobs:
    example_matrix:
      matrix:
        version: [10, 12, 14]
        os: [ubuntu-latest, windows-latest]
  ```

**Type:** *single*

---

## Q016

How do you access matrix variables in a matrix strategy job?

- A. Using the `vars` context
- B. Using the `job` context
- C. Using the `matrix` context
- D. Using the `jobs` context

**Type:** *single*

---

## Q017

When using the `pull_request` and `pull_request_target` events, how do you configure the workflow to run only when targeting the `prod` branch?

- A. Using `branch` filter
- B. Using `branches` filter
- C. You create the workflow only on `prod` branch
- D. Using glob patterns

**Type:** *single*

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

- A. the target branch name starts with `release`
- B. the target branch name starts with `release` but does not end with `-alpha`
- C. the source branch name starts with `release` but does not end with `-alpha`
- D. the source branch name starts with `release`

**Type:** *single*

---

## Q019

Fill in the blank: When using `push` event trigger filters you can use <____> patterns to target multiple branches

- A. glob
- B. action
- C. scheme
- D. regex

**Type:** *single*

---

## Q020

Which event allows you to manually trigger a workflow from the GitHub UI?

- A. workflow_dispatch
- B. manual_dispatch
- C. workflow_trigger
- D. manual_trigger

**Type:** *single*

---

## Q021

What are the possible types of an input variable for a manually triggered workflow?

- A. choice
- B. string
- C. number
- D. environment
- E. boolean
- F. dropdown
- G. select

**Type:** *multi-select (5 correct)*

---

## Q022

A workflow that has only `workflow_dispatch` event trigger can be triggered using GitHub's REST API

- A. True
- B. False

**Type:** *single*

---

## Q023

To stop a workflow from running temporarily without modifying the source code you should

- A. Remove secrets that are required for this workflow
- B. Delete environment that is required for this workflow
- C. Prevent any new commits to main branch
- D. Use the `Disable workflow` option in GitHub Actions

**Type:** *single*

---

## Q024

What are `activity types` of an event used for ?

- A. Limiting workflow runs to specific activity types using the `types` filter
- B. Checking if the activity comes from an user or a bot
- C. Reacting to new activity on a repository (e.g new contributor)

**Type:** *single*

---

## Q025

You want to create a reusable workflow `CI` that runs some quality checks, linting and tests on code changes. What event trigger should the `CI` workflow define to allow reusing it in other workflows?

- A. workflow_dispatch
- B. workflow_call
- C. workflow_run
- D. workflow_trigger

**Type:** *single*

---

## Q026

A reusable workflow named `build` creates zip file artifacts. How do you pass the zip file location to the caller workflow that is calling the `build` workflow?

- A. You define an output on workflow level in the `build` workflow
- B. All outputs are automatically passed to the caller workflows
- C. In the `build` workflow you write the output into `$GITHUB_OUTPUT` in one of the steps
- D. You define an output on job level in the `build` workflow

**Type:** *multi-select (3 correct)*

---

## Q027

What are the valid use cases for using **defaults**?

- A. Using defaults.run on job level to set default working-directory for all steps in a single job
- B. Using defaults.env on workflow level to set default environment variables for an entire workflow
- C. Using defaults.env on job level to set default environment variables for all steps in a single job
- D. Using defaults.run on workflow level to set default shell (e.g bash) for an entire workflow
- E. Using defaults.run on step level to set default shell (e.g bash) for that single step

**Type:** *multi-select (2 correct)*

---

## Q028

How can you ensure that a workflow called `Deploy Prod` is always running at most one at a time?

- A. Use `queue` on workflow level
  ```yaml
  queue: ${{ github.workflow }}
  ```
- B. Use `order` on workflow level
  ```yaml
  order: ${{ github.workflow }}
  ```
- C. Use `concurrency` on workflow level
  ```yaml
  concurrency: ${{ github.workflow }}
  ```
- D. Use `parallel` on workflow level
  ```yaml
  parallel: ${{ github.workflow }}
  ```

**Type:** *single*

---

## Q029

Your Pull Request analysis workflow uses multiple code analysis tools and takes about 20minutes to fully complete. It is triggered on `pull_request` event with `branches` filter set to `master`. Therefore if a developer pushes multiple commits within few minutes multiple workflows are running in parallel. How can you stop all previous workflow runs and only run the one with latest changes?

- A. Use activity types filter
  ```yaml
  on:
    pull_request:
      branches:
        - master
      types: [latest]
  ```
- B. Use concurrency
  ```yaml
  concurrency:
    group: ${{ github.ref }}
  ```
- C. Use concurrency with cancel-in-progress
  ```yaml
  concurrency:
    group: ${{ github.workflow }}-${{ github.ref }}
    cancel-in-progress: true
  ```
- D. Use cancel-in-progress flag for `pull_request` event
  ```yaml
  on:
    pull_request:
      branches:
        - master
      cancel-in-progress: true
  ```

**Type:** *single*

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
- B. job3 will run after job1 and job2 have been successfully completed
- C. You cannot use `if: ${{ always() }}` and `needs` together. The workflow will fail on startup.
- D. job3 will run after both job1 and job2 have failed

**Type:** *single*

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

- A. `if: ${{ github.organization == 'my-org' && github.repository == 'my-repo' }}`
- B. `if: github.repository == 'my-org/my-repo'`
- C. `if: ${{ github.repository == 'my-org/my-repo' }}`
- D. `if: ${{ github.org == 'my-org' && github.repository == 'my-repo' }}`

**Type:** *multi-select (2 correct)*

---

## Q032

What GitHub-hosted runner types are available to use?

- A. Ubuntu Linux
- B. Windows
- C. macOS
- D. Android

**Type:** *multi-select (3 correct)*

---

## Q033

Is this statement true? `Not all steps run actions, but all actions run as a step`

- A. False
- B. True

**Type:** *single*

---

## Q034

For any action published in GitHub Marketplace, you can often use it in multiple versions. Which approach is the most stable and secure?

- A. Reference the main branch
- B. Reference the commit SHA
- C. Reference a version tag

**Type:** *single*

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

**Type:** *single*

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

- A. It's not possible, a matrix will always run all of the jobs in parallel if there are runners available
- B. Use GitHub's REST API to check if the job count is lesser than 2
- C. Set `jobs.example_matrix.strategy.concurrency` to 2
- D. Set `jobs.example_matrix.strategy.max-parallel` to 2

**Type:** *single*

---

## Q037

Which of these is a proper way of setting an output parameter `PET` with a value of `DOG` in a `step`.

- A. `echo "DOG=PET" >> "$GITHUB_OUTPUT"`
- B. `echo "PET=DOG" >> "$GITHUB_OUTPUT"`
- C. `gh set-output "DOG=PET"`
- D. `gh set-output "PET=DOG"`

**Type:** *single*

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

- A. `run: echo "${{ action_state }}"`
- B. `run: echo "${{ steps.step_one.outputs.action_state }}"`
- C. `run: echo "$action_state"`
- D. `run: echo "$steps.step_one.outputs.action_state"`

**Type:** *single*

---

## Q039

Is this statement true? `Workflows can be reused, but a reusable workflow cannot call another reusable workflow.`

- A. False
- B. True

**Type:** *single*

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

- A. Only repository and environment secrets available to `workflow A` will be available to `workflow B`, but not to `workflow C`. Organization scoped secrets cannot be inherited
- B. All secrets from `octo-org` organization and `octo-org/example-repo` repository will be available to `workflow B`, but not to `workflow C`
- C. All secrets available to `workflow A` will be also available to `workflow B` and `workflow C`
- D. All secrets available to `workflow A` will be also available to `workflow B`, but not to `workflow C`

**Type:** *single*

---

## Q041

When should you use `caching`?

- A. When you want to reuse files that don't change often between jobs or workflow runs, such as build dependencies from a package management system.
- B. When you want to save files produced by a job to view after a workflow run has ended, such as built binaries or build logs.
- C. When you want to reuse files that do change often between jobs or workflow runs, such as build dependencies from a package management system.
- D. When you want to save binaries produced by a build job to use in a subsequent deploy job to deploy a new version of an application

**Type:** *single*

---

## Q042

When should you use `artifacts`?

- A. Use artifacts to save binaries produced by a build job to use in a subsequent deploy job to deploy a new version of an application
- B. Use artifacts to create new versions of your application together with release notes, mentions and/or contributors
- C. Use artifacts to reuse files that don't change often between jobs or workflow runs, such as build dependencies from a package management system.
- D. Use artifacts to save files produced by a job to view after a workflow run has ended, such as test results or build logs.

**Type:** *multi-select (2 correct)*

---

## Q043

If a workflow runs on a `feature-a` branch, can it restore `caches` created in the default `main` branch?

- A. No, caches can only be restored from the same branch
- B. Yes, all caches can be accessed by workflows on any branch within the same repository
- C. Yes but only if no files were changed on `feature-a` branch
- D. Yes, all branches can restore caches created on the default branch

**Type:** *single*

---

## Q044

To access an `artifact` that was created in another, previously triggered workflow run you can:

- A. Use the `actions/download-artifact` action and make sure the artifact is not expired
- B. Use the `actions/download-artifact` action with elevated permissions.
- C. Use the `actions/upload-artifact` action.
- D. You cannot access `artifacts` that were created in a different workflow run

**Type:** *single*

---

## Q045

What should you use to store coverage reports or screenshots generated during a workflow that runs automated testing for a repository?

- A. Packages
- B. Caches
- C. Artifacts
- D. Releases

**Type:** *single*

---

## Q046

You can only upload a single file at a time when using `actions/upload-artifact` action

- A. True
- B. Only directories can be uploaded, not individual files
- C. False

**Type:** *single*

---

## Q047

In job `deploy`, if you want to access binaries (containing your application) that were created in job `build` you should

- A. upload the binaries as artifacts in `deploy` and download them in `build`
- B. cache the binaries in `build` and read the files from cache in `deploy`
- C. upload the binaries as artifacts in `build` and download them in `deploy`
- D. cache the binaries in `deploy` and read the files from cache in `build`

**Type:** *single*

---

## Q048

A job called `job2` is using artifacts created in `job1`. Therefore it's important to make sure `job1` finishes before `job2` starts looking for the artifacts. How should you create that dependency?

- A. create this dependency using the `concurrency` keyword in `job2`
- B. this dependency is created implicitly when using `actions/download-artifact` to download artifact from `job1`
- C. create this dependency using the `needs` keyword in `job2`
- D. create this dependency by defining `job2` after `job1` in the workflow's `.yaml` definition

**Type:** *single*

---

## Q049

Which is true about `Starter Workflows` ?

- A. They allow users to leverage ready-to-use (or requiring minimal changes) workflow templates
- B. Starter workflows are a paid GitHub feature
- C. Starter workflows are provided ready-to-use and cannot be modified or enhanced
- D. GitHub provides and maintains starter workflows for different categories, languages and tooling
- E. Your organization can create custom starter workflows for users in your organization
- F. Starter workflows cannot call reusable workflows

**Type:** *multi-select (3 correct)*

---

## Q050

Secrets and configuration variables can be scoped to:

- A. An environment in a repository
- B. An environment shared across multiple repositories
- C. Multiple repositories that do not share an organization/enterprise
- D. A single repository
- E. A specific job in a workflow
- F. A specific workflow in a repository
- G. The entire organization, or selected repositories in an organization

**Type:** *multi-select (3 correct)*

---

## Q051

What are the three types of Actions?

- A. `Docker container Actions`, `JavaScript Actions`, `Custom Actions`
- B. `Docker container actions`, `Java Actions`, `Composite Actions`
- C. `Python Actions`, `JavaScript Actions`, `Custom Actions`
- D. `Docker container actions`, `JavaScript Actions`, `Composite Actions`

**Type:** *single*

---

## Q052

Is this statement true? `Docker container actions are usually slower than JavaScript actions`

- A. True
- B. False

**Type:** *single*

---

## Q053

When creating a custom GitHub Action you have to store the source code in `.github/workflows` directory

- A. False
- B. Only for Docker container actions
- C. True
- D. Only if the action is reusable

**Type:** *single*

---

## Q054

When creating custom GitHub Actions - in what file does all the action `metadata` have to be defined?

Metadata examples: name, description, outputs or required inputs

- A. It's edited in GitHub Marketplace UI when published for sharing
- B. In the `action.yml` or `action.yaml` file in the action repository
- C. In the repository `README` file
- D. In the `action.yml` or `action.yaml` file in the action repository, but it is not required if the action is not meant to be shared and used by the public

**Type:** *single*

---

## Q055

A workflow was initially run on `commit A` and failed. You fixed the workflow with the subsequent `commit B`. When you re-run that workflow it will run with code from which commit?

- A. It will run with code from `commit B`
- B. It will run with code from `commit A`
- C. It will trigger two workflows, one with code from `commit A` and one with code from `commit B`
- D. You cannot re-run workflows in GitHub Actions. You have to trigger a new workflow which will run with latest changes

**Type:** *single*

---

## Q056

How can you require manual approvals by a maintainer if the workflow run is targeting the `production` environment?

- A. Manual approvals are not supported by GitHub Actions
- B. Using branch protection rules
- C. Setting the required reviewers in the `production` workflow
- D. Using deployment protection rules

**Type:** *single*

---

## Q057

Which is true about environments?

- A. Each workflow can reference a single environment.
- B. Each workflow can reference a maximum of two environments.
- C. Each job in a workflow can reference a maximum of two environments.
- D. Each job in a workflow can reference a single environment.

**Type:** *single*

---

## Q058

When using GitHub Actions to access resources in one of the cloud providers (such as AWS, Azure or GCP) the safest and recommended way to authenticate is

- A. Using Vault
- B. Using OIDC
- C. Storing access keys in `variables`
- D. Storing access keys in `secrets`

**Type:** *single*

---

## Q059

Your open-source publicly available repository contains a workflow with a `pull_request` event trigger. How can you require approvals for workflow runs triggered from forks of your repository?

- A. Setup deployment protection rules for the repository
- B. Setup branch protection rules for the repository
- C. Setup required approvals for fork runs in the repository
- D. The workflow will not trigger for forks if using `pull_request` event. If you want to do that you should use `fork_pull_request` event trigger with `require-approval` flag.

**Type:** *single*

---

## Q060

Which of the following default environment variables contains the name of the person or app that initiated the workflow run?

- A. `GITHUB_USER`
- B. `GITHUB_REPOSITORY`
- C. `GITHUB_WORKFLOW`
- D. `GITHUB_ACTOR`

**Type:** *single*

---

## Q061

Which of the following are default environment variables in GitHub Actions?

- A. `GITHUB_REPOSITORY`
- B. `GITHUB_TOKEN`
- C. `GITHUB_ORGANIZATION`
- D. `GITHUB_ACTOR`
- E. `GITHUB_USER`
- F. `GITHUB_WORKFLOW`

**Type:** *multi-select (3 correct)*

---

## Q062

Your organization defines a secret `SomeSecret`, however when you reference that secret in a workflow using `${{ secrets.SomeSecret }}` it provides a different value than expected. What may be the reason for that?

- A. The secret `SomeSecret` is also declared in repository scope
- B. The secret `SomeSecret` is also declared in enterprise scope
- C. You need to use the GitHub API to access organization scoped secrets
- D. `${{ secrets.SomeSecret }}` expression is only used for repository scoped secrets

**Type:** *single*

---

## Q063

Which is a correct way to print a debug message?

- A. `echo "Watch out here!" >> $GITHUB_DEBUG`
- B. `echo "::debug::Watch out here!"`
- C. `echo "::debug::message=Watch out here!"`
- D. `echo ":debug:Watch out here!"`

**Type:** *single*

---

## Q064

How can organizations which are using GitHub Enterprise Server enable automatic syncing of third party GitHub Actions hosted on GitHub.com to their GitHub Enterprise Server instance?

- A. Using GitHub Connect
- B. GitHub Enterprise Server has access to all GitHub.com Actions by default
- C. GitHub Enterprise Server (GHES) cannot use GitHub.com Actions because of its on-premise nature and no internet access.
- D. Using actions-sync tool

**Type:** *single*

---

## Q065

Where can you find network connectivity logs for a GitHub self-hosted-runner?

- A. On GitHub.com on that specific Runner's page
- B. In the job run logs of a job that ran on that Runner with debug logging enabled
- C. In the job run logs of a job that ran on that Runner
- D. In the `_diag` folder directly on the runner machine

**Type:** *single*

---

## Q066

How can you validate that your GitHub self-hosted-runner can access all required GitHub services?

- A. Using a GitHub provided script on the runner machine
- B. By using the predefined GitHub Actions workflow `network-connectivity.yml`
- C. By trying to access the runner machine by `ssh` to validate the network connectivity
- D. GitHub will validate the network connectivity automatically when the runner application is installed on the runner machine

**Type:** *single*

---

## Q067

Which is the correct way of triggering a job only if configuration variable `MY_VAR` has the value of `MY_VALUE`?

- A. It's not possible because configuration variables cannot be used in `if` conditionals
- B. It's not possible because configuration variables cannot be used in job level `if` conditionals
- C. By creating the following conditional on job level
  ```yaml
  my-job:
    if: ${{ vars.MY_VAR == 'MY_VALUE' }}
  ```
- D. By creating the following conditional on job level
  ```yaml
  my-job:
    if: ${{ vars.MY_VAR }} == 'MY_VALUE'
  ```

**Type:** *single*

---

## Q068

To run a `step` only if the secret `MY_SECRET` has been set, you can:

- A. By creating the following conditional on job level
  ```yaml
  my-job:
    runs-on: ubuntu-latest
    if: ${{ secrets.MY_SECRET == '' }}
  ```
- B. By creating the following conditional on step level
  ```yaml
  my-job:
    runs-on: ubuntu-latest
    steps:
      - if: ${{ secrets.MY_SECRET }}
  ```
- C. By creating the following conditional on step level
  ```yaml
  my-job:
    runs-on: ubuntu-latest
    steps:
      - if: ${{ secrets.MY_SECRET == '' }}
  ```
- D. Set the secret `MY_SECRET` as a job level environment variable, then reference that environment variable to conditionally run that step
  ```yaml
  my-job:
    runs-on: ubuntu-latest
    env:
      my_secret: ${{ secrets.MY_SECRET }}
    steps:
      - if: ${{ env.my_secret != '' }}
  ```

**Type:** *single*

---

## Q069

How can you use the GitHub API to download workflow run logs?

- A. `GET /repos/{owner}/{repo}/actions/runs/{run_id}/logs`
- B. `POST /repos/{owner}/{repo}/actions/runs/{run_id}/logs`
- C. `HEAD /repos/{owner}/{repo}/actions/runs/{run_id}/logs`
- D. `PUT /repos/{owner}/{repo}/actions/runs/{run_id}/logs`

**Type:** *single*

---

## Q070

How can you use the GitHub API to create or update a repository secret?

- A. `HEAD /repos/{owner}/{repo}/actions/secrets/{secret_name}`
- B. `POST /repos/{owner}/{repo}/actions/secrets/{secret_name}`
- C. `GET /repos/{owner}/{repo}/actions/secrets/{secret_name}`
- D. `PUT /repos/{owner}/{repo}/actions/secrets/{secret_name}`

**Type:** *single*

---

## Q071

How can you override an organization-level GitHub Secret `API_KEY` with a different value when working within a repository?

- A. By creating a environment secret with the same name `API_KEY`
- B. By creating a environment secret with the name `OVERRIDE_API_KEY`
- C. By creating a repository secret with the name `OVERRIDE_API_KEY`
- D. By creating a environment secret with the name `ENVIRONMENT_API_KEY`
- E. By creating a repository secret with the same name `API_KEY`
- F. By creating a enterprise secret with the name `OVERRIDE_API_KEY`
- G. By creating a repository secret with the name `REPOSITORY_API_KEY`
- H. By creating a enterprise secret with the same name `API_KEY`

**Type:** *multi-select (2 correct)*

---

## Q072

What components can be reused within a GitHub Organization?

- A. Configuration Variables
- B. Workflow Templates
- C. Artifacts
- D. Cache
- E. Secrets
- F. Self Hosted Runners
- G. Environment Variables

**Type:** *multi-select (4 correct)*

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

- A. 6
- B. 7
- C. 4
- D. 5

**Type:** *single*

---

## Q074

Which of the following default environment variables contains the full name (e.g `octocat/hello-world`) of the repository where the workflow is running?

- A. `GITHUB_REPOSITORY_ID`
- B. `GITHUB_REPOSITORY_OWNER`
- C. `GITHUB_REPOSITORY`
- D. `GITHUB_REPOSITORY_OWNER_ID`

**Type:** *single*

---

## Q075

In a workflow that has multiple jobs, all running on GitHub-hosted runners, is it true that all jobs are guaranteed to run on the same runner machine?

- A. Yes
- B. Only if they use the same `runs-on` label
- C. No
- D. Only if they run in parallel

**Type:** *single*

---

## Q076

What's the maximum amount of reusable workflows that can be called from a single workflow file?

- A. 1
- B. 50
- C. 5
- D. 20
- E. 10

**Type:** *single*

---

## Q077

What is a self-hosted runner?

- A. A self-hosted runner is a system that you deploy and manage to execute jobs from GitHub Actions on GitHub.com
- B. A self-hosted runner is a system to upload code to a private server
- C. A self-hosted runner is a system to manage pull requests from users of the organization
- D. A self-hosted runner is a system to be able to create workloads automatically

**Type:** *single*

---

## Q078

Which of the following is a correct statement about GitHub Workflows and Actions?

- A. Each action is composed of one or more jobs which is composed of one or more steps, and each step is a workflow
- B. Each workflow is composed of one or more actions which is composed of one or more jobs, and each job is composed of one or more steps
- C. Each workflow is composed of one or more jobs which is composed of one or more steps, and each step is an action or a script
- D. Each action is composed of one or more workflows which is composed of one or more jobs, and each job is composed of one or more steps

**Type:** *single*

---

## Q079

On which commit and branch do scheduled workflows run in GitHub Actions?

- A. Scheduled workflows run on the latest commit on the repository default branch.
- B. Scheduled workflows run on the specific commit on last modified branch.
- C. Scheduled workflows run on the specific commit on the main branch.
- D. Scheduled workflows run on the latest commit on the main branch.

**Type:** *single*

---

## Q080

What is the correct syntax for setting the directory for all `run` commands in a workflow?

- A. set `directory` under `defaults.run`
  ```yaml
  defaults:
    run:
      shell: bash
      directory: ./scripts
  ```
- B. set `directory` under `job`
  ```yaml
  defaults:
    run:
      shell: bash
  job:
    directory: ./scripts
  ```
- C. set `working-directory` under `defaults.run`
  ```yaml
  defaults:
    run:
      shell: bash
      working-directory: ./scripts
  ```
- D. set `working-directory` under `job`
  ```yaml
  defaults:
    run:
      shell: bash
  job:
    working-directory: ./scripts
  ```

**Type:** *single*

---

## Q081

How can you reuse a defined workflow in multiple repositories?

- A. By creating a reusable action
- B. By copying the workflow file to each repository
- C. By using workflow templates
- D. By defining the workflow in a central repository

**Type:** *multi-select (2 correct)*

---

## Q082

How can you ensure a job runs only on a specific branch?

- A. By using the runs-on filter
- B. By using the branches filter
- C. By using the branch keyword
- D. By using the jobs filter

**Type:** *single*

---

## Q083

What does the `needs` keyword do in a GitHub Actions workflow?

- A. Defines environment variables
- B. Specifies the dependencies of a job
- C. Triggers a job based on an event
- D. Sets up the environment

**Type:** *single*

---

## Q084

Which keyword allows you to define environment variables in a GitHub Actions workflow?

- A. env
- B. secrets
- C. vars
- D. config

**Type:** *single*

---

## Q085

What is the purpose of the `with` keyword in a GitHub Actions workflow?

- A. To specify input parameters for an action
- B. To set up dependencies
- C. To trigger another workflow
- D. To define environment variables

**Type:** *single*

---

## Q086

Which of the following GitHub Actions syntax is used to run multiple commands in a single step?

- A. Using && to chain commands
- B. Using a multiline string with |
- C. Defining commands in an array
- D. Separating commands with a semicolon ;

**Type:** *single*

---

## Q087

How can you cache dependencies to speed up workflow execution?

- A. Using the actions/cache action
- B. By storing them in the repository
- C. By using the store keyword
- D. Using the cache keyword

**Type:** *single*

---

## Q088

What does the `matrix` keyword do in a GitHub Actions workflow?

- A. Defines secrets for the workflow
- B. Sets environment variables for the job
- C. Triggers workflows based on a schedule
- D. Allows defining multiple job configurations to run in parallel

**Type:** *single*

---

## Q089

Which of the following can be used to limit the number of concurrent jobs running in a GitHub Actions workflow?

- A. concurrency
- B. limit
- C. max-jobs
- D. parallelism

**Type:** *single*

---

## Q090

What is the default timeout for a GitHub Actions job?

- A. 60 minutes
- B. 360 minutes
- C. 120 minutes
- D. 30 minutes

**Type:** *single*

---

## Q091

How can you specify the operating system for a job in GitHub Actions?

- A. Using the os keyword
- B. Using the runs-on keyword
- C. Using the env keyword
- D. Using the platform keyword

**Type:** *single*

---

## Q092

In a GitHub Actions workflow, how do you specify a specific version of Node.js to use in a job?

- A. 
  ```yaml
  uses: setup-node@v4
  with:
    version: 20
  ```
- B. 
  ```yaml
  uses: setup-node@v4
  with:
    node: 20
  ```
- C. 
  ```yaml
  uses: actions/node-setup@v4
  with:
    node-version: 20
  ```
- D. 
  ```yaml
  uses: actions/setup-node@v4
  with:
    node-version: 20
  ```

**Type:** *single*

---

## Q093

How do you reference a secret stored in GitHub Secrets in a workflow?

- A. ${{ secrets.SECRET_NAME }}
- B. ${{ secret.SECRET_NAME }}
- C. ${{ env.SECRET_NAME }}
- D. ${{ config.SECRET_NAME }}

**Type:** *single*

---

## Q094

What is the default shell used by GitHub Actions on Windows runners?

- A. powershell
- B. cmd
- C. bash
- D. sh

**Type:** *single*

---

## Q095

Which of the following statements are true about adding a self-hosted runner in GitHub Actions?

- A. You can add a self-hosted runner to a workflow
- B. You can add a self-hosted runner to an enterprise
- C. You can add a self-hosted runner to a step
- D. You can add a self-hosted runner to an organization
- E. You can add a self-hosted runner to a repository

**Type:** *multi-select (3 correct)*

---

## Q096

Select the default environment variable that contains the operating system of the runner executing the job

- A. `RUNNER_ARCH`
- B. `RUNNER_NAME`
- C. `GITHUB_RUNNER_OS`
- D. `RUNNER_OS`

**Type:** *single*

---

## Q097

How does the `actions/cache` action in GitHub Actions handle a cache miss?

- A. by searching for a cache in other repositories
- B. by automatically creating a new cache if the job is completed successfully
- C. by terminating the workflow if a cache miss occurs
- D. by requiring manual intervention to create a new cache

**Type:** *single*

---

## Q098

How can you specify the schedule of a GitHub actions workflow to run on weekdays only?

- A. it is not possible in GitHub actions
- B. use the on: schedule: weekdays event trigger
- C. add a condition in the workflow YAML for weekdays
- D. use the on: schedule: cron event trigger

**Type:** *single*

---

## Q099

What is the recommended approach for storing secrets larger than 48 KB?

- A. avoid storing large secrets entirely to ensure security
- B. secrets larger than 48 KB cannot be stored
- C. store large secrets directly as repository secrets to avoid limitations
- D. encrypt and store secrets in the repository but keep the decryption passphrase as a secret

**Type:** *single*

---

## Q100

Select status check functions in GitHub Actions

- A. `success()`, `always()`, `cancelled()` and `failure()`
- B. `completed()`, `always()`, `cancelled()` and `failure()`
- C. `state()`, `always()`, `cancelled()` and `failure()`
- D. `status()`, `always()`, `cancelled()` and `failure()`

**Type:** *single*

---

## Q101

How do you ensure that `Upload Failure test report` step is executed only if `Run Tests` step fails?

- A. 
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
- B. 
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
- C. 
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
- D. 
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

**Type:** *single*

---

## Q102

Which context holds information about the event that triggered a workflow run?

- A. `github.repository`
- B. `github.event`
- C. `jobs.<job_id>.result`
- D. `github.job`

**Type:** *single*

---

## Q103

In GitHub Actions, if you define both branches and paths filter, what is the effect on the workflow execution?

- A. the workflow will only run when both `branches` and `paths` are satisfied
- B. the workflow will not run when both `branches` and `paths` are satisfied
- C. the workflow will run when either `branches` or `paths` are satisfied, but will only apply the matching filter
- D. the workflow will run when either `branches` or `paths` are satisfied

**Type:** *single*

---

## Q104

What is the recommended practice for treating environment variables in GitHub Actions, regardless of the operating system and shell used?

- A. ignore case sensitivity as GitHub Actions handles it automatically
- B. depend on the behavior of the operating system in use
- C. use only uppercase letters for environment variable names
- D. treat environment variables as case-sensitive

**Type:** *single*

---

## Q105

Which of the following statements accurately describes the behavior of workflow jobs referencing an environment's protection rules?

- A. workflow jobs will start if at least one protection rule passes
- B. workflow jobs won't start until all the environment's protection rules pass
- C. workflow jobs will fail if protection rules are configured
- D. workflow jobs will start immediately and protection rules are evaluated during execution

**Type:** *single*

---

## Q106

What is the purpose of the `restore-keys` parameter in `actions/cache` in GitHub Actions?

- A. indicate whether a cache hit occurred
- B. specify the location of the cached files
- C. provide alternative keys to use in case of a cache miss
- D. enable cross-OS cache functionality

**Type:** *single*

---

## Q107

Which variable would you set to `true` in order to enable step debug logging?

- A. `ACTIONS_RUNNER_DEBUG`
- B. `ACTIONS_WORKFLOW_DEBUG`
- C. `ACTIONS_STEP_DEBUG`
- D. `ACTIONS_JOB_DEBUG`

**Type:** *single*

---

## Q108

Which configuration is appropriate for triggering a workflow to run on webhook events related to check_run actions?

- A. 
  ```yaml
  on:
      check_run:
          types: [started]
  ```
- B. 
  ```yaml
  on:
      check_run:
          types: [rerequested, completed]
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

**Type:** *single*

---

## Q109

What is the purpose of the `timeout-minutes` keyword in a step?

- A. it defines the time interval for individual commands within a step
- B. it sets the timeout for waiting on external events before proceeding to the next step
- C. it specifies the maximum duration a job is allowed to run
- D. it limits the execution time for individual step

**Type:** *single*

---

## Q110

Dave is creating a templated workflow for his organization. Where must Dave store the workflow files and associated metadata files for the templated workflow?

- A. inside a directory named `workflow-templates` within the current repository
- B. inside a directory named `.github/org-templates`
- C. inside a directory named `.github/workflow-templates`
- D. inside a directory named `workflow-templates` within a repository named `.github`

**Type:** *single*

---

## Q111

Dave wants to be notified when a comment is created on an issue within a GitHub repository. Which event trigger should be used within the workflow configuration?

- A. `issues`
- B. `issue_comment`
- C. `issues.comment`
- D. `comment`

**Type:** *single*

---

## Q112

What level of access is required on a GitHub repository in order to delete log files from workflow runs?

- A. admin
- B. write 
- C. read
- D. owner

**Type:** *single*

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

- A. the `production-deploy` job will execute three steps
- B. the `production-deploy` job will be marked as skipped
- C. the `production-deploy` job will run if the `node-version` is `14`
- D. the `production-deploy` job will error

**Type:** *single*

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

- A. by accessing the variables directly with the syntax `version` and `os`
- B. reference variables through the `matrix` context with syntax like`matrix.version` and `matrix.os`
- C. by using the `matrix.property` syntax
- D. by using the `context` keyword within the job configuration

**Type:** *single*

---

## Q115

What level of permission is required to re-run the workflows

- A. admin
- B. write 
- C. read
- D. owner

**Type:** *single*

---

## Q116

When can you delete workflow runs?

- A. After the workflow run has completed and at least 30 days have passed.
- B. Workflow runs can be deleted at any time, regardless of their status or age.
- C. After the workflow run has completed, regardless of its age.
- D. Workflow runs cannot be deleted, but they can be archived.

**Type:** *single*

---

## Q117

Who can bypass configured deployment protection rules to force deployment (by default)

- A. Anyone with repository write permission
- B. Anyone with repository read permission
- C. Repository administrators

**Type:** *single*

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

**Type:** *single*

---

## Q119

How can you determine if an action is a container action by looking at its action.yml file?

- A. `runs.using` has `Dockerfile` as value
- B. `runs.using` has `docker` as value
- C. `runs.main` has `container` as value
- D. `runs.using` has `container` as value

**Type:** *single*

---

## Q120

What is the correct syntax for specifying a cleanup script in a container action?

- A. 
  ```yaml
  runs:
    using: 'docker'
    image: 'Dockerfile'
    entrypoint: 'entrypoint.sh'
    after-entrypoint: 'cleanup.sh'
  ```
- B. 
  ```yaml
  runs:
    using: 'docker'
    image: 'Dockerfile'
    entrypoint: 'entrypoint.sh'
    cleanup: 'cleanup.sh'
  ```
- C. 
  ```yaml
  runs:
    using: 'docker'
    image: 'Dockerfile'
    entrypoint: 'entrypoint.sh'
    post-entrypoint: 'cleanup.sh'
  ```
- D. 
  ```yaml
  runs:
    using: 'docker'
    image: 'Dockerfile'
    entrypoint: 'entrypoint.sh'
    after: 'cleanup.sh'
  ```
- E. 
  ```yaml
  runs:
    using: 'docker'
    image: 'Dockerfile'
    entrypoint: 'entrypoint.sh'
    post: 'cleanup.sh'
  ```

**Type:** *single*

---

## Q121

What’s true about default variables?

- A. Default environment variables can be accessed using the env context
- B. Currently, the value of the default CI environment variable can be overwritten, but it's not guaranteed this will always be possible
- C. You can add a new default environment variable adding the prefix “GITHUB_” to it
- D. Default environment variables always have the prefix “GITHUB_”
- E. Most of the default environment variables have a corresponding context property
- F. Default environment variables are set by GitHub and not defined in a workflow

**Type:** *multi-select (3 correct)*

---

## Q122

What are the scopes defined for custom variables in a workflow?

- A. All the jobs within a workflow, by using `jobs.env`
- B. The contents of a job within a workflow, by using `jobs.<job_id>.env`
- C. A specific environment in the repository, by using `environment.<environment_id>.env` at the top level of the workflow file
- D. The entire workflow, by using `env` at the top level of the workflow file
- E. A specific step within a job, by using `jobs.<job_id>.steps[*].env`
- F. The entire workflow, by using `custom.env` at the top level of the workflow file

**Type:** *multi-select (3 correct)*

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

- A. The environmental variable `GITHUB_TOKEN`
  ```yaml
  with:
      repository: my-org/my-private-repo
      path: ./.github/actions/my-org/my-private-repo
      token: $GITHUB_TOKEN
  ```
- B. Leave as is since access tokens will be passed automatically
  ```yaml
  with:
      repository: my-org/my-private-repo
      path: ./.github/actions/my-org/my-private-repo
  ```
- C. Create a GitHub secret `MY_ACCESS_TOKEN`
  ```yaml
  with:
      repository: my-org/my-private-repo
      path: ./.github/actions/my-org/my-private-repo
      token: ${{ secrets.MY_ACCESS_TOKEN }}
  ```
- D. Create an input `MY_ACCESS_TOKEN`
  ```yaml
  with:
      repository: my-org/my-private-repo
      path: ./.github/actions/my-org/my-private-repo
      token: ${{ MY_ACCESS_TOKEN }}
  ```

**Type:** *single*

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

- A. 7 jobs
- B. 5 jobs
- C. 4 jobs
- D. 6 jobs
- E. No jobs will run because the syntax is invalid.

**Type:** *single*

---

## Q125

At what levels can environment variables be defined ?

- A. Workflow level
- B. Step level
- C. Job level
- D. Action level

**Type:** *multi-select (3 correct)*

---

## Q126

How should a dependent job reference the `output1` value produced by a job named `job1` earlier in the same workflow?

- A. `${{job1.outputs.output1}}`
- B. `${{needs.job1.outputs.output1}}`
- C. `${{needs.job1.output1}}`
- D. `${{depends.job1.output1}}`

**Type:** *single*

---

## Q127

Which workflow command syntax correctly sets an environment variable named 'API_VERSION' with the value '2.1' for subsequent steps in a GitHub Actions job?

- A. `export API_VERSION=2.1 >> "$GITHUB_ENV"`
- B. `echo "API_VERSION=2.1" >> "$GITHUB_ENV"`
- C. `echo "API_VERSION=2.1" >> "$GITHUB_OUTPUT"`
- D. `set-env name=API_VERSION value=2.1`

**Type:** *single*

---

## Q128

A workflow is triggered when pull requests are reopened. Why might this be the cause?

- A. `types: [reopened]` is defined under the `pull_request` event. 
- B. `on: schedule` was configured with `pull_requests: [reopened]`
- C. Branch protection rules were improperly configured.
- D. No activity types are defined under the `pull_request` event.

**Type:** *multi-select (2 correct)*

---

## Q129

`GITHUB_TOKEN` can be used to check out any repository.

- A. True
- B. False
- C. Only with elevated permissions

**Type:** *single*

---

## Q130

Which of the following are true regarding workflow-level vs. job-level outputs blocks?

- A. A workflow-level `outputs` block should only be used in reusable workflows, not caller workflows.
- B. Job-level `outputs` blocks should only be used in caller workflows, not reusable workflows.
- C. A job-level `outputs` block must have the following structure:
  ```
  outputs:
      <output-name>
          value: ${{ steps.<step-name>.outputs.<output-name> }}
  ```
- D. A reusable workflow can have both workflow-level and job-level `outputs` blocks.
- E. A workflow-level `outputs` block must have the following structure:
  ```
  outputs:
      <output-name>
          value: ${{ jobs.<job-name>.outputs.<output-name> }}
  ```

**Type:** *multi-select (3 correct)*

---

## Q131

Which of the following are true regarding calling reusable workflows versus calling composite actions?

- A. Secrets can be passed to both reusable workflows and calling composite actions via the `uses.secrets` block.
- B. Composite actions must be called as a step within a job
- C. Reusable workflows must be called on workflow job level (not from step-level).
- D. Composite actions are called via referencing the folder that contains their `action.yml` file.
- E. Reusable workflows can use a different runner type than the caller workflow, while composite actions cannot. 
- F. Reusable workflows are called via referencing the folder that contains their `action.yml` file.
- G. Only reusable workflows can accept inputs.

**Type:** *multi-select (4 correct)*

---

## Q132

Which of the following are true regarding GitHub Enterprise Server (GHES)?

- A. GHES workflows cannot access GitHub.com nor GitHub Marketplace actions by default. 
- B. GHES is allowed to use enhanced versions of GitHub-hosted runners.
- C. `actions/actions-sync` is primarily devoted to moving GitHub.com actions to a GHES instance.
- D. Using GitHub Connect, users can follow a manual process to access GitHub.com actions. This process must be done once per desired action.
- E. GitHub Enterprise Server instances are self-hosted, compared to GitHub Enterprise Cloud (GHEC) which is hosted and managed by GitHub.

**Type:** *multi-select (3 correct)*

---

## Q133

Why use a commit SHA versus a tag to pin an action?

- A. Commit SHAs are more secure
- B. Commit SHAs are more convenient to use as opposed to tags
- C. Commit SHAs are immutable, whereas tags have the potential to be changed
- D. Commit SHAs are guaranteed to point to the exact same code every time, tags are not
- E. Commit SHAs are more difficult to trace in an audit, making it difficult for bad actors to determine how an action's code factors in overall processes.

**Type:** *multi-select (3 correct)*

---

## Q134

How do you run custom JavaScript scripts directly in a GitHub Actions workflow?

- A. Via the `actions/github-script` action
- B. Write the contents of a script block to the `GITHUB_SCRIPT` environmental variable
- C. By enabling the 'Allow custom JavaScript scripts' configuration in the Actions settings of a repository
- D. By enabling the 'Allow custom JavaScript scripts' configuration in the Actions settings of an organization
- E. In a JavaScript Action, set the `using` key to `'github-script'`

**Type:** *single*

---

## Q135

You have forked a repository to enhance a workflow that uses a secret to access a third-party application. You trigger the workflow before editing its code to get a baseline result, but find that the workflow fails. Why would this occur?

- A. The inherited secret had a size larger than 48 KB
- B. Forked repositories only inherit repository secrets, so the secret being used in the workflow must have been an organizational or environment secret.
- C. When inheriting the secret from the original repository, there was an error during the fork that resulted in a malformed, invalid secret
- D. Forked repositories do not inherit secrets from the original repository  

**Type:** *single*

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

- A. Set `jobs.<job_id>.strategy.matrix.fail-fast` to `false`
- B. Nothing needs to be done, since `jobs.<job_id>.strategy.fail-fast` has a default setting of `false`
- C. Set `jobs.<job_id>.strategy.fail-fast` to `false`
- D. Nothing needs to be done, since `jobs.<job_id>.strategy.matrix.fail-fast` has a default setting of `false`
- E. There is no way to enforce this behavior, it cannot be worked around.

**Type:** *single*

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

- A. 10
- B. 5
- C. 6
- D. 7

**Type:** *single*

---

## Q138

You want to create a workflow `Post-Deploy` that performs post-deploy related activity. What event trigger should the `Post-Deploy` workflow use so it runs automatically after a specified workflow is completed?

- A. `workflow_run`
- B. `workflow_call`
- C. `workflow_dispatch`
- D. `workflow_trigger`

**Type:** *single*

---

## Q139

In what ways can you enable runner diagnostic logging?

- A. Renaming the `_diag` directory of a self-hosted runner to `runner-diagnostic-logs`
- B. By adding a `runner-diagnostic-logs` subfolder to the `_diag` directory of the self-hosted runner being used
- C. Re-running a workflow with `Enable debug logging enabled`
- D. By adding a `ACTIONS_RUNNER_DEBUG` top-level folder to the workflow's repository
- E. Setting a secret or variable named `ACTIONS_RUNNER_DEBUG` to `true`

**Type:** *multi-select (2 correct)*

---

## Q140

You are writing a reusable workflow which has `branch-name` as an input. How can you conditionally run a step in that workflow if the branch name begins with 'smoke-test'?

- A. Use shell conditionals in combination with `jobs.<job_id>.steps[*].if`
  ```yaml
      if: [[ "${{inputs.branch-name}}" == "smoke-test"* ]]
  ```
- B. Use the `branches` filter under `workflow_call`
  ```yaml
  on:
    workflow_call:
      branches:
          - 'smoke-test/**'
  ```
- C. Use the built-in `startsWith` method in combination with `jobs.<job_id>.steps[*].if`
  ```yaml
      if: inputs.branch-name.startsWith('smoke-test')
  ``` 
- D. Use the built-in `startsWith` method in combination with `jobs.<job_id>.steps[*].if`
  ```yaml
      if: startsWith(inputs.branch-name, 'smoke-test')
  ```

**Type:** *single*

---

## Q141

Why might you use `hashFiles` when utilizing `actions/cache`?

```yaml
  - uses: actions/cache@v5
    with:
      path: ~/.npm
      key: ${{ runner.os }}-build-${{ env.cache-name }}-${{ hashFiles('**/package-lock.json') }}
```

- A. When using `hashFiles` as part of a cache key, an additional step will be generated in the caller workflow. This workflow step prints the value of the SHA-256 hash of the cache key for reference purposes.  
- B. If a cache key contains the dependencies file wrapped in `hashFiles`, the key changes when the dependencies file is updated, which helps keep it up to date.
- C. `hashFiles` is required for compatibility with Windows runners.
- D. When using `hashFiles` as part of a cache key, if there is a cache miss, `hashFiles` gives additional debug info.  

**Type:** *single*

---

## Q142

Which of the following answers is correct regarding installation access tokens?

- A. The `actions/create-github-app-token` can be called within workflows to create an installation access token, but the installation access token can only be used in future runs of the workflow.
- B. The `actions/create-github-app-token` can be called within workflows to create an installation access token available for immediate use. 
- C. Installation access tokens are short-lived tokens ideal for automation activities, but require setting up a Github App.
- D. `GITHUB_TOKEN` is a type of installation access token.
- E. Installation access tokens cannot be configured to act on behalf of their associated Github App. 

**Type:** *multi-select (3 correct)*

---

## Q143

Your organization wants to lower the retention period for stored artifacts, citing storage concerns. How can this be done at an organizational level?

- A. By using self-hosted runners, creating a `.github/retention-policy.yml` file, and specifying the value of the `artifact-retention-period` key 
- B. By navigating to the organization's Actions settings and editing the value of the "Artifact and log retention" setting
- C. This cannot be done at an organizational level. All workflows that utilize `actions/upload-artifact` must use the required `retention-days` input.
- D. This cannot be done: artifacts are strictly stored for 90 days across all systems implementing Github Actions. 

**Type:** *single*

---

## Q144

How can you change the retention period for artifacts generated by a certain workflow?

- A. By navigating to the organization's Actions settings and editing the value of the "Artifact and log retention" setting
- B. By utilizing the `retention-days` input in `actions/upload-artifact` 
- C. By utilizing the `retention-days` input in `actions/download-artifact`
- D. In the workflow's repository, navigate to the Actions settings and editing the value of the "Artifact and log retention" setting for the workflow listed.

**Type:** *single*

---

## Q145

In what ways can you download an artifact?

- A. By using a specific GitHub API endpoint
- B. By remotely accessing self-hosted runners via SSH and accessing the `.github/artifacts` directory
- C. By using the `actions/download-artifact` action in a workflow 
- D. By downloading artifacts from the Github Actions UI workflow run
- E. By using the `actions/upload-artifact` action in a workflow

**Type:** *multi-select (3 correct)*

---

## Q146

Which statements are true regarding `github.ref` when the workflow is triggered by a `pull_request` event?

- A. In pull requests (regardless of merge status), `github.ref` refers to the pull request number 
- B. In pull requests that have not been merged, `github.ref` is the fully-formed ref of the pull request title. 
- C. In pull requests that have been merged, `github.ref` is the type of fully-formed ref that triggered the workflow run. The value will either be `branch`, `tag`, or `null` (if the ref was not fully-formed).
- D. In pull requests that have been merged, `github.ref` refers to the fully-formed ref of the branch that was merged into.
- E. In pull requests that have not been merged, `github.ref` refers to the fully-formed ref of the pull request merge branch/tag 
- F. In pull requests (regardless of merge status), `github.ref` is the SHA of the last merge commit on the `GITHUB_REF` branch.

**Type:** *multi-select (2 correct)*

---

## Q147

You have a base-64 encoded secret that you decode in a GitHub Actions workflow. How can you make sure the decoded secret does not show up in the workflow log accidentally?

- A. Using the built-in `maskSecret` function to redact the decoded secret in instances where it may be utilized.
- B. Avoiding the usage of print statements that contain the decoded secret, since this is the only way the decoded secret could appear in the workflow log
- C. Nothing needs to be done since Github Actions infrastructure automatically redacts decoded secrets.
- D. Using `add-mask` workflow command in jobs where the decoded secret may be utilized.

**Type:** *single*

---

## Q148

Which statement is true regarding `github.ref` when the workflow is triggered by a push event?

- A. In push events, `github.ref` is SHA of the commit that triggered the workflow.
- B. In push events, `github.ref` is the type of fully-formed ref that triggered the workflow run. The value will either be `branch`, `tag`, or `null` (if the ref was not fully-formed).
- C. In push events, `github.ref` is the description of the commit that triggered the workflow.
- D. In push events, `github.ref` is the message of the commit that triggered the workflow.
- E. In push events, `github.ref` is the fully-formed ref of the branch or tag ref that was pushed. 

**Type:** *single*

---

## Q149

What does writing to `GITHUB_STEP_SUMMARY` do?

```yaml
- name: "Write results of test suite"
  run: |
    echo "The results of the testing suite are:" >> $GITHUB_STEP_SUMMARY
```

- A. Adds this line to the job summary
- B. Prints this line as a step-level debug message
- C. Adds this line to the built-in artifact `github-steps-summary.md`
- D. Adds this line as a subtitle to the step name in the GitHub Actions UI

**Type:** *single*

---

## Q150

Dorothea is troubleshooting a workflow triggered by a push event and is interested in seeing details about the webhook. How can she view the entire payload of the webhook that triggered the workflow?

- A. Navigating to the "Webhooks" section of the repository settings 
- B. Checking the "Show event webhook payload" checkbox under the workflow run options.
- C. Setting a secret or variable named `SHOW_EVENT_PAYLOAD` to `true`
- D. Printing the contents of the `github.event` object in a step

**Type:** *single*

---

## Q151

Which should you use when passing information between jobs: job outputs or `GITHUB_ENV`?

- A. Job outputs, because they are simpler to set up
- B. Job outputs, because the value of environmental variables set via writing to `GITHUB_ENV` only applies to the current job.
- C. `GITHUB_ENV`, because using it to set environmental variables puts significantly less strain on the runner, reducing workflow runtime.
- D. `GITHUB_ENV`, because job outputs can only be set and referenced within the same job.

**Type:** *single*

---

## Q152

Fill in the blank: When using self-hosted runners, the tool cache ___

- A. starts off the same as GitHub-hosted runners in that it is pre-populated with certain tools
- B. cannot be populated
- C. starts with the same tools GitHub-hosted runners do, as well as a selected assortment of custom tools to enhance self-hosted runner management
- D. starts off empty and must be populated in order to save tools between runs

**Type:** *single*

---

## Q153

Which of the following events can trigger a workflow that has not been merged to the default branch?

- A. `pull_request`
- B. `issues`
- C. `push`
- D. `repository_dispatch`
- E. `star`
- F. `issue_comment`

**Type:** *multi-select (2 correct)*

---

## Q154

When would you build a Docker container action to share in the GitHub Actions marketplace?

- A. Docker container actions allow you to utilize Docker without requiring an `action.yml` file
- B. Docker container actions ensure a consistent runtime environment and specific dependencies without users needing to handle these aspects themselves
- C. Docker container actions have fast startup speed on Windows and macOS runners
- D. Docker container actions are a bundle of steps within other workflows that run within the context of the calling workflow/action
- E. Docker container actions are an out-of-the-box, low-overhead action

**Type:** *single*

---

## Q155

Marianne has a feature branch that contains her new workflow file, which is set to be triggered at 2 AM every day, using the syntax seen below. However, the next day, the workflow does not trigger. Why might this be the case?

```yaml
on:
    schedule:
        cron:
            "0 2 * * *"
```

- A. The private repository containing the workflow has not had any repository activity in greater than 60 days, automatically disabling the workflow.
- B. The `cron` syntax is not scheduled correctly
- C. `schedule` cannot be the only event in the workflow. It must be paired with a repository-based event, such as `push`
- D. The `@daily` syntax was not used
- E. The workflow file must exist on the default branch in order to be triggered by the `schedule` event

**Type:** *single*

---

## Q156

In what ways can you delete workflow artifacts?

- A. By using the `actions/delete-artifact` action in a workflow 
- B. By remotely accessing self-hosted runners via SSH, navigating to the `.github/artifacts` directory, and deleting the selected artifacts
- C. By using a specific GitHub API endpoint
- D. By using the Github Actions UI to delete the workflow run that generated the artifacts
- E. By using the Github Actions UI to navigate to a workflow run and delete the artifacts individually
- F. By setting the artifact retention period to 0 days

**Type:** *multi-select (3 correct)*

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
- B.  Specify the `pull_request` activity type as `merged` (no need for a job-level conditional)
  ```yaml
  on:
      pull_request:
          types: [merged]
  jobs:
      post-merge:
  ``` 
- C.  Specify the `pull_request` activity type as `merged`, and use a job-level conditional to check if `github.event.pull_request.merged` is true
  ```yaml
  on:
      pull_request:
          types: [merged]
  jobs:
      post-merge:
          if: github.event.pull_request.merged == true
  ``` 
- D.  Specify the the `pull_request` activity type as `closed` and use a job-level conditional to check if `github.ref` is equal to the merge branch of the pull request.
  ```yaml
  on:
      pull_request:
          types: [closed]
  jobs:
      post-merge: 
          if: ${{ github.ref == github.event.pull_request.base.ref }}
  ``` 
- E. Specify the the `pull_request` activity type as `closed` (no need for a job-level conditional)
  ```yaml
  on:
      pull_request:
          types: [closed]
  jobs:
      post-merge:
  ``` 

**Type:** *single*

---

## Q159

Which of the following are true when comparing the pull_request and pull_request_target events?

- A. Workflows will not run on `pull_request_target` activity if there is a merge conflict
- B. Workflows will not run on `pull_request` activity if there is a merge conflict
- C. Both `pull_request` and `pull_request_target` events have default activity types of `opened`, `synchronize`, and `reopened`.
- D. `pull_request` should be used with caution, since PRs from forks will allow the workflow to access all secrets within the repository due to being associated with the default branch.
- E. The `pull_request_target` event should be used when you want to run code contained in a PR's changed files, to do things like performing CI checks or running test suites.
- F. The `pull_request` event runs within the context of the merge commit, while `pull_request_target` runs in the context of the default branch of the base repository.

**Type:** *multi-select (3 correct)*

---

## Q160

Why should you use OIDC when connecting a workflow to cloud providers?

- A. Cloud providers require the use of OIDC.
- B. Using OIDC within a workflow will automatically save that workflow's logs in cloud storage
- C. Using OIDC allows you to circumvent setting up trust policies with cloud providers
- D. OIDC involves the generation and use of short-lived tokens, which is more secure
- E. OIDC generates JSON web tokens (JWTs) that can be used across workflow jobs
- F. OIDC prevents you from having to keep cloud credentials as long-lived GitHub secrets 

**Type:** *multi-select (2 correct)*

---

## Q161

How do workflows integrate with OIDC after a trust relationship has been established?

- A. The `on: OIDC_request` event trigger requests a cloud access token from GitHub's cloud access provider. The token is then validated by the cloud provider, which allows the workflow access to cloud resources.
- B. A workflow job requests an OIDC token from GitHub's OIDC provider. The OIDC token is then validated by the cloud provider, which then provides a cloud-access token so the workflow can access cloud resources.
- C. A workflow job requests an cloud access token from GitHub's cloud access provider. The token is then validated by the cloud provider, which then provides a OIDC token so the workflow can access cloud resources.
- D. After adding a workflow to the "OIDC-allowed workflows" list in the repository settings, workflows will automatically create OIDC and cloud access tokens on their own behalf. These tokens can then be used immediately in the workflow to interface with cloud providers
- E. The `on: OIDC_request` event trigger requests an OIDC token from GitHub's OIDC provider. The token is then validated by the cloud provider, which allows the workflow access to cloud resources.

**Type:** *single*

---

## Q162

Mercedes wants to publish a Docker container action she has created to the GitHub Actions Marketplace. What files does she need at a minimum to do so?

- A. `README.md`
- B. A `Dockerfile`, if the image is to be referenced from an image registry
- C. `CONTRIBUTING.md`
- D. `action.yml`
- E. A `Dockerfile`, if the image is built as part of the action during the workflow run
- F. `.dockerignore`

**Type:** *multi-select (2 correct)*

---

## Q163

Annette needs to write a workflow to publish a custom `npm` package that only members in her private organization will use. What should her workflow include?

- A. An `on:registry_package` event with `types:[published]` 
- B. A token with `admin:packages` permissions
- C. A token with `write:packages` permissions 
- D. Communication logic with the corresponding GitHub Packages registry `https://npm.pkg.github.com`
- E. Logic to publish to GitHub Packages
- F. An `on:registry_package` event with no activity types specified

**Type:** *multi-select (3 correct)*

---

## Q164

At what levels can `if:` be used in workflows?

- A. Workflow-level
- B. Step-level
- C. Job-level
- D. Environment-level
- E. Organization-level

**Type:** *multi-select (2 correct)*

---

## Q165

How does `repository_dispatch` enable systems outside of GitHub to trigger a workflow?

- A. The external system makes a POST request to the GitHub API to create a repository dispatch event.
- B. The workflow is triggered by the creation of a repository dispatch event 
- C. The external system makes a PUT request to the GitHub API to create a repository dispatch event
- D. The workflow is triggered by a POST request to the workflow using the following endpoint `/repos/OWNER/REPO/actions/workflows/<WORKFLOW_ID>/dispatches` 
- E. The `on.repository_dispatch.types` workflow key corresponds to the `event_type` parameter in the request payload, restricting the workflow to only trigger on relevant external events 
- F. The `on.repository_dispatch.event_types` workflow key corresponds to the `event_type` parameter in the request payload, restricting the workflow to only trigger on relevant external events

**Type:** *multi-select (3 correct)*

---

## Q166

JavaScript actions and `actions/github-script` both use JavaScript. Why should you use `actions/github-script` versus creating your own JavaScript action?

- A. JavaScript actions should be used when you want a custom reusable action to be used across repositories 
- B. JavaScript actions should be used when you want a low-overhead solution to making GitHub API calls.
- C. `actions/github-script` should be used when you need to utilize a fine-tuned Node.js environment with several specific dependencies
- D. JavaScript actions should be used for short inline scripts
- E. `actions/github-script` should be used for short inline scripts
- F. `actions/github-script` should be used when you want to use a pre-authenticated client to interact with the GitHub API.

**Type:** *multi-select (3 correct)*

---

## Q167

Hilda needs access to an artifact generated by a recent workflow run, but the workflow file itself has since been deleted. Will she still be able to recover the artifact?

- A. Yes, but only if she has administrator privileges
- B. No, because while workflow runs will remain after a workflow is deleted, generated artifacts become corrupted
- C. No, because deleting a workflow automatically deletes its runs and generated artifacts
- D. Yes, because deleting a workflow does not automatically delete its runs and generated artifacts

**Type:** *single*

---

## Q168

Which keys are required when making an `action.yml` file?

- A. `runs`
- B. `author`
- C. `inputs`
- D. `description`
- E. `name`
- F. `outputs`

**Type:** *multi-select (3 correct)*

---

## Q169

Manuela is setting up self-hosted runners for her organization, which has heavily restricted communication with IP addresses. How can she ensure the self-hosted runners can communicate with GitHub?

- A. Selecting the 'Allow access from self-hosted runners' checkbox in the organization's IP allow list settings
- B. Adding the `.ip-exception` file to the top-level of the self-hosted runner's directory structure
- C. Switch to GitHub-hosted standard runners, since self-hosted runners will be blocked if IP allow lists are enabled
- D. Adding the self-hosted runners' IP address(es) to the organization's IP allow list
- E. Adding the self-hosted runners' operating system to the organization's operating system allow list

**Type:** *single*

---

## Q170

Observe the values in `runs-on` key as seen in the below workflow job. Which is true regarding how the  the job will run?

```yaml
jobs:
    fire_emblem_deploy:
        name: "Deploy the 'Fire Emblem' application"
        runs-on: [self-hosted,nes,linux]
```

- A. The job will still be able to run on GitHub-hosted runners, since they can have custom labels applied to them
- B. The job will run on a runner (self-hosted or GitHub-hosted, whichever is first available) with the name `self-hosted,nes,linux`
- C. The job will run on a self-hosted runner that has any of the labels applied.
- D. The job will run on a self-hosted runner that has all the labels applied.

**Type:** *single*

---

## Q171

Why would you re-run a workflow versus generating a new workflow run?

- A. Re-running a workflow ensures `GITHUB_ACTOR` is updated, so it is unambiguous as to who re-ran the workflow
- B. Re-running a workflow means the workflow jobs run in the same context of the commit SHA and git ref of the original event that triggered the job
- C. Re-running a workflow lets you re-run failed workflow jobs, as opposed to generating a new run which will run all jobs.
- D. Re-running a workflow allows you to enable extra debug logging for the selected job(s).
- E. Re-running a workflow ensures `GITHUB_TRIGGERING_ACTOR` remains unchanged, so it is unambiguous as to who originally triggered the workflow
- F. Re-running a workflow overwrites the failing job runs, making runs appear more straightforward.

**Type:** *multi-select (3 correct)*

---

## Q172

Ingrid's organization has a subset of self-hosted Linux runners that should only be used by certain repositories. What is the best approach for her to enforce this behavior?

- A. Create a new runner label, add the labels to the runners, then select which repositories are allowed access to the label in the label settings.
- B. Create a new runner group, select "Linux" as the OS, and use glob patterns to define which repositories are allowed access in the group settings.  
- C. Create a new runner group, add the runners to the group, then select which repositories are allowed access to the group in the group settings.
- D. Create a new runner label, add the labels to the runners, then make sure all workflows in the repositories have that label included in their `runs-on` field.

**Type:** *single*

---

## Q173

An organization has several repositories that share a specialized Node.js environment hosted on a private network. The organization's next objective involves the setup of node-locking software within that network. Which of the following would best suit the organization's needs when it comes to executing workflows?

- A. GitHub-hosted runners, using `runs-on: [node<version>]` (`<version>` being the desired Node version) in all workflows.
- B. GitHub-hosted runners set up at the organization-level
- C. Self-hosted runners set up at the organization-level
- D. GitHub-hosted runners, with all workflows utilizing `actions/setup-node`
- E. One self-hosted runner per repository, set up at the repository level

**Type:** *single*

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

- A. The reusable workflow will create an issue in the repository titled `"Issue Report"`
- B. Both the caller and reusable workflow will not get called, because `issues` is not an available trigger for GitHub Actions. 
- C. The reusable workflow will not be called, since reusable workflows must be in a subfolder of `.github/workflows`
- D. The reusable workflow will return an error, since the job that called it only has `contents:read` permissions

**Type:** *single*

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

- A. The Python script will not run, because `runs-on` does not have a value of `python`.
- B. The Python script will not run, because `actions/checkout` is not included in the workflow.
- C. The Python script will not run, because `actions/python-setup` is not the correct action for setting up Python.
- D. The Python script will run successfully, because the `chmod` command grants execute permissions to the script.

**Type:** *single*

---

## Q176

Judith has a workflow that should be triggered every time a commit is made to the repository. The repository is not always that active, so Judith desires the workflow to programmatically run once a week as a failsafe. What combination of events should she use to enforce this behavior?

- A. This is not possible: `schedule` cannot be combined with other events
- B. `push` and `weekly`
- C. `push` and `workflow_dispatch`
- D. `pull_request` (with `types:[closed]`) and `schedule`
- E. `push` and `schedule`

**Type:** *single*

---

## Q177

Your workflow must fire off at 12:00 AM every Monday and Friday. Which of the following snippets correlates to this behavior?

- A. 
  ```yaml
  on:
    workflow_schedule:
      - cron: '0 0 * * 1,5'
  ```
- B. 
  ```yaml
  on:
    workflow_call:
      - days: [Mon,Fri]
      - times: [00]
  ```
- C. 
  ```yaml
  on:
    workflow_schedule:
      - cron: '1,5 * * 0 0'
  ```
- D. 
  ```yaml
  on:
    schedule:
      - cron: '0 0 * * 1,5'
  ```
- E. 
  ```yaml
  on:
    schedule:
      - cron: '0 12 * * Mon,Fri'
  ```

**Type:** *single*

---

## Q178

You need to ensure that your `prod` environment requires manual approvals before deploys can proceed. Out of the following options, which are true regarding how this is set up?

- A. If you list required reviewers, all of them need to approve to continue with the deployment.
- B. Required reviewers need at least `write` access to the repository in order to approve.
- C. If you list required reviewers, only one of them needs to approve to continue with the deployment.
- D. You cannot prevent self-reviews, but you can set up alerts to see who triggered the deployment.
- E. Only individual users can be assigned as required reviewers, not teams.
- F. You can prevent self-reviews in the event the person who wants to deploy is also a required reviewer.

**Type:** *multi-select (2 correct)*

---

## Q179

You are considering a Marketplace action to utilize in your workflow. What are some aspects you can look for that indicate the action is trustworthy?

- A. The README is thorough in defining the purpose of the action and how it works
- B. The amount of Stars is low on the Marketplace page for the action
- C. The source code for the action has not been updated in a long time, indicating development on that action has finished
- D. A 'Verified Creator' badge on the Marketplace page for the action
- E. The `action.yml` is very brief

**Type:** *multi-select (2 correct)*

---
