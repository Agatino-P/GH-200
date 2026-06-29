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

### GHCertified Q032  (presented 2026-06-29T12:42Z) [multi-select]
- **Stem:** What GitHub-hosted runner types are available to use?
- **Presented (shuffled):** A. Windows · B. Android · C. Ubuntu Linux · D. macOS
- **Source Q-ID:** GHCertified Q032
- **Correct (shuffled frame):** A, C, D  — content: Windows, Ubuntu Linux, macOS
- **shuffle→orig map:** A<-A  B<-D  C<-B  D<-C
- **Learner answer:** A, C, D
- **Grade:** ✓  (correct A,C,D == learner A,C,D)

### GHCertified Q033  (presented 2026-06-29T12:42Z) [single]
- **Stem:** Is this statement true? `Not all steps run actions, but all actions run as a step`
- **Presented (shuffled):** A. False · B. True
- **Source Q-ID:** GHCertified Q033
- **Correct (shuffled frame):** B  — content: True
- **shuffle→orig map:** A<-B  B<-A
- **Learner answer:** B
- **Grade:** ✓  (correct B == learner B)

### GHCertified Q034  (presented 2026-06-29T12:42Z) [single]
- **Stem:** For any Marketplace action usable in multiple versions, which approach is most stable and secure?
- **Presented (shuffled):** A. Reference a version tag · B. Reference the main branch · C. Reference the commit SHA
- **Source Q-ID:** GHCertified Q034
- **Correct (shuffled frame):** C  — content: Reference the commit SHA
- **shuffle→orig map:** A<-B  B<-C  C<-A
- **Learner answer:** C
- **Grade:** ✓  (correct C == learner C)

### GHCertified Q035  (presented 2026-06-29T12:42Z) [single, code-block options]
- **Stem:** To prevent a job from failing when one step fails, you can include:
- **Presented (shuffled):** A. `continue-on-error: true` · B. `if: failure()` · C. `if: always()` · D. `ignore-error: true`
- **Source Q-ID:** GHCertified Q035
- **Correct (shuffled frame):** A  — content: continue-on-error flag in the failing step
- **shuffle→orig map:** A<-A  B<-C  C<-D  D<-B
- **Learner answer:** A
- **Grade:** ✓  (correct A == learner A)

### GHCertified Q036  (presented 2026-06-29T12:43Z) [single, code in stem]
- **Stem:** Given matrix job example_matrix (version[10,12,14] x os[ubuntu,windows]), how to limit to max 2 jobs at a time?
- **Presented (shuffled):** A. not possible · B. strategy.max-parallel=2 · C. strategy.concurrency=2 · D. REST API check
- **Source Q-ID:** GHCertified Q036
- **Correct (shuffled frame):** B  — content: strategy.max-parallel to 2
- **shuffle→orig map:** A<-D  B<-A  C<-B  D<-C
- **Learner answer:** B
- **Grade:** ✓  (correct B == learner B)

### GHCertified Q037  (presented 2026-06-29T12:44Z) [single]
- **Stem:** Proper way to set output parameter PET=DOG in a step?
- **Presented (shuffled):** A. gh set-output "PET=DOG" · B. echo "DOG=PET" >> "$GITHUB_OUTPUT" · C. gh set-output "DOG=PET" · D. echo "PET=DOG" >> "$GITHUB_OUTPUT"
- **Source Q-ID:** GHCertified Q037
- **Correct (shuffled frame):** D  — content: echo "PET=DOG" >> "$GITHUB_OUTPUT"
- **shuffle->orig map:** A<-D  B<-B  C<-C  D<-A
- **Learner answer:** D
- **Grade:** ✓  (correct D == learner D)

### GHCertified Q038  (presented 2026-06-29T12:45Z) [single, code in stem]
- **Stem:** step_one writes action_state=yellow to $GITHUB_ENV; how to use it in step_two?
- **Presented (shuffled):** A. echo "${{ steps.step_one.outputs.action_state }}" · B. echo "$action_state" · C. echo "${{ action_state }}" · D. echo "$steps.step_one.outputs.action_state"
- **Source Q-ID:** GHCertified Q038
- **Correct (shuffled frame):** B  — content: echo "$action_state" (env var via $GITHUB_ENV)
- **shuffle->orig map:** A<-B  B<-A  C<-D  D<-C
- **Learner answer:** B
- **Grade:** ✓  (correct B == learner B)

### GHCertified Q039  (presented 2026-06-29T12:47Z) [single]
- **Stem:** True? "Workflows can be reused, but a reusable workflow cannot call another reusable workflow."
- **Presented (shuffled):** A. True · B. False
- **Source Q-ID:** GHCertified Q039
- **Correct (shuffled frame):** B  — content: False (reusable workflows CAN be nested)
- **shuffle->orig map:** A<-B  B<-A
- **Learner answer:** B
- **Grade:** ✓  (correct B == learner B)

### GHCertified Q040  (presented 2026-06-29T12:47Z) [single, code in stem]
- **Stem:** A passes secrets:inherit to B; B calls C without inherit. Which secrets statement is true?
- **Presented (shuffled):** A. octo-org org+repo secrets to B not C · B. to B and C · C. all A's secrets to B not C · D. only repo+env to B not C, org can't inherit
- **Source Q-ID:** GHCertified Q040
- **Correct (shuffled frame):** C  — content: all secrets available to A also to B, but not C
- **shuffle->orig map:** A<-B  B<-C  C<-A  D<-D
- **Learner answer:** A
- **Grade:** ✗  (correct C != learner A) — bucket (c)/(a): secrets:inherit = all secrets *available to caller*, source-agnostic; chain stops at B. Learner's ambiguity-instinct was right but applied inverted.

### GHCertified Q041  (presented 2026-06-29T12:52Z) [single]
- **Stem:** When should you use caching?
- **Presented (shuffled):** A. save files to view after run (artifacts) · B. reuse files that DO change often · C. save binaries for subsequent deploy job (artifacts) · D. reuse files that DON'T change often, e.g. build deps
- **Source Q-ID:** GHCertified Q041
- **Correct (shuffled frame):** D  — content: reuse files that don't change often (build dependencies)
- **shuffle->orig map:** A<-C  B<-B  C<-D  D<-A
- **Learner answer:** B
- **Grade:** ✗  (correct D != learner B) — bucket (a)/(c): cache = reuse files that DON'T change often (build deps). B is the one-word inverse ('do change often'). A/C = artifacts.

### GHCertified Q042  (presented 2026-06-29T12:54Z) [multi-select]
- **Stem:** When should you use artifacts?
- **Presented (shuffled):** A. save binaries for subsequent deploy job · B. save files to view after run (test results/logs) · C. reuse files that don't change often (caching) · D. create new versions with release notes
- **Source Q-ID:** GHCertified Q042
- **Correct (shuffled frame):** A, B  — content: save-binaries-for-deploy + save-files-to-view-after-run
- **shuffle->orig map:** A<-B  B<-A  C<-C  D<-D
- **Learner answer:** A, B
- **Grade:** ✓ matches key (A,B) — ⚠ **LEAKED during caching refresh (answer revealed pre-answer); EXCLUDED from clean score**, knowledge preserved. Learner stated would have chosen A,B regardless.
- **Refresh correction (artifact scope):** artifact stored UNDER the run; default download = current run only (no token); cross-run/cross-repo via download-artifact v4+ with actions:read + run-id (+repository). Cache branch-scope = hard isolation; artifact run-scope = soft default. Verified vs docs.github.com.

### GHCertified Q043  (presented 2026-06-29T13:03Z) [single] — NOTE: concept freshly reviewed in cache refresh; presenter slip corrected (prose first showed original order, re-presented shuffled)
- **Stem:** Workflow on feature-a branch — can it restore caches created on default main branch?
- **Presented (shuffled):** A. No, only same branch · B. Yes, any branch in same repo · C. Yes, only if no files changed on feature-a · D. Yes, all branches can restore caches created on the default branch
- **Source Q-ID:** GHCertified Q043
- **Correct (shuffled frame):** D  — content: Yes, all branches can restore caches created on the default branch
- **shuffle->orig map:** A<-C  B<-B  C<-D  D<-A
- **Learner answer:** A (shuffled = 'No, only same branch')
- **Grade:** VOID — uninterpretable. Presenter showed two conflicting letter schemes; learner cannot reliably be scored. NOT counted, NO gap logged against learner. Cache branch-scope stays on review list ONLY due to prior A1·Q043, not this instance.

