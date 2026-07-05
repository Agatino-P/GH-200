# GH-200 practice session 2026-07-05-a

Generated 2026-07-05 from `gh-200-ghcertified-bank-full-2026-06-24.md` — 56 questions, options shuffled and re-lettered.
Answers withheld: grade each commitment with `log_answer.py` (see QUIZ-PROTOCOL.md).

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
- C. Yes
- D. No

**Type:** *single*

---

## Q022

A workflow that has only `workflow_dispatch` event trigger can be triggered using GitHub's REST API

- A. True
- B. False

**Type:** *single*

---

## Q027

What are the valid use cases for using **defaults**?

- A. Using defaults.run on workflow level to set default shell (e.g bash) for an entire workflow
- B. Using defaults.run on job level to set default working-directory for all steps in a single job
- C. Using defaults.run on step level to set default shell (e.g bash) for that single step
- D. Using defaults.env on job level to set default environment variables for all steps in a single job
- E. Using defaults.env on workflow level to set default environment variables for an entire workflow

**Type:** *multi-select (2 correct)*

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

- A. Set `jobs.example_matrix.strategy.concurrency` to 2
- B. It's not possible, a matrix will always run all of the jobs in parallel if there are runners available
- C. Use GitHub's REST API to check if the job count is lesser than 2
- D. Set `jobs.example_matrix.strategy.max-parallel` to 2

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

- A. `run: echo "$action_state"`
- B. `run: echo "${{ action_state }}"`
- C. `run: echo "${{ steps.step_one.outputs.action_state }}"`
- D. `run: echo "$steps.step_one.outputs.action_state"`

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
- C. All secrets available to `workflow A` will be also available to `workflow B`, but not to `workflow C`
- D. All secrets available to `workflow A` will be also available to `workflow B` and `workflow C`

**Type:** *single*

---

## Q041

When should you use `caching`?

- A. When you want to save binaries produced by a build job to use in a subsequent deploy job to deploy a new version of an application
- B. When you want to reuse files that don't change often between jobs or workflow runs, such as build dependencies from a package management system.
- C. When you want to reuse files that do change often between jobs or workflow runs, such as build dependencies from a package management system.
- D. When you want to save files produced by a job to view after a workflow run has ended, such as built binaries or build logs.

**Type:** *single*

---

## Q042

When should you use `artifacts`?

- A. Use artifacts to create new versions of your application together with release notes, mentions and/or contributors
- B. Use artifacts to save files produced by a job to view after a workflow run has ended, such as test results or build logs.
- C. Use artifacts to save binaries produced by a build job to use in a subsequent deploy job to deploy a new version of an application
- D. Use artifacts to reuse files that don't change often between jobs or workflow runs, such as build dependencies from a package management system.

**Type:** *multi-select (2 correct)*

---

## Q043

If a workflow runs on a `feature-a` branch, can it restore `caches` created in the default `main` branch?

- A. Yes, all branches can restore caches created on the default branch
- B. Yes, all caches can be accessed by workflows on any branch within the same repository
- C. No, caches can only be restored from the same branch
- D. Yes but only if no files were changed on `feature-a` branch

**Type:** *single*

---

## Q046

You can only upload a single file at a time when using `actions/upload-artifact` action

- A. False
- B. Only directories can be uploaded, not individual files
- C. True

**Type:** *single*

---

## Q059

Your open-source publicly available repository contains a workflow with a `pull_request` event trigger. How can you require approvals for workflow runs triggered from forks of your repository?

- A. Setup required approvals for fork runs in the repository
- B. Setup branch protection rules for the repository
- C. The workflow will not trigger for forks if using `pull_request` event. If you want to do that you should use `fork_pull_request` event trigger with `require-approval` flag.
- D. Setup deployment protection rules for the repository

**Type:** *single*

---

## Q064

How can organizations which are using GitHub Enterprise Server enable automatic syncing of third party GitHub Actions hosted on GitHub.com to their GitHub Enterprise Server instance?

