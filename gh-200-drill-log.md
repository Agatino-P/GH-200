# GH-200 — Drill Log (per-question audit)

**Last updated: 2026-06-28 20:52 UTC** *(bump on every edit; `date -u`)*

*Per-question audit trail for the practice phase, mandated by practice-protocol §4.15. One entry per question, recording the four things grading needs so it is **mechanical and auditable**, never reconstructed from memory:*
*(a) the exact shuffled question as presented · (b) the source Q-ID · (c) the correct option in the shuffled frame (presented letter + content) + the shuffled→original map · (d) the grading (learner's answer + ✓/✗ by letter-vs-letter).*

**Rules (from §4.15):**
- The correct option's **shuffled letter** is written here **at presentation time**, before the learner answers.
- Grading compares the learner's letter to the recorded correct letter. **Never** glue the bank's original-answer word onto the learner's letter.
- This file is synced with project + repo + HD (§4.9) and is the audit trail behind the §6b coverage-ledger pass/fail column.

**Status:** Pass 1 reset to Q000 on 2026-06-28 (prior Q001–Q020 voided for integrity failures — see protocol §6). Next question to draw = **GHCertified Q001**. No valid entries yet.

---

## Entry format (template)

```
### <Q-ID> · <bank> · <date>
Stem: <question stem as presented>
Options (shuffled, as presented):
  A. <text>
  B. <text>
  C. <text>
  D. <text>
Shuffle map (presented → original): A→<o>, B→<o>, C→<o>, D→<o>
Correct (shuffled frame): <letter> = <content>
Learner answer: <letter> = <content>
Grade: <✓|✗>   Bucket (if ✗): <a|b|c|d>   Objective: <id>
Note: <one line, only if needed>
```

---

## Pass 1 — entries

*(none yet — begins at GHCertified Q001)*

### GHCertified Q001  (presented 2026-06-28T21:12Z)
Stem: Which statement is correct regarding passing permissions to reusable workflows?
- A. The `GITHUB_TOKEN` permissions passed from the caller workflow can be only downgraded by the called workflow.
- B. The `GITHUB_TOKEN` permissions passed from the caller workflow can be neither downgraded or elevated by the called workflow.
- C. The `GITHUB_TOKEN` permissions passed from the caller workflow can be both downgraded and elevated by the called workflow.
- D. The `GITHUB_TOKEN` permissions passed from the caller workflow can be only elevated by the called workflow.

shuffle map (presented<-original): A<-A B<-D C<-C D<-B 
correct (shuffled frame): A
learner answer: A   grade: OK-correct

### GHCertified Q002  (presented 2026-06-28T21:15Z)
Stem: What are the different permission levels you can assign to `GITHUB_TOKEN` in the `permissions` block?
A. read, write
B. read, write, delete
C. none, write, read
shuffle map (presented<-original): A<-C B<-B C<-A 
correct (shuffled frame): C
learner answer: C   grade: OK-correct

### GHCertified Q003  (presented 2026-06-28T21:17Z)
Stem: You can use `permissions` to modify the `GITHUB_TOKEN` permissions on:
A. Step level
B. Job level
C. Workflow level
shuffle map (presented<-original): A<-C B<-B C<-A 
correct (shuffled frame): B,C   [MULTI: 2 correct]
learner answer: B,C   grade: OK-correct

### GHCertified Q004  (presented 2026-06-28T21:18Z)
Stem: Are GitHub Actions free for public repositories?
A. No, only self-hosted runners are free for public repositories
B. No, all GitHub Actions usage is billed
C. Yes, but only for the first 2,000 minutes per month
D. Yes, when using standard GitHub-hosted runners
shuffle map (presented<-original): A<-D B<-B C<-C D<-A 
correct (shuffled frame): D   [single]
learner answer: D   grade: OK-correct

### GHCertified Q005  (presented 2026-06-28T21:20Z)
Stem: Which of these is not a valid event that could trigger a workflow?
A. A branch is created
B. Committing a file to master branch
C. Cloning the repository
D. Adding a label to a pull request
shuffle map (presented<-original): A<-C B<-B C<-A D<-D 
correct (shuffled frame): C   [single]
learner answer: C   grade: OK-correct

### GHCertified Q006  (presented 2026-06-28T21:20Z)
Stem: Which is true about workflows?
A. Workflows have to be defined in the `.github/workflows` directory
B. Workflows can be triggered manually, by an event or run on a schedule
C. Workflows can run one or multiple jobs at a time
D. Workflows can only be run on a schedule
shuffle map (presented<-original): A<-C B<-B C<-A D<-D 
correct (shuffled frame): A,B,C   [MULTI: 3]
learner answer: A,B,C   grade: OK-correct

### GHCertified Q007  (presented 2026-06-28T21:21Z)
Stem: Which components are required for a workflow?
A. One or more jobs
B. One or more events that will trigger the workflow
C. Workflow name
D. Defined branches on which the workflow will run
shuffle map (presented<-original): A<-B B<-A C<-C D<-D 
correct (shuffled frame): A,B   [MULTI: 2]
learner answer: A,B   grade: OK-correct

### GHCertified Q008  (presented 2026-06-28T21:21Z)
Stem: Which event is triggered by a webhook action from outside of the repository?
A. remote_dispatch
B. webhook_dispatch
C. workflow_dispatch
D. repository_dispatch
shuffle map (presented<-original): A<-D B<-B C<-C D<-A 
correct (shuffled frame): D   [single]
learner answer: D   grade: OK-correct

### GHCertified Q009  (presented 2026-06-28T21:22Z)
Stem: Workflows are defined in which format
A. xml
B. toml
C. json
D. yaml
shuffle map (presented<-original): A<-D B<-B C<-C D<-A 
correct (shuffled frame): D   [single]
learner answer: D   grade: OK-correct

### GHCertified Q010  (presented 2026-06-28T21:22Z)
Stem: Where should you store sensitive data such as passwords or certificates that will be used in workflows
A. environment variables
B. config variables
C. vault
D. secrets
shuffle map (presented<-original): A<-D B<-B C<-C D<-A 
correct (shuffled frame): D   [single]
learner answer: D   grade: OK-correct

### GHCertified Q011  (presented 2026-06-28T21:23Z)
Stem: In a workflow with multiple jobs the default behavior is:
A. Jobs run based on the order they are defined in the workflow file
B. Jobs run in sequence
C. All jobs run in parallel
D. Only the first job runs, others require manual approval
shuffle map (presented<-original): A<-C B<-B C<-A D<-D 
correct (shuffled frame): C   [single]
learner answer: C   grade: OK-correct

### GHCertified Q012  (presented 2026-06-28T21:24Z)
Stem: If job B requires job A to be finished you have to:
A. use the `requires` keyword in job B to create this dependency
B. use the `needs` keyword in job A to create this dependency
C. use the `needs` keyword in job B to create this dependency
D. use the `requires` keyword in job A to create this dependency
shuffle map (presented<-original): A<-C B<-B C<-A D<-D 
correct (shuffled frame): C   [single]
learner answer: C   grade: OK-correct

### GHCertified Q013  (presented 2026-06-28T21:25Z)
Stem: In a workflow with multiple jobs, if job A fails then:
A. the jobs that are dependent on job A are skipped
B. the workflow immediately cancels all other jobs
C. the jobs that are dependent on job A fail
shuffle map (presented<-original): A<-A B<-C C<-B 
correct (shuffled frame): A   [single]
learner answer: A   grade: OK-correct

### GHCertified Q014  (presented 2026-06-28T21:26Z)
Stem: This code will launch 6 different jobs in parallel using the matrix strategy. Can you use the matrix strategy to parallelize entire workflows?
```yaml
jobs:
  example_matrix:
    strategy:
      matrix:
        version: [10, 12, 14]
        os: [ubuntu-latest, windows-latest]
```
A. Only if the workflows are in the same repository
B. No
C. Yes
D. Only with self-hosted runners
shuffle map (presented<-original): A<-C B<-B C<-A D<-D 
correct (shuffled frame): C   [single]
learner answer: B   grade: X-wrong  bucket:(d) loose wording — known flag §8#1/gap#5


### GHCertified Q015  (presented 2026-06-28T21:28Z) [code-block options]
Stem: Which matrix job definition is syntactically correct?
shuffle map (presented<-original): A<-D B<-C C<-B D<-A 
correct (shuffled frame): D   [single]
learner answer: D   grade: OK-correct

### GHCertified Q016  (presented 2026-06-28T21:29Z) [code-block options]
Stem: How do you access matrix variables in a matrix strategy job?
shuffle map (presented<-original): A<-C B<-B C<-A D<-D 
correct (shuffled frame): B   [single]
learner answer: B   grade: OK-correct

### GHCertified Q017  (presented 2026-06-28T21:32Z)
Stem: When using the `pull_request` and `pull_request_target` events, how do you configure the workflow to run only when targeting the `prod` branch?
shuffle map (presented<-original): A<-B B<-A C<-C D<-D 
correct (shuffled frame): B   [single]
learner answer: B   grade: OK-correct

### GHCertified Q018  (presented 2026-06-28T21:36Z)
Stem: This workflow will run on all pull requests where:
```yaml
on:
  pull_request:
    branches:
      - 'release/**'
      - '!release/**-alpha'
```
shuffle map (presented<-original): A<-B B<-A C<-C D<-D 
correct (shuffled frame): B   [single]
learner answer: B   grade: OK-correct

### GHCertified Q019  (presented 2026-06-28T21:37Z)
Stem: Fill in the blank: When using `push` event trigger filters you can use <____> patterns to target multiple branches
shuffle map (presented<-original): A<-C B<-B C<-A D<-D 
correct (shuffled frame): C   [single]
learner answer: C   grade: OK-correct

### GHCertified Q020  (presented 2026-06-28T21:38Z)
Stem: Which event allows you to manually trigger a workflow from the GitHub UI?
shuffle map (presented<-original): A<-D B<-B C<-C D<-A 
correct (shuffled frame): D   [single]
learner answer: D   grade: OK-correct


### GHCertified Q021  (presented 2026-06-28T21:39Z)
Stem: What are the possible types of an input variable for a manually triggered workflow?
shuffle map (presented<-original): A<-A B<-C C<-D D<-B E<-E F<-F G<-G 
correct (shuffled frame): A,B,C,D,E   [MULTI: 5]
learner answer: A,B,C,D,E   grade: OK-correct (number confirmed valid vs live docs)

### GHCertified Q022  (presented 2026-06-28T21:42Z)
Stem: A workflow that has only `workflow_dispatch` event trigger can be triggered using GitHub's REST API
shuffle map (presented<-original): A<-A B<-B 
correct (shuffled frame): A   [single]
learner answer: B   grade: X-wrong  bucket:(c) retention — workflow_dispatch IS triggerable via REST API/CLI/UI [→§7 miss ledger]

### GHCertified Q023  (presented 2026-06-28T21:43Z)
Stem: To stop a workflow from running temporarily without modifying the source code you should
shuffle map (presented<-original): A<-B B<-A C<-C D<-D 
correct (shuffled frame): B   [single]
learner answer: B   grade: OK-correct

### GHCertified Q024  (presented 2026-06-28T21:45Z)
Stem: What are `activity types` of an event used for ?
shuffle map (presented<-original): A<-C B<-A C<-B 
correct (shuffled frame): B   [single]
learner answer: B   grade: OK-correct


### GHCertified Q025  (presented 2026-06-28T21:46Z)
Stem: You want to create a reusable workflow `CI` that runs some quality checks, linting and tests on code changes. What event trigger should the `CI` workflow define to allow reusing it in other workflows?
shuffle map (presented<-original): A<-D B<-B C<-C D<-A 
correct (shuffled frame): D   [single]
learner answer: D   grade: OK-correct

### GHCertified Q026  (presented 2026-06-28T21:47Z)
Stem: A reusable workflow named `build` creates zip file artifacts. How do you pass the zip file location to the caller workflow that is calling the `build` workflow?
shuffle map (presented<-original): A<-B B<-A C<-C D<-D 
correct (shuffled frame): A,B,C   [MULTI: 3]
learner answer: A,B,C   grade: OK-correct

### GHCertified Q027  (presented 2026-06-28T21:48Z)
Stem: What are the valid use cases for using **defaults**?
shuffle map (presented<-original): A<-B B<-D C<-E D<-A E<-C 
correct (shuffled frame): A,D   [MULTI: 2]
learner answer: B,D   grade: X-wrong  bucket:(b) defaults supports ONLY run (shell+working-directory); no defaults.env [verified docs] [→§7]

### GHCertified Q028  (presented 2026-06-28T21:50Z) [code-block options]
Stem: How can you ensure that a workflow called `Deploy Prod` is always running at most one at a time?
shuffle map (presented<-original): A<-C B<-B C<-A D<-D 
correct (shuffled frame): C   [single]
learner answer: C   grade: OK-correct

### GHCertified Q029  (presented 2026-06-28T21:51Z) [code-block options]
Stem: Your Pull Request analysis workflow uses multiple code analysis tools and takes about 20minutes to fully complete. It is triggered on `pull_request` event with `branches` filter set to `master`. Therefore if a developer pushes multiple commits within few minutes multiple workflows are running in parallel. How can you stop all previous workflow runs and only run the one with latest changes?
shuffle map (presented<-original): A<-D B<-B C<-C D<-A 
correct (shuffled frame): D   [single]
learner answer: D   grade: OK-correct (correct by deduction; flagged: concurrency.group value semantics not fully understood -> contexts deep-dive §7b)
[keeper queued for §7b contexts deep-dive: concurrency.group string scopes mutual-exclusion; github.ref=refs/pull/<n>/merge on PR, refs/heads/<branch> on push; github.workflow keeps workflows separate]

### GHCertified Q030  (presented 2026-06-28T21:56Z)
Stem: When will job3 run?
```yaml
jobs:
  job1:
  job2:
    needs: job1
  job3:
    if: ${{ always() }}
    needs: [job1, job2]
```
shuffle map (presented<-original): A<-B B<-A C<-C D<-D 
correct (shuffled frame): B   [single]
learner answer: B   grade: OK-correct
[keeper queued for §7b: STUDY DEEPER — if: + status-function combinations (success/failure/always/cancelled) x needs; reconfirms §7b#1 — learner-flagged 2026-06-28]

### GHCertified Q031  (presented 2026-06-28T22:02Z)
Stem: What `jobs.job_id.if` conditional will make sure that job `production-deploy` is triggered only on `my-org/my-repo` repository?
```yaml
jobs:
  production-deploy:  
    if: <CONDITION>
    runs-on: ubuntu-latest
    steps:
      ...
```
shuffle map (presented<-original): A<-D B<-B C<-C D<-A 
correct (shuffled frame): B,D   [MULTI: 2]
learner answer: B,D   grade: OK-correct