### GHCertified Q044  (presented 2026-06-29T13:07Z) [single] — NOTE: concept freshly discussed (cross-run artifact access); shuffle done BEFORE prose this time
- **Stem:** To access an artifact created in another, previously triggered workflow run you can:
- **Presented (shuffled):** A. use upload-artifact · B. use download-artifact with elevated permissions · C. you cannot access cross-run artifacts · D. use download-artifact and make sure artifact not expired
- **Source Q-ID:** GHCertified Q044
- **Correct (shuffled frame):** B  — content: download-artifact with elevated permissions (token + run-id + actions:read)
- **shuffle->orig map:** A<-C  B<-B  C<-A  D<-D
- **Learner answer:** B
- **Grade:** ✓  (correct B == learner B). Learner correctly flagged D as a distractor (expiry real but not the cross-run enabler).

### GHCertified Q045  (presented 2026-06-29T13:10Z) [single]
- **Stem:** What to use to store coverage reports/screenshots from automated testing?
- **Presented (shuffled):** A. Caches · B. Artifacts · C. Releases · D. Packages
- **Source Q-ID:** GHCertified Q045
- **Correct (shuffled frame):** B  — content: Artifacts
- **shuffle->orig map:** A<-B  B<-A  C<-D  D<-C
- **Learner answer:** B
- **Grade:** ✓  (correct B == learner B)

### GHCertified Q046  (presented 2026-06-29T13:12Z) [single]
- **Stem:** True/False: "You can only upload a single file at a time when using actions/upload-artifact"
- **Presented (shuffled):** A. Only directories, not individual files · B. True · C. False
- **Source Q-ID:** GHCertified Q046
- **Correct (shuffled frame):** C  — content: False (can upload multiple files/dirs/wildcards)
- **shuffle->orig map:** A<-C  B<-B  C<-A
- **Learner answer:** B (True)
- **Grade:** ✗  (correct C != learner B) — bucket (b)/(c): upload-artifact accepts single file, directory, OR multiple files/dirs + wildcards/exclusions. Statement 'only single file at a time' is False. → §7

### GHCertified Q047  (presented 2026-06-29T13:13Z) [single]
- **Stem:** Job deploy needs binaries created in job build — how?
- **Presented (shuffled):** A. cache in deploy, read in build · B. upload artifacts in build, download in deploy · C. cache in build, read in deploy · D. upload artifacts in deploy, download in build
- **Source Q-ID:** GHCertified Q047
- **Correct (shuffled frame):** B  — content: upload artifacts in build, download in deploy
- **shuffle->orig map:** A<-D  B<-A  C<-C  D<-B
- **Learner answer:** B
- **Grade:** ✓  (correct B == learner B)

### GHCertified Q048  (presented 2026-06-29T13:14Z) [single]
- **Stem:** job2 uses artifacts from job1 — ensure job1 finishes first. How to create the dependency?
- **Presented (shuffled):** A. implicit via download-artifact · B. order in .yaml · C. needs keyword in job2 · D. concurrency keyword in job2
- **Source Q-ID:** GHCertified Q048
- **Correct (shuffled frame):** C  — content: needs keyword in job2
- **shuffle->orig map:** A<-B  B<-C  C<-A  D<-D
- **Learner answer:** C
- **Grade:** ✓  (correct C == learner C)

### GHCertified Q049  (presented 2026-06-29T13:15Z) [multi-select, 6 opts A-F]
- **Stem:** Which is true about Starter Workflows?
- **Presented (shuffled):** A. paid feature · B. cannot call reusable wf · C. GitHub provides/maintains per category/lang/tooling · D. ready-to-use templates (minimal changes) · E. org can create custom starter workflows · F. cannot be modified
- **Source Q-ID:** GHCertified Q049
- **Correct (shuffled frame):** C, D, E  — content: GitHub-provided + ready-to-use templates + org-custom
- **shuffle->orig map:** A<-E  B<-D  C<-B  D<-A  E<-C  F<-F
- **Learner answer:** C, D, E
- **Grade:** ✓  (correct C,D,E == learner C,D,E)

### GHCertified Q050  (presented 2026-06-29T13:22Z) [multi-select, 7 opts A-G] — NOTE: same Q-ID as A1·Q050 (prior (c) miss: no cross-repo environment)
- **Stem:** Secrets and configuration variables can be scoped to:
- **Presented (shuffled):** A. single repo · B. environment shared across multiple repos · C. entire org or selected repos · D. specific workflow · E. environment in a repo · F. specific job · G. multiple repos not sharing org/enterprise
- **Source Q-ID:** GHCertified Q050
- **Correct (shuffled frame):** A, C, E  — content: single repo + org(or selected repos) + environment-in-a-repo
- **shuffle->orig map:** A<-B  B<-D  C<-A  D<-F  E<-C  F<-G  G<-E
- **Learner answer:** A, C, E
- **Grade:** ✓  (correct A,C,E == learner A,C,E). RESOLVES prior A1·Q050 (c) miss — learner correctly rejected cross-repo environment + non-org multi-repo traps.

### GHCertified Q051  (presented 2026-06-29T13:24Z) [single]
- **Stem:** What are the three types of Actions?
- **Presented (shuffled):** A. Python/JavaScript/Custom · B. Docker/JavaScript/Custom · C. Docker/Java/Composite · D. Docker container/JavaScript/Composite
- **Source Q-ID:** GHCertified Q051
- **Correct (shuffled frame):** D  — content: Docker container, JavaScript, Composite
- **shuffle->orig map:** A<-B  B<-C  C<-D  D<-A
- **Learner answer:** D
- **Grade:** ✓  (correct D == learner D)

### GHCertified Q052  (presented 2026-06-29T13:25Z) [single]
- **Stem:** True? "Docker container actions are usually slower than JavaScript actions"
- **Presented (shuffled):** A. False · B. True
- **Source Q-ID:** GHCertified Q052
- **Correct (shuffled frame):** B  — content: True (Docker image retrieval/build adds latency)
- **shuffle->orig map:** A<-B  B<-A
- **Learner answer:** B
- **Grade:** ✓  (correct B == learner B)

### GHCertified Q053  (presented 2026-06-29T13:25Z) [single]
- **Stem:** True/False: custom action source must be in .github/workflows
- **Presented (shuffled):** A. Only if reusable · B. True · C. False · D. Only for Docker container actions
- **Source Q-ID:** GHCertified Q053
- **Correct (shuffled frame):** C  — content: False (.github/workflows is for workflow files; actions live elsewhere w/ action.yml)
- **shuffle->orig map:** A<-C  B<-B  C<-A  D<-D
- **Learner answer:** C
- **Grade:** ✓  (correct C == learner C)

### GHCertified Q054  (presented 2026-06-29T13:26Z) [single]
- **Stem:** Custom action metadata must be defined in which file?
- **Presented (shuffled):** A. README · B. action.yml/.yaml in action repo · C. Marketplace UI · D. action.yml/.yaml but not required if not shared
- **Source Q-ID:** GHCertified Q054
- **Correct (shuffled frame):** B  — content: action.yml/action.yaml in the action repository (always required)
- **shuffle->orig map:** A<-B  B<-A  C<-C  D<-D
- **Learner answer:** B
- **Grade:** ✓  (correct B == learner B)

### GHCertified Q055  (presented 2026-06-29T13:40Z) [single] — relates to §7 A1·Q171 (re-run reuses SHA)
- **Stem:** Workflow ran on commit A (failed), fixed in commit B; re-run uses which commit's code?
- **Presented (shuffled):** A. triggers two workflows · B. cannot re-run · C. code from commit A · D. code from commit B
- **Source Q-ID:** GHCertified Q055
- **Correct (shuffled frame):** C  — content: commit A (re-run reuses original SHA, not latest)
- **shuffle->orig map:** A<-D  B<-C  C<-A  D<-B
- **Learner answer:** C
- **Grade:** ✓  (correct C == learner C)

