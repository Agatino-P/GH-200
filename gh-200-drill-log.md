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

### GHCertified Q123  (presented 2026-06-29T16:44Z) [single]
- **Stem:** What must be added to `actions/checkout` if `my-org/my-private-repo` is a private repository differing from the one containing the current workflow? ```yaml name: deploy-workflow on: [push] jobs: my-job: runs-on: ubuntu-latest steps: - name: "Checkout GitHub Action" uses: actions/checkout@v4 with: repository: my-org/my-private-repo path: ./.github/actions/my-org/my-private-repo ```
- **Presented (shuffled):** A. Leave as is since access tokens will be passed automatically ```yaml with: repos · B. The environmental variable `GITHUB_TOKEN` ```yaml with: repository: my-org/my-pr · C. Create an input `MY_ACCESS_TOKEN` ```yaml with: repository: my-org/my-private-re · D. Create a GitHub secret `MY_ACCESS_TOKEN` ```yaml with: repository: my-org/my-pri
- **Source Q-ID:** GHCertified Q123
- **Correct (shuffled frame):** D
- **shuffle->orig map:** A<-D  B<-C  C<-B  D<-A
- **Learner answer:** D
- **Grade:** ✓  (correct D vs learner D)

### GHCertified Q124  (presented 2026-06-29T16:47Z) [single]
- **Stem:** Given the following configuration, how many jobs will GitHub Actions run when this matrix is evaluated? ```yaml strategy: matrix: os: [ubuntu-latest, windows-latest] node: [14, 16] include: - os: macos-latest node: 18 - os: ubuntu-latest node: 14 ```
- **Presented (shuffled):** A. 5 jobs · B. 7 jobs · C. 4 jobs · D. 6 jobs · E. No jobs will run because the syntax is invalid.
- **Source Q-ID:** GHCertified Q124
- **Correct (shuffled frame):** A
- **shuffle->orig map:** A<-B  B<-D  C<-A  D<-C  E<-E
- **Learner answer:** A
- **Grade:** ✓  (correct A vs learner A)

### GHCertified Q125  (presented 2026-06-29T16:48Z) [multi]
- **Stem:** At what levels can environment variables be defined ?
- **Presented (shuffled):** A. Step level · B. Action level · C. Workflow level · D. Job level
- **Source Q-ID:** GHCertified Q125
- **Correct (shuffled frame):** A, C, D
- **shuffle->orig map:** A<-C  B<-D  C<-A  D<-B
- **Learner answer:** C, D
- **Grade:** ✗  (correct A,C,D vs learner C,D) — bucket (c) RECONFIRMS Q122: env: scopes = workflow/job/STEP. Missed STEP level AGAIN (specific recurring piece). NOT action level. → §7 (pinpoint: step-level env)

### GHCertified Q126  (presented 2026-06-29T16:48Z) [single]
- **Stem:** How should a dependent job reference the `output1` value produced by a job named `job1` earlier in the same workflow?
- **Presented (shuffled):** A. `${{job1.outputs.output1}}` · B. `${{needs.job1.outputs.output1}}` · C. `${{depends.job1.output1}}` · D. `${{needs.job1.output1}}`
- **Source Q-ID:** GHCertified Q126
- **Correct (shuffled frame):** B
- **shuffle->orig map:** A<-B  B<-A  C<-D  D<-C
- **Learner answer:** B
- **Grade:** ✓  (correct B vs learner B)

### GHCertified Q127  (presented 2026-06-29T16:49Z) [single]
- **Stem:** Which workflow command syntax correctly sets an environment variable named 'API_VERSION' with the value '2.1' for subsequent steps in a GitHub Actions job?
- **Presented (shuffled):** A. `set-env name=API_VERSION value=2.1` · B. `echo "API_VERSION=2.1" >> "$GITHUB_OUTPUT"` · C. `echo "API_VERSION=2.1" >> "$GITHUB_ENV"` · D. `export API_VERSION=2.1 >> "$GITHUB_ENV"`
- **Source Q-ID:** GHCertified Q127
- **Correct (shuffled frame):** C
- **shuffle->orig map:** A<-D  B<-B  C<-A  D<-C
- **Learner answer:** C
- **Grade:** ✓  (correct C vs learner C)

### GHCertified Q128  (presented 2026-06-29T16:50Z) [multi]
- **Stem:** A workflow is triggered when pull requests are reopened. Why might this be the cause?
- **Presented (shuffled):** A. No activity types are defined under the `pull_request` event. · B. `types: [reopened]` is defined under the `pull_request` event. · C. Branch protection rules were improperly configured. · D. `on: schedule` was configured with `pull_requests: [reopened]`
- **Source Q-ID:** GHCertified Q128
- **Correct (shuffled frame):** A, B
- **shuffle->orig map:** A<-C  B<-A  C<-B  D<-D
- **Learner answer:** A, B
- **Grade:** ✓  (correct A,B vs learner A,B)

### GHCertified Q129  (presented 2026-06-29T16:51Z) [single]
- **Stem:** `GITHUB_TOKEN` can be used to check out any repository.
- **Presented (shuffled):** A. False · B. True · C. Only with elevated permissions
- **Source Q-ID:** GHCertified Q129
- **Correct (shuffled frame):** A
- **shuffle->orig map:** A<-C  B<-A  C<-B
- **Learner answer:** A
- **Grade:** ✓  (correct A vs learner A)

### GHCertified Q130  (presented 2026-06-29T16:51Z) [multi]
- **Stem:** Which of the following are true regarding workflow-level vs. job-level outputs blocks?
- **Presented (shuffled):** A. A workflow-level `outputs` block must have the following structure: ``` outputs: · B. A reusable workflow can have both workflow-level and job-level `outputs` blocks. · C. A workflow-level `outputs` block should only be used in reusable workflows, not  · D. Job-level `outputs` blocks should only be used in caller workflows, not reusable · E. A job-level `outputs` block must have the following structure: ``` outputs: <out
- **Source Q-ID:** GHCertified Q130
- **Correct (shuffled frame):** A, B, C
- **shuffle->orig map:** A<-E  B<-C  C<-B  D<-A  E<-D
- **Learner answer:** A, B, C, E
- **Grade:** ✗  (correct A,B,C vs learner A,B,C,E) — bucket (c): `value:` key is WORKFLOW-LEVEL (workflow_call) outputs ONLY. Job-level outputs map directly `<name>: ${{ steps... }}` (no value:). Learner added E. → §7 (cheat keeper) 

