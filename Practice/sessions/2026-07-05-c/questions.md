# GH-200 practice session 2026-07-05-c

Generated 2026-07-05 from `gh-200-ghcertified-bank-full-2026-06-24.md` — 5 questions, options shuffled and re-lettered.
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

## Q081

How can you reuse a defined workflow in multiple repositories?

- A. By using workflow templates
- B. By creating a reusable action
- C. By defining the workflow in a central repository
- D. By copying the workflow file to each repository

**Type:** *multi-select (2 correct)*

---

## Q098

How can you specify the schedule of a GitHub actions workflow to run on weekdays only?

- A. add a condition in the workflow YAML for weekdays
- B. use the on: schedule: cron event trigger
- C. use the on: schedule: weekdays event trigger
- D. it is not possible in GitHub actions

**Type:** *single*

---

## Q125

At what levels can environment variables be defined ?

- A. Job level
- B. Action level
- C. Step level
- D. Workflow level

**Type:** *multi-select (3 correct)*

---

## Q158

Petra is building a workflow whose sole job is named `post-merge`. How can she set up the job to be triggered upon a merged pull request?

- A.  Specify the `pull_request` activity type as `merged` (no need for a job-level conditional)
  ```yaml
  on:
      pull_request:
          types: [merged]
  jobs:
      post-merge:
  ``` 
- B. Specify the the `pull_request` activity type as `closed` (no need for a job-level conditional)
  ```yaml
  on:
      pull_request:
          types: [closed]
  jobs:
      post-merge:
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
- D.  Specify the `pull_request` activity type as `merged`, and use a job-level conditional to check if `github.event.pull_request.merged` is true
  ```yaml
  on:
      pull_request:
          types: [merged]
  jobs:
      post-merge:
          if: github.event.pull_request.merged == true
  ``` 
- E.  Specify the the `pull_request` activity type as `closed` and use a job-level conditional to check if `github.ref` is equal to the merge branch of the pull request.
  ```yaml
  on:
      pull_request:
          types: [closed]
  jobs:
      post-merge: 
          if: ${{ github.ref == github.event.pull_request.base.ref }}
  ``` 

**Type:** *single*

---
