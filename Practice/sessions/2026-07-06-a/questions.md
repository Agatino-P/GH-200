# GH-200 practice session 2026-07-06-a

Generated 2026-07-06 from `gh-200-gap-bank-2026-07-03.md` — 52 questions, options shuffled and re-lettered.
Answers withheld: grade each commitment with `log_answer.py` (see QUIZ-PROTOCOL.md).

---

## Q501

What does an artifact attestation establish about a build artifact?

- A. Unfalsifiable provenance: which workflow, repository, and commit produced the artifact
- B. That the artifact contains no known vulnerabilities
- C. That a reviewer approved the artifact for deployment
- D. That all of the artifact's tests passed

**Type:** *single*

---

## Q502

In addition to `contents: read`, which permissions does a job need to generate build provenance for a binary with `actions/attest-build-provenance`?

- A. `packages: write`
- B. `actions: write`
- C. `id-token: write`
- D. `attestations: write`

**Type:** *multi-select (2 correct)*

---

## Q503

Which command verifies an artifact attestation from a terminal?

- A. `gh artifact verify <path>`
- B. `git verify-attestation <path>`
- C. `gh provenance verify <path>`
- D. `gh attestation verify <path> --owner <org>`

**Type:** *single*

---

## Q504

How does GitHub document reaching SLSA Build Level 3 with artifact attestations?

- A. Enable required reviewers on the production environment
- B. Perform the build and attestation inside a reusable workflow that acts as a trusted builder, isolated from the calling workflow
- C. Run the build on larger runners
- D. Sign the artifact with a personal GPG key after the build

**Type:** *single*

---

## Q505

Where can artifact attestations be generated?

- A. Public repositories on any GitHub plan
- B. Any repository on GitHub Enterprise Server
- C. Private and internal repositories on GitHub Enterprise Cloud
- D. Public repositories only if the organization has GitHub Advanced Security

**Type:** *multi-select (2 correct)*

---

## Q506

Why does `gh attestation verify` require an `--owner` or `--repo` flag?

- A. Verification must confirm the attestation was produced by the expected source — the signature alone doesn't prove who built the artifact
- B. It selects which account is billed for the verification API call
- C. The flag is needed to download the artifact from that repository first
- D. It is optional and only speeds verification up

**Type:** *single*

---

## Q507

Which details are recorded in an artifact's build provenance?

- A. The names of organization members with repository access
- B. The commit SHA the build ran against
- C. The workflow and repository that produced the artifact
- D. The list of CVEs present in the artifact

**Type:** *multi-select (2 correct)*

---

## Q508

How do you generate an attestation for a container image rather than a file?

- A. Enable two-factor authentication on the registry account
- B. Export the image as a tarball and attest the tarball instead
- C. Pass the image's digest to `attest-build-provenance` (`subject-digest`) and verify with an `oci://` reference
- D. Container images cannot be attested

**Type:** *single*

---

## Q509

What signs artifact attestations?

- A. The workflow author's SSH signing key
- B. GitHub staff, manually, on request
- C. The runner's TLS certificate
- D. Sigstore — the public-good instance for public repositories, GitHub's internal Sigstore instance for private ones

**Type:** *single*

---

## Q510

Why is this step a security risk in a workflow triggered by `issues`?

```yaml
- run: echo "Title: ${{ github.event.issue.title }}"
```

- A. `echo` automatically leaks secrets to the log
- B. The `issues` event cannot safely trigger workflows at all
- C. `github.event` is not available inside `run:` steps
- D. The title is attacker-controlled and is substituted into the script before the shell runs, enabling command injection

**Type:** *single*

---

## Q511

What is the recommended way to use `github.event.pull_request.title` inside a `run:` script?

- A. Only use it on self-hosted runners
- B. Assign it to an `env:` variable and reference the quoted variable (e.g. `"$TITLE"`) in the script
- C. Escape the expression with backslashes
- D. Wrap the expression in single quotes inside the script

**Type:** *single*

---

## Q512

Which of these values are attacker-controllable and must be treated as untrusted input?

- A. `github.event.pull_request.body`
- B. `github.workflow`
- C. `github.run_id`
- D. `github.event.issue.title`
- E. `github.head_ref`

