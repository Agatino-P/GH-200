# GH-200 practice session 2026-07-04-a

Generated 2026-07-04 from `gh-200-ghcertified-bank-full-2026-06-24.md` — 138 questions, options shuffled and re-lettered.
Answers withheld: grade each commitment with `log_answer.py` (see QUIZ-PROTOCOL.md).

---

## Q041

When should you use `caching`?

- A. When you want to reuse files that do change often between jobs or workflow runs, such as build dependencies from a package management system.
- B. When you want to save files produced by a job to view after a workflow run has ended, such as built binaries or build logs.
- C. When you want to save binaries produced by a build job to use in a subsequent deploy job to deploy a new version of an application
- D. When you want to reuse files that don't change often between jobs or workflow runs, such as build dependencies from a package management system.

**Type:** *single*

---

## Q042

When should you use `artifacts`?

- A. Use artifacts to save files produced by a job to view after a workflow run has ended, such as test results or build logs.
- B. Use artifacts to save binaries produced by a build job to use in a subsequent deploy job to deploy a new version of an application
- C. Use artifacts to create new versions of your application together with release notes, mentions and/or contributors
- D. Use artifacts to reuse files that don't change often between jobs or workflow runs, such as build dependencies from a package management system.

**Type:** *multi-select (2 correct)*

---

## Q043

If a workflow runs on a `feature-a` branch, can it restore `caches` created in the default `main` branch?

- A. Yes but only if no files were changed on `feature-a` branch
- B. Yes, all branches can restore caches created on the default branch
- C. Yes, all caches can be accessed by workflows on any branch within the same repository
- D. No, caches can only be restored from the same branch

**Type:** *single*

---

## Q044

To access an `artifact` that was created in another, previously triggered workflow run you can:

- A. You cannot access `artifacts` that were created in a different workflow run
- B. Use the `actions/upload-artifact` action.
- C. Use the `actions/download-artifact` action and make sure the artifact is not expired
- D. Use the `actions/download-artifact` action with elevated permissions.

**Type:** *single*

---

## Q045

What should you use to store coverage reports or screenshots generated during a workflow that runs automated testing for a repository?

- A. Artifacts
- B. Packages
- C. Releases
- D. Caches

**Type:** *single*

---

## Q046

You can only upload a single file at a time when using `actions/upload-artifact` action

- A. False
- B. Only directories can be uploaded, not individual files
- C. True

**Type:** *single*

---

## Q047

In job `deploy`, if you want to access binaries (containing your application) that were created in job `build` you should

- A. upload the binaries as artifacts in `deploy` and download them in `build`
- B. cache the binaries in `deploy` and read the files from cache in `build`
- C. cache the binaries in `build` and read the files from cache in `deploy`
- D. upload the binaries as artifacts in `build` and download them in `deploy`

**Type:** *single*

---

## Q048

A job called `job2` is using artifacts created in `job1`. Therefore it's important to make sure `job1` finishes before `job2` starts looking for the artifacts. How should you create that dependency?

- A. create this dependency by defining `job2` after `job1` in the workflow's `.yaml` definition
- B. this dependency is created implicitly when using `actions/download-artifact` to download artifact from `job1`
- C. create this dependency using the `concurrency` keyword in `job2`
- D. create this dependency using the `needs` keyword in `job2`

**Type:** *single*

---

## Q049

Which is true about `Starter Workflows` ?

- A. Starter workflows cannot call reusable workflows
- B. They allow users to leverage ready-to-use (or requiring minimal changes) workflow templates
- C. Starter workflows are provided ready-to-use and cannot be modified or enhanced
- D. GitHub provides and maintains starter workflows for different categories, languages and tooling
- E. Your organization can create custom starter workflows for users in your organization
- F. Starter workflows are a paid GitHub feature

**Type:** *multi-select (3 correct)*

---

## Q050

Secrets and configuration variables can be scoped to:

- A. The entire organization, or selected repositories in an organization
- B. A single repository
- C. A specific workflow in a repository
- D. An environment in a repository
- E. An environment shared across multiple repositories
- F. Multiple repositories that do not share an organization/enterprise
- G. A specific job in a workflow

**Type:** *multi-select (3 correct)*

---

## Q051

What are the three types of Actions?

- A. `Docker container actions`, `JavaScript Actions`, `Composite Actions`
- B. `Docker container Actions`, `JavaScript Actions`, `Custom Actions`
- C. `Python Actions`, `JavaScript Actions`, `Custom Actions`
- D. `Docker container actions`, `Java Actions`, `Composite Actions`

**Type:** *single*

---

## Q052

Is this statement true? `Docker container actions are usually slower than JavaScript actions`

- A. False
- B. True

**Type:** *single*

---

## Q053

When creating a custom GitHub Action you have to store the source code in `.github/workflows` directory

- A. True
- B. Only if the action is reusable
- C. False
- D. Only for Docker container actions

**Type:** *single*

---

## Q054

When creating custom GitHub Actions - in what file does all the action `metadata` have to be defined?

Metadata examples: name, description, outputs or required inputs

- A. In the repository `README` file
- B. In the `action.yml` or `action.yaml` file in the action repository, but it is not required if the action is not meant to be shared and used by the public
- C. It's edited in GitHub Marketplace UI when published for sharing
- D. In the `action.yml` or `action.yaml` file in the action repository

**Type:** *single*

---

## Q055

A workflow was initially run on `commit A` and failed. You fixed the workflow with the subsequent `commit B`. When you re-run that workflow it will run with code from which commit?

- A. It will run with code from `commit A`
- B. It will run with code from `commit B`
- C. It will trigger two workflows, one with code from `commit A` and one with code from `commit B`
- D. You cannot re-run workflows in GitHub Actions. You have to trigger a new workflow which will run with latest changes

**Type:** *single*

---

## Q056

How can you require manual approvals by a maintainer if the workflow run is targeting the `production` environment?

- A. Setting the required reviewers in the `production` workflow
- B. Manual approvals are not supported by GitHub Actions
- C. Using branch protection rules
- D. Using deployment protection rules

**Type:** *single*

---

## Q057

Which is true about environments?

- A. Each job in a workflow can reference a maximum of two environments.
- B. Each workflow can reference a maximum of two environments.
- C. Each job in a workflow can reference a single environment.
- D. Each workflow can reference a single environment.

**Type:** *single*

---

## Q058

When using GitHub Actions to access resources in one of the cloud providers (such as AWS, Azure or GCP) the safest and recommended way to authenticate is

- A. Using OIDC
- B. Using Vault
- C. Storing access keys in `variables`
- D. Storing access keys in `secrets`

