# GH-200 practice session 2026-07-07-b

Generated 2026-07-07 from `gh-200-gap-bank-2026-07-03.md` — 52 questions, options shuffled and re-lettered.
Answers withheld: grade each commitment with `log_answer.py` (see QUIZ-PROTOCOL.md).

---

## Q501

What does an artifact attestation establish about a build artifact?

- A. Unfalsifiable provenance: which workflow, repository, and commit produced the artifact
- B. That all of the artifact's tests passed
- C. That the artifact contains no known vulnerabilities
- D. That a reviewer approved the artifact for deployment

**Type:** *single*

---

## Q502

In addition to `contents: read`, which permissions does a job need to generate build provenance for a binary with `actions/attest-build-provenance`?

- A. `attestations: write`
- B. `actions: write`
- C. `id-token: write`
- D. `packages: write`

**Type:** *multi-select (2 correct)*

---

## Q503

Which command verifies an artifact attestation from a terminal?

- A. `git verify-attestation <path>`
- B. `gh attestation verify <path> --owner <org>`
- C. `gh provenance verify <path>`
- D. `gh artifact verify <path>`

**Type:** *single*

---

## Q504

How does GitHub document reaching SLSA Build Level 3 with artifact attestations?

- A. Perform the build and attestation inside a reusable workflow that acts as a trusted builder, isolated from the calling workflow
- B. Sign the artifact with a personal GPG key after the build
- C. Enable required reviewers on the production environment
- D. Run the build on larger runners

**Type:** *single*

---

## Q505

Where can artifact attestations be generated?

- A. Private and internal repositories on GitHub Enterprise Cloud
- B. Public repositories on any GitHub plan
- C. Public repositories only if the organization has GitHub Advanced Security
- D. Any repository on GitHub Enterprise Server

**Type:** *multi-select (2 correct)*

---

## Q506

Why does `gh attestation verify` require an `--owner` or `--repo` flag?

- A. The flag is needed to download the artifact from that repository first
- B. Verification must confirm the attestation was produced by the expected source — the signature alone doesn't prove who built the artifact
- C. It selects which account is billed for the verification API call
- D. It is optional and only speeds verification up

**Type:** *single*

---

## Q507

Which details are recorded in an artifact's build provenance?

- A. The names of organization members with repository access
- B. The workflow and repository that produced the artifact
- C. The commit SHA the build ran against
- D. The list of CVEs present in the artifact

**Type:** *multi-select (2 correct)*

---

## Q508

How do you generate an attestation for a container image rather than a file?

- A. Export the image as a tarball and attest the tarball instead
- B. Enable two-factor authentication on the registry account
- C. Container images cannot be attested
- D. Pass the image's digest to `attest-build-provenance` (`subject-digest`) and verify with an `oci://` reference

**Type:** *single*

---

## Q509

What signs artifact attestations?

- A. The workflow author's SSH signing key
- B. Sigstore — the public-good instance for public repositories, GitHub's internal Sigstore instance for private ones
- C. The runner's TLS certificate
- D. GitHub staff, manually, on request

**Type:** *single*

---

## Q510

Why is this step a security risk in a workflow triggered by `issues`?

```yaml
- run: echo "Title: ${{ github.event.issue.title }}"
```

- A. `github.event` is not available inside `run:` steps
- B. The title is attacker-controlled and is substituted into the script before the shell runs, enabling command injection
- C. `echo` automatically leaks secrets to the log
- D. The `issues` event cannot safely trigger workflows at all

**Type:** *single*

---

## Q511

What is the recommended way to use `github.event.pull_request.title` inside a `run:` script?

- A. Escape the expression with backslashes
- B. Assign it to an `env:` variable and reference the quoted variable (e.g. `"$TITLE"`) in the script
- C. Wrap the expression in single quotes inside the script
- D. Only use it on self-hosted runners

**Type:** *single*

---

## Q512

Which of these values are attacker-controllable and must be treated as untrusted input?

- A. `github.event.issue.title`
- B. `github.head_ref`
- C. `github.run_id`
- D. `github.event.pull_request.body`
- E. `github.workflow`

**Type:** *multi-select (3 correct)*

---

## Q513

Why does routing untrusted input through an `env:` variable prevent script injection?

- A. The shell refuses to expand variables that originate from event payloads
- B. `env:` values are sanitized by stripping shell metacharacters
- C. `env:` values are encrypted at rest
- D. The value reaches the process as data in memory instead of being pasted into the script text the shell parses

**Type:** *single*

---

## Q514

Besides intermediate environment variables, which are documented mitigations against script injection?