### GHCertified Q131  (presented 2026-06-29T16:53Z) [multi]
- **Stem:** Which of the following are true regarding calling reusable workflows versus calling composite actions?
- **Presented (shuffled):** A. Composite actions must be called as a step within a job · B. Reusable workflows are called via referencing the folder that contains their `ac · C. Composite actions are called via referencing the folder that contains their `act · D. Secrets can be passed to both reusable workflows and calling composite actions v · E. Only reusable workflows can accept inputs. · F. Reusable workflows can use a different runner type than the caller workflow, whi · G. Reusable workflows must be called on workflow job level (not from step-level).
- **Source Q-ID:** GHCertified Q131
- **Correct (shuffled frame):** A, C, F, G
- **shuffle->orig map:** A<-C  B<-B  C<-A  D<-E  E<-F  F<-G  G<-D
- **Learner answer:** A, C, D, F
- **Grade:** ✗  (correct A,C,F,G vs learner A,C,D,F) — bucket (c) KEEPER: composite action = STEP in a job, caller's runner, NO secrets block (secrets via with:/env). Reusable wf = JOB-level uses:, own runner, secrets: block. Learner added D (composite has no uses.secrets) and missed G (job-level). → §7 cheat keeper

### GHCertified Q132  (presented 2026-06-29T16:56Z) [multi]
- **Stem:** Which of the following are true regarding GitHub Enterprise Server (GHES)?
- **Presented (shuffled):** A. GHES workflows cannot access GitHub.com nor GitHub Marketplace actions by defaul · B. Using GitHub Connect, users can follow a manual process to access GitHub.com act · C. GitHub Enterprise Server instances are self-hosted, compared to GitHub Enterpris · D. GHES is allowed to use enhanced versions of GitHub-hosted runners. · E. `actions/actions-sync` is primarily devoted to moving GitHub.com actions to a GH
- **Source Q-ID:** GHCertified Q132
- **Correct (shuffled frame):** A, C, E
- **shuffle->orig map:** A<-A  B<-D  C<-E  D<-C  E<-B
- **Learner answer:** A, C, E
- **Grade:** ✓  (correct A,C,E vs learner A,C,E)
- **Note:** ⚑ LEARNER-FLAGGED: GHEC vs GHES / enterprise hosting = giant training gap → §7b study area (GHEC=hosted SaaS; GHES=self-hosted; Connect auto / actions-sync manual; no Marketplace by default).

### GHCertified Q133  (presented 2026-06-29T16:58Z) [multi]
- **Stem:** Why use a commit SHA versus a tag to pin an action?
- **Presented (shuffled):** A. Commit SHAs are more difficult to trace in an audit, making it difficult for bad · B. Commit SHAs are immutable, whereas tags have the potential to be changed · C. Commit SHAs are more secure · D. Commit SHAs are guaranteed to point to the exact same code every time, tags are  · E. Commit SHAs are more convenient to use as opposed to tags
- **Source Q-ID:** GHCertified Q133
- **Correct (shuffled frame):** B, C, D
- **shuffle->orig map:** A<-E  B<-B  C<-A  D<-D  E<-C
- **Learner answer:** B, C, D
- **Grade:** ✓  (correct B,C,D vs learner B,C,D)

### GHCertified Q134  (presented 2026-06-29T16:59Z) [single]
- **Stem:** How do you run custom JavaScript scripts directly in a GitHub Actions workflow?
- **Presented (shuffled):** A. Via the `actions/github-script` action · B. By enabling the 'Allow custom JavaScript scripts' configuration in the Actions s · C. Write the contents of a script block to the `GITHUB_SCRIPT` environmental variab · D. By enabling the 'Allow custom JavaScript scripts' configuration in the Actions s · E. In a JavaScript Action, set the `using` key to `'github-script'`
- **Source Q-ID:** GHCertified Q134
- **Correct (shuffled frame):** A
- **shuffle->orig map:** A<-A  B<-C  C<-D  D<-B  E<-E
- **Learner answer:** A
- **Grade:** ✓  (correct A vs learner A)

### GHCertified Q135  (presented 2026-06-29T16:59Z) [single]
- **Stem:** You have forked a repository to enhance a workflow that uses a secret to access a third-party application. You trigger the workflow before editing its code to get a baseline result, but find that the workflow fails. Why would this occur?
- **Presented (shuffled):** A. Forked repositories only inherit repository secrets, so the secret being used in · B. Forked repositories do not inherit secrets from the original repository · C. The inherited secret had a size larger than 48 KB · D. When inheriting the secret from the original repository, there was an error duri
- **Source Q-ID:** GHCertified Q135
- **Correct (shuffled frame):** B
- **shuffle->orig map:** A<-D  B<-A  C<-C  D<-B
- **Learner answer:** B
- **Grade:** ✓  (correct B vs learner B)

### GHCertified Q136  (presented 2026-06-29T17:00Z) [single]
- **Stem:** You have a workflow that uses the matrix below. If a job in the matrix fails, how can you ensure other in-progress and queued jobs in the matrix are not cancelled? ```yaml jobs: deploy: strategy: matrix: version: ["1", "1.2", "1.3"] os: [ubuntu-latest, windows-latest] ```
- **Presented (shuffled):** A. Nothing needs to be done, since `jobs.<job_id>.strategy.fail-fast` has a default · B. Set `jobs.<job_id>.strategy.matrix.fail-fast` to `false` · C. Nothing needs to be done, since `jobs.<job_id>.strategy.matrix.fail-fast` has a  · D. Set `jobs.<job_id>.strategy.fail-fast` to `false` · E. There is no way to enforce this behavior, it cannot be worked around.
- **Source Q-ID:** GHCertified Q136
- **Correct (shuffled frame):** D
- **shuffle->orig map:** A<-B  B<-C  C<-D  D<-A  E<-E
- **Learner answer:** D
- **Grade:** ✓  (correct D vs learner D)

### GHCertified Q137  (presented 2026-06-29T17:01Z) [single]
- **Stem:** How many jobs will run in the following matrix? ```yaml jobs: test_deploy: strategy: matrix: os: [ubuntu-latest, windows-latest] version: [1, 2] include: - comment-color: "green" - error-color: "red" - os: "ubuntu-latest" comment-color: "blue" - os: "macos-latest" comment-color: "yellow" ```
- **Presented (shuffled):** A. 7 · B. 10 · C. 6 · D. 5
- **Source Q-ID:** GHCertified Q137
- **Correct (shuffled frame):** D
- **shuffle->orig map:** A<-C  B<-D  C<-B  D<-A
- **Learner answer:** D
- **Grade:** ✓  (correct D vs learner D)
- **Note:** §8 calibration flag #1 RESOLVED — matrix-include counting correct 3/3 (Q073/Q124/Q137).

### GHCertified Q138  (presented 2026-06-29T17:04Z) [single]
- **Stem:** You want to create a workflow `Post-Deploy` that performs post-deploy related activity. What event trigger should the `Post-Deploy` workflow use so it runs automatically after a specified workflow is completed?
- **Presented (shuffled):** A. `workflow_trigger` · B. `workflow_run` · C. `workflow_dispatch` · D. `workflow_call`
- **Source Q-ID:** GHCertified Q138
- **Correct (shuffled frame):** B
- **shuffle->orig map:** A<-B  B<-A  C<-C  D<-D
- **Learner answer:** B
- **Grade:** ✓  (correct B vs learner B)