**Type:** *single*

---

## Q059

Your open-source publicly available repository contains a workflow with a `pull_request` event trigger. How can you require approvals for workflow runs triggered from forks of your repository?

- A. The workflow will not trigger for forks if using `pull_request` event. If you want to do that you should use `fork_pull_request` event trigger with `require-approval` flag.
- B. Setup required approvals for fork runs in the repository
- C. Setup branch protection rules for the repository
- D. Setup deployment protection rules for the repository

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

- A. `GITHUB_USER`
- B. `GITHUB_ACTOR`
- C. `GITHUB_ORGANIZATION`
- D. `GITHUB_REPOSITORY`
- E. `GITHUB_WORKFLOW`
- F. `GITHUB_TOKEN`

**Type:** *multi-select (3 correct)*

---

## Q062

Your organization defines a secret `SomeSecret`, however when you reference that secret in a workflow using `${{ secrets.SomeSecret }}` it provides a different value than expected. What may be the reason for that?

- A. The secret `SomeSecret` is also declared in enterprise scope
- B. You need to use the GitHub API to access organization scoped secrets
- C. The secret `SomeSecret` is also declared in repository scope
- D. `${{ secrets.SomeSecret }}` expression is only used for repository scoped secrets

**Type:** *single*

---

## Q063

Which is a correct way to print a debug message?

- A. `echo "::debug::Watch out here!"`
- B. `echo ":debug:Watch out here!"`
- C. `echo "::debug::message=Watch out here!"`
- D. `echo "Watch out here!" >> $GITHUB_DEBUG`

**Type:** *single*

---

## Q064

How can organizations which are using GitHub Enterprise Server enable automatic syncing of third party GitHub Actions hosted on GitHub.com to their GitHub Enterprise Server instance?

- A. GitHub Enterprise Server has access to all GitHub.com Actions by default
- B. Using GitHub Connect
- C. GitHub Enterprise Server (GHES) cannot use GitHub.com Actions because of its on-premise nature and no internet access.
- D. Using actions-sync tool

**Type:** *single*

---

## Q065

Where can you find network connectivity logs for a GitHub self-hosted-runner?

- A. In the `_diag` folder directly on the runner machine
- B. In the job run logs of a job that ran on that Runner
- C. On GitHub.com on that specific Runner's page
- D. In the job run logs of a job that ran on that Runner with debug logging enabled

**Type:** *single*

---

## Q066

How can you validate that your GitHub self-hosted-runner can access all required GitHub services?

- A. Using a GitHub provided script on the runner machine
- B. GitHub will validate the network connectivity automatically when the runner application is installed on the runner machine
- C. By using the predefined GitHub Actions workflow `network-connectivity.yml`
- D. By trying to access the runner machine by `ssh` to validate the network connectivity

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

- A. Set the secret `MY_SECRET` as a job level environment variable, then reference that environment variable to conditionally run that step
  ```yaml
  my-job:
    runs-on: ubuntu-latest
    env:
      my_secret: ${{ secrets.MY_SECRET }}
    steps:
      - if: ${{ env.my_secret != '' }}
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
- D. By creating the following conditional on job level
  ```yaml
  my-job:
    runs-on: ubuntu-latest
    if: ${{ secrets.MY_SECRET == '' }}
  ```

**Type:** *single*

---

## Q069

How can you use the GitHub API to download workflow run logs?

- A. `HEAD /repos/{owner}/{repo}/actions/runs/{run_id}/logs`
- B. `POST /repos/{owner}/{repo}/actions/runs/{run_id}/logs`
- C. `GET /repos/{owner}/{repo}/actions/runs/{run_id}/logs`
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

- A. By creating a environment secret with the name `ENVIRONMENT_API_KEY`
- B. By creating a environment secret with the name `OVERRIDE_API_KEY`
- C. By creating a repository secret with the name `OVERRIDE_API_KEY`
- D. By creating a repository secret with the name `REPOSITORY_API_KEY`
- E. By creating a enterprise secret with the name `OVERRIDE_API_KEY`
- F. By creating a enterprise secret with the same name `API_KEY`
- G. By creating a environment secret with the same name `API_KEY`
- H. By creating a repository secret with the same name `API_KEY`

**Type:** *multi-select (2 correct)*

---

## Q072

What components can be reused within a GitHub Organization?

- A. Artifacts
- B. Configuration Variables
- C. Environment Variables
- D. Self Hosted Runners
- E. Workflow Templates
- F. Cache
- G. Secrets

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
- B. 4
- C. 5
- D. 7

**Type:** *single*

---

## Q074

Which of the following default environment variables contains the full name (e.g `octocat/hello-world`) of the repository where the workflow is running?

- A. `GITHUB_REPOSITORY_OWNER_ID`
- B. `GITHUB_REPOSITORY_OWNER`
- C. `GITHUB_REPOSITORY`
- D. `GITHUB_REPOSITORY_ID`

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

- A. 50
- B. 20
- C. 10
- D. 1
- E. 5

**Type:** *single*

---

## Q077

What is a self-hosted runner?

- A. A self-hosted runner is a system to manage pull requests from users of the organization
- B. A self-hosted runner is a system that you deploy and manage to execute jobs from GitHub Actions on GitHub.com
- C. A self-hosted runner is a system to upload code to a private server
- D. A self-hosted runner is a system to be able to create workloads automatically

**Type:** *single*

---

## Q078

Which of the following is a correct statement about GitHub Workflows and Actions?

- A. Each workflow is composed of one or more jobs which is composed of one or more steps, and each step is an action or a script
- B. Each action is composed of one or more jobs which is composed of one or more steps, and each step is a workflow
- C. Each workflow is composed of one or more actions which is composed of one or more jobs, and each job is composed of one or more steps
- D. Each action is composed of one or more workflows which is composed of one or more jobs, and each job is composed of one or more steps

**Type:** *single*

---

## Q079

On which commit and branch do scheduled workflows run in GitHub Actions?

- A. Scheduled workflows run on the specific commit on the main branch.
- B. Scheduled workflows run on the latest commit on the repository default branch.
- C. Scheduled workflows run on the latest commit on the main branch.
- D. Scheduled workflows run on the specific commit on last modified branch.

**Type:** *single*

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
- B. set `working-directory` under `job`
  ```yaml
  defaults:
    run:
      shell: bash
  job:
    working-directory: ./scripts
  ```
- C. set `directory` under `defaults.run`
  ```yaml
  defaults:
    run:
      shell: bash
      directory: ./scripts
  ```
- D. set `directory` under `job`
  ```yaml
  defaults:
    run:
      shell: bash
  job:
    directory: ./scripts
  ```

**Type:** *single*

---

## Q081

How can you reuse a defined workflow in multiple repositories?

- A. By copying the workflow file to each repository
- B. By using workflow templates
- C. By creating a reusable action
- D. By defining the workflow in a central repository

**Type:** *multi-select (2 correct)*

---

## Q082

How can you ensure a job runs only on a specific branch?

- A. By using the runs-on filter
- B. By using the jobs filter
- C. By using the branches filter
- D. By using the branch keyword

**Type:** *single*

---

## Q083

What does the `needs` keyword do in a GitHub Actions workflow?

- A. Sets up the environment
- B. Defines environment variables
- C. Specifies the dependencies of a job
- D. Triggers a job based on an event

**Type:** *single*

---

## Q084

Which keyword allows you to define environment variables in a GitHub Actions workflow?

- A. secrets
- B. config
- C. env
- D. vars

**Type:** *single*

---

## Q085

What is the purpose of the `with` keyword in a GitHub Actions workflow?

- A. To specify input parameters for an action
- B. To trigger another workflow
- C. To define environment variables
- D. To set up dependencies

**Type:** *single*

---

## Q086

Which of the following GitHub Actions syntax is used to run multiple commands in a single step?

- A. Separating commands with a semicolon ;
- B. Using && to chain commands
- C. Using a multiline string with |
- D. Defining commands in an array

**Type:** *single*

---

## Q087

How can you cache dependencies to speed up workflow execution?

- A. Using the cache keyword
- B. By storing them in the repository
- C. By using the store keyword
- D. Using the actions/cache action

**Type:** *single*

---

## Q088

What does the `matrix` keyword do in a GitHub Actions workflow?

- A. Triggers workflows based on a schedule
- B. Defines secrets for the workflow
- C. Sets environment variables for the job
- D. Allows defining multiple job configurations to run in parallel

**Type:** *single*

---

## Q089

Which of the following can be used to limit the number of concurrent jobs running in a GitHub Actions workflow?

- A. limit
- B. parallelism
- C. max-jobs
- D. concurrency

**Type:** *single*

---

## Q090

What is the default timeout for a GitHub Actions job?

- A. 120 minutes
- B. 60 minutes
- C. 360 minutes
- D. 30 minutes

**Type:** *single*

---

## Q091

How can you specify the operating system for a job in GitHub Actions?

- A. Using the runs-on keyword
- B. Using the platform keyword
- C. Using the env keyword
- D. Using the os keyword

**Type:** *single*

---

## Q092

In a GitHub Actions workflow, how do you specify a specific version of Node.js to use in a job?

- A. 
  ```yaml
  uses: setup-node@v4
  with:
    node: 20
  ```
- B. 
  ```yaml
  uses: actions/node-setup@v4
  with:
    node-version: 20
  ```
- C. 
  ```yaml
  uses: actions/setup-node@v4
  with:
    node-version: 20
  ```
- D. 
  ```yaml
  uses: setup-node@v4
  with:
    version: 20
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