- A. Use an action that consumes the untrusted value as an input, instead of an inline script
- B. Base64-encode the untrusted value inside the `run:` script
- C. Move the step to a Windows runner where bash is not the default shell
- D. Use code scanning (e.g. CodeQL) to detect vulnerable workflow patterns

**Type:** *multi-select (2 correct)*

---

## Q515

How does restricting `GITHUB_TOKEN` permissions relate to script injection?

- A. It is unrelated to injection risk
- B. The token is never accessible from `run:` steps anyway
- C. It prevents the injection from executing in the first place
- D. It limits the blast radius — a successful injection only gets the token's reduced scopes

**Type:** *single*

---

## Q516

Which combination is the classic "pwn request" vulnerability?

- A. A `pull_request_target` workflow that checks out and executes the pull request's head code
- B. A `schedule` workflow that reads repository code
- C. A `pull_request` workflow that builds the merge commit
- D. A `workflow_dispatch` workflow with typed inputs

**Type:** *single*

---

## Q517

Why doesn't wrapping `${{ github.event.comment.body }}` in single quotes inside `run:` protect against injection?

- A. Single quotes are not valid in bash scripts
- B. It does protect fully — this is the documented mitigation
- C. Comment bodies cannot contain quote characters
- D. Actions expands the expression before the shell parses the script, so the payload can include a quote and break out

**Type:** *single*

---

## Q518

In a workflow file, what does `&shared` do on the `steps:` line of job `a`?

```yaml
jobs:
  a:
    runs-on: ubuntu-latest
    steps: &shared
      - uses: actions/checkout@v6
      - run: make build
```

- A. Creates an alias to a node defined elsewhere
- B. Defines an anchor, so the steps list can be reused elsewhere in this file via `*shared`
- C. Marks the steps list as deprecated
- D. Declares an environment variable named shared

**Type:** *single*

---

## Q519

Continuing the previous file, what does `steps: *shared` in job `b` do?

- A. Reuses the exact steps list anchored as `shared` in job `a`
- B. Imports steps from a file named shared.yml
- C. It is a YAML syntax error
- D. Runs job `a` before job `b`

**Type:** *single*

---

## Q520

Which YAML reuse constructs do GitHub Actions workflow files support?

- A. Anchors (`&`) and aliases (`*`) only — merge keys (`<<`) are a YAML 1.1 feature and Actions follows YAML 1.2
- B. Anchors, aliases, and merge keys
- C. None — all YAML reuse constructs are rejected by workflow validation
- D. Merge keys only

**Type:** *single*

---

## Q521

What happens when this workflow file is pushed?

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    env: &base
      LOG_LEVEL: info
      RETRIES: "3"
    steps:
      - run: make build
  test:
    runs-on: ubuntu-latest
    env:
      <<: *base
      LOG_LEVEL: debug
    steps:
      - run: make test
```

- A. It runs with `LOG_LEVEL: info` in job `test` — merged keys override local ones
- B. It fails to parse with a duplicate-key error
- C. It runs with `LOG_LEVEL: debug` in job `test` — the local key overrides the merged one
- D. The workflow is invalid — GitHub Actions does not support YAML merge keys (`<<:`), only anchors and aliases

**Type:** *single*

---

## Q522

Can `*shared` in one workflow file reference an anchor `&shared` defined in a different workflow file?

- A. Yes, if both files are in `.github/workflows`
- B. No — anchors and aliases are scoped to a single YAML file
- C. Only between a workflow and its reusable workflow
- D. Yes, via the `uses:` keyword

**Type:** *single*

---

## Q523

Job `b` reuses job `a`'s steps with `steps: *shared`, but needs one extra step at the end. What is true?

- A. Pass the extra step as a parameter to the alias
- B. Use `<<:` on the steps sequence to append the extra step
- C. An alias reproduces the anchored node exactly and cannot be extended — job `b` needs its own steps list
- D. Extra list items written under the alias are appended automatically

**Type:** *single*

---

## Q524

Which runner does job `deploy` use?

```yaml
jobs:
  build:
    runs-on: &r ubuntu-24.04
    steps:
      - run: make build
  deploy:
    runs-on: *r
    steps:
      - run: make deploy
```

- A. `ubuntu-24.04` — the alias resolves to the anchored value
- B. `ubuntu-latest` — aliases fall back to the default
- C. Whatever runner picked up job `build`
- D. It fails: aliases are not allowed in `runs-on`

**Type:** *single*

---

## Q525

How does a step add rendered Markdown to the workflow run summary page?

- A. Write a `summary` key to `$GITHUB_OUTPUT`
- B. Print `::summary::## Results` to stdout
- C. Append Markdown to the file at `$GITHUB_STEP_SUMMARY` (e.g. `echo "## Results" >> "$GITHUB_STEP_SUMMARY"`)
- D. Call the run-summaries REST API from the step