- A. GitHub Enterprise Server has access to all GitHub.com Actions by default
- B. Using actions-sync tool
- C. Using GitHub Connect
- D. GitHub Enterprise Server (GHES) cannot use GitHub.com Actions because of its on-premise nature and no internet access.

**Type:** *single*

---

## Q065

Where can you find network connectivity logs for a GitHub self-hosted-runner?

- A. In the job run logs of a job that ran on that Runner
- B. In the job run logs of a job that ran on that Runner with debug logging enabled
- C. In the `_diag` folder directly on the runner machine
- D. On GitHub.com on that specific Runner's page

**Type:** *single*

---

## Q066

How can you validate that your GitHub self-hosted-runner can access all required GitHub services?

- A. GitHub will validate the network connectivity automatically when the runner application is installed on the runner machine
- B. By trying to access the runner machine by `ssh` to validate the network connectivity
- C. Using a GitHub provided script on the runner machine
- D. By using the predefined GitHub Actions workflow `network-connectivity.yml`

**Type:** *single*

---

## Q067

Which is the correct way of triggering a job only if configuration variable `MY_VAR` has the value of `MY_VALUE`?

- A. It's not possible because configuration variables cannot be used in job level `if` conditionals
- B. By creating the following conditional on job level
  ```yaml
  my-job:
    if: ${{ vars.MY_VAR == 'MY_VALUE' }}
  ```
- C. By creating the following conditional on job level
  ```yaml
  my-job:
    if: ${{ vars.MY_VAR }} == 'MY_VALUE'
  ```
- D. It's not possible because configuration variables cannot be used in `if` conditionals

**Type:** *single*

---

## Q070

How can you use the GitHub API to create or update a repository secret?

- A. `PUT /repos/{owner}/{repo}/actions/secrets/{secret_name}`
- B. `GET /repos/{owner}/{repo}/actions/secrets/{secret_name}`
- C. `POST /repos/{owner}/{repo}/actions/secrets/{secret_name}`
- D. `HEAD /repos/{owner}/{repo}/actions/secrets/{secret_name}`

**Type:** *single*

---

## Q071

How can you override an organization-level GitHub Secret `API_KEY` with a different value when working within a repository?

- A. By creating a enterprise secret with the name `OVERRIDE_API_KEY`
- B. By creating a enterprise secret with the same name `API_KEY`
- C. By creating a environment secret with the name `ENVIRONMENT_API_KEY`
- D. By creating a repository secret with the name `REPOSITORY_API_KEY`
- E. By creating a environment secret with the name `OVERRIDE_API_KEY`
- F. By creating a environment secret with the same name `API_KEY`
- G. By creating a repository secret with the name `OVERRIDE_API_KEY`
- H. By creating a repository secret with the same name `API_KEY`

**Type:** *multi-select (2 correct)*

---

## Q072

What components can be reused within a GitHub Organization?

- A. Cache
- B. Workflow Templates
- C. Artifacts
- D. Secrets
- E. Configuration Variables
- F. Self Hosted Runners
- G. Environment Variables

**Type:** *multi-select (4 correct)*

---

## Q081

How can you reuse a defined workflow in multiple repositories?

- A. By defining the workflow in a central repository
- B. By creating a reusable action
- C. By using workflow templates
- D. By copying the workflow file to each repository

**Type:** *multi-select (2 correct)*

---

## Q086

Which of the following GitHub Actions syntax is used to run multiple commands in a single step?

- A. Separating commands with a semicolon ;
- B. Defining commands in an array
- C. Using a multiline string with |
- D. Using && to chain commands

**Type:** *single*

---

## Q089

Which of the following can be used to limit the number of concurrent jobs running in a GitHub Actions workflow?

- A. max-jobs
- B. parallelism
- C. limit
- D. concurrency

**Type:** *single*

---

## Q093

How do you reference a secret stored in GitHub Secrets in a workflow?

- A. ${{ config.SECRET_NAME }}
- B. ${{ env.SECRET_NAME }}
- C. ${{ secrets.SECRET_NAME }}
- D. ${{ secret.SECRET_NAME }}

**Type:** *single*

---

## Q095

Which of the following statements are true about adding a self-hosted runner in GitHub Actions?