### GHCertified Q139  (presented 2026-06-29T17:05Z) [multi]
- **Stem:** In what ways can you enable runner diagnostic logging?
- **Presented (shuffled):** A. Renaming the `_diag` directory of a self-hosted runner to `runner-diagnostic-log · B. Re-running a workflow with `Enable debug logging enabled` · C. Setting a secret or variable named `ACTIONS_RUNNER_DEBUG` to `true` · D. By adding a `ACTIONS_RUNNER_DEBUG` top-level folder to the workflow's repository · E. By adding a `runner-diagnostic-logs` subfolder to the `_diag` directory of the s
- **Source Q-ID:** GHCertified Q139
- **Correct (shuffled frame):** B, C
- **shuffle->orig map:** A<-E  B<-B  C<-A  D<-C  E<-D
- **Learner answer:** B, C, E
- **Grade:** ✗  (correct B,C vs learner B,C,E) — bucket (b): runner diag logging enabled via ACTIONS_RUNNER_DEBUG (secret OR variable)=true, or re-run 'Enable debug logging'. Logs auto-land in runner `_diag`. E (manual _diag subfolder) invented. Learner-flagged self-hosted-diag training gap → reinforces §7b runner-diag. → §7

### GHCertified Q140  (presented 2026-06-29T17:07Z) [single]
- **Stem:** You are writing a reusable workflow which has `branch-name` as an input. How can you conditionally run a step in that workflow if the branch name begins with 'smoke-test'?
- **Presented (shuffled):** A. Use the `branches` filter under `workflow_call` ```yaml on: workflow_call: branc · B. Use the built-in `startsWith` method in combination with `jobs.<job_id>.steps[*] · C. Use shell conditionals in combination with `jobs.<job_id>.steps[*].if` ```yaml i · D. Use the built-in `startsWith` method in combination with `jobs.<job_id>.steps[*]
- **Source Q-ID:** GHCertified Q140
- **Correct (shuffled frame):** D
- **shuffle->orig map:** A<-C  B<-B  C<-D  D<-A
- **Learner answer:** D
- **Grade:** ✓  (correct D vs learner D)

### GHCertified Q141  (presented 2026-06-29T17:30Z) [single]
- **Stem:** Why might you use `hashFiles` when utilizing `actions/cache`? ```yaml - uses: actions/cache@v5 with: path: ~/.npm key: ${{ runner.os }}-build-${{ env.cache-name }}-${{ hashFiles('**/package-lock.json') }} ```
- **Presented (shuffled):** A. If a cache key contains the dependencies file wrapped in `hashFiles`, the key ch · B. When using `hashFiles` as part of a cache key, an additional step will be genera · C. `hashFiles` is required for compatibility with Windows runners. · D. When using `hashFiles` as part of a cache key, if there is a cache miss, `hashFi
- **Source Q-ID:** GHCertified Q141
- **Correct (shuffled frame):** A
- **shuffle->orig map:** A<-A  B<-D  C<-B  D<-C
- **Learner answer:** A
- **Grade:** ✓  (correct A vs learner A)

### GHCertified Q142  (presented 2026-06-29T17:30Z) [multi]
- **Stem:** Which of the following answers is correct regarding installation access tokens?
- **Presented (shuffled):** A. `GITHUB_TOKEN` is a type of installation access token. · B. The `actions/create-github-app-token` can be called within workflows to create a · C. Installation access tokens are short-lived tokens ideal for automation activitie · D. The `actions/create-github-app-token` can be called within workflows to create a · E. Installation access tokens cannot be configured to act on behalf of their associ
- **Source Q-ID:** GHCertified Q142
- **Correct (shuffled frame):** A, B, C
- **shuffle->orig map:** A<-B  B<-C  C<-A  D<-D  E<-E
- **Learner answer:** (none — learner: first time reading about installation access tokens)
- **Grade:** GAP (not scored) — bucket (c) RETENTION (concept IS in recaps L1852/1879: GITHUB_TOKEN=installation access token, App tokens short-lived/not user-bound). Correct A,B,C. New detail = `actions/create-github-app-token` (immediate use). → §7 study (revisit App-token recap section)

### GHCertified Q143  (presented 2026-06-29T17:31Z) [single]
- **Stem:** Your organization wants to lower the retention period for stored artifacts, citing storage concerns. How can this be done at an organizational level?
- **Presented (shuffled):** A. This cannot be done: artifacts are strictly stored for 90 days across all system · B. This cannot be done at an organizational level. All workflows that utilize `acti · C. By navigating to the organization's Actions settings and editing the value of th · D. By using self-hosted runners, creating a `.github/retention-policy.yml` file, an
- **Source Q-ID:** GHCertified Q143
- **Correct (shuffled frame):** C
- **shuffle->orig map:** A<-D  B<-C  C<-A  D<-B
- **Learner answer:** C
- **Grade:** ✓  (correct C vs learner C)

### KEEPER (cheat-sheet) — added 2026-06-29, learner-requested (installation access tokens)
- **DEST:** GH-200_Combined_Cheat_Sheets.md → new dedicated paragraph (currently only embedded in recap "GITHUB_TOKEN vs PAT 5.4").
- Installation access token = short-lived (~1h), not user-bound, used by a GitHub App authenticating as an *installation*.
- GITHUB_TOKEN = the installation token for the App that Actions auto-installs (per-job, repo-scoped).
- `actions/create-github-app-token` mints an App installation token in-workflow for immediate use in that run. (NOT currently in recaps — new detail from Q142.)
- Escalation order: GITHUB_TOKEN → GitHub App installation token → fine-grained PAT (w/ expiry) last. Prefer App token over PAT (short-lived, not user-bound).

### §7b STUDY TOPIC (learner-requested deeper study) — added 2026-06-29
- **GitHub Apps + installation access tokens** — under-covered in course material; study for exam AND general knowledge.
  Read: GitHub docs "Authenticating with a GitHub App" / "Making authenticated API requests with a GitHub App installation".
  Cover: App registration vs installation, installation access tokens (short-lived, per-installation), permissions/events model, `actions/create-github-app-token`, App token vs PAT vs GITHUB_TOKEN.

### GHCertified Q144  (presented 2026-06-29T17:37Z) [single]
- **Stem:** How can you change the retention period for artifacts generated by a certain workflow?
- **Presented (shuffled):** A. In the workflow's repository, navigate to the Actions settings and editing the v · B. By navigating to the organization's Actions settings and editing the value of th · C. By utilizing the `retention-days` input in `actions/download-artifact` · D. By utilizing the `retention-days` input in `actions/upload-artifact`
- **Source Q-ID:** GHCertified Q144
- **Correct (shuffled frame):** D
- **shuffle->orig map:** A<-C  B<-D  C<-B  D<-A
- **Learner answer:** A
- **Grade:** ✗  (correct D vs learner A) — bucket (b)/(c): per-workflow artifact retention = `retention-days` input on actions/upload-artifact (override, capped by repo/org max). Settings = default/ceiling only; no per-workflow UI. → §7

### GHCertified Q145  (presented 2026-06-29T17:37Z) [multi]
- **Stem:** In what ways can you download an artifact?
- **Presented (shuffled):** A. By downloading artifacts from the Github Actions UI workflow run · B. By remotely accessing self-hosted runners via SSH and accessing the `.github/art · C. By using the `actions/download-artifact` action in a workflow · D. By using a specific GitHub API endpoint · E. By using the `actions/upload-artifact` action in a workflow
- **Source Q-ID:** GHCertified Q145
- **Correct (shuffled frame):** A, C, D
- **shuffle->orig map:** A<-B  B<-E  C<-A  D<-C  E<-D
- **Learner answer:** A, C, D
- **Grade:** ✓  (correct A,C,D vs learner A,C,D)

