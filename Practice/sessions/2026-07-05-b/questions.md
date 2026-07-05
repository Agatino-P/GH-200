# GH-200 practice session 2026-07-05-b

Generated 2026-07-05 from `gh-200-ghcertified-bank-full-2026-06-24.md` — 15 questions, options shuffled and re-lettered.
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

- A. Yes
- B. Only with self-hosted runners
- C. No
- D. Only if the workflows are in the same repository

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

- A. Using defaults.env on job level to set default environment variables for all steps in a single job
- B. Using defaults.run on step level to set default shell (e.g bash) for that single step
- C. Using defaults.run on job level to set default working-directory for all steps in a single job
- D. Using defaults.env on workflow level to set default environment variables for an entire workflow
- E. Using defaults.run on workflow level to set default shell (e.g bash) for an entire workflow

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

- A. Set `jobs.example_matrix.strategy.max-parallel` to 2
- B. Set `jobs.example_matrix.strategy.concurrency` to 2
- C. It's not possible, a matrix will always run all of the jobs in parallel if there are runners available
- D. Use GitHub's REST API to check if the job count is lesser than 2

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
- B. `run: echo "$action_state"`
- C. `run: echo "$steps.step_one.outputs.action_state"`
- D. `run: echo "${{ steps.step_one.outputs.action_state }}"`

**Type:** *single*

---

## Q072

What components can be reused within a GitHub Organization?

- A. Self Hosted Runners
- B. Cache
- C. Secrets
- D. Configuration Variables
- E. Environment Variables
- F. Artifacts
- G. Workflow Templates

**Type:** *multi-select (4 correct)*

---

## Q081

How can you reuse a defined workflow in multiple repositories?

- A. By defining the workflow in a central repository
- B. By using workflow templates
- C. By copying the workflow file to each repository
- D. By creating a reusable action

**Type:** *multi-select (2 correct)*

---

## Q098

How can you specify the schedule of a GitHub actions workflow to run on weekdays only?

- A. use the on: schedule: cron event trigger
- B. it is not possible in GitHub actions
- C. add a condition in the workflow YAML for weekdays
- D. use the on: schedule: weekdays event trigger

**Type:** *single*

---

## Q115

What level of permission is required to re-run the workflows

- A. write 
- B. read
- C. admin
- D. owner

**Type:** *single*

---

## Q121

What’s true about default variables?

- A. Currently, the value of the default CI environment variable can be overwritten, but it's not guaranteed this will always be possible
- B. You can add a new default environment variable adding the prefix “GITHUB_” to it
- C. Default environment variables can be accessed using the env context
- D. Default environment variables are set by GitHub and not defined in a workflow
- E. Default environment variables always have the prefix “GITHUB_”
- F. Most of the default environment variables have a corresponding context property

**Type:** *multi-select (3 correct)*

---

## Q125

At what levels can environment variables be defined ?

- A. Step level
- B. Workflow level
- C. Job level
- D. Action level

**Type:** *multi-select (3 correct)*

---

## Q132

Which of the following are true regarding GitHub Enterprise Server (GHES)?

- A. Using GitHub Connect, users can follow a manual process to access GitHub.com actions. This process must be done once per desired action.
- B. `actions/actions-sync` is primarily devoted to moving GitHub.com actions to a GHES instance.
- C. GitHub Enterprise Server instances are self-hosted, compared to GitHub Enterprise Cloud (GHEC) which is hosted and managed by GitHub.
- D. GHES workflows cannot access GitHub.com nor GitHub Marketplace actions by default. 
- E. GHES is allowed to use enhanced versions of GitHub-hosted runners.

**Type:** *multi-select (3 correct)*

---

## Q148

Which statement is true regarding `github.ref` when the workflow is triggered by a push event?

- A. In push events, `github.ref` is the fully-formed ref of the branch or tag ref that was pushed. 
- B. In push events, `github.ref` is SHA of the commit that triggered the workflow.
- C. In push events, `github.ref` is the type of fully-formed ref that triggered the workflow run. The value will either be `branch`, `tag`, or `null` (if the ref was not fully-formed).
- D. In push events, `github.ref` is the message of the commit that triggered the workflow.
- E. In push events, `github.ref` is the description of the commit that triggered the workflow.

**Type:** *single*

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
- B.  Specify the `pull_request` activity type as `closed`, and use a job-level conditional to check if `github.event.pull_request.merged` is true
  ```yaml
  on:
      pull_request:
          types: [closed]
  jobs:
      post-merge:
          if: github.event.pull_request.merged == true
  ``` 
- C.  Specify the `pull_request` activity type as `merged` (no need for a job-level conditional)
  ```yaml
  on:
      pull_request:
          types: [merged]
  jobs:
      post-merge:
  ``` 
- D.  Specify the `pull_request` activity type as `merged`, and use a job-level conditional to check if `github.event.pull_request.merged` is true
  ```yaml
  on:
      pull_request:
          types: [merged]
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

## Q162

Mercedes wants to publish a Docker container action she has created to the GitHub Actions Marketplace. What files does she need at a minimum to do so?

- A. `action.yml`
- B. `CONTRIBUTING.md`
- C. `README.md`
- D. A `Dockerfile`, if the image is built as part of the action during the workflow run
- E. A `Dockerfile`, if the image is to be referenced from an image registry
- F. `.dockerignore`

**Type:** *multi-select (2 correct)*

---