- A. You can add a self-hosted runner to a step
- B. You can add a self-hosted runner to a workflow
- C. You can add a self-hosted runner to a repository
- D. You can add a self-hosted runner to an enterprise
- E. You can add a self-hosted runner to an organization

**Type:** *multi-select (3 correct)*

---

## Q098

How can you specify the schedule of a GitHub actions workflow to run on weekdays only?

- A. use the on: schedule: cron event trigger
- B. use the on: schedule: weekdays event trigger
- C. it is not possible in GitHub actions
- D. add a condition in the workflow YAML for weekdays

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
    if: always()
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
    if: steps.run-tests.outcome == 'failure'
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
    if: failure() && steps.run-tests.outcome == 'failure'
    uses: actions/upload-artifact@v3
    with:
      name: test-report
      path: test-reports.html
  ```

**Type:** *single*

---

## Q104

What is the recommended practice for treating environment variables in GitHub Actions, regardless of the operating system and shell used?

- A. use only uppercase letters for environment variable names
- B. depend on the behavior of the operating system in use
- C. treat environment variables as case-sensitive
- D. ignore case sensitivity as GitHub Actions handles it automatically

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
          filter: [requested]
  ```
- C. 
  ```yaml
  on:
      check_run:
          types: [rerequested, completed]
  ```
- D. 
  ```yaml
  on:
      check_run:
          type: [closed]
  ```

**Type:** *single*

---

## Q115

What level of permission is required to re-run the workflows