### GHCertified Q146  (presented 2026-06-29T17:38Z) [multi]
- **Stem:** Which statements are true regarding `github.ref` when the workflow is triggered by a `pull_request` event?
- **Presented (shuffled):** A. In pull requests that have not been merged, `github.ref` is the fully-formed ref · B. In pull requests (regardless of merge status), `github.ref` refers to the pull r · C. In pull requests that have not been merged, `github.ref` refers to the fully-for · D. In pull requests that have been merged, `github.ref` refers to the fully-formed  · E. In pull requests that have been merged, `github.ref` is the type of fully-formed · F. In pull requests (regardless of merge status), `github.ref` is the SHA of the la
- **Source Q-ID:** GHCertified Q146
- **Correct (shuffled frame):** C, D
- **shuffle->orig map:** A<-E  B<-C  C<-A  D<-B  E<-F  F<-D
- **Learner answer:** C, E
- **Grade:** ✗  (correct C,D vs learner C,E) — bucket (c) REINFORCES §7b#8 github.ref: PR unmerged=refs/pull/<n>/merge (C); PR merged=refs/heads/<base> (D). E confuses github.ref with github.ref_type (branch/tag/null). Learner-confirmed unstudied gap. → §7/§7b#8

### GHCertified Q147  (presented 2026-06-29T17:41Z) [single]
- **Stem:** You have a base-64 encoded secret that you decode in a GitHub Actions workflow. How can you make sure the decoded secret does not show up in the workflow log accidentally?
- **Presented (shuffled):** A. Using the built-in `maskSecret` function to redact the decoded secret in instanc · B. Avoiding the usage of print statements that contain the decoded secret, since th · C. Nothing needs to be done since Github Actions infrastructure automatically redac · D. Using `add-mask` workflow command in jobs where the decoded secret may be utiliz
- **Source Q-ID:** GHCertified Q147
- **Correct (shuffled frame):** D
- **shuffle->orig map:** A<-D  B<-C  C<-B  D<-A
- **Learner answer:** C
- **Grade:** ✗  (correct D vs learner C) — bucket (c) KEEPER: auto-masking covers the registered secret AND common ENCODINGS of it (incl. base64 — best-effort, brittle; base64(secret+suffix) can slip); a decoded/derived value is a NEW string → NOT auto-masked → use `::add-mask::` to register it. → §7 cheat keeper

### GHCertified Q148  (presented 2026-06-29T17:44Z) [single]
- **Stem:** Which statement is true regarding `github.ref` when the workflow is triggered by a push event?
- **Presented (shuffled):** A. In push events, `github.ref` is the type of fully-formed ref that triggered the  · B. In push events, `github.ref` is the description of the commit that triggered the · C. In push events, `github.ref` is the message of the commit that triggered the wor · D. In push events, `github.ref` is the fully-formed ref of the branch or tag ref th · E. In push events, `github.ref` is SHA of the commit that triggered the workflow.
- **Source Q-ID:** GHCertified Q148
- **Correct (shuffled frame):** D
- **shuffle->orig map:** A<-E  B<-D  C<-B  D<-A  E<-C
- **Learner answer:** E
- **Grade:** ✗  (correct D vs learner E) — bucket (c) REINFORCES §7b#8: push → github.ref = refs/heads/<branch> or refs/tags/<tag> (fully-formed ref). E=SHA is github.sha, not github.ref. ref-vs-SHA confusion (cf Q146). → §7/§7b#8

### GHCertified Q149  (presented 2026-06-29T17:47Z) [single]
- **Stem:** What does writing to `GITHUB_STEP_SUMMARY` do? ```yaml - name: "Write results of test suite" run: | echo "The results of the testing suite are:" >> $GITHUB_STEP_SUMMARY ```
- **Presented (shuffled):** A. Adds this line to the built-in artifact `github-steps-summary.md` · B. Adds this line to the job summary · C. Adds this line as a subtitle to the step name in the GitHub Actions UI · D. Prints this line as a step-level debug message
- **Source Q-ID:** GHCertified Q149
- **Correct (shuffled frame):** B
- **shuffle->orig map:** A<-C  B<-A  C<-B  D<-D
- **Learner answer:** C
- **Grade:** ✗  (correct B vs learner C) — bucket (b)/(c): writing to $GITHUB_STEP_SUMMARY adds markdown to the JOB SUMMARY (run summary page). Thin-coverage area (1.14 job summaries). → §7

### GHCertified Q150  (presented 2026-06-29T17:49Z) [single]
- **Stem:** Dorothea is troubleshooting a workflow triggered by a push event and is interested in seeing details about the webhook. How can she view the entire payload of the webhook that triggered the workflow?
- **Presented (shuffled):** A. Checking the "Show event webhook payload" checkbox under the workflow run option · B. Navigating to the "Webhooks" section of the repository settings · C. Printing the contents of the `github.event` object in a step · D. Setting a secret or variable named `SHOW_EVENT_PAYLOAD` to `true`
- **Source Q-ID:** GHCertified Q150
- **Correct (shuffled frame):** C
- **shuffle->orig map:** A<-B  B<-D  C<-A  D<-C
- **Learner answer:** C
- **Grade:** ✓  (correct C vs learner C)