**Type:** *multi-select (3 correct)*

---

## Q513

Why does routing untrusted input through an `env:` variable prevent script injection?

- A. The value reaches the process as data in memory instead of being pasted into the script text the shell parses
- B. `env:` values are encrypted at rest
- C. The shell refuses to expand variables that originate from event payloads
- D. `env:` values are sanitized by stripping shell metacharacters

**Type:** *single*

---

## Q514

Besides intermediate environment variables, which are documented mitigations against script injection?

- A. Use an action that consumes the untrusted value as an input, instead of an inline script
- B. Base64-encode the untrusted value inside the `run:` script
- C. Use code scanning (e.g. CodeQL) to detect vulnerable workflow patterns
- D. Move the step to a Windows runner where bash is not the default shell

**Type:** *multi-select (2 correct)*

---

## Q515

How does restricting `GITHUB_TOKEN` permissions relate to script injection?

- A. It is unrelated to injection risk
- B. It prevents the injection from executing in the first place
- C. The token is never accessible from `run:` steps anyway
- D. It limits the blast radius — a successful injection only gets the token's reduced scopes

**Type:** *single*

---

## Q516

Which combination is the classic "pwn request" vulnerability?

- A. A `schedule` workflow that reads repository code
- B. A `workflow_dispatch` workflow with typed inputs
- C. A `pull_request` workflow that builds the merge commit
- D. A `pull_request_target` workflow that checks out and executes the pull request's head code

**Type:** *single*

---

## Q517

Why doesn't wrapping `${{ github.event.comment.body }}` in single quotes inside `run:` protect against injection?

- A. It does protect fully — this is the documented mitigation
- B. Actions expands the expression before the shell parses the script, so the payload can include a quote and break out
- C. Single quotes are not valid in bash scripts
- D. Comment bodies cannot contain quote characters

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

- A. Defines an anchor, so the steps list can be reused elsewhere in this file via `*shared`
- B. Creates an alias to a node defined elsewhere
- C. Marks the steps list as deprecated
- D. Declares an environment variable named shared

**Type:** *single*

---

## Q519

Continuing the previous file, what does `steps: *shared` in job `b` do?

- A. Runs job `a` before job `b`
- B. Reuses the exact steps list anchored as `shared` in job `a`
- C. It is a YAML syntax error
- D. Imports steps from a file named shared.yml

**Type:** *single*

---

## Q520

Which YAML reuse constructs do GitHub Actions workflow files support?

- A. Anchors, aliases, and merge keys
- B. Anchors (`&`) and aliases (`*`) only — merge keys (`<<`) are a YAML 1.1 feature and Actions follows YAML 1.2
- C. Merge keys only
- D. None — all YAML reuse constructs are rejected by workflow validation

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
- B. The workflow is invalid — GitHub Actions does not support YAML merge keys (`<<:`), only anchors and aliases
- C. It runs with `LOG_LEVEL: debug` in job `test` — the local key overrides the merged one
- D. It fails to parse with a duplicate-key error

**Type:** *single*

---

## Q522

Can `*shared` in one workflow file reference an anchor `&shared` defined in a different workflow file?

- A. Only between a workflow and its reusable workflow
- B. Yes, if both files are in `.github/workflows`
- C. Yes, via the `uses:` keyword
- D. No — anchors and aliases are scoped to a single YAML file

**Type:** *single*

---

## Q523

Job `b` reuses job `a`'s steps with `steps: *shared`, but needs one extra step at the end. What is true?

- A. Pass the extra step as a parameter to the alias
- B. An alias reproduces the anchored node exactly and cannot be extended — job `b` needs its own steps list
- C. Use `<<:` on the steps sequence to append the extra step
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
- B. Append Markdown to the file at `$GITHUB_STEP_SUMMARY` (e.g. `echo "## Results" >> "$GITHUB_STEP_SUMMARY"`)
- C. Print `::summary::## Results` to stdout
- D. Call the run-summaries REST API from the step

**Type:** *single*

---

## Q526

What is `GITHUB_STEP_SUMMARY`?