- A. bash
- B. cmd
- C. sh
- D. powershell

**Type:** *single*

---

## Q095

Which of the following statements are true about adding a self-hosted runner in GitHub Actions?

- A. You can add a self-hosted runner to a step
- B. You can add a self-hosted runner to an organization
- C. You can add a self-hosted runner to an enterprise
- D. You can add a self-hosted runner to a repository
- E. You can add a self-hosted runner to a workflow

**Type:** *multi-select (3 correct)*

---

## Q096

Select the default environment variable that contains the operating system of the runner executing the job

- A. `RUNNER_OS`
- B. `RUNNER_ARCH`
- C. `RUNNER_NAME`
- D. `GITHUB_RUNNER_OS`

**Type:** *single*

---

## Q097

How does the `actions/cache` action in GitHub Actions handle a cache miss?

- A. by terminating the workflow if a cache miss occurs
- B. by automatically creating a new cache if the job is completed successfully
- C. by searching for a cache in other repositories
- D. by requiring manual intervention to create a new cache

**Type:** *single*

---

## Q098

How can you specify the schedule of a GitHub actions workflow to run on weekdays only?

- A. use the on: schedule: weekdays event trigger
- B. use the on: schedule: cron event trigger
- C. it is not possible in GitHub actions
- D. add a condition in the workflow YAML for weekdays

**Type:** *single*

---

## Q099

What is the recommended approach for storing secrets larger than 48 KB?

- A. secrets larger than 48 KB cannot be stored
- B. encrypt and store secrets in the repository but keep the decryption passphrase as a secret
- C. store large secrets directly as repository secrets to avoid limitations
- D. avoid storing large secrets entirely to ensure security

**Type:** *single*

---

## Q100

Select status check functions in GitHub Actions

- A. `success()`, `always()`, `cancelled()` and `failure()`
- B. `status()`, `always()`, `cancelled()` and `failure()`
- C. `completed()`, `always()`, `cancelled()` and `failure()`
- D. `state()`, `always()`, `cancelled()` and `failure()`

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
    if: always()
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
    if: failure() && steps.run-tests.outcome == 'failure'
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
    if: steps.run-tests.outcome == 'failure'
    uses: actions/upload-artifact@v3
    with:
      name: test-report
      path: test-reports.html
  ```

**Type:** *single*

---

## Q102

Which context holds information about the event that triggered a workflow run?

- A. `jobs.<job_id>.result`
- B. `github.repository`
- C. `github.event`
- D. `github.job`

**Type:** *single*

---

## Q103

In GitHub Actions, if you define both branches and paths filter, what is the effect on the workflow execution?

- A. the workflow will run when either `branches` or `paths` are satisfied
- B. the workflow will not run when both `branches` and `paths` are satisfied
- C. the workflow will run when either `branches` or `paths` are satisfied, but will only apply the matching filter
- D. the workflow will only run when both `branches` and `paths` are satisfied

**Type:** *single*

---

## Q104

What is the recommended practice for treating environment variables in GitHub Actions, regardless of the operating system and shell used?

- A. use only uppercase letters for environment variable names
- B. ignore case sensitivity as GitHub Actions handles it automatically
- C. depend on the behavior of the operating system in use
- D. treat environment variables as case-sensitive

**Type:** *single*

---

## Q105

Which of the following statements accurately describes the behavior of workflow jobs referencing an environment's protection rules?

- A. workflow jobs will start if at least one protection rule passes
- B. workflow jobs will start immediately and protection rules are evaluated during execution
- C. workflow jobs won't start until all the environment's protection rules pass
- D. workflow jobs will fail if protection rules are configured

**Type:** *single*

---

## Q106

What is the purpose of the `restore-keys` parameter in `actions/cache` in GitHub Actions?

- A. indicate whether a cache hit occurred
- B. enable cross-OS cache functionality
- C. specify the location of the cached files
- D. provide alternative keys to use in case of a cache miss

**Type:** *single*

---

## Q107

Which variable would you set to `true` in order to enable step debug logging?

- A. `ACTIONS_WORKFLOW_DEBUG`
- B. `ACTIONS_STEP_DEBUG`
- C. `ACTIONS_RUNNER_DEBUG`
- D. `ACTIONS_JOB_DEBUG`

**Type:** *single*

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
          filter: [requested]
  ```