### GHCertified Q151  (presented 2026-06-29T17:50Z) [single]
- **Stem:** Which should you use when passing information between jobs: job outputs or `GITHUB_ENV`?
- **Presented (shuffled):** A. `GITHUB_ENV`, because using it to set environmental variables puts significantly · B. `GITHUB_ENV`, because job outputs can only be set and referenced within the same · C. Job outputs, because the value of environmental variables set via writing to `GI · D. Job outputs, because they are simpler to set up
- **Source Q-ID:** GHCertified Q151
- **Correct (shuffled frame):** C
- **shuffle->orig map:** A<-D  B<-B  C<-A  D<-C
- **Learner answer:** C
- **Grade:** ✓  (correct C vs learner C)

### GHCertified Q152  (presented 2026-06-29T17:50Z) [single]
- **Stem:** Fill in the blank: When using self-hosted runners, the tool cache ___
- **Presented (shuffled):** A. cannot be populated · B. starts off empty and must be populated in order to save tools between runs · C. starts with the same tools GitHub-hosted runners do, as well as a selected assor · D. starts off the same as GitHub-hosted runners in that it is pre-populated with ce
- **Source Q-ID:** GHCertified Q152
- **Correct (shuffled frame):** B
- **shuffle->orig map:** A<-D  B<-A  C<-C  D<-B
- **Learner answer:** B
- **Grade:** ✓  (correct B vs learner B)

### GHCertified Q153  (presented 2026-06-29T17:51Z) [multi]
- **Stem:** Which of the following events can trigger a workflow that has not been merged to the default branch?
- **Presented (shuffled):** A. `star` · B. `push` · C. `issues` · D. `repository_dispatch` · E. `pull_request` · F. `issue_comment`
- **Source Q-ID:** GHCertified Q153
- **Correct (shuffled frame):** B, E
- **shuffle->orig map:** A<-D  B<-A  C<-E  D<-C  E<-B  F<-F
- **Learner answer:** B, D, E
- **Grade:** ✗  (correct B,E vs learner B,D,E) — bucket (c) KEEPER (learner-confirmed gap): ONLY push & pull_request run the workflow file from the event's branch → can trigger a not-yet-merged (feature-branch) workflow. ALL other events (repository_dispatch, star, issues, issue_comment, schedule, workflow_dispatch) use the DEFAULT-branch version. Learner added D (repository_dispatch) wrongly. → §7 cheat keeper

### GHCertified Q154  (presented 2026-06-29T17:54Z) [single]
- **Stem:** When would you build a Docker container action to share in the GitHub Actions marketplace?
- **Presented (shuffled):** A. Docker container actions have fast startup speed on Windows and macOS runners · B. Docker container actions allow you to utilize Docker without requiring an `actio · C. Docker container actions are a bundle of steps within other workflows that run w · D. Docker container actions are an out-of-the-box, low-overhead action · E. Docker container actions ensure a consistent runtime environment and specific de
- **Source Q-ID:** GHCertified Q154
- **Correct (shuffled frame):** E
- **shuffle->orig map:** A<-C  B<-E  C<-D  D<-B  E<-A
- **Learner answer:** E
- **Grade:** ✓  (correct E vs learner E)

### NOTE (triggers reference, §7b#2) — added 2026-06-29 (learner-requested)
- `star` event = fires when a repo is starred/unstarred (activity types: created, deleted). Runs from DEFAULT-branch workflow (like all events except push/pull_request). Niche (thank-you bots, star-milestone tracking).

### GHCertified Q155  (presented 2026-06-29T17:55Z) [single]
- **Stem:** Marianne has a feature branch that contains her new workflow file, which is set to be triggered at 2 AM every day, using the syntax seen below. However, the next day, the workflow does not trigger. Why might this be the case? ```yaml on: schedule: cron: "0 2 * * *" ```
- **Presented (shuffled):** A. The private repository containing the workflow has not had any repository activi · B. The `@daily` syntax was not used · C. `schedule` cannot be the only event in the workflow. It must be paired with a re · D. The workflow file must exist on the default branch in order to be triggered by t · E. The `cron` syntax is not scheduled correctly
- **Source Q-ID:** GHCertified Q155
- **Correct (shuffled frame):** D
- **shuffle->orig map:** A<-E  B<-D  C<-C  D<-A  E<-B
- **Learner answer:** D
- **Grade:** ✓  (correct D vs learner D)

### GHCertified Q156  (presented 2026-06-29T17:56Z) [multi]
- **Stem:** In what ways can you delete workflow artifacts?
- **Presented (shuffled):** A. By setting the artifact retention period to 0 days · B. By using the `actions/delete-artifact` action in a workflow · C. By remotely accessing self-hosted runners via SSH, navigating to the `.github/ar · D. By using a specific GitHub API endpoint · E. By using the Github Actions UI to delete the workflow run that generated the art · F. By using the Github Actions UI to navigate to a workflow run and delete the arti
- **Source Q-ID:** GHCertified Q156
- **Correct (shuffled frame):** D, E, F
- **shuffle->orig map:** A<-F  B<-D  C<-E  D<-C  E<-B  F<-A
- **Learner answer:** B, D, E, F
- **Grade:** ✗  (correct D,E,F vs learner B,D,E,F) — bucket (b)/(c): delete artifacts via API (D) / delete the run (E) / per-artifact UI delete (F). NO official actions/delete-artifact (B wrong; only upload/download official). retention min=1 (A '0 days' invalid). → §7

### GHCertified Q158  (presented 2026-06-29T17:58Z) [single]
- **Stem:** Petra is building a workflow whose sole job is named `post-merge`. How can she set up the job to be triggered upon a merged pull request?
- **Presented (shuffled):** A. Specify the the `pull_request` activity type as `closed` (no need for a job-leve · B. Specify the the `pull_request` activity type as `closed` and use a job-level con · C. Specify the `pull_request` activity type as `merged` (no need for a job-level co · D. Specify the `pull_request` activity type as `merged`, and use a job-level condit · E. Specify the `pull_request` activity type as `closed`, and use a job-level condit
- **Source Q-ID:** GHCertified Q158
- **Correct (shuffled frame):** E
- **shuffle->orig map:** A<-D  B<-E  C<-C  D<-B  E<-A
- **Learner answer:** E
- **Grade:** ✓  (correct E vs learner E)

### GHCertified Q159  (presented 2026-06-29T18:00Z) [multi]
- **Stem:** Which of the following are true when comparing the pull_request and pull_request_target events?
- **Presented (shuffled):** A. The `pull_request` event runs within the context of the merge commit, while `pul · B. Workflows will not run on `pull_request_target` activity if there is a merge con · C. Both `pull_request` and `pull_request_target` events have default activity types · D. Workflows will not run on `pull_request` activity if there is a merge conflict · E. `pull_request` should be used with caution, since PRs from forks will allow the  · F. The `pull_request_target` event should be used when you want to run code contain
- **Source Q-ID:** GHCertified Q159
- **Correct (shuffled frame):** A, C, D
- **shuffle->orig map:** A<-A  B<-E  C<-C  D<-B  E<-D  F<-F
- **Learner answer:** (none — declined to guess)
- **Grade:** GAP (not scored) — bucket (b) study area. Correct A,C,D. pull_request=merge commit, NO fork secrets, blocked by merge conflict, SAFE for PR code. pull_request_target=base branch context, FULL secrets incl forks, not blocked by conflict, DANGEROUS for untrusted PR code. Both default types opened/synchronize/reopened. → §7b SECURITY study area (ties 5.3 script injection)