### GHCertified Q056  (presented 2026-06-29T13:41Z) [single]
- **Stem:** How to require manual maintainer approval when targeting production environment?
- **Presented (shuffled):** A. not supported · B. branch protection rules · C. deployment protection rules · D. required reviewers in the production workflow
- **Source Q-ID:** GHCertified Q056
- **Correct (shuffled frame):** C  — content: deployment protection rules (environment required reviewers)
- **shuffle->orig map:** A<-D  B<-C  C<-A  D<-B
- **Learner answer:** C
- **Grade:** ✓  (correct C == learner C) — ⚑ LEARNER-FLAGGED 'track this': correct concept (protect environment) but low confidence on exact term. WATCH ITEM → §7: environment 'deployment protection rules' = required reviewers + wait timer + deployment branch/tag policies (+custom via apps); set ON the environment, not in workflow.

### GHCertified Q057  (presented 2026-06-29T13:46Z) [single]
- **Stem:** Which is true about environments?
- **Presented (shuffled):** A. workflow max two envs · B. each job references a single environment · C. each job max two envs · D. each workflow references a single env
- **Source Q-ID:** GHCertified Q057
- **Correct (shuffled frame):** B  — content: each job in a workflow can reference a single environment
- **shuffle->orig map:** A<-D  B<-A  C<-C  D<-B
- **Learner answer:** B
- **Grade:** ✓  (correct B == learner B)

### GHCertified Q058  (presented 2026-06-29T13:47Z) [single]
- **Stem:** Safest/recommended way to authenticate to cloud (AWS/Azure/GCP) from Actions?
- **Presented (shuffled):** A. Using OIDC · B. access keys in variables · C. Using Vault · D. access keys in secrets
- **Source Q-ID:** GHCertified Q058
- **Correct (shuffled frame):** A  — content: OIDC
- **shuffle->orig map:** A<-A  B<-D  C<-B  D<-C
- **Learner answer:** A
- **Grade:** ✓  (correct A == learner A)

### GHCertified Q059  (presented 2026-06-29T13:48Z) [single]
- **Stem:** Public repo, pull_request workflow — how to require approval for runs from forks?
- **Presented (shuffled):** A. required approvals for fork runs in repo · B. deployment protection rules · C. fork_pull_request event w/ require-approval (made-up) · D. branch protection rules
- **Source Q-ID:** GHCertified Q059
- **Correct (shuffled frame):** A  — content: setup required approvals for fork runs in the repository
- **shuffle->orig map:** A<-A  B<-B  C<-D  D<-C
- **Learner answer:** B (deployment protection rules)
- **Grade:** ✗  (correct A != learner B) — bucket (c): CONFLATED env deployment-protection-rules with the repo/org Actions setting 'Require approval for fork pull request workflows'. Fork-PR approval = gate on whether a fork contributor's run executes; deployment protection rules = environment deployment gate. → §7 (pairs with Q056 watch item).

### GHCertified Q060  (presented 2026-06-29T13:49Z) [single] — relates to §7 A1·Q061 (default env-var list)
- **Stem:** Which default env var = name of person/app that initiated the run?
- **Presented (shuffled):** A. GITHUB_ACTOR · B. GITHUB_REPOSITORY · C. GITHUB_USER · D. GITHUB_WORKFLOW
- **Source Q-ID:** GHCertified Q060
- **Correct (shuffled frame):** A  — content: GITHUB_ACTOR (GITHUB_USER does not exist)
- **shuffle->orig map:** A<-D  B<-B  C<-A  D<-C
- **Learner answer:** A
- **Grade:** ✓  (correct A == learner A)

### GHCertified Q061  (presented 2026-06-29T13:50Z) [multi-select, 6 opts] — same Q-ID as A1·Q061 prior (c) miss (GITHUB_TOKEN is a secret, not default env var)
- **Stem:** Which are default environment variables in GitHub Actions?
- **Presented (shuffled):** A. GITHUB_ORGANIZATION · B. GITHUB_REPOSITORY · C. GITHUB_ACTOR · D. GITHUB_USER · E. GITHUB_WORKFLOW · F. GITHUB_TOKEN
- **Source Q-ID:** GHCertified Q061
- **Correct (shuffled frame):** B, C, E  — content: GITHUB_REPOSITORY + GITHUB_ACTOR + GITHUB_WORKFLOW (NOT USER/ORGANIZATION/TOKEN; TOKEN is a secret)
- **shuffle->orig map:** A<-E  B<-A  C<-C  D<-D  E<-B  F<-F
- **Learner answer:** B, C, E
- **Grade:** ✓  (correct B,C,E == learner B,C,E). RESOLVES prior A1·Q061 (c) miss — learner correctly excluded GITHUB_TOKEN (secret, not default env var) + nonexistent USER/ORGANIZATION.

### GHCertified Q062  (presented 2026-06-29T13:51Z) [single]
- **Stem:** Org secret SomeSecret gives unexpected value via secrets.SomeSecret — why?
- **Presented (shuffled):** A. also declared in enterprise scope · B. need GitHub API for org secrets · C. also declared in repository scope · D. expression only for repo-scoped secrets
- **Source Q-ID:** GHCertified Q062
- **Correct (shuffled frame):** C  — content: also declared in repository scope (repo overrides org; precedence repo>org>enterprise)
- **shuffle->orig map:** A<-B  B<-D  C<-A  D<-C
- **Learner answer:** C
- **Grade:** ✓  (correct C == learner C)

### GHCertified Q063  (presented 2026-06-29T13:55Z) [single]
- **Stem:** Which is a correct way to print a debug message?
- **Presented (shuffled):** A. `echo "Watch out here!" >> $GITHUB_DEBUG` · B. `echo ":debug:Watch out here!"` · C. `echo "::debug::message=Watch out here!"` · D. `echo "::debug::Watch out here!"`
- **Source Q-ID:** GHCertified Q063
- **Correct (shuffled frame):** D
- **shuffle->orig map:** A<-D  B<-B  C<-C  D<-A
- **Learner answer:** D
- **Grade:** ✓  (correct D vs learner D)

### GHCertified Q064  (presented 2026-06-29T13:55Z) [single]
- **Stem:** How can organizations which are using GitHub Enterprise Server enable automatic syncing of third party GitHub Actions hosted on GitHub.com to their GitHub Enterprise Server instance?
- **Presented (shuffled):** A. Using actions-sync tool · B. Using GitHub Connect · C. GitHub Enterprise Server (GHES) cannot use GitHub.com Actions because of its on- · D. GitHub Enterprise Server has access to all GitHub.com Actions by default
- **Source Q-ID:** GHCertified Q064
- **Correct (shuffled frame):** B
- **shuffle->orig map:** A<-C  B<-A  C<-D  D<-B
- **Learner answer:** (none — learner flagged as genuinely unknown)
- **Grade:** GAP (not scored) — bucket (b) breadth: Domain-5 GHES. GitHub Connect = auto access to GitHub.com actions from GHES; actions-sync = manual (air-gapped); no access by default. → §7
- **Study-material check:** CONFIRMED NOT covered (GitHub Connect/actions-sync absent from recaps/cheats/indexes) → §7b course-gap agenda.

### GHCertified Q065  (presented 2026-06-29T13:58Z) [single]
- **Stem:** Where can you find network connectivity logs for a GitHub self-hosted-runner?
- **Presented (shuffled):** A. In the `_diag` folder directly on the runner machine · B. In the job run logs of a job that ran on that Runner · C. On GitHub.com on that specific Runner's page · D. In the job run logs of a job that ran on that Runner with debug logging enabled
- **Source Q-ID:** GHCertified Q065
- **Correct (shuffled frame):** A
- **shuffle->orig map:** A<-A  B<-C  C<-B  D<-D
- **Learner answer:** D
- **Grade:** ✗  (correct A vs learner D) — bucket (b)/(c): self-hosted runner network-connectivity logs live in the `_diag` folder ON the runner machine, not job logs. → §7

### GHCertified Q066  (presented 2026-06-29T14:01Z) [single]
- **Stem:** How can you validate that your GitHub self-hosted-runner can access all required GitHub services?
- **Presented (shuffled):** A. Using a GitHub provided script on the runner machine · B. By trying to access the runner machine by `ssh` to validate the network connecti · C. GitHub will validate the network connectivity automatically when the runner appl · D. By using the predefined GitHub Actions workflow `network-connectivity.yml`
- **Source Q-ID:** GHCertified Q066
- **Correct (shuffled frame):** A
- **shuffle->orig map:** A<-A  B<-B  C<-D  D<-C
- **Learner answer:** (none — learner flagged unknown)
- **Grade:** GAP (not scored) — bucket (b) study gap: runner connectivity validated by GitHub-provided script = runner `config.sh`/`run.sh` `--check`. No network-connectivity.yml; no auto-validate on install. Verified bank flags wording as loose (⚑). Study material does NOT cover --check → §7b.