- D. 
  ```yaml
  on:
      check_run:
          type: [closed]
  ```

**Type:** *single*

---

## Q109

What is the purpose of the `timeout-minutes` keyword in a step?

- A. it limits the execution time for individual step
- B. it defines the time interval for individual commands within a step
- C. it sets the timeout for waiting on external events before proceeding to the next step
- D. it specifies the maximum duration a job is allowed to run

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

- A. `issue_comment`
- B. `issues`
- C. `comment`
- D. `issues.comment`

**Type:** *single*

---

## Q112

What level of access is required on a GitHub repository in order to delete log files from workflow runs?

- A. owner
- B. admin
- C. read
- D. write 

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

- A. the `production-deploy` job will be marked as skipped
- B. the `production-deploy` job will execute three steps
- C. the `production-deploy` job will error
- D. the `production-deploy` job will run if the `node-version` is `14`

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
- B. by using the `matrix.property` syntax
- C. by using the `context` keyword within the job configuration
- D. reference variables through the `matrix` context with syntax like`matrix.version` and `matrix.os`

**Type:** *single*

---

## Q115

What level of permission is required to re-run the workflows

- A. admin
- B. owner
- C. write 
- D. read

**Type:** *single*

---

## Q116

When can you delete workflow runs?

- A. Workflow runs can be deleted at any time, regardless of their status or age.
- B. Workflow runs cannot be deleted, but they can be archived.
- C. After the workflow run has completed, regardless of its age.
- D. After the workflow run has completed and at least 30 days have passed.

**Type:** *single*

---

## Q117

Who can bypass configured deployment protection rules to force deployment (by default)

- A. Anyone with repository read permission
- B. Anyone with repository write permission
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

- A. Provide `SKIP_WORKFLOW` in the commit message
- B. By including any one of the following keywords in the commit message or in the title of the pull-request
  ```yaml
  [skip ci]
  [ci skip]
  [no ci]
  [skip actions]
  [actions skip]
  ```
- C. The above workflow will run in every event of push or pull request in every case

**Type:** *single*

---

## Q119

How can you determine if an action is a container action by looking at its action.yml file?

- A. `runs.using` has `container` as value
- B. `runs.using` has `docker` as value
- C. `runs.using` has `Dockerfile` as value
- D. `runs.main` has `container` as value

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
    after: 'cleanup.sh'
  ```
- C. 
  ```yaml
  runs:
    using: 'docker'
    image: 'Dockerfile'
    entrypoint: 'entrypoint.sh'
    post: 'cleanup.sh'
  ```
- D. 
  ```yaml
  runs:
    using: 'docker'
    image: 'Dockerfile'
    entrypoint: 'entrypoint.sh'
    post-entrypoint: 'cleanup.sh'
  ```
- E. 
  ```yaml
  runs:
    using: 'docker'
    image: 'Dockerfile'
    entrypoint: 'entrypoint.sh'
    cleanup: 'cleanup.sh'
  ```

**Type:** *single*

---

## Q121

What’s true about default variables?

- A. Default environment variables can be accessed using the env context
- B. Most of the default environment variables have a corresponding context property
- C. Default environment variables are set by GitHub and not defined in a workflow
- D. Default environment variables always have the prefix “GITHUB_”
- E. You can add a new default environment variable adding the prefix “GITHUB_” to it
- F. Currently, the value of the default CI environment variable can be overwritten, but it's not guaranteed this will always be possible

**Type:** *multi-select (3 correct)*

---

## Q122

What are the scopes defined for custom variables in a workflow?

- A. The contents of a job within a workflow, by using `jobs.<job_id>.env`
- B. All the jobs within a workflow, by using `jobs.env`
- C. The entire workflow, by using `custom.env` at the top level of the workflow file
- D. The entire workflow, by using `env` at the top level of the workflow file
- E. A specific step within a job, by using `jobs.<job_id>.steps[*].env`
- F. A specific environment in the repository, by using `environment.<environment_id>.env` at the top level of the workflow file

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
- B. Create an input `MY_ACCESS_TOKEN`
  ```yaml
  with:
      repository: my-org/my-private-repo
      path: ./.github/actions/my-org/my-private-repo
      token: ${{ MY_ACCESS_TOKEN }}
  ```
- C. Leave as is since access tokens will be passed automatically
  ```yaml
  with:
      repository: my-org/my-private-repo
      path: ./.github/actions/my-org/my-private-repo
  ```
- D. Create a GitHub secret `MY_ACCESS_TOKEN`
  ```yaml
  with:
      repository: my-org/my-private-repo
      path: ./.github/actions/my-org/my-private-repo
      token: ${{ secrets.MY_ACCESS_TOKEN }}
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

- A. No jobs will run because the syntax is invalid.
- B. 4 jobs
- C. 7 jobs
- D. 5 jobs
- E. 6 jobs

**Type:** *single*

---

## Q125

At what levels can environment variables be defined ?

- A. Job level
- B. Action level
- C. Workflow level
- D. Step level

**Type:** *multi-select (3 correct)*

---

## Q126

How should a dependent job reference the `output1` value produced by a job named `job1` earlier in the same workflow?

- A. `${{depends.job1.output1}}`
- B. `${{needs.job1.outputs.output1}}`
- C. `${{needs.job1.output1}}`
- D. `${{job1.outputs.output1}}`

**Type:** *single*

---

## Q127

Which workflow command syntax correctly sets an environment variable named 'API_VERSION' with the value '2.1' for subsequent steps in a GitHub Actions job?

- A. `echo "API_VERSION=2.1" >> "$GITHUB_ENV"`
- B. `set-env name=API_VERSION value=2.1`
- C. `export API_VERSION=2.1 >> "$GITHUB_ENV"`
- D. `echo "API_VERSION=2.1" >> "$GITHUB_OUTPUT"`

**Type:** *single*

---

## Q128