### GHCertified Q160  (presented 2026-06-29T18:09Z) [multi]
- **Stem:** Why should you use OIDC when connecting a workflow to cloud providers?
- **Presented (shuffled):** A. Cloud providers require the use of OIDC. · B. OIDC generates JSON web tokens (JWTs) that can be used across workflow jobs · C. Using OIDC allows you to circumvent setting up trust policies with cloud provide · D. OIDC prevents you from having to keep cloud credentials as long-lived GitHub sec · E. Using OIDC within a workflow will automatically save that workflow's logs in clo · F. OIDC involves the generation and use of short-lived tokens, which is more secure
- **Source Q-ID:** GHCertified Q160
- **Correct (shuffled frame):** D, F
- **shuffle->orig map:** A<-C  B<-E  C<-D  D<-A  E<-F  F<-B
- **Learner answer:** B, D, F
- **Grade:** ✗  (correct D,F vs learner B,D,F) — bucket (c): OIDC reasons = no long-lived secrets (D) + short-lived tokens/more secure (F). The JWT is exchanged WITH the cloud provider for temp creds, not 'across jobs' (B distractor). → §7

### GHCertified Q161  (presented 2026-06-29T18:12Z) [single]
- **Stem:** How do workflows integrate with OIDC after a trust relationship has been established?
- **Presented (shuffled):** A. After adding a workflow to the "OIDC-allowed workflows" list in the repository s · B. The `on: OIDC_request` event trigger requests an OIDC token from GitHub's OIDC p · C. The `on: OIDC_request` event trigger requests a cloud access token from GitHub's · D. A workflow job requests an OIDC token from GitHub's OIDC provider. The OIDC toke · E. A workflow job requests an cloud access token from GitHub's cloud access provide
- **Source Q-ID:** GHCertified Q161
- **Correct (shuffled frame):** D
- **shuffle->orig map:** A<-E  B<-D  C<-C  D<-A  E<-B
- **Learner answer:** D
- **Grade:** ✓ EXPLANATION-PRIMED (Claude just walked the mechanism) — reinforced, not cold recall. ⚑ REVIEW: OIDC two-token flow — JWT (identity) exchanged with cloud provider for TEMPORARY cloud credentials. Learner forgot temp-creds; ties prior OIDC gap. → §7 review

### GHCertified Q162  (presented 2026-06-29T18:16Z) [multi]
- **Stem:** Mercedes wants to publish a Docker container action she has created to the GitHub Actions Marketplace. What files does she need at a minimum to do so?
- **Presented (shuffled):** A. `.dockerignore` · B. `action.yml` · C. A `Dockerfile`, if the image is built as part of the action during the workflow  · D. `CONTRIBUTING.md` · E. A `Dockerfile`, if the image is to be referenced from an image registry · F. `README.md`
- **Source Q-ID:** GHCertified Q162
- **Correct (shuffled frame):** B, C
- **shuffle->orig map:** A<-E  B<-A  C<-B  D<-F  E<-C  F<-D
- **Learner answer:** B, C
- **Grade:** ✓  (correct B,C vs learner B,C)

### GHCertified Q163  (presented 2026-06-29T18:17Z) [multi]
- **Stem:** Annette needs to write a workflow to publish a custom `npm` package that only members in her private organization will use. What should her workflow include?
- **Presented (shuffled):** A. An `on:registry_package` event with `types:[published]` · B. A token with `admin:packages` permissions · C. An `on:registry_package` event with no activity types specified · D. A token with `write:packages` permissions · E. Communication logic with the corresponding GitHub Packages registry `https://npm · F. Logic to publish to GitHub Packages
- **Source Q-ID:** GHCertified Q163
- **Correct (shuffled frame):** D, E, F
- **shuffle->orig map:** A<-F  B<-E  C<-D  D<-B  E<-C  F<-A
- **Learner answer:** C, D
- **Grade:** ✗  (correct D,E,F vs learner C,D) — bucket (b)/(c) learner-flagged shaky area: PUBLISH a package = write:packages token + registry config (npm.pkg.github.com) + publish logic (D,E,F). registry_package event (A/C) = react TO a publish, not do one. admin:packages (B) too much. → §7 + §7b GitHub Packages study area

### GHCertified Q164  (presented 2026-06-29T18:19Z) [multi]
- **Stem:** At what levels can `if:` be used in workflows?
- **Presented (shuffled):** A. Organization-level · B. Workflow-level · C. Environment-level · D. Job-level · E. Step-level
- **Source Q-ID:** GHCertified Q164
- **Correct (shuffled frame):** D, E
- **shuffle->orig map:** A<-E  B<-C  C<-D  D<-A  E<-B
- **Learner answer:** B, D, E
- **Grade:** ✗  (correct D,E vs learner B,D,E) — bucket (c) KEEPER: if: = JOB + STEP only (no workflow-level if). Contrast env: = workflow/job/step. Learner over-extended to workflow level. → §7 cheat keeper

### GHCertified Q165  (presented 2026-06-29T18:20Z) [multi]
- **Stem:** How does `repository_dispatch` enable systems outside of GitHub to trigger a workflow?
- **Presented (shuffled):** A. The external system makes a PUT request to the GitHub API to create a repository · B. The external system makes a POST request to the GitHub API to create a repositor · C. The workflow is triggered by a POST request to the workflow using the following  · D. The `on.repository_dispatch.types` workflow key corresponds to the `event_type`  · E. The workflow is triggered by the creation of a repository dispatch event · F. The `on.repository_dispatch.event_types` workflow key corresponds to the `event_
- **Source Q-ID:** GHCertified Q165
- **Correct (shuffled frame):** B, D, E
- **shuffle->orig map:** A<-D  B<-A  C<-E  D<-C  E<-B  F<-F
- **Learner answer:** B, C, D, E
- **Grade:** ✗  (correct B,D,E vs learner B,C,D,E) — bucket (b)/(c): repository_dispatch = POST /repos/O/R/dispatches (external event_type, filtered by on.repository_dispatch.types). workflow_dispatch = POST /repos/O/R/actions/workflows/<id>/dispatches (manual run of a specific wf). C conflated the two. Both POST. → §7b (workflow_dispatch vs repository_dispatch). NOT rote-path memorization.