- A. owner
- B. read
- C. admin
- D. write 

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
    cleanup: 'cleanup.sh'
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
    after-entrypoint: 'cleanup.sh'
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
    post: 'cleanup.sh'
  ```

**Type:** *single*

---

## Q121

What’s true about default variables?

- A. Most of the default environment variables have a corresponding context property
- B. Default environment variables are set by GitHub and not defined in a workflow
- C. You can add a new default environment variable adding the prefix “GITHUB_” to it
- D. Default environment variables always have the prefix “GITHUB_”
- E. Currently, the value of the default CI environment variable can be overwritten, but it's not guaranteed this will always be possible
- F. Default environment variables can be accessed using the env context

**Type:** *multi-select (3 correct)*

---

## Q122

What are the scopes defined for custom variables in a workflow?

- A. The contents of a job within a workflow, by using `jobs.<job_id>.env`
- B. All the jobs within a workflow, by using `jobs.env`
- C. A specific environment in the repository, by using `environment.<environment_id>.env` at the top level of the workflow file
- D. A specific step within a job, by using `jobs.<job_id>.steps[*].env`
- E. The entire workflow, by using `custom.env` at the top level of the workflow file
- F. The entire workflow, by using `env` at the top level of the workflow file

**Type:** *multi-select (3 correct)*

---

## Q125

At what levels can environment variables be defined ?

- A. Action level
- B. Job level
- C. Step level
- D. Workflow level

**Type:** *multi-select (3 correct)*

---

## Q130

Which of the following are true regarding workflow-level vs. job-level outputs blocks?

- A. A workflow-level `outputs` block must have the following structure:
  ```
  outputs:
      <output-name>
          value: ${{ jobs.<job-name>.outputs.<output-name> }}
  ```
- B. A reusable workflow can have both workflow-level and job-level `outputs` blocks.
- C. A workflow-level `outputs` block should only be used in reusable workflows, not caller workflows.
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

- A. Reusable workflows must be called on workflow job level (not from step-level).
- B. Composite actions are called via referencing the folder that contains their `action.yml` file.
- C. Secrets can be passed to both reusable workflows and calling composite actions via the `uses.secrets` block.
- D. Reusable workflows can use a different runner type than the caller workflow, while composite actions cannot. 
- E. Reusable workflows are called via referencing the folder that contains their `action.yml` file.
- F. Only reusable workflows can accept inputs.
- G. Composite actions must be called as a step within a job

**Type:** *multi-select (4 correct)*

---

## Q132

Which of the following are true regarding GitHub Enterprise Server (GHES)?

- A. GitHub Enterprise Server instances are self-hosted, compared to GitHub Enterprise Cloud (GHEC) which is hosted and managed by GitHub.
- B. `actions/actions-sync` is primarily devoted to moving GitHub.com actions to a GHES instance.
- C. GHES workflows cannot access GitHub.com nor GitHub Marketplace actions by default. 
- D. Using GitHub Connect, users can follow a manual process to access GitHub.com actions. This process must be done once per desired action.
- E. GHES is allowed to use enhanced versions of GitHub-hosted runners.

**Type:** *multi-select (3 correct)*

---

## Q139

In what ways can you enable runner diagnostic logging?

- A. Setting a secret or variable named `ACTIONS_RUNNER_DEBUG` to `true`
- B. By adding a `runner-diagnostic-logs` subfolder to the `_diag` directory of the self-hosted runner being used
- C. Re-running a workflow with `Enable debug logging enabled`
- D. Renaming the `_diag` directory of a self-hosted runner to `runner-diagnostic-logs`
- E. By adding a `ACTIONS_RUNNER_DEBUG` top-level folder to the workflow's repository

**Type:** *multi-select (2 correct)*

---

## Q142

Which of the following answers is correct regarding installation access tokens?

- A. Installation access tokens cannot be configured to act on behalf of their associated Github App. 
- B. The `actions/create-github-app-token` can be called within workflows to create an installation access token, but the installation access token can only be used in future runs of the workflow.
- C. The `actions/create-github-app-token` can be called within workflows to create an installation access token available for immediate use. 
- D. `GITHUB_TOKEN` is a type of installation access token.
- E. Installation access tokens are short-lived tokens ideal for automation activities, but require setting up a Github App.

**Type:** *multi-select (3 correct)*

---

## Q144

How can you change the retention period for artifacts generated by a certain workflow?

- A. By navigating to the organization's Actions settings and editing the value of the "Artifact and log retention" setting
- B. In the workflow's repository, navigate to the Actions settings and editing the value of the "Artifact and log retention" setting for the workflow listed.
- C. By utilizing the `retention-days` input in `actions/upload-artifact` 
- D. By utilizing the `retention-days` input in `actions/download-artifact`

**Type:** *single*

---

## Q146

Which statements are true regarding `github.ref` when the workflow is triggered by a `pull_request` event?

- A. In pull requests that have not been merged, `github.ref` refers to the fully-formed ref of the pull request merge branch/tag 
- B. In pull requests (regardless of merge status), `github.ref` is the SHA of the last merge commit on the `GITHUB_REF` branch.
- C. In pull requests that have not been merged, `github.ref` is the fully-formed ref of the pull request title. 
- D. In pull requests (regardless of merge status), `github.ref` refers to the pull request number 
- E. In pull requests that have been merged, `github.ref` is the type of fully-formed ref that triggered the workflow run. The value will either be `branch`, `tag`, or `null` (if the ref was not fully-formed).
- F. In pull requests that have been merged, `github.ref` refers to the fully-formed ref of the branch that was merged into.

**Type:** *multi-select (2 correct)*

---

## Q147

You have a base-64 encoded secret that you decode in a GitHub Actions workflow. How can you make sure the decoded secret does not show up in the workflow log accidentally?

- A. Avoiding the usage of print statements that contain the decoded secret, since this is the only way the decoded secret could appear in the workflow log
- B. Using `add-mask` workflow command in jobs where the decoded secret may be utilized.
- C. Using the built-in `maskSecret` function to redact the decoded secret in instances where it may be utilized.
- D. Nothing needs to be done since Github Actions infrastructure automatically redacts decoded secrets.

**Type:** *single*

---

## Q148

Which statement is true regarding `github.ref` when the workflow is triggered by a push event?

- A. In push events, `github.ref` is SHA of the commit that triggered the workflow.
- B. In push events, `github.ref` is the description of the commit that triggered the workflow.
- C. In push events, `github.ref` is the message of the commit that triggered the workflow.
- D. In push events, `github.ref` is the type of fully-formed ref that triggered the workflow run. The value will either be `branch`, `tag`, or `null` (if the ref was not fully-formed).
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

- A. Adds this line as a subtitle to the step name in the GitHub Actions UI
- B. Adds this line to the job summary
- C. Adds this line to the built-in artifact `github-steps-summary.md`
- D. Prints this line as a step-level debug message

**Type:** *single*

---

## Q153

Which of the following events can trigger a workflow that has not been merged to the default branch?

- A. `issue_comment`
- B. `star`
- C. `issues`
- D. `push`
- E. `pull_request`
- F. `repository_dispatch`

**Type:** *multi-select (2 correct)*

---

## Q156

In what ways can you delete workflow artifacts?

- A. By using a specific GitHub API endpoint
- B. By using the Github Actions UI to delete the workflow run that generated the artifacts
- C. By setting the artifact retention period to 0 days
- D. By using the `actions/delete-artifact` action in a workflow 
- E. By remotely accessing self-hosted runners via SSH, navigating to the `.github/artifacts` directory, and deleting the selected artifacts
- F. By using the Github Actions UI to navigate to a workflow run and delete the artifacts individually

**Type:** *multi-select (3 correct)*

---

## Q158

Petra is building a workflow whose sole job is named `post-merge`. How can she set up the job to be triggered upon a merged pull request?

- A.  Specify the the `pull_request` activity type as `closed` and use a job-level conditional to check if `github.ref` is equal to the merge branch of the pull request.
  ```yaml
  on:
      pull_request:
          types: [closed]
  jobs:
      post-merge: 
          if: ${{ github.ref == github.event.pull_request.base.ref }}
  ``` 
- B.  Specify the `pull_request` activity type as `merged`, and use a job-level conditional to check if `github.event.pull_request.merged` is true
  ```yaml
  on:
      pull_request:
          types: [merged]
  jobs:
      post-merge:
          if: github.event.pull_request.merged == true
  ``` 
- C.  Specify the `pull_request` activity type as `closed`, and use a job-level conditional to check if `github.event.pull_request.merged` is true
  ```yaml
  on:
      pull_request:
          types: [closed]
  jobs:
      post-merge:
          if: github.event.pull_request.merged == true
  ``` 
- D. Specify the the `pull_request` activity type as `closed` (no need for a job-level conditional)
  ```yaml
  on:
      pull_request:
          types: [closed]
  jobs:
      post-merge:
  ``` 
- E.  Specify the `pull_request` activity type as `merged` (no need for a job-level conditional)
  ```yaml
  on:
      pull_request:
          types: [merged]
  jobs:
      post-merge:
  ``` 

**Type:** *single*

---

## Q159

Which of the following are true when comparing the pull_request and pull_request_target events?

- A. Workflows will not run on `pull_request` activity if there is a merge conflict
- B. The `pull_request` event runs within the context of the merge commit, while `pull_request_target` runs in the context of the default branch of the base repository.
- C. Workflows will not run on `pull_request_target` activity if there is a merge conflict
- D. The `pull_request_target` event should be used when you want to run code contained in a PR's changed files, to do things like performing CI checks or running test suites.
- E. Both `pull_request` and `pull_request_target` events have default activity types of `opened`, `synchronize`, and `reopened`.
- F. `pull_request` should be used with caution, since PRs from forks will allow the workflow to access all secrets within the repository due to being associated with the default branch.

**Type:** *multi-select (3 correct)*

---

## Q160

Why should you use OIDC when connecting a workflow to cloud providers?

- A. OIDC involves the generation and use of short-lived tokens, which is more secure
- B. Using OIDC allows you to circumvent setting up trust policies with cloud providers
- C. OIDC generates JSON web tokens (JWTs) that can be used across workflow jobs
- D. Cloud providers require the use of OIDC.
- E. Using OIDC within a workflow will automatically save that workflow's logs in cloud storage
- F. OIDC prevents you from having to keep cloud credentials as long-lived GitHub secrets 

**Type:** *multi-select (2 correct)*

---

## Q162

Mercedes wants to publish a Docker container action she has created to the GitHub Actions Marketplace. What files does she need at a minimum to do so?

- A. `CONTRIBUTING.md`
- B. `README.md`
- C. `action.yml`
- D. A `Dockerfile`, if the image is built as part of the action during the workflow run
- E. `.dockerignore`
- F. A `Dockerfile`, if the image is to be referenced from an image registry

**Type:** *multi-select (2 correct)*

---

## Q163

Annette needs to write a workflow to publish a custom `npm` package that only members in her private organization will use. What should her workflow include?

- A. An `on:registry_package` event with no activity types specified
- B. A token with `admin:packages` permissions
- C. Logic to publish to GitHub Packages
- D. Communication logic with the corresponding GitHub Packages registry `https://npm.pkg.github.com`
- E. A token with `write:packages` permissions 
- F. An `on:registry_package` event with `types:[published]` 