A workflow is triggered when pull requests are reopened. Why might this be the cause?

- A. Branch protection rules were improperly configured.
- B. `on: schedule` was configured with `pull_requests: [reopened]`
- C. `types: [reopened]` is defined under the `pull_request` event. 
- D. No activity types are defined under the `pull_request` event.

**Type:** *multi-select (2 correct)*

---

## Q129

`GITHUB_TOKEN` can be used to check out any repository.

- A. False
- B. Only with elevated permissions
- C. True

**Type:** *single*

---

## Q130

Which of the following are true regarding workflow-level vs. job-level outputs blocks?

- A. A workflow-level `outputs` block should only be used in reusable workflows, not caller workflows.
- B. A reusable workflow can have both workflow-level and job-level `outputs` blocks.
- C. A workflow-level `outputs` block must have the following structure:
  ```
  outputs:
      <output-name>
          value: ${{ jobs.<job-name>.outputs.<output-name> }}
  ```
- D. Job-level `outputs` blocks should only be used in caller workflows, not reusable workflows.
- E. A job-level `outputs` block must have the following structure:
  ```
  outputs:
      <output-name>
          value: ${{ steps.<step-name>.outputs.<output-name> }}
  ```

**Type:** *multi-select (3 correct)*

---

## Q131

Which of the following are true regarding calling reusable workflows versus calling composite actions?

- A. Only reusable workflows can accept inputs.
- B. Composite actions must be called as a step within a job
- C. Composite actions are called via referencing the folder that contains their `action.yml` file.
- D. Reusable workflows must be called on workflow job level (not from step-level).
- E. Secrets can be passed to both reusable workflows and calling composite actions via the `uses.secrets` block.
- F. Reusable workflows can use a different runner type than the caller workflow, while composite actions cannot. 
- G. Reusable workflows are called via referencing the folder that contains their `action.yml` file.

**Type:** *multi-select (4 correct)*

---

## Q132

Which of the following are true regarding GitHub Enterprise Server (GHES)?

- A. GitHub Enterprise Server instances are self-hosted, compared to GitHub Enterprise Cloud (GHEC) which is hosted and managed by GitHub.
- B. Using GitHub Connect, users can follow a manual process to access GitHub.com actions. This process must be done once per desired action.
- C. GHES workflows cannot access GitHub.com nor GitHub Marketplace actions by default. 
- D. `actions/actions-sync` is primarily devoted to moving GitHub.com actions to a GHES instance.
- E. GHES is allowed to use enhanced versions of GitHub-hosted runners.

**Type:** *multi-select (3 correct)*

---

## Q133

Why use a commit SHA versus a tag to pin an action?

- A. Commit SHAs are more difficult to trace in an audit, making it difficult for bad actors to determine how an action's code factors in overall processes.
- B. Commit SHAs are more convenient to use as opposed to tags
- C. Commit SHAs are more secure
- D. Commit SHAs are immutable, whereas tags have the potential to be changed
- E. Commit SHAs are guaranteed to point to the exact same code every time, tags are not

**Type:** *multi-select (3 correct)*

---

## Q134

How do you run custom JavaScript scripts directly in a GitHub Actions workflow?

- A. In a JavaScript Action, set the `using` key to `'github-script'`
- B. Write the contents of a script block to the `GITHUB_SCRIPT` environmental variable
- C. By enabling the 'Allow custom JavaScript scripts' configuration in the Actions settings of an organization
- D. Via the `actions/github-script` action
- E. By enabling the 'Allow custom JavaScript scripts' configuration in the Actions settings of a repository

**Type:** *single*

---

## Q135

You have forked a repository to enhance a workflow that uses a secret to access a third-party application. You trigger the workflow before editing its code to get a baseline result, but find that the workflow fails. Why would this occur?

- A. When inheriting the secret from the original repository, there was an error during the fork that resulted in a malformed, invalid secret
- B. Forked repositories only inherit repository secrets, so the secret being used in the workflow must have been an organizational or environment secret.
- C. The inherited secret had a size larger than 48 KB
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

- A. Nothing needs to be done, since `jobs.<job_id>.strategy.matrix.fail-fast` has a default setting of `false`
- B. Nothing needs to be done, since `jobs.<job_id>.strategy.fail-fast` has a default setting of `false`
- C. There is no way to enforce this behavior, it cannot be worked around.
- D. Set `jobs.<job_id>.strategy.matrix.fail-fast` to `false`
- E. Set `jobs.<job_id>.strategy.fail-fast` to `false`

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

- A. 7
- B. 10
- C. 5
- D. 6

**Type:** *single*

---

## Q138

You want to create a workflow `Post-Deploy` that performs post-deploy related activity. What event trigger should the `Post-Deploy` workflow use so it runs automatically after a specified workflow is completed?

- A. `workflow_call`
- B. `workflow_dispatch`
- C. `workflow_trigger`
- D. `workflow_run`

**Type:** *single*

---

## Q139

In what ways can you enable runner diagnostic logging?

- A. Renaming the `_diag` directory of a self-hosted runner to `runner-diagnostic-logs`
- B. Re-running a workflow with `Enable debug logging enabled`
- C. By adding a `runner-diagnostic-logs` subfolder to the `_diag` directory of the self-hosted runner being used
- D. By adding a `ACTIONS_RUNNER_DEBUG` top-level folder to the workflow's repository
- E. Setting a secret or variable named `ACTIONS_RUNNER_DEBUG` to `true`

**Type:** *multi-select (2 correct)*

---

## Q140

You are writing a reusable workflow which has `branch-name` as an input. How can you conditionally run a step in that workflow if the branch name begins with 'smoke-test'?

- A. Use the built-in `startsWith` method in combination with `jobs.<job_id>.steps[*].if`
  ```yaml
      if: inputs.branch-name.startsWith('smoke-test')
  ``` 
- B. Use the built-in `startsWith` method in combination with `jobs.<job_id>.steps[*].if`
  ```yaml
      if: startsWith(inputs.branch-name, 'smoke-test')
  ```
- C. Use the `branches` filter under `workflow_call`
  ```yaml
  on:
    workflow_call:
      branches:
          - 'smoke-test/**'
  ```