- A. An environment variable holding the path to a temporary file, unique per step, whose content becomes part of the job summary
- B. An automatically created secret
- C. A context property containing the text of previous steps' summaries
- D. A boolean flag that turns summaries on

**Type:** *single*

---

## Q527

Two steps in the same job each append a heading to their `$GITHUB_STEP_SUMMARY`. What appears on the run summary page?

- A. Only the first step's content
- B. Nothing: only one step per job may write a summary
- C. Only the last step's content
- D. Both headings — each step's summary content is grouped into the job's summary

**Type:** *single*

---

## Q528

What format is job summary content written in?

- A. Plain text only
- B. HTML only
- C. GitHub-flavored Markdown
- D. AsciiDoc

**Type:** *single*

---

## Q529

You want a Markdown test report visible directly on the run page, without downloading artifacts. Which file does the step write to?

- A. `$GITHUB_OUTPUT`
- B. `$GITHUB_PATH`
- C. `$GITHUB_ENV`
- D. `$GITHUB_STEP_SUMMARY`

**Type:** *single*

---

## Q530

What are service containers?

- A. Long-running containers shared across workflow runs
- B. Docker containers that Actions starts for a job (e.g. a database), manages, and destroys when the job ends
- C. Kubernetes pods managed by GitHub
- D. The containers all jobs always execute in

**Type:** *single*

---

## Q531

Which runners can host service containers?

- A. Larger runners only
- B. All GitHub-hosted runners, including Windows and macOS
- C. Linux runners with Docker installed (e.g. `ubuntu-latest`, or a Linux self-hosted runner with Docker)
- D. Self-hosted runners only

**Type:** *single*

---

## Q532

The job itself runs in a container. How do its steps reach a service container labeled `redis`?

- A. Only through the `job.services.redis.url` context property
- B. Via the service's public IP address
- C. Always via `localhost:6379`
- D. By hostname `redis` — the service label is the hostname on the shared Docker network

**Type:** *single*

---

## Q533

The job runs directly on the runner machine (no `container:`). How do steps reach the `redis` service container?

- A. Via a Docker network alias
- B. They can't — a job container is mandatory for services
- C. By hostname `redis`
- D. Via `localhost` and a host port mapped with `ports:` (e.g. `6379:6379`)

**Type:** *single*

---

## Q534

Where do you configure Docker health-check settings for a service container?

- A. In a dedicated `healthcheck:` block
- B. Health checks are not supported for services
- C. In `runs-on`
- D. In the service's `options:` key (`--health-cmd`, `--health-interval`, …)

**Type:** *single*

---

## Q535

A service maps `ports: ["6379/tcp"]`, letting Docker assign a random host port. How do steps discover the assigned port?

- A. Randomly assigned ports cannot be discovered
- B. The variable `$REDIS_PORT` is set automatically
- C. `${{ job.services.redis.ports[6379] }}`
- D. `${{ services.redis.port }}`

**Type:** *single*

---

## Q536

Your organization enables an IP allow list. What does GitHub document about standard GitHub-hosted runners?

- A. IP allow lists do not affect Actions at all
- B. They automatically bypass the allow list
- C. Add the keyword `azure` to the allow list to cover them
- D. They can't be used with the allow list — the ranges are too numerous and updated weekly; use self-hosted runners or larger runners with static IPs

**Type:** *single*

---

## Q537

Which feature provides GitHub-managed runners with fixed IP ranges that can be allow-listed?

- A. Runner groups
- B. The `meta` REST API
- C. Standard `ubuntu-latest` runners
- D. Larger runners with static IP addresses

**Type:** *single*

---

## Q538

Where do you obtain the current IP ranges used by GitHub-hosted runners?

- A. They are fixed and listed in the organization settings UI
- B. A monthly email from GitHub
- C. The runner's `_diag` folder
- D. The REST API: `GET https://api.github.com/meta` (the `actions` key)

**Type:** *single*

---

## Q539

Which network access does a self-hosted runner require to receive jobs?

- A. Outbound SMTP for job notifications
- B. Inbound and outbound SSH (22)
- C. Outbound HTTPS (443) to GitHub only — it polls for jobs; no inbound ports are needed
- D. An inbound HTTPS port reachable from GitHub's webhook IPs