**Type:** *multi-select (3 correct)*

---

## Q164

At what levels can `if:` be used in workflows?

- A. Job-level
- B. Step-level
- C. Environment-level
- D. Workflow-level
- E. Organization-level

**Type:** *multi-select (2 correct)*

---

## Q165

How does `repository_dispatch` enable systems outside of GitHub to trigger a workflow?

- A. The `on.repository_dispatch.event_types` workflow key corresponds to the `event_type` parameter in the request payload, restricting the workflow to only trigger on relevant external events
- B. The external system makes a PUT request to the GitHub API to create a repository dispatch event
- C. The workflow is triggered by the creation of a repository dispatch event 
- D. The workflow is triggered by a POST request to the workflow using the following endpoint `/repos/OWNER/REPO/actions/workflows/<WORKFLOW_ID>/dispatches` 
- E. The external system makes a POST request to the GitHub API to create a repository dispatch event.
- F. The `on.repository_dispatch.types` workflow key corresponds to the `event_type` parameter in the request payload, restricting the workflow to only trigger on relevant external events 

**Type:** *multi-select (3 correct)*

---

## Q168

Which keys are required when making an `action.yml` file?

- A. `inputs`
- B. `description`
- C. `outputs`
- D. `runs`
- E. `author`
- F. `name`