- D. Use shell conditionals in combination with `jobs.<job_id>.steps[*].if`
  ```yaml
      if: [[ "${{inputs.branch-name}}" == "smoke-test"* ]]
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
- B. `hashFiles` is required for compatibility with Windows runners.
- C. When using `hashFiles` as part of a cache key, if there is a cache miss, `hashFiles` gives additional debug info.  
- D. If a cache key contains the dependencies file wrapped in `hashFiles`, the key changes when the dependencies file is updated, which helps keep it up to date.

**Type:** *single*

---

## Q142

Which of the following answers is correct regarding installation access tokens?

- A. The `actions/create-github-app-token` can be called within workflows to create an installation access token, but the installation access token can only be used in future runs of the workflow.
- B. Installation access tokens are short-lived tokens ideal for automation activities, but require setting up a Github App.
- C. The `actions/create-github-app-token` can be called within workflows to create an installation access token available for immediate use. 
- D. Installation access tokens cannot be configured to act on behalf of their associated Github App. 
- E. `GITHUB_TOKEN` is a type of installation access token.

**Type:** *multi-select (3 correct)*

---

## Q143

Your organization wants to lower the retention period for stored artifacts, citing storage concerns. How can this be done at an organizational level?

- A. This cannot be done at an organizational level. All workflows that utilize `actions/upload-artifact` must use the required `retention-days` input.
- B. This cannot be done: artifacts are strictly stored for 90 days across all systems implementing Github Actions. 
- C. By using self-hosted runners, creating a `.github/retention-policy.yml` file, and specifying the value of the `artifact-retention-period` key 
- D. By navigating to the organization's Actions settings and editing the value of the "Artifact and log retention" setting

**Type:** *single*

---

## Q144

How can you change the retention period for artifacts generated by a certain workflow?

- A. By utilizing the `retention-days` input in `actions/upload-artifact` 
- B. By navigating to the organization's Actions settings and editing the value of the "Artifact and log retention" setting
- C. In the workflow's repository, navigate to the Actions settings and editing the value of the "Artifact and log retention" setting for the workflow listed.
- D. By utilizing the `retention-days` input in `actions/download-artifact`

**Type:** *single*

---

## Q145

In what ways can you download an artifact?

- A. By using the `actions/upload-artifact` action in a workflow
- B. By remotely accessing self-hosted runners via SSH and accessing the `.github/artifacts` directory
- C. By downloading artifacts from the Github Actions UI workflow run
- D. By using a specific GitHub API endpoint
- E. By using the `actions/download-artifact` action in a workflow 

**Type:** *multi-select (3 correct)*

---

## Q146

Which statements are true regarding `github.ref` when the workflow is triggered by a `pull_request` event?

- A. In pull requests (regardless of merge status), `github.ref` is the SHA of the last merge commit on the `GITHUB_REF` branch.
- B. In pull requests that have been merged, `github.ref` refers to the fully-formed ref of the branch that was merged into.
- C. In pull requests that have not been merged, `github.ref` is the fully-formed ref of the pull request title. 
- D. In pull requests that have not been merged, `github.ref` refers to the fully-formed ref of the pull request merge branch/tag 
- E. In pull requests that have been merged, `github.ref` is the type of fully-formed ref that triggered the workflow run. The value will either be `branch`, `tag`, or `null` (if the ref was not fully-formed).
- F. In pull requests (regardless of merge status), `github.ref` refers to the pull request number 

**Type:** *multi-select (2 correct)*

---

## Q147

You have a base-64 encoded secret that you decode in a GitHub Actions workflow. How can you make sure the decoded secret does not show up in the workflow log accidentally?

- A. Using `add-mask` workflow command in jobs where the decoded secret may be utilized.
- B. Using the built-in `maskSecret` function to redact the decoded secret in instances where it may be utilized.
- C. Nothing needs to be done since Github Actions infrastructure automatically redacts decoded secrets.
- D. Avoiding the usage of print statements that contain the decoded secret, since this is the only way the decoded secret could appear in the workflow log

**Type:** *single*

---

## Q148

Which statement is true regarding `github.ref` when the workflow is triggered by a push event?

- A. In push events, `github.ref` is the description of the commit that triggered the workflow.
- B. In push events, `github.ref` is SHA of the commit that triggered the workflow.
- C. In push events, `github.ref` is the fully-formed ref of the branch or tag ref that was pushed. 
- D. In push events, `github.ref` is the message of the commit that triggered the workflow.
- E. In push events, `github.ref` is the type of fully-formed ref that triggered the workflow run. The value will either be `branch`, `tag`, or `null` (if the ref was not fully-formed).

**Type:** *single*

---

## Q149

What does writing to `GITHUB_STEP_SUMMARY` do?

```yaml
- name: "Write results of test suite"
  run: |
    echo "The results of the testing suite are:" >> $GITHUB_STEP_SUMMARY
```

- A. Adds this line to the built-in artifact `github-steps-summary.md`
- B. Adds this line to the job summary
- C. Prints this line as a step-level debug message
- D. Adds this line as a subtitle to the step name in the GitHub Actions UI

**Type:** *single*

---

## Q150

Dorothea is troubleshooting a workflow triggered by a push event and is interested in seeing details about the webhook. How can she view the entire payload of the webhook that triggered the workflow?

- A. Navigating to the "Webhooks" section of the repository settings 
- B. Printing the contents of the `github.event` object in a step
- C. Setting a secret or variable named `SHOW_EVENT_PAYLOAD` to `true`
- D. Checking the "Show event webhook payload" checkbox under the workflow run options.

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
- C. starts off empty and must be populated in order to save tools between runs
- D. starts with the same tools GitHub-hosted runners do, as well as a selected assortment of custom tools to enhance self-hosted runner management

**Type:** *single*

---

## Q153

Which of the following events can trigger a workflow that has not been merged to the default branch?

- A. `issues`
- B. `push`
- C. `pull_request`
- D. `star`
- E. `repository_dispatch`
- F. `issue_comment`

**Type:** *multi-select (2 correct)*

---

## Q154

When would you build a Docker container action to share in the GitHub Actions marketplace?

- A. Docker container actions allow you to utilize Docker without requiring an `action.yml` file
- B. Docker container actions ensure a consistent runtime environment and specific dependencies without users needing to handle these aspects themselves
- C. Docker container actions are an out-of-the-box, low-overhead action
- D. Docker container actions have fast startup speed on Windows and macOS runners
- E. Docker container actions are a bundle of steps within other workflows that run within the context of the calling workflow/action

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
- C. The `@daily` syntax was not used
- D. The workflow file must exist on the default branch in order to be triggered by the `schedule` event
- E. `schedule` cannot be the only event in the workflow. It must be paired with a repository-based event, such as `push`

**Type:** *single*

---

## Q156

In what ways can you delete workflow artifacts?

- A. By using the Github Actions UI to navigate to a workflow run and delete the artifacts individually
- B. By remotely accessing self-hosted runners via SSH, navigating to the `.github/artifacts` directory, and deleting the selected artifacts
- C. By setting the artifact retention period to 0 days
- D. By using the Github Actions UI to delete the workflow run that generated the artifacts
- E. By using a specific GitHub API endpoint
- F. By using the `actions/delete-artifact` action in a workflow 

**Type:** *multi-select (3 correct)*

---

## Q158

Petra is building a workflow whose sole job is named `post-merge`. How can she set up the job to be triggered upon a merged pull request?

- A.  Specify the `pull_request` activity type as `merged`, and use a job-level conditional to check if `github.event.pull_request.merged` is true
  ```yaml
  on:
      pull_request:
          types: [merged]
  jobs:
      post-merge:
          if: github.event.pull_request.merged == true
  ``` 
- B.  Specify the the `pull_request` activity type as `closed` and use a job-level conditional to check if `github.ref` is equal to the merge branch of the pull request.
  ```yaml
  on:
      pull_request:
          types: [closed]
  jobs:
      post-merge: 
          if: ${{ github.ref == github.event.pull_request.base.ref }}
  ``` 
- C.  Specify the `pull_request` activity type as `merged` (no need for a job-level conditional)
  ```yaml
  on:
      pull_request:
          types: [merged]
  jobs:
      post-merge:
  ``` 
- D.  Specify the `pull_request` activity type as `closed`, and use a job-level conditional to check if `github.event.pull_request.merged` is true
  ```yaml
  on:
      pull_request:
          types: [closed]
  jobs:
      post-merge:
          if: github.event.pull_request.merged == true
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