### GHCertified Q166  (presented 2026-06-29T18:24Z) [multi]
- **Stem:** JavaScript actions and `actions/github-script` both use JavaScript. Why should you use `actions/github-script` versus creating your own JavaScript action?
- **Presented (shuffled):** A. `actions/github-script` should be used for short inline scripts · B. `actions/github-script` should be used when you need to utilize a fine-tuned Nod · C. JavaScript actions should be used when you want a low-overhead solution to makin · D. JavaScript actions should be used when you want a custom reusable action to be u · E. `actions/github-script` should be used when you want to use a pre-authenticated  · F. JavaScript actions should be used for short inline scripts
- **Source Q-ID:** GHCertified Q166
- **Correct (shuffled frame):** A, D, E
- **shuffle->orig map:** A<-A  B<-E  C<-F  D<-C  E<-B  F<-D
- **Learner answer:** A, D, E
- **Grade:** ✓  (correct A,D,E vs learner A,D,E)

### GHCertified Q167  (presented 2026-06-29T18:25Z) [single]
- **Stem:** Hilda needs access to an artifact generated by a recent workflow run, but the workflow file itself has since been deleted. Will she still be able to recover the artifact?
- **Presented (shuffled):** A. Yes, because deleting a workflow does not automatically delete its runs and gene · B. Yes, but only if she has administrator privileges · C. No, because while workflow runs will remain after a workflow is deleted, generat · D. No, because deleting a workflow automatically deletes its runs and generated art
- **Source Q-ID:** GHCertified Q167
- **Correct (shuffled frame):** A
- **shuffle->orig map:** A<-A  B<-C  C<-D  D<-B
- **Learner answer:** A
- **Grade:** ✓  (correct A vs learner A)

### GHCertified Q168  (presented 2026-06-29T18:26Z) [multi]
- **Stem:** Which keys are required when making an `action.yml` file?
- **Presented (shuffled):** A. `outputs` · B. `author` · C. `inputs` · D. `description` · E. `runs` · F. `name`
- **Source Q-ID:** GHCertified Q168
- **Correct (shuffled frame):** D, E, F
- **shuffle->orig map:** A<-F  B<-D  C<-E  D<-B  E<-C  F<-A
- **Learner answer:** E, F
- **Grade:** ✗  (correct D,E,F vs learner E,F) — bucket (b)/(c): action.yml REQUIRED keys = name + description + runs (missed description). author/inputs/outputs/branding optional. → §7

### GHCertified Q169  (presented 2026-06-29T18:26Z) [single]
- **Stem:** Manuela is setting up self-hosted runners for her organization, which has heavily restricted communication with IP addresses. How can she ensure the self-hosted runners can communicate with GitHub?
- **Presented (shuffled):** A. Adding the `.ip-exception` file to the top-level of the self-hosted runner's dir · B. Selecting the 'Allow access from self-hosted runners' checkbox in the organizati · C. Switch to GitHub-hosted standard runners, since self-hosted runners will be bloc · D. Adding the self-hosted runners' operating system to the organization's operating · E. Adding the self-hosted runners' IP address(es) to the organization's IP allow li
- **Source Q-ID:** GHCertified Q169
- **Correct (shuffled frame):** E
- **shuffle->orig map:** A<-C  B<-E  C<-D  D<-B  E<-A
- **Learner answer:** C
- **Grade:** ✗  (correct E vs learner C) — bucket (b)/(c): self-hosted runners + restrictive IP allow list → add runner IPs to org IP allow list (E). Thin area 4.4 IP allow lists. → §7
- **Real-world caveat (learner Q):** self-hosted runner IPs are stable only if infra gives them static/reserved IPs; ephemeral/autoscaled runners change IP → route egress through a fixed NAT/proxy IP and allow-list that. Exam answer (E) assumes known egress IPs.