**Type:** *multi-select (3 correct)*

---

## Q169

Manuela is setting up self-hosted runners for her organization, which has heavily restricted communication with IP addresses. How can she ensure the self-hosted runners can communicate with GitHub?

- A. Adding the self-hosted runners' IP address(es) to the organization's IP allow list
- B. Adding the self-hosted runners' operating system to the organization's operating system allow list
- C. Adding the `.ip-exception` file to the top-level of the self-hosted runner's directory structure
- D. Switch to GitHub-hosted standard runners, since self-hosted runners will be blocked if IP allow lists are enabled
- E. Selecting the 'Allow access from self-hosted runners' checkbox in the organization's IP allow list settings

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

- A. The job will run on a self-hosted runner that has all the labels applied.
- B. The job will run on a self-hosted runner that has any of the labels applied.
- C. The job will run on a runner (self-hosted or GitHub-hosted, whichever is first available) with the name `self-hosted,nes,linux`
- D. The job will still be able to run on GitHub-hosted runners, since they can have custom labels applied to them

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
- B. The Python script will run successfully, because the `chmod` command grants execute permissions to the script.
- C. The Python script will not run, because `actions/python-setup` is not the correct action for setting up Python.
- D. The Python script will not run, because `actions/checkout` is not included in the workflow.

**Type:** *single*

---

## Q178

You need to ensure that your `prod` environment requires manual approvals before deploys can proceed. Out of the following options, which are true regarding how this is set up?

- A. You cannot prevent self-reviews, but you can set up alerts to see who triggered the deployment.
- B. Required reviewers need at least `write` access to the repository in order to approve.
- C. Only individual users can be assigned as required reviewers, not teams.
- D. If you list required reviewers, all of them need to approve to continue with the deployment.
- E. You can prevent self-reviews in the event the person who wants to deploy is also a required reviewer.
- F. If you list required reviewers, only one of them needs to approve to continue with the deployment.

**Type:** *multi-select (2 correct)*

---