### GHCertified Q067  (presented 2026-06-29T14:02Z) [single]
- **Stem:** Which is the correct way of triggering a job only if configuration variable `MY_VAR` has the value of `MY_VALUE`?
- **Presented (shuffled):** A. It's not possible because configuration variables cannot be used in job level `i · B. By creating the following conditional on job level ```yaml my-job: if: ${{ vars. · C. By creating the following conditional on job level ```yaml my-job: if: ${{ vars. · D. It's not possible because configuration variables cannot be used in `if` conditi
- **Source Q-ID:** GHCertified Q067
- **Correct (shuffled frame):** B
- **shuffle->orig map:** A<-D  B<-A  C<-B  D<-C
- **Learner answer:** A
- **Grade:** ✗  (correct B vs learner A) — bucket (b)/(c): vars CAN be used in job-level if; correct form `if: ${{ vars.MY_VAR == 'MY_VALUE' }}` (whole comparison INSIDE the braces). → §7

### GHCertified Q068  (presented 2026-06-29T14:04Z) [single]
- **Stem:** To run a `step` only if the secret `MY_SECRET` has been set, you can:
- **Presented (shuffled):** A. By creating the following conditional on step level ```yaml my-job: runs-on: ubu · B. By creating the following conditional on job level ```yaml my-job: runs-on: ubun · C. By creating the following conditional on step level ```yaml my-job: runs-on: ubu · D. Set the secret `MY_SECRET` as a job level environment variable, then reference t
- **Source Q-ID:** GHCertified Q068
- **Correct (shuffled frame):** D
- **shuffle->orig map:** A<-D  B<-B  C<-C  D<-A
- **Learner answer:** D
- **Grade:** ✓  (correct D vs learner D)

### GHCertified Q069  (presented 2026-06-29T14:06Z) [single]
- **Stem:** How can you use the GitHub API to download workflow run logs?
- **Presented (shuffled):** A. `PUT /repos/{owner}/{repo}/actions/runs/{run_id}/logs` · B. `HEAD /repos/{owner}/{repo}/actions/runs/{run_id}/logs` · C. `GET /repos/{owner}/{repo}/actions/runs/{run_id}/logs` · D. `POST /repos/{owner}/{repo}/actions/runs/{run_id}/logs`
- **Source Q-ID:** GHCertified Q069
- **Correct (shuffled frame):** C
- **shuffle->orig map:** A<-D  B<-C  C<-A  D<-B
- **Learner answer:** C
- **Grade:** ✓  (correct C vs learner C)

### GHCertified Q070  (presented 2026-06-29T14:08Z) [single]
- **Stem:** How can you use the GitHub API to create or update a repository secret?
- **Presented (shuffled):** A. `PUT /repos/{owner}/{repo}/actions/secrets/{secret_name}` · B. `GET /repos/{owner}/{repo}/actions/secrets/{secret_name}` · C. `POST /repos/{owner}/{repo}/actions/secrets/{secret_name}` · D. `HEAD /repos/{owner}/{repo}/actions/secrets/{secret_name}`
- **Source Q-ID:** GHCertified Q070
- **Correct (shuffled frame):** A
- **shuffle->orig map:** A<-A  B<-D  C<-B  D<-C
- **Learner answer:** C
- **Grade:** ✗  (correct A vs learner C) — bucket (b)/(c): create-or-update repo secret = PUT (idempotent), not POST. REST-verb pattern. → §7

### GHCertified Q071  (presented 2026-06-29T14:12Z) [multi]
- **Stem:** How can you override an organization-level GitHub Secret `API_KEY` with a different value when working within a repository?
- **Presented (shuffled):** A. By creating a environment secret with the name `ENVIRONMENT_API_KEY` · B. By creating a enterprise secret with the same name `API_KEY` · C. By creating a repository secret with the same name `API_KEY` · D. By creating a environment secret with the same name `API_KEY` · E. By creating a repository secret with the name `REPOSITORY_API_KEY` · F. By creating a environment secret with the name `OVERRIDE_API_KEY` · G. By creating a enterprise secret with the name `OVERRIDE_API_KEY` · H. By creating a repository secret with the name `OVERRIDE_API_KEY`
- **Source Q-ID:** GHCertified Q071
- **Correct (shuffled frame):** C, D
- **shuffle->orig map:** A<-H  B<-C  C<-A  D<-B  E<-G  F<-F  G<-D  H<-E
- **Learner answer:** C, D
- **Grade:** ✓  (correct C,D vs learner C,D)

### GHCertified Q072  (presented 2026-06-29T14:13Z) [multi]
- **Stem:** What components can be reused within a GitHub Organization?
- **Presented (shuffled):** A. Artifacts · B. Environment Variables · C. Cache · D. Workflow Templates · E. Secrets · F. Self Hosted Runners · G. Configuration Variables
- **Source Q-ID:** GHCertified Q072
- **Correct (shuffled frame):** D, E, F, G
- **shuffle->orig map:** A<-E  B<-G  C<-F  D<-D  E<-A  F<-C  G<-B
- **Learner answer:** B, E, F
- **Grade:** ✗  (correct D,E,F,G vs learner B,E,F) — bucket (c) RECONFIRMS A1·Q072: org-reusable = Secrets + Configuration Variables + Self-Hosted Runners + Workflow Templates. Learner picked 'Environment Variables' (not org-reusable) and missed Workflow Templates + Configuration Variables. env-vars vs config-vars confusion again. → §7

### GHCertified Q073  (presented 2026-06-29T14:16Z) [single]
- **Stem:** How many jobs will be executed in the following workflow? ```yaml jobs: matrix-job: runs-on: ubuntu-latest strategy: matrix: pet: [cat, dog] color: [pink, brown] include: - color: white pet: dog steps: - run: echo "Hello ${{ matrix.color }} ${{ matrix.pet }}" ```
- **Presented (shuffled):** A. 7 · B. 5 · C. 4 · D. 6
- **Source Q-ID:** GHCertified Q073
- **Correct (shuffled frame):** B
- **shuffle->orig map:** A<-D  B<-A  C<-B  D<-C
- **Learner answer:** B
- **Grade:** ✓  (correct B vs learner B)

### GHCertified Q074  (presented 2026-06-29T14:17Z) [single]
- **Stem:** Which of the following default environment variables contains the full name (e.g `octocat/hello-world`) of the repository where the workflow is running?
- **Presented (shuffled):** A. `GITHUB_REPOSITORY_ID` · B. `GITHUB_REPOSITORY` · C. `GITHUB_REPOSITORY_OWNER_ID` · D. `GITHUB_REPOSITORY_OWNER`
- **Source Q-ID:** GHCertified Q074
- **Correct (shuffled frame):** B
- **shuffle->orig map:** A<-B  B<-A  C<-D  D<-C
- **Learner answer:** B
- **Grade:** ✓  (correct B vs learner B)

### GHCertified Q075  (presented 2026-06-29T14:18Z) [single]
- **Stem:** In a workflow that has multiple jobs, all running on GitHub-hosted runners, is it true that all jobs are guaranteed to run on the same runner machine?
- **Presented (shuffled):** A. No · B. Only if they use the same `runs-on` label · C. Yes · D. Only if they run in parallel
- **Source Q-ID:** GHCertified Q075
- **Correct (shuffled frame):** A
- **shuffle->orig map:** A<-A  B<-D  C<-B  D<-C
- **Learner answer:** A
- **Grade:** ✓  (correct A vs learner A)

### GHCertified Q076  (presented 2026-06-29T14:18Z) [single]
- **Stem:** What's the maximum amount of reusable workflows that can be called from a single workflow file?
- **Presented (shuffled):** A. 50 · B. 1 · C. 5 · D. 10 · E. 20
- **Source Q-ID:** GHCertified Q076
- **Correct (shuffled frame):** A
- **shuffle->orig map:** A<-E  B<-C  C<-B  D<-D  E<-A
- **Learner answer:** A
- **Grade:** ✓  (correct A vs learner A)
- **Note:** RESOLVES prior A1·Q076 (reusable-wf cap 50/file, was 20).

### GHCertified Q077  (presented 2026-06-29T14:21Z) [single]
- **Stem:** What is a self-hosted runner?
- **Presented (shuffled):** A. A self-hosted runner is a system to manage pull requests from users of the organ · B. A self-hosted runner is a system that you deploy and manage to execute jobs from · C. A self-hosted runner is a system to be able to create workloads automatically · D. A self-hosted runner is a system to upload code to a private server
- **Source Q-ID:** GHCertified Q077
- **Correct (shuffled frame):** B
- **shuffle->orig map:** A<-D  B<-A  C<-C  D<-B
- **Learner answer:** B
- **Grade:** ✓  (correct B vs learner B)

### GHCertified Q078  (presented 2026-06-29T14:24Z) [single]
- **Stem:** Which of the following is a correct statement about GitHub Workflows and Actions?
- **Presented (shuffled):** A. Each action is composed of one or more workflows which is composed of one or mor · B. Each workflow is composed of one or more jobs which is composed of one or more s · C. Each action is composed of one or more jobs which is composed of one or more ste · D. Each workflow is composed of one or more actions which is composed of one or mor
- **Source Q-ID:** GHCertified Q078
- **Correct (shuffled frame):** B
- **shuffle->orig map:** A<-A  B<-C  C<-D  D<-B
- **Learner answer:** B
- **Grade:** ✓  (correct B vs learner B)

### GHCertified Q079  (presented 2026-06-29T14:43Z) [single]
- **Stem:** On which commit and branch do scheduled workflows run in GitHub Actions?
- **Presented (shuffled):** A. Scheduled workflows run on the specific commit on the main branch. · B. Scheduled workflows run on the specific commit on last modified branch. · C. Scheduled workflows run on the latest commit on the main branch. · D. Scheduled workflows run on the latest commit on the repository default branch.
- **Source Q-ID:** GHCertified Q079
- **Correct (shuffled frame):** D
- **shuffle->orig map:** A<-B  B<-A  C<-D  D<-C
- **Learner answer:** D
- **Grade:** ✓  (correct D vs learner D)
- **Note:** ⚑ LEARNER-FLAGGED low-confidence guess (correct). WATCH: scheduled = LATEST commit on DEFAULT branch (not literally 'main', not a fixed commit). → §7 watch.

### GHCertified Q080  (presented 2026-06-29T14:44Z) [single]
- **Stem:** What is the correct syntax for setting the directory for all `run` commands in a workflow?
- **Presented (shuffled):** A. set `directory` under `job` ```yaml defaults: run: shell: bash job: directory: . · B. set `directory` under `defaults.run` ```yaml defaults: run: shell: bash director · C. set `working-directory` under `defaults.run` ```yaml defaults: run: shell: bash  · D. set `working-directory` under `job` ```yaml defaults: run: shell: bash job: work
- **Source Q-ID:** GHCertified Q080
- **Correct (shuffled frame):** C
- **shuffle->orig map:** A<-D  B<-B  C<-A  D<-C
- **Learner answer:** C
- **Grade:** ✓  (correct C vs learner C)

### GHCertified Q081  (presented 2026-06-29T14:45Z) [multi]
- **Stem:** How can you reuse a defined workflow in multiple repositories?
- **Presented (shuffled):** A. By using workflow templates · B. By defining the workflow in a central repository · C. By copying the workflow file to each repository · D. By creating a reusable action
- **Source Q-ID:** GHCertified Q081
- **Correct (shuffled frame):** A, B
- **shuffle->orig map:** A<-B  B<-D  C<-A  D<-C
- **Learner answer:** B
- **Grade:** ✗  (correct A,B vs learner B) — RECLASSIFIED bucket (a) careless per learner: missed that it was multi-select (knew the concept). NOT a knowledge gap; removed from §7 review.

### GHCertified Q082  (presented 2026-06-29T14:46Z) [single]
- **Stem:** How can you ensure a job runs only on a specific branch?
- **Presented (shuffled):** A. By using the jobs filter · B. By using the branch keyword · C. By using the branches filter · D. By using the runs-on filter
- **Source Q-ID:** GHCertified Q082
- **Correct (shuffled frame):** C
- **shuffle->orig map:** A<-C  B<-D  C<-A  D<-B
- **Learner answer:** C
- **Grade:** ✓  (correct C vs learner C)

### GHCertified Q083  (presented 2026-06-29T14:47Z) [single]
- **Stem:** What does the `needs` keyword do in a GitHub Actions workflow?
- **Presented (shuffled):** A. Specifies the dependencies of a job · B. Triggers a job based on an event · C. Defines environment variables · D. Sets up the environment
- **Source Q-ID:** GHCertified Q083
- **Correct (shuffled frame):** A
- **shuffle->orig map:** A<-A  B<-D  C<-B  D<-C
- **Learner answer:** A
- **Grade:** ✓  (correct A vs learner A)

### GHCertified Q084  (presented 2026-06-29T14:48Z) [single]
- **Stem:** Which keyword allows you to define environment variables in a GitHub Actions workflow?
- **Presented (shuffled):** A. secrets · B. config · C. vars · D. env
- **Source Q-ID:** GHCertified Q084
- **Correct (shuffled frame):** D
- **shuffle->orig map:** A<-C  B<-D  C<-B  D<-A
- **Learner answer:** D
- **Grade:** ✓  (correct D vs learner D)

### GHCertified Q085  (presented 2026-06-29T14:48Z) [single]
- **Stem:** What is the purpose of the `with` keyword in a GitHub Actions workflow?
- **Presented (shuffled):** A. To trigger another workflow · B. To define environment variables · C. To set up dependencies · D. To specify input parameters for an action
- **Source Q-ID:** GHCertified Q085
- **Correct (shuffled frame):** D
- **shuffle->orig map:** A<-D  B<-A  C<-C  D<-B
- **Learner answer:** D
- **Grade:** ✓  (correct D vs learner D)

### GHCertified Q086  (presented 2026-06-29T14:48Z) [single]
- **Stem:** Which of the following GitHub Actions syntax is used to run multiple commands in a single step?
- **Presented (shuffled):** A. Using && to chain commands · B. Separating commands with a semicolon ; · C. Defining commands in an array · D. Using a multiline string with |
- **Source Q-ID:** GHCertified Q086
- **Correct (shuffled frame):** D
- **shuffle->orig map:** A<-A  B<-D  C<-B  D<-C
- **Learner answer:** C
- **Grade:** ✗ (chose C=array, invalid) — RECLASSIFIED bucket (d) ambiguous: && (A) and ; (B) also run multiple commands in one step, so D not uniquely correct. Learner's pick C (array) was invalid regardless. NOT a knowledge gap; removed from §7 review.

### GHCertified Q087  (presented 2026-06-29T14:50Z) [single]
- **Stem:** How can you cache dependencies to speed up workflow execution?
- **Presented (shuffled):** A. By storing them in the repository · B. By using the store keyword · C. Using the cache keyword · D. Using the actions/cache action
- **Source Q-ID:** GHCertified Q087
- **Correct (shuffled frame):** D
- **shuffle->orig map:** A<-C  B<-D  C<-A  D<-B
- **Learner answer:** D
- **Grade:** ✓  (correct D vs learner D)

### GHCertified Q088  (presented 2026-06-29T14:52Z) [single]
- **Stem:** What does the `matrix` keyword do in a GitHub Actions workflow?
- **Presented (shuffled):** A. Defines secrets for the workflow · B. Sets environment variables for the job · C. Allows defining multiple job configurations to run in parallel · D. Triggers workflows based on a schedule
- **Source Q-ID:** GHCertified Q088
- **Correct (shuffled frame):** C
- **shuffle->orig map:** A<-D  B<-B  C<-A  D<-C
- **Learner answer:** C
- **Grade:** ✓  (correct C vs learner C)

### GHCertified Q089  (presented 2026-06-29T14:53Z) [single]
- **Stem:** Which of the following can be used to limit the number of concurrent jobs running in a GitHub Actions workflow?
- **Presented (shuffled):** A. limit · B. max-jobs · C. parallelism · D. concurrency
- **Source Q-ID:** GHCertified Q089
- **Correct (shuffled frame):** D
- **shuffle->orig map:** A<-B  B<-C  C<-D  D<-A
- **Learner answer:** C
- **Grade:** ✗  (correct D vs learner C) — bucket (b)/(c): real keyword is `concurrency`; `parallelism` invented. (cf. `max-parallel` for matrix throttling, Q036.) → §7

### GHCertified Q090  (presented 2026-06-29T14:53Z) [single]
- **Stem:** What is the default timeout for a GitHub Actions job?
- **Presented (shuffled):** A. 30 minutes · B. 360 minutes · C. 120 minutes · D. 60 minutes
- **Source Q-ID:** GHCertified Q090
- **Correct (shuffled frame):** B
- **shuffle->orig map:** A<-A  B<-D  C<-C  D<-B
- **Learner answer:** B
- **Grade:** ✓  (correct B vs learner B)

### GHCertified Q091  (presented 2026-06-29T14:54Z) [single]
- **Stem:** How can you specify the operating system for a job in GitHub Actions?
- **Presented (shuffled):** A. Using the env keyword · B. Using the os keyword · C. Using the platform keyword · D. Using the runs-on keyword
- **Source Q-ID:** GHCertified Q091
- **Correct (shuffled frame):** D
- **shuffle->orig map:** A<-D  B<-A  C<-C  D<-B
- **Learner answer:** D
- **Grade:** ✓  (correct D vs learner D)

### GHCertified Q092  (presented 2026-06-29T14:54Z) [single]
- **Stem:** In a GitHub Actions workflow, how do you specify a specific version of Node.js to use in a job?
- **Presented (shuffled):** A. ```yaml uses: setup-node@v4 with: version: 20 ``` · B. ```yaml uses: actions/setup-node@v4 with: node-version: 20 ``` · C. ```yaml uses: setup-node@v4 with: node: 20 ``` · D. ```yaml uses: actions/node-setup@v4 with: node-version: 20 ```
- **Source Q-ID:** GHCertified Q092
- **Correct (shuffled frame):** B
- **shuffle->orig map:** A<-C  B<-A  C<-D  D<-B
- **Learner answer:** B
- **Grade:** ✓  (correct B vs learner B)

### GHCertified Q093  (presented 2026-06-29T14:55Z) [single]
- **Stem:** How do you reference a secret stored in GitHub Secrets in a workflow?
- **Presented (shuffled):** A. ${{ secrets.SECRET_NAME }} · B. ${{ secret.SECRET_NAME }} · C. ${{ config.SECRET_NAME }} · D. ${{ env.SECRET_NAME }}
- **Source Q-ID:** GHCertified Q093
- **Correct (shuffled frame):** A
- **shuffle->orig map:** A<-A  B<-B  C<-D  D<-C
- **Learner answer:** B
- **Grade:** ✗  (correct A vs learner B) — bucket (a) careless: context is `secrets` (plural), chose singular `secret`. Knows the concept. → pacing note

### GHCertified Q094  (presented 2026-06-29T14:56Z) [single]
- **Stem:** What is the default shell used by GitHub Actions on Windows runners?
- **Presented (shuffled):** A. powershell · B. cmd · C. bash · D. sh
- **Source Q-ID:** GHCertified Q094
- **Correct (shuffled frame):** A
- **shuffle->orig map:** A<-C  B<-D  C<-A  D<-B
- **Learner answer:** A
- **Grade:** ✓  (correct A vs learner A)
- **Note:** ⚑ Precision watch — real default Windows shell is `pwsh` (fallback `powershell`); bank simplifies to 'powershell'. If exam offers pwsh, prefer it.

### GHCertified Q095  (presented 2026-06-29T14:56Z) [multi]
- **Stem:** Which of the following statements are true about adding a self-hosted runner in GitHub Actions?
- **Presented (shuffled):** A. You can add a self-hosted runner to an organization · B. You can add a self-hosted runner to a workflow · C. You can add a self-hosted runner to an enterprise · D. You can add a self-hosted runner to a step · E. You can add a self-hosted runner to a repository
- **Source Q-ID:** GHCertified Q095
- **Correct (shuffled frame):** A, C, E
- **shuffle->orig map:** A<-B  B<-D  C<-C  D<-E  E<-A
- **Learner answer:** A, C
- **Grade:** ✗  (correct A,C,E vs learner A,C) — bucket (b)/(c): self-hosted runner levels = repository + organization + enterprise. Missed repository. → §7

### GHCertified Q096  (presented 2026-06-29T14:57Z) [single]
- **Stem:** Select the default environment variable that contains the operating system of the runner executing the job
- **Presented (shuffled):** A. `RUNNER_NAME` · B. `GITHUB_RUNNER_OS` · C. `RUNNER_ARCH` · D. `RUNNER_OS`
- **Source Q-ID:** GHCertified Q096
- **Correct (shuffled frame):** D
- **shuffle->orig map:** A<-D  B<-B  C<-C  D<-A
- **Learner answer:** D
- **Grade:** ✓  (correct D vs learner D)
- **Note:** RESOLVES prior A1·Q096 (RUNNER_ family default env vars).

### GHCertified Q097  (presented 2026-06-29T14:58Z) [single]
- **Stem:** How does the `actions/cache` action in GitHub Actions handle a cache miss?
- **Presented (shuffled):** A. by terminating the workflow if a cache miss occurs · B. by requiring manual intervention to create a new cache · C. by automatically creating a new cache if the job is completed successfully · D. by searching for a cache in other repositories
- **Source Q-ID:** GHCertified Q097
- **Correct (shuffled frame):** C
- **shuffle->orig map:** A<-D  B<-A  C<-C  D<-B
- **Learner answer:** C
- **Grade:** ✓  (correct C vs learner C)

### GHCertified Q098  (presented 2026-06-29T14:58Z) [single]
- **Stem:** How can you specify the schedule of a GitHub actions workflow to run on weekdays only?
- **Presented (shuffled):** A. it is not possible in GitHub actions · B. use the on: schedule: weekdays event trigger · C. use the on: schedule: cron event trigger · D. add a condition in the workflow YAML for weekdays
- **Source Q-ID:** GHCertified Q098
- **Correct (shuffled frame):** C
- **shuffle->orig map:** A<-B  B<-C  C<-D  D<-A
- **Learner answer:** D
- **Grade:** ✗  (correct C vs learner D) — bucket (b)/(c): weekdays via cron day-of-week field `cron: '0 0 * * 1-5'`. No `weekdays` keyword; no separate condition needed. → §7

### GHCertified Q099  (presented 2026-06-29T14:59Z) [single]
- **Stem:** What is the recommended approach for storing secrets larger than 48 KB?
- **Presented (shuffled):** A. encrypt and store secrets in the repository but keep the decryption passphrase a · B. avoid storing large secrets entirely to ensure security · C. store large secrets directly as repository secrets to avoid limitations · D. secrets larger than 48 KB cannot be stored
- **Source Q-ID:** GHCertified Q099
- **Correct (shuffled frame):** A
- **shuffle->orig map:** A<-C  B<-A  C<-D  D<-B
- **Learner answer:** A
- **Grade:** ✓  (correct A vs learner A)

### GHCertified Q100  (presented 2026-06-29T15:00Z) [single]
- **Stem:** Select status check functions in GitHub Actions
- **Presented (shuffled):** A. `state()`, `always()`, `cancelled()` and `failure()` · B. `completed()`, `always()`, `cancelled()` and `failure()` · C. `status()`, `always()`, `cancelled()` and `failure()` · D. `success()`, `always()`, `cancelled()` and `failure()`
- **Source Q-ID:** GHCertified Q100
- **Correct (shuffled frame):** D
- **shuffle->orig map:** A<-D  B<-B  C<-C  D<-A
- **Learner answer:** D
- **Grade:** ✓  (correct D vs learner D)
- **Note:** RESOLVES prior A1·Q100 (status-check function family, previously bit twice).

### GHCertified Q101  (presented 2026-06-29T15:01Z) [single]
- **Stem:** How do you ensure that `Upload Failure test report` step is executed only if `Run Tests` step fails?
- **Presented (shuffled):** A. ```yaml - name: Run Tests id: run-tests run: npm run test - name: Upload Failure · B. ```yaml - name: Run Tests id: run-tests run: npm run test - name: Upload Failure · C. ```yaml - name: Run Tests id: run-tests run: npm run test - name: Upload Failure · D. ```yaml - name: Run Tests id: run-tests run: npm run test - name: Upload Failure
- **Source Q-ID:** GHCertified Q101
- **Correct (shuffled frame):** D
- **shuffle->orig map:** A<-B  B<-C  C<-D  D<-A
- **Learner answer:** B
- **Grade:** ✗  (correct D vs learner B) — bucket (c) HIGH-VALUE: implicit if:success() gate skips steps after a failure UNLESS a status fn (failure()/always()/cancelled()) lifts it. B lacks failure() so it's skipped; D needs failure() && outcome check. Ties §7b#9. Learner asked the right question (default = failing step stops job). → §7

### GHCertified Q102  (presented 2026-06-29T15:03Z) [single]
- **Stem:** Which context holds information about the event that triggered a workflow run?
- **Presented (shuffled):** A. `github.repository` · B. `github.event` · C. `jobs.<job_id>.result` · D. `github.job`
- **Source Q-ID:** GHCertified Q102
- **Correct (shuffled frame):** B
- **shuffle->orig map:** A<-B  B<-A  C<-D  D<-C
- **Learner answer:** B
- **Grade:** ✓  (correct B vs learner B)

### GHCertified Q103  (presented 2026-06-29T15:04Z) [single]
- **Stem:** In GitHub Actions, if you define both branches and paths filter, what is the effect on the workflow execution?
- **Presented (shuffled):** A. the workflow will only run when both `branches` and `paths` are satisfied · B. the workflow will not run when both `branches` and `paths` are satisfied · C. the workflow will run when either `branches` or `paths` are satisfied, but will  · D. the workflow will run when either `branches` or `paths` are satisfied
- **Source Q-ID:** GHCertified Q103
- **Correct (shuffled frame):** A
- **shuffle->orig map:** A<-A  B<-D  C<-B  D<-C
- **Learner answer:** A
- **Grade:** ✓  (correct A vs learner A)

### GHCertified Q104  (presented 2026-06-29T15:05Z) [single]
- **Stem:** What is the recommended practice for treating environment variables in GitHub Actions, regardless of the operating system and shell used?
- **Presented (shuffled):** A. treat environment variables as case-sensitive · B. ignore case sensitivity as GitHub Actions handles it automatically · C. depend on the behavior of the operating system in use · D. use only uppercase letters for environment variable names
- **Source Q-ID:** GHCertified Q104
- **Correct (shuffled frame):** A
- **shuffle->orig map:** A<-A  B<-C  C<-D  D<-B
- **Learner answer:** D
- **Grade:** ✗  (correct A vs learner D) — bucket (b)/(c): recommended practice = treat env var names as CASE-SENSITIVE regardless of OS/shell. Uppercase-only is convention, not the documented recommendation. → §7

### GHCertified Q105  (presented 2026-06-29T15:05Z) [single]
- **Stem:** Which of the following statements accurately describes the behavior of workflow jobs referencing an environment's protection rules?
- **Presented (shuffled):** A. workflow jobs will fail if protection rules are configured · B. workflow jobs won't start until all the environment's protection rules pass · C. workflow jobs will start immediately and protection rules are evaluated during e · D. workflow jobs will start if at least one protection rule passes
- **Source Q-ID:** GHCertified Q105
- **Correct (shuffled frame):** B
- **shuffle->orig map:** A<-D  B<-A  C<-B  D<-C
- **Learner answer:** B
- **Grade:** ✓  (correct B vs learner B)

### GHCertified Q106  (presented 2026-06-29T15:06Z) [single]
- **Stem:** What is the purpose of the `restore-keys` parameter in `actions/cache` in GitHub Actions?
- **Presented (shuffled):** A. enable cross-OS cache functionality · B. indicate whether a cache hit occurred · C. provide alternative keys to use in case of a cache miss · D. specify the location of the cached files
- **Source Q-ID:** GHCertified Q106
- **Correct (shuffled frame):** C
- **shuffle->orig map:** A<-D  B<-B  C<-A  D<-C
- **Learner answer:** C
- **Grade:** ✓  (correct C vs learner C)
- **Note:** RESOLVES prior A1·Q106 (restore-keys = prefix fallbacks).

### GHCertified Q107  (presented 2026-06-29T15:07Z) [single]
- **Stem:** Which variable would you set to `true` in order to enable step debug logging?
- **Presented (shuffled):** A. `ACTIONS_WORKFLOW_DEBUG` · B. `ACTIONS_JOB_DEBUG` · C. `ACTIONS_STEP_DEBUG` · D. `ACTIONS_RUNNER_DEBUG`
- **Source Q-ID:** GHCertified Q107
- **Correct (shuffled frame):** C
- **shuffle->orig map:** A<-D  B<-B  C<-A  D<-C
- **Learner answer:** C
- **Grade:** ✓  (correct C vs learner C)

### GHCertified Q108  (presented 2026-06-29T15:07Z) [single]
- **Stem:** Which configuration is appropriate for triggering a workflow to run on webhook events related to check_run actions?
- **Presented (shuffled):** A. ```yaml on: check_run: types: [started] ``` · B. ```yaml on: check_run: types: [rerequested, completed] ``` · C. ```yaml on: check_run: filter: [requested] ``` · D. ```yaml on: check_run: type: [closed] ```
- **Source Q-ID:** GHCertified Q108
- **Correct (shuffled frame):** B
- **shuffle->orig map:** A<-B  B<-A  C<-D  D<-C
- **Learner answer:** C
- **Grade:** ✗  (correct B vs learner C) — ⚑ learner guessing. bucket (b)/(c): activity types keyword = `types:` (not filter/type). check_run types: created, rerequested, completed, requested_action. → §7 / §7b#2

### GHCertified Q109  (presented 2026-06-29T15:08Z) [single]
- **Stem:** What is the purpose of the `timeout-minutes` keyword in a step?
- **Presented (shuffled):** A. it sets the timeout for waiting on external events before proceeding to the next · B. it specifies the maximum duration a job is allowed to run · C. it defines the time interval for individual commands within a step · D. it limits the execution time for individual step
- **Source Q-ID:** GHCertified Q109
- **Correct (shuffled frame):** D
- **shuffle->orig map:** A<-C  B<-D  C<-B  D<-A
- **Learner answer:** D
- **Grade:** ✓  (correct D vs learner D)

### GHCertified Q110  (presented 2026-06-29T15:09Z) [single]
- **Stem:** Dave is creating a templated workflow for his organization. Where must Dave store the workflow files and associated metadata files for the templated workflow?
- **Presented (shuffled):** A. inside a directory named `workflow-templates` within the current repository · B. inside a directory named `workflow-templates` within a repository named `.github · C. inside a directory named `.github/org-templates` · D. inside a directory named `.github/workflow-templates`
- **Source Q-ID:** GHCertified Q110
- **Correct (shuffled frame):** B
- **shuffle->orig map:** A<-B  B<-A  C<-C  D<-D
- **Learner answer:** B
- **Grade:** ✓  (correct B vs learner B)