### GHCertified Q170  (presented 2026-06-29T18:28Z) [single]
- **Stem:** Observe the values in `runs-on` key as seen in the below workflow job. Which is true regarding how the the job will run? ```yaml jobs: fire_emblem_deploy: name: "Deploy the 'Fire Emblem' application" runs-on: [self-hosted,nes,linux] ```
- **Presented (shuffled):** A. The job will run on a self-hosted runner that has all the labels applied. · B. The job will still be able to run on GitHub-hosted runners, since they can have  · C. The job will run on a self-hosted runner that has any of the labels applied. · D. The job will run on a runner (self-hosted or GitHub-hosted, whichever is first a
- **Source Q-ID:** GHCertified Q170
- **Correct (shuffled frame):** A
- **shuffle->orig map:** A<-A  B<-C  C<-B  D<-D
- **Learner answer:** C
- **Grade:** ✗  (correct A vs learner C) — bucket (b)/(c) KEEPER: runs-on label ARRAY = runner must have ALL labels (AND), not any. → §7 cheat keeper

### GHCertified Q171  (presented 2026-06-29T18:32Z) [multi]
- **Stem:** Why would you re-run a workflow versus generating a new workflow run?
- **Presented (shuffled):** A. Re-running a workflow overwrites the failing job runs, making runs appear more s · B. Re-running a workflow ensures `GITHUB_TRIGGERING_ACTOR` remains unchanged, so it · C. Re-running a workflow ensures `GITHUB_ACTOR` is updated, so it is unambiguous as · D. Re-running a workflow means the workflow jobs run in the same context of the com · E. Re-running a workflow allows you to enable extra debug logging for the selected  · F. Re-running a workflow lets you re-run failed workflow jobs, as opposed to genera
- **Source Q-ID:** GHCertified Q171
- **Correct (shuffled frame):** D, E, F
- **shuffle->orig map:** A<-F  B<-D  C<-E  D<-B  E<-C  F<-A
- **Learner answer:** D, E, F
- **Grade:** ✓  (correct D,E,F vs learner D,E,F)

### §7b STUDY TOPIC (learner-requested) — added 2026-06-29
- **Self-hosted runner labels** — learner-flagged unknown. Cover: default labels (`self-hosted`, OS e.g. `linux`, arch e.g. `x64`), custom labels, `runs-on` array = runner must match ALL labels (AND), label-based routing, and runner GROUPS (ties thin area 4.5). Read GitHub docs "Using labels with self-hosted runners" + "Managing access to self-hosted runners using groups".

### GHCertified Q172  (presented 2026-06-29T18:34Z) [single]
- **Stem:** Ingrid's organization has a subset of self-hosted Linux runners that should only be used by certain repositories. What is the best approach for her to enforce this behavior?
- **Presented (shuffled):** A. Create a new runner group, add the runners to the group, then select which repos · B. Create a new runner label, add the labels to the runners, then select which repo · C. Create a new runner group, select "Linux" as the OS, and use glob patterns to de · D. Create a new runner label, add the labels to the runners, then make sure all wor
- **Source Q-ID:** GHCertified Q172
- **Correct (shuffled frame):** A
- **shuffle->orig map:** A<-A  B<-B  C<-D  D<-C
- **Learner answer:** A
- **Grade:** ✓  (correct A vs learner A)
- **Note:** KEEPER — runner GROUPS = access control (which repos/orgs may use runners); LABELS = job routing only. Reinforces §7b 4.5.

### GHCertified Q173  (presented 2026-06-29T18:35Z) [single]
- **Stem:** An organization has several repositories that share a specialized Node.js environment hosted on a private network. The organization's next objective involves the setup of node-locking software within that network. Which of the following would best suit the organization's needs when it comes to executing workflows?
- **Presented (shuffled):** A. One self-hosted runner per repository, set up at the repository level · B. GitHub-hosted runners, with all workflows utilizing `actions/setup-node` · C. GitHub-hosted runners, using `runs-on: [node<version>]` (`<version>` being the d · D. Self-hosted runners set up at the organization-level · E. GitHub-hosted runners set up at the organization-level
- **Source Q-ID:** GHCertified Q173
- **Correct (shuffled frame):** D
- **shuffle->orig map:** A<-B  B<-C  C<-E  D<-A  E<-D
- **Learner answer:** D
- **Grade:** ✓  (correct D vs learner D)

### GHCertified Q174  (presented 2026-06-29T18:36Z) [single]
- **Stem:** The following workflow that calls a reusable workflows in one of its jobs. The reusable workflow has `permissions` defined at workflow level as seen below. What will be the result of calling the reusable workflow? ```yaml # caller workflow on: issues: types: [opened] permissions: contents: write jobs: issue_creator: permissions: contents: read uses: ./.github/workflows/issue-creator.yml # reusable
- **Presented (shuffled):** A. Both the caller and reusable workflow will not get called, because `issues` is n · B. The reusable workflow will create an issue in the repository titled `"Issue Repo · C. The reusable workflow will not be called, since reusable workflows must be in a  · D. The reusable workflow will return an error, since the job that called it only ha
- **Source Q-ID:** GHCertified Q174
- **Correct (shuffled frame):** D
- **shuffle->orig map:** A<-D  B<-B  C<-C  D<-A
- **Learner answer:** D
- **Grade:** ✓  (correct D vs learner D)

### GHCertified Q175  (presented 2026-06-29T18:39Z) [single]
- **Stem:** Catherine writes the following workflow job below. What will be the result of the job? ```yaml jobs: doc-generate: name: "Generate Scaffold Doc" runs-on: ubuntu-latest steps: - name: Setup Python 3.13 uses: actions/setup-python@v6 with: python-version: '3.13' - name: Grant Execute Permission to Scaffolding Python Script run: chmod +x ./scripts/scaffold-doc.py - name: Execute Scaffolding Python Scr
- **Presented (shuffled):** A. The Python script will not run, because `runs-on` does not have a value of `pyth · B. The Python script will not run, because `actions/python-setup` is not the correc · C. The Python script will run successfully, because the `chmod` command grants exec · D. The Python script will not run, because `actions/checkout` is not included in th
- **Source Q-ID:** GHCertified Q175
- **Correct (shuffled frame):** D
- **shuffle->orig map:** A<-C  B<-D  C<-B  D<-A
- **Learner answer:** C
- **Grade:** ✗  (correct D vs learner C) — bucket (c) KEEPER: no actions/checkout → repo files (the script) NOT on runner → chmod fails. Python is a red herring. Always need checkout to access repo files. → §7 cheat keeper

### GHCertified Q176  (presented 2026-06-29T18:42Z) [single]
- **Stem:** Judith has a workflow that should be triggered every time a commit is made to the repository. The repository is not always that active, so Judith desires the workflow to programmatically run once a week as a failsafe. What combination of events should she use to enforce this behavior?
- **Presented (shuffled):** A. `push` and `schedule` · B. This is not possible: `schedule` cannot be combined with other events · C. `push` and `workflow_dispatch` · D. `push` and `weekly` · E. `pull_request` (with `types:[closed]`) and `schedule`
- **Source Q-ID:** GHCertified Q176
- **Correct (shuffled frame):** A
- **shuffle->orig map:** A<-A  B<-E  C<-C  D<-D  E<-B
- **Learner answer:** A
- **Grade:** ✓  (correct A vs learner A)

### GHCertified Q177  (presented 2026-06-29T18:44Z) [single]
- **Stem:** Your workflow must fire off at 12:00 AM every Monday and Friday. Which of the following snippets correlates to this behavior?
- **Presented (shuffled):** A. ```yaml on: workflow_schedule: - cron: '1,5 * * 0 0' ``` · B. ```yaml on: workflow_schedule: - cron: '0 0 * * 1,5' ``` · C. ```yaml on: schedule: - cron: '0 0 * * 1,5' ``` · D. ```yaml on: schedule: - cron: '0 12 * * Mon,Fri' ``` · E. ```yaml on: workflow_call: - days: [Mon,Fri] - times: [00] ```
- **Source Q-ID:** GHCertified Q177
- **Correct (shuffled frame):** C
- **shuffle->orig map:** A<-D  B<-C  C<-A  D<-B  E<-E
- **Learner answer:** C
- **Grade:** ✓  (correct C vs learner C)

### GHCertified Q178  (presented 2026-06-29T18:48Z) [multi]
- **Stem:** You need to ensure that your `prod` environment requires manual approvals before deploys can proceed. Out of the following options, which are true regarding how this is set up?
- **Presented (shuffled):** A. If you list required reviewers, only one of them needs to approve to continue wi · B. Required reviewers need at least `write` access to the repository in order to ap · C. You can prevent self-reviews in the event the person who wants to deploy is also · D. You cannot prevent self-reviews, but you can set up alerts to see who triggered  · E. Only individual users can be assigned as required reviewers, not teams. · F. If you list required reviewers, all of them need to approve to continue with the
- **Source Q-ID:** GHCertified Q178
- **Correct (shuffled frame):** A, C
- **shuffle->orig map:** A<-A  B<-F  C<-B  D<-D  E<-E  F<-C
- **Learner answer:** A, B, C
- **Grade:** ✗  (correct A,C vs learner A,B,C) — bucket (c) KEEPER (verified vs GitHub docs): environment required reviewers = up to 6 users/teams, at least READ access (NOT write — B's trap), ONE approval suffices (not all), self-review preventable, teams allowed. → §7 cheat keeper

### GHCertified Q179  (presented 2026-06-29T18:52Z) [multi]
- **Stem:** You are considering a Marketplace action to utilize in your workflow. What are some aspects you can look for that indicate the action is trustworthy?
- **Presented (shuffled):** A. A 'Verified Creator' badge on the Marketplace page for the action · B. The `action.yml` is very brief · C. The source code for the action has not been updated in a long time, indicating d · D. The amount of Stars is low on the Marketplace page for the action · E. The README is thorough in defining the purpose of the action and how it works
- **Source Q-ID:** GHCertified Q179
- **Correct (shuffled frame):** A, E
- **shuffle->orig map:** A<-A  B<-C  C<-E  D<-D  E<-B
- **Learner answer:** A, E
- **Grade:** ✓  (correct A,E vs learner A,E)