**Type:** *single*

---

## Q526

What is `GITHUB_STEP_SUMMARY`?

- A. A boolean flag that turns summaries on
- B. A context property containing the text of previous steps' summaries
- C. An automatically created secret
- D. An environment variable holding the path to a temporary file, unique per step, whose content becomes part of the job summary

**Type:** *single*

---

## Q527

Two steps in the same job each append a heading to their `$GITHUB_STEP_SUMMARY`. What appears on the run summary page?

- A. Only the last step's content
- B. Both headings — each step's summary content is grouped into the job's summary
- C. Nothing: only one step per job may write a summary
- D. Only the first step's content

**Type:** *single*

---

## Q528

What format is job summary content written in?

- A. AsciiDoc
- B. HTML only
- C. Plain text only
- D. GitHub-flavored Markdown

**Type:** *single*

---

## Q529

You want a Markdown test report visible directly on the run page, without downloading artifacts. Which file does the step write to?

- A. `$GITHUB_STEP_SUMMARY`
- B. `$GITHUB_ENV`
- C. `$GITHUB_PATH`
- D. `$GITHUB_OUTPUT`

**Type:** *single*

---

## Q530

What are service containers?

- A. The containers all jobs always execute in
- B. Docker containers that Actions starts for a job (e.g. a database), manages, and destroys when the job ends
- C. Long-running containers shared across workflow runs
- D. Kubernetes pods managed by GitHub

**Type:** *single*

---

## Q531

Which runners can host service containers?

- A. All GitHub-hosted runners, including Windows and macOS
- B. Self-hosted runners only
- C. Larger runners only
- D. Linux runners with Docker installed (e.g. `ubuntu-latest`, or a Linux self-hosted runner with Docker)

**Type:** *single*

---

## Q532

The job itself runs in a container. How do its steps reach a service container labeled `redis`?

- A. Via the service's public IP address
- B. Only through the `job.services.redis.url` context property
- C. Always via `localhost:6379`
- D. By hostname `redis` — the service label is the hostname on the shared Docker network

**Type:** *single*

---

## Q533

The job runs directly on the runner machine (no `container:`). How do steps reach the `redis` service container?

- A. Via a Docker network alias
- B. Via `localhost` and a host port mapped with `ports:` (e.g. `6379:6379`)
- C. By hostname `redis`
- D. They can't — a job container is mandatory for services

**Type:** *single*

---

## Q534

Where do you configure Docker health-check settings for a service container?

- A. In the service's `options:` key (`--health-cmd`, `--health-interval`, …)
- B. In a dedicated `healthcheck:` block
- C. Health checks are not supported for services
- D. In `runs-on`

**Type:** *single*

---

## Q535

A service maps `ports: ["6379/tcp"]`, letting Docker assign a random host port. How do steps discover the assigned port?

- A. The variable `$REDIS_PORT` is set automatically
- B. `${{ services.redis.port }}`
- C. Randomly assigned ports cannot be discovered
- D. `${{ job.services.redis.ports[6379] }}`

**Type:** *single*

---

## Q536

Your organization enables an IP allow list. What does GitHub document about standard GitHub-hosted runners?

- A. They can't be used with the allow list — the ranges are too numerous and updated weekly; use self-hosted runners or larger runners with static IPs
- B. They automatically bypass the allow list
- C. Add the keyword `azure` to the allow list to cover them
- D. IP allow lists do not affect Actions at all

**Type:** *single*

---

## Q537

Which feature provides GitHub-managed runners with fixed IP ranges that can be allow-listed?

- A. Larger runners with static IP addresses
- B. Standard `ubuntu-latest` runners
- C. Runner groups
- D. The `meta` REST API

**Type:** *single*

---

## Q538

Where do you obtain the current IP ranges used by GitHub-hosted runners?

- A. A monthly email from GitHub
- B. They are fixed and listed in the organization settings UI
- C. The runner's `_diag` folder
- D. The REST API: `GET https://api.github.com/meta` (the `actions` key)

**Type:** *single*

---

## Q539

Which network access does a self-hosted runner require to receive jobs?

- A. Inbound and outbound SSH (22)
- B. Outbound HTTPS (443) to GitHub only — it polls for jobs; no inbound ports are needed
- C. Outbound SMTP for job notifications
- D. An inbound HTTPS port reachable from GitHub's webhook IPs