### GHCertified Q111  (presented 2026-06-29T15:09Z) [single]
- **Stem:** Dave wants to be notified when a comment is created on an issue within a GitHub repository. Which event trigger should be used within the workflow configuration?
- **Presented (shuffled):** A. `issues` · B. `comment` · C. `issue_comment` · D. `issues.comment`
- **Source Q-ID:** GHCertified Q111
- **Correct (shuffled frame):** C
- **shuffle->orig map:** A<-C  B<-D  C<-A  D<-B
- **Learner answer:** C
- **Grade:** ✓  (correct C vs learner C)
- **Note:** ⚑ LEARNER-FLAGGED known gap (correct). WATCH: `issue_comment` = comments on issues AND PRs; `issues` = issue lifecycle. → §7 watch / §7b#2 triggers.

### GHCertified Q112  (presented 2026-06-29T15:10Z) [single]
- **Stem:** What level of access is required on a GitHub repository in order to delete log files from workflow runs?
- **Presented (shuffled):** A. read · B. admin · C. write · D. owner
- **Source Q-ID:** GHCertified Q112
- **Correct (shuffled frame):** C
- **shuffle->orig map:** A<-B  B<-C  C<-A  D<-D
- **Learner answer:** C
- **Grade:** ✓  (correct C vs learner C)