- A. Both `pull_request` and `pull_request_target` events have default activity types of `opened`, `synchronize`, and `reopened`.
- B. The `pull_request_target` event should be used when you want to run code contained in a PR's changed files, to do things like performing CI checks or running test suites.
- C. The `pull_request` event runs within the context of the merge commit, while `pull_request_target` runs in the context of the default branch of the base repository.
- D. `pull_request` should be used with caution, since PRs from forks will allow the workflow to access all secrets within the repository due to being associated with the default branch.
- E. Workflows will not run on `pull_request` activity if there is a merge conflict
- F. Workflows will not run on `pull_request_target` activity if there is a merge conflict

**Type:** *multi-select (3 correct)*

---

## Q160

Why should you use OIDC when connecting a workflow to cloud providers?

- A. OIDC involves the generation and use of short-lived tokens, which is more secure
- B. OIDC generates JSON web tokens (JWTs) that can be used across workflow jobs
- C. Using OIDC within a workflow will automatically save that workflow's logs in cloud storage
- D. OIDC prevents you from having to keep cloud credentials as long-lived GitHub secrets 
- E. Cloud providers require the use of OIDC.
- F. Using OIDC allows you to circumvent setting up trust policies with cloud providers

**Type:** *multi-select (2 correct)*

---

## Q161

How do workflows integrate with OIDC after a trust relationship has been established?

- A. A workflow job requests an cloud access token from GitHub's cloud access provider. The token is then validated by the cloud provider, which then provides a OIDC token so the workflow can access cloud resources.
- B. The `on: OIDC_request` event trigger requests a cloud access token from GitHub's cloud access provider. The token is then validated by the cloud provider, which allows the workflow access to cloud resources.
- C. After adding a workflow to the "OIDC-allowed workflows" list in the repository settings, workflows will automatically create OIDC and cloud access tokens on their own behalf. These tokens can then be used immediately in the workflow to interface with cloud providers
- D. A workflow job requests an OIDC token from GitHub's OIDC provider. The OIDC token is then validated by the cloud provider, which then provides a cloud-access token so the workflow can access cloud resources.
- E. The `on: OIDC_request` event trigger requests an OIDC token from GitHub's OIDC provider. The token is then validated by the cloud provider, which allows the workflow access to cloud resources.

**Type:** *single*

---

## Q162

Mercedes wants to publish a Docker container action she has created to the GitHub Actions Marketplace. What files does she need at a minimum to do so?

- A. A `Dockerfile`, if the image is built as part of the action during the workflow run
- B. `CONTRIBUTING.md`
- C. A `Dockerfile`, if the image is to be referenced from an image registry
- D. `action.yml`
- E. `README.md`
- F. `.dockerignore`

**Type:** *multi-select (2 correct)*

---

## Q163

Annette needs to write a workflow to publish a custom `npm` package that only members in her private organization will use. What should her workflow include?

- A. An `on:registry_package` event with no activity types specified
- B. A token with `write:packages` permissions 
- C. An `on:registry_package` event with `types:[published]` 
- D. Logic to publish to GitHub Packages
- E. A token with `admin:packages` permissions
- F. Communication logic with the corresponding GitHub Packages registry `https://npm.pkg.github.com`

**Type:** *multi-select (3 correct)*

---

## Q164

At what levels can `if:` be used in workflows?

- A. Organization-level
- B. Job-level
- C. Step-level
- D. Environment-level
- E. Workflow-level

**Type:** *multi-select (2 correct)*

---

## Q165

How does `repository_dispatch` enable systems outside of GitHub to trigger a workflow?

- A. The workflow is triggered by the creation of a repository dispatch event 
- B. The external system makes a PUT request to the GitHub API to create a repository dispatch event
- C. The `on.repository_dispatch.types` workflow key corresponds to the `event_type` parameter in the request payload, restricting the workflow to only trigger on relevant external events 
- D. The workflow is triggered by a POST request to the workflow using the following endpoint `/repos/OWNER/REPO/actions/workflows/<WORKFLOW_ID>/dispatches` 
- E. The external system makes a POST request to the GitHub API to create a repository dispatch event.
- F. The `on.repository_dispatch.event_types` workflow key corresponds to the `event_type` parameter in the request payload, restricting the workflow to only trigger on relevant external events

**Type:** *multi-select (3 correct)*

---

## Q166

JavaScript actions and `actions/github-script` both use JavaScript. Why should you use `actions/github-script` versus creating your own JavaScript action?

- A. `actions/github-script` should be used when you want to use a pre-authenticated client to interact with the GitHub API.
- B. JavaScript actions should be used for short inline scripts
- C. JavaScript actions should be used when you want a low-overhead solution to making GitHub API calls.
- D. `actions/github-script` should be used when you need to utilize a fine-tuned Node.js environment with several specific dependencies
- E. `actions/github-script` should be used for short inline scripts
- F. JavaScript actions should be used when you want a custom reusable action to be used across repositories 

**Type:** *multi-select (3 correct)*

---

## Q167

Hilda needs access to an artifact generated by a recent workflow run, but the workflow file itself has since been deleted. Will she still be able to recover the artifact?

