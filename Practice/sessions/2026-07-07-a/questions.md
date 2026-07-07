# GH-200 practice session 2026-07-07-a

Generated 2026-07-07 from `gh-200-gap-bank-2026-07-03.md` — 12 questions, options shuffled and re-lettered.
Answers withheld: grade each commitment with `log_answer.py` (see QUIZ-PROTOCOL.md).

---

## Q502

In addition to `contents: read`, which permissions does a job need to generate build provenance for a binary with `actions/attest-build-provenance`?

- A. `packages: write`
- B. `actions: write`
- C. `id-token: write`
- D. `attestations: write`

**Type:** *multi-select (2 correct)*

---

## Q505

Where can artifact attestations be generated?

- A. Private and internal repositories on GitHub Enterprise Cloud
- B. Any repository on GitHub Enterprise Server
- C. Public repositories only if the organization has GitHub Advanced Security
- D. Public repositories on any GitHub plan

**Type:** *multi-select (2 correct)*

---

## Q507

Which details are recorded in an artifact's build provenance?

- A. The list of CVEs present in the artifact
- B. The names of organization members with repository access
- C. The commit SHA the build ran against
- D. The workflow and repository that produced the artifact

**Type:** *multi-select (2 correct)*

---

## Q523

Job `b` reuses job `a`'s steps with `steps: *shared`, but needs one extra step at the end. What is true?

- A. An alias reproduces the anchored node exactly and cannot be extended — job `b` needs its own steps list
- B. Pass the extra step as a parameter to the alias
- C. Use `<<:` on the steps sequence to append the extra step
- D. Extra list items written under the alias are appended automatically

**Type:** *single*

---

## Q531

Which runners can host service containers?

- A. Larger runners only
- B. Linux runners with Docker installed (e.g. `ubuntu-latest`, or a Linux self-hosted runner with Docker)
- C. Self-hosted runners only
- D. All GitHub-hosted runners, including Windows and macOS

**Type:** *single*

---

## Q534

Where do you configure Docker health-check settings for a service container?

- A. In the service's `options:` key (`--health-cmd`, `--health-interval`, …)
- B. In `runs-on`
- C. In a dedicated `healthcheck:` block
- D. Health checks are not supported for services

**Type:** *single*

---

## Q535

A service maps `ports: ["6379/tcp"]`, letting Docker assign a random host port. How do steps discover the assigned port?

- A. The variable `$REDIS_PORT` is set automatically
- B. `${{ job.services.redis.ports[6379] }}`
- C. `${{ services.redis.port }}`
- D. Randomly assigned ports cannot be discovered

**Type:** *single*

---

## Q538

Where do you obtain the current IP ranges used by GitHub-hosted runners?

- A. A monthly email from GitHub
- B. The runner's `_diag` folder
- C. They are fixed and listed in the organization settings UI
- D. The REST API: `GET https://api.github.com/meta` (the `actions` key)

**Type:** *single*

---

## Q541

How do you make a self-hosted runner route its traffic through an outbound HTTP proxy?

- A. Pass a `--proxy` flag in the workflow's `runs-on`
- B. Proxies are not supported by the runner application
- C. Set the `https_proxy`/`http_proxy` (and optionally `no_proxy`) environment variables for the runner, or put them in a `.env` file in the runner directory
- D. Set a `proxy:` key in the workflow YAML

**Type:** *single*

---

## Q542

At which levels can self-hosted runner groups be created?

- A. Organization and enterprise
- B. Repository, organization, and enterprise
- C. Enterprise only
- D. Repository only

**Type:** *single*

---

## Q546

How do you check a self-hosted runner's connectivity to GitHub services without running a job?

- A. `gh runner ping`
- B. `run.sh --diagnose`
- C. `config.sh --check --url <repo-url> --pat <token>` (or `config.cmd` on Windows)
- D. Pinging `github.com` is the documented method

**Type:** *single*

---

## Q551

How does a JavaScript action signal failure to the runner?

- A. Return `false` from the entry function
- B. Write the string `failure` to `$GITHUB_OUTPUT`
- C. Failures can only be signaled from Docker actions
- D. Call `core.setFailed('message')` — it logs an error and sets a failing exit code

**Type:** *single*

---