### GHCertified Q113  (presented 2026-06-29T15:11Z) [single]
- **Stem:** What is true about the following workflow configuration if triggered against the `octo/my-dev-repo` repository? ```yaml name: deploy-workflow on: [push] jobs: production-deploy: if: github.repository == 'octo/my-prod-repo' runs-on: ubuntu-latest steps: - uses: actions/checkout@v4 - uses: actions/setup-node@v4 with: node-version: '14' - run: npm install -g bats ```
- **Presented (shuffled):** A. the `production-deploy` job will execute three steps · B. the `production-deploy` job will error · C. the `production-deploy` job will run if the `node-version` is `14` · D. the `production-deploy` job will be marked as skipped
- **Source Q-ID:** GHCertified Q113
- **Correct (shuffled frame):** D
- **shuffle->orig map:** A<-C  B<-B  C<-D  D<-A
- **Learner answer:** D
- **Grade:** ✓  (correct D vs learner D)

### GHCertified Q114  (presented 2026-06-29T15:11Z) [single]
- **Stem:** How can you access the current values of variables in a matrix within a job in the example below: ```yaml jobs: example_matrix: strategy: matrix: version: [10, 12, 14] os: [ubuntu-latest, windows-latest] ```
- **Presented (shuffled):** A. by accessing the variables directly with the syntax `version` and `os` · B. reference variables through the `matrix` context with syntax like`matrix.version · C. by using the `matrix.property` syntax · D. by using the `context` keyword within the job configuration
- **Source Q-ID:** GHCertified Q114
- **Correct (shuffled frame):** B
- **shuffle->orig map:** A<-D  B<-A  C<-B  D<-C
- **Learner answer:** B
- **Grade:** ✓  (correct B vs learner B)

### GHCertified Q115  (presented 2026-06-29T15:12Z) [single]
- **Stem:** What level of permission is required to re-run the workflows
- **Presented (shuffled):** A. write · B. read · C. owner · D. admin
- **Source Q-ID:** GHCertified Q115
- **Correct (shuffled frame):** A
- **shuffle->orig map:** A<-A  B<-B  C<-D  D<-C
- **Learner answer:** B
- **Grade:** ✗  (correct A vs learner B) — bucket (b)/(c): re-run workflows needs WRITE (read insufficient). Pairs w/ Q112 (write to delete logs). → §7

### GHCertified Q116  (presented 2026-06-29T15:13Z) [single]
- **Stem:** When can you delete workflow runs?
- **Presented (shuffled):** A. Workflow runs can be deleted at any time, regardless of their status or age. · B. Workflow runs cannot be deleted, but they can be archived. · C. After the workflow run has completed, regardless of its age. · D. After the workflow run has completed and at least 30 days have passed.
- **Source Q-ID:** GHCertified Q116
- **Correct (shuffled frame):** C
- **shuffle->orig map:** A<-C  B<-D  C<-A  D<-B
- **Learner answer:** C
- **Grade:** ✓  (correct C vs learner C)

### GHCertified Q117  (presented 2026-06-29T15:13Z) [single]
- **Stem:** Who can bypass configured deployment protection rules to force deployment (by default)
- **Presented (shuffled):** A. Anyone with repository write permission · B. Anyone with repository read permission · C. Repository administrators
- **Source Q-ID:** GHCertified Q117
- **Correct (shuffled frame):** C
- **shuffle->orig map:** A<-B  B<-C  C<-A
- **Learner answer:** C
- **Grade:** ✓  (correct C vs learner C)

### GHCertified Q118  (presented 2026-06-29T15:14Z) [single]
- **Stem:** How can you skip the following workflow run when you commit or create a PR? ```yaml name: Build on: [push, pull_request] jobs: build: runs-on: ubuntu-latest name: Extract artifact version ... ```
- **Presented (shuffled):** A. Provide `SKIP_WORKFLOW` in the commit message · B. The above workflow will run in every event of push or pull request in every case · C. By including any one of the following keywords in the commit message or in the t
- **Source Q-ID:** GHCertified Q118
- **Correct (shuffled frame):** C
- **shuffle->orig map:** A<-B  B<-C  C<-A
- **Learner answer:** C
- **Grade:** ✓  (correct C vs learner C)
- **Note:** RESOLVES prior A1·Q118 (skip-ci keyword set).

### GHCertified Q119  (presented 2026-06-29T15:14Z) [single]
- **Stem:** How can you determine if an action is a container action by looking at its action.yml file?
- **Presented (shuffled):** A. `runs.using` has `docker` as value · B. `runs.using` has `container` as value · C. `runs.main` has `container` as value · D. `runs.using` has `Dockerfile` as value
- **Source Q-ID:** GHCertified Q119
- **Correct (shuffled frame):** A
- **shuffle->orig map:** A<-A  B<-B  C<-D  D<-C
- **Learner answer:** A
- **Grade:** ✓  (correct A vs learner A)

### GHCertified Q120  (presented 2026-06-29T15:15Z) [single]
- **Stem:** What is the correct syntax for specifying a cleanup script in a container action?
- **Presented (shuffled):** A. ```yaml runs: using: 'docker' image: 'Dockerfile' entrypoint: 'entrypoint.sh' cl · B. ```yaml runs: using: 'docker' image: 'Dockerfile' entrypoint: 'entrypoint.sh' po · C. ```yaml runs: using: 'docker' image: 'Dockerfile' entrypoint: 'entrypoint.sh' af · D. ```yaml runs: using: 'docker' image: 'Dockerfile' entrypoint: 'entrypoint.sh' af · E. ```yaml runs: using: 'docker' image: 'Dockerfile' entrypoint: 'entrypoint.sh' po
- **Source Q-ID:** GHCertified Q120
- **Correct (shuffled frame):** E
- **shuffle->orig map:** A<-E  B<-B  C<-C  D<-D  E<-A
- **Learner answer:** B
- **Grade:** ✗  (correct E vs learner B) — bucket (b)/(c): container action cleanup = `post-entrypoint`; `post` is the JavaScript-action cleanup hook. → §7