- A. No, because while workflow runs will remain after a workflow is deleted, generated artifacts become corrupted
- B. Yes, but only if she has administrator privileges
- C. No, because deleting a workflow automatically deletes its runs and generated artifacts
- D. Yes, because deleting a workflow does not automatically delete its runs and generated artifacts

**Type:** *single*

---

## Q168

Which keys are required when making an `action.yml` file?

- A. `name`
- B. `description`
- C. `outputs`
- D. `author`
- E. `inputs`
- F. `runs`

**Type:** *multi-select (3 correct)*

---

## Q169

Manuela is setting up self-hosted runners for her organization, which has heavily restricted communication with IP addresses. How can she ensure the self-hosted runners can communicate with GitHub?

- A. Adding the self-hosted runners' IP address(es) to the organization's IP allow list
- B. Selecting the 'Allow access from self-hosted runners' checkbox in the organization's IP allow list settings
- C. Adding the `.ip-exception` file to the top-level of the self-hosted runner's directory structure
- D. Adding the self-hosted runners' operating system to the organization's operating system allow list
- E. Switch to GitHub-hosted standard runners, since self-hosted runners will be blocked if IP allow lists are enabled

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

- A. The job will run on a runner (self-hosted or GitHub-hosted, whichever is first available) with the name `self-hosted,nes,linux`
- B. The job will still be able to run on GitHub-hosted runners, since they can have custom labels applied to them
- C. The job will run on a self-hosted runner that has any of the labels applied.
- D. The job will run on a self-hosted runner that has all the labels applied.

**Type:** *single*

---

## Q171

Why would you re-run a workflow versus generating a new workflow run?

- A. Re-running a workflow lets you re-run failed workflow jobs, as opposed to generating a new run which will run all jobs.
- B. Re-running a workflow means the workflow jobs run in the same context of the commit SHA and git ref of the original event that triggered the job
- C. Re-running a workflow ensures `GITHUB_TRIGGERING_ACTOR` remains unchanged, so it is unambiguous as to who originally triggered the workflow
- D. Re-running a workflow allows you to enable extra debug logging for the selected job(s).
- E. Re-running a workflow ensures `GITHUB_ACTOR` is updated, so it is unambiguous as to who re-ran the workflow
- F. Re-running a workflow overwrites the failing job runs, making runs appear more straightforward.

**Type:** *multi-select (3 correct)*

---

## Q172

Ingrid's organization has a subset of self-hosted Linux runners that should only be used by certain repositories. What is the best approach for her to enforce this behavior?

- A. Create a new runner label, add the labels to the runners, then make sure all workflows in the repositories have that label included in their `runs-on` field.
- B. Create a new runner label, add the labels to the runners, then select which repositories are allowed access to the label in the label settings.
- C. Create a new runner group, select "Linux" as the OS, and use glob patterns to define which repositories are allowed access in the group settings.  
- D. Create a new runner group, add the runners to the group, then select which repositories are allowed access to the group in the group settings.

**Type:** *single*

---

## Q173

An organization has several repositories that share a specialized Node.js environment hosted on a private network. The organization's next objective involves the setup of node-locking software within that network. Which of the following would best suit the organization's needs when it comes to executing workflows?

- A. GitHub-hosted runners, with all workflows utilizing `actions/setup-node`
- B. GitHub-hosted runners set up at the organization-level
- C. GitHub-hosted runners, using `runs-on: [node<version>]` (`<version>` being the desired Node version) in all workflows.
- D. Self-hosted runners set up at the organization-level
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

- A. The reusable workflow will return an error, since the job that called it only has `contents:read` permissions
- B. The reusable workflow will not be called, since reusable workflows must be in a subfolder of `.github/workflows`
- C. The reusable workflow will create an issue in the repository titled `"Issue Report"`
- D. Both the caller and reusable workflow will not get called, because `issues` is not an available trigger for GitHub Actions. 

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

- A. The Python script will not run, because `actions/checkout` is not included in the workflow.
- B. The Python script will not run, because `actions/python-setup` is not the correct action for setting up Python.
- C. The Python script will not run, because `runs-on` does not have a value of `python`.
- D. The Python script will run successfully, because the `chmod` command grants execute permissions to the script.

**Type:** *single*

---

## Q176

Judith has a workflow that should be triggered every time a commit is made to the repository. The repository is not always that active, so Judith desires the workflow to programmatically run once a week as a failsafe. What combination of events should she use to enforce this behavior?

- A. `push` and `weekly`
- B. This is not possible: `schedule` cannot be combined with other events
- C. `push` and `schedule`
- D. `pull_request` (with `types:[closed]`) and `schedule`
- E. `push` and `workflow_dispatch`

**Type:** *single*

---

## Q177

Your workflow must fire off at 12:00 AM every Monday and Friday. Which of the following snippets correlates to this behavior?

- A. 
  ```yaml
  on:
    workflow_call:
      - days: [Mon,Fri]
      - times: [00]
  ```
- B. 
  ```yaml
  on:
    schedule:
      - cron: '0 0 * * 1,5'
  ```
- C. 
  ```yaml
  on:
    workflow_schedule:
      - cron: '0 0 * * 1,5'
  ```
- D. 
  ```yaml
  on:
    schedule:
      - cron: '0 12 * * Mon,Fri'
  ```
- E. 
  ```yaml
  on:
    workflow_schedule:
      - cron: '1,5 * * 0 0'
  ```

**Type:** *single*

---

## Q178

You need to ensure that your `prod` environment requires manual approvals before deploys can proceed. Out of the following options, which are true regarding how this is set up?

- A. Required reviewers need at least `write` access to the repository in order to approve.
- B. You cannot prevent self-reviews, but you can set up alerts to see who triggered the deployment.
- C. Only individual users can be assigned as required reviewers, not teams.
- D. If you list required reviewers, only one of them needs to approve to continue with the deployment.
- E. You can prevent self-reviews in the event the person who wants to deploy is also a required reviewer.
- F. If you list required reviewers, all of them need to approve to continue with the deployment.

**Type:** *multi-select (2 correct)*

---

## Q179

You are considering a Marketplace action to utilize in your workflow. What are some aspects you can look for that indicate the action is trustworthy?

- A. A 'Verified Creator' badge on the Marketplace page for the action
- B. The README is thorough in defining the purpose of the action and how it works
- C. The amount of Stars is low on the Marketplace page for the action
- D. The source code for the action has not been updated in a long time, indicating development on that action has finished
- E. The `action.yml` is very brief

**Type:** *multi-select (2 correct)*

---