**Type:** *single*

---

## Q540

Autoscaled ephemeral self-hosted runners get changing IPs, but the organization uses an IP allow list. What is the documented approach?

- A. Disable the allow list during business hours
- B. Give the runners a stable egress IP range — GitHub recommends a load balancer providing a single IP range — and add it to the allow list
- C. Add `0.0.0.0/0` to the allow list
- D. Ephemeral runners bypass IP allow lists automatically

**Type:** *single*

---

## Q541

How do you make a self-hosted runner route its traffic through an outbound HTTP proxy?

- A. Proxies are not supported by the runner application
- B. Pass a `--proxy` flag in the workflow's `runs-on`
- C. Set the `https_proxy`/`http_proxy` (and optionally `no_proxy`) environment variables for the runner, or put them in a `.env` file in the runner directory
- D. Set a `proxy:` key in the workflow YAML

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

- A. No — new runner groups exclude public repositories by default; access must be explicitly enabled
- B. Yes, every repository in the org can use every group
- C. Groups have no repository-level access control
- D. Only if the runners carry a `public` label

**Type:** *single*

---

## Q544

What is the difference between runner groups and runner labels?

- A. Labels exist only on GitHub-hosted runners
- B. Groups route jobs; labels control repository access
- C. Groups control which repositories/organizations may use the runners; labels route jobs to matching runners via `runs-on`
- D. They are two names for the same mechanism

**Type:** *single*

---

## Q545

Where does a self-hosted runner write its diagnostic log files?

- A. `/var/log/github/` on the runner host
- B. The Actions tab of the repository
- C. The system journal only
- D. The `_diag` directory inside the runner application's install directory

**Type:** *single*

---

## Q546

How do you check a self-hosted runner's connectivity to GitHub services without running a job?

- A. `config.sh --check --url <repo-url> --pat <token>` (or `config.cmd` on Windows)
- B. Pinging `github.com` is the documented method
- C. `run.sh --diagnose`
- D. `gh runner ping`

**Type:** *single*

---

## Q547

How do you enable verbose debug output for workflow runs?

- A. Only GitHub support can enable debug logs
- B. Add `runs-on: debug` to the job
- C. Pass `--verbose` to `actions/checkout`
- D. Set the secret or variable `ACTIONS_STEP_DEBUG=true` (step debug) and `ACTIONS_RUNNER_DEBUG=true` (runner diagnostics)

**Type:** *single*

---

## Q548

A workflow that uses a Docker container action fails immediately when moved to `windows-latest`. Why?

- A. Docker container actions run only on Linux runners
- B. Docker actions require a personal access token
- C. `windows-latest` has no shell installed
- D. Docker actions require larger runners

**Type:** *single*

---

## Q549

Your JavaScript action works locally but fails in workflows with `Cannot find module 'axios'`. What is the most likely cause?

- A. The runner blocks npm traffic
- B. The action declared the wrong shell
- C. Third-party modules are not allowed in actions
- D. Actions don't get a dependency install at runtime — the action must ship its dependencies, e.g. bundled into one file with `ncc` (committing `node_modules` also works but is discouraged)

**Type:** *single*

---

## Q550

A composite action ships a helper script in its own repository. How should a step in the action reference it?

- A. `$GITHUB_WORKSPACE/script.sh`
- B. `${{ github.action_path }}/script.sh`
- C. `/usr/local/actions/script.sh`
- D. `./script.sh` relative to the consumer's workspace

**Type:** *single*

---

## Q551

How does a JavaScript action signal failure to the runner?

- A. Failures can only be signaled from Docker actions
- B. Return `false` from the entry function
- C. Call `core.setFailed('message')` — it logs an error and sets a failing exit code
- D. Write the string `failure` to `$GITHUB_OUTPUT`

**Type:** *single*

---

## Q552

Your action's `core.debug()` messages never appear in the workflow log. Why?

- A. The action must run in a container for debug output
- B. Debug output is written only to the runner's `_diag` folder
- C. `core.debug` is deprecated and does nothing
- D. Debug messages are shown only when step debug logging is enabled (`ACTIONS_STEP_DEBUG=true`)

**Type:** *single*

---