**Type:** *single*

---

## Q540

Autoscaled ephemeral self-hosted runners get changing IPs, but the organization uses an IP allow list. What is the documented approach?

- A. Add `0.0.0.0/0` to the allow list
- B. Give the runners a stable egress IP range — GitHub recommends a load balancer providing a single IP range — and add it to the allow list
- C. Disable the allow list during business hours
- D. Ephemeral runners bypass IP allow lists automatically

**Type:** *single*

---

## Q541

How do you make a self-hosted runner route its traffic through an outbound HTTP proxy?

- A. Pass a `--proxy` flag in the workflow's `runs-on`
- B. Set a `proxy:` key in the workflow YAML
- C. Proxies are not supported by the runner application
- D. Set the `https_proxy`/`http_proxy` (and optionally `no_proxy`) environment variables for the runner, or put them in a `.env` file in the runner directory

**Type:** *single*

---

## Q542

At which levels can self-hosted runner groups be created?

- A. Enterprise only
- B. Repository only
- C. Organization and enterprise
- D. Repository, organization, and enterprise

**Type:** *single*

---

## Q543

By default, can a public repository use an organization's runner group?

- A. Groups have no repository-level access control
- B. Yes, every repository in the org can use every group
- C. Only if the runners carry a `public` label
- D. No — new runner groups exclude public repositories by default; access must be explicitly enabled

**Type:** *single*

---

## Q544

What is the difference between runner groups and runner labels?

- A. Groups route jobs; labels control repository access
- B. Labels exist only on GitHub-hosted runners
- C. They are two names for the same mechanism
- D. Groups control which repositories/organizations may use the runners; labels route jobs to matching runners via `runs-on`

**Type:** *single*

---

## Q545

Where does a self-hosted runner write its diagnostic log files?

- A. `/var/log/github/` on the runner host
- B. The Actions tab of the repository
- C. The `_diag` directory inside the runner application's install directory
- D. The system journal only

**Type:** *single*

---

## Q546

How do you check a self-hosted runner's connectivity to GitHub services without running a job?

- A. Pinging `github.com` is the documented method
- B. `config.sh --check --url <repo-url> --pat <token>` (or `config.cmd` on Windows)
- C. `gh runner ping`
- D. `run.sh --diagnose`

**Type:** *single*

---

## Q547

How do you enable verbose debug output for workflow runs?

- A. Pass `--verbose` to `actions/checkout`
- B. Set the secret or variable `ACTIONS_STEP_DEBUG=true` (step debug) and `ACTIONS_RUNNER_DEBUG=true` (runner diagnostics)
- C. Add `runs-on: debug` to the job
- D. Only GitHub support can enable debug logs

**Type:** *single*

---

## Q548

A workflow that uses a Docker container action fails immediately when moved to `windows-latest`. Why?

- A. Docker actions require larger runners
- B. Docker actions require a personal access token
- C. `windows-latest` has no shell installed
- D. Docker container actions run only on Linux runners

**Type:** *single*

---

## Q549

Your JavaScript action works locally but fails in workflows with `Cannot find module 'axios'`. What is the most likely cause?

- A. The runner blocks npm traffic
- B. Third-party modules are not allowed in actions
- C. The action declared the wrong shell
- D. Actions don't get a dependency install at runtime — the action must ship its dependencies, e.g. bundled into one file with `ncc` (committing `node_modules` also works but is discouraged)

**Type:** *single*

---

## Q550

A composite action ships a helper script in its own repository. How should a step in the action reference it?

- A. `./script.sh` relative to the consumer's workspace
- B. `$GITHUB_WORKSPACE/script.sh`
- C. `${{ github.action_path }}/script.sh`
- D. `/usr/local/actions/script.sh`

**Type:** *single*

---

## Q551

How does a JavaScript action signal failure to the runner?

- A. Write the string `failure` to `$GITHUB_OUTPUT`
- B. Return `false` from the entry function
- C. Call `core.setFailed('message')` — it logs an error and sets a failing exit code
- D. Failures can only be signaled from Docker actions

**Type:** *single*

---

## Q552

Your action's `core.debug()` messages never appear in the workflow log. Why?

- A. The action must run in a container for debug output
- B. `core.debug` is deprecated and does nothing
- C. Debug output is written only to the runner's `_diag` folder
- D. Debug messages are shown only when step debug logging is enabled (`ACTIONS_STEP_DEBUG=true`)

**Type:** *single*

---