### GHCertified Q121  (presented 2026-06-29T15:15Z) [multi]
- **Stem:** What’s true about default variables?
- **Presented (shuffled):** A. Most of the default environment variables have a corresponding context property · B. Default environment variables can be accessed using the env context · C. Default environment variables are set by GitHub and not defined in a workflow · D. Currently, the value of the default CI environment variable can be overwritten,  · E. You can add a new default environment variable adding the prefix “GITHUB_” to it · F. Default environment variables always have the prefix “GITHUB_”
- **Source Q-ID:** GHCertified Q121
- **Correct (shuffled frame):** A, C, D
- **shuffle->orig map:** A<-B  B<-F  C<-A  D<-C  E<-D  F<-E
- **Learner answer:** A, B, C
- **Grade:** ✗  (correct A,C,D vs learner A,B,C) — bucket (b)/(c): default env vars read via github context or directly, NOT env context (B false); CI var currently overwritable (D true). → §7
- **Note:** ⚑ LEARNER-FLAGGED for future study (default-variable behavior).

### GHCertified Q122  (presented 2026-06-29T15:17Z) [multi]
- **Stem:** What are the scopes defined for custom variables in a workflow?
- **Presented (shuffled):** A. The contents of a job within a workflow, by using `jobs.<job_id>.env` · B. All the jobs within a workflow, by using `jobs.env` · C. A specific step within a job, by using `jobs.<job_id>.steps[*].env` · D. A specific environment in the repository, by using `environment.<environment_id> · E. The entire workflow, by using `env` at the top level of the workflow file · F. The entire workflow, by using `custom.env` at the top level of the workflow file
- **Source Q-ID:** GHCertified Q122
- **Correct (shuffled frame):** A, C, E
- **shuffle->orig map:** A<-B  B<-D  C<-C  D<-F  E<-A  F<-E
- **Learner answer:** A, D, E
- **Grade:** ✗  (correct A,C,E vs learner A,D,E) — bucket (c) GAP (learner-suspected): `env:` key scopes = workflow / job (jobs.<id>.env) / step (steps[*].env). NO environment.<id>.env key. Environment-level vars are a SEPARATE feature (config vars/secrets via vars/secrets contexts). → §7

### KEEPER (cheat-sheet) — added 2026-06-29, learner-requested
- **Variables disambiguation (exam heuristic):** when a stem says "variables" ambiguously, let the OPTIONS disambiguate:
  - `env:` / `.env` keys in YAML → **custom environment variables** (scopes: workflow / job / step only).
  - `${{ vars.X }}` → **configuration variables** (set in settings UI; scopes: enterprise / org / repo / environment).
  - Cross-step sharing of env values is NOT via sibling reference → use `$GITHUB_ENV` (later steps) or step outputs (`$GITHUB_OUTPUT` → `steps.<id>.outputs.X`).
  - DEST: GH-200_Combined_Cheat_Sheets.md → 'Drill-Surfaced Keepers — Pass 1'.
