# GH-200 Coverage Map — Official Study Guide vs. Pluralsight Path

**Purpose:** Map every objective in the official GH-200 study guide (skills measured *as of January 2026*) against what the five Pluralsight courses actually teach, so we can target study effort. This is a living document — we'll add your self-rated confidence next.

**Legend**
- `✅ Covered` — taught directly, usually with a hands-on demo
- `🟡 Partial` — touched on, but not to likely exam depth, or one or more sub-parts are missing
- `❌ Gap` — not covered by the courses (verified against transcripts, not just lesson titles)

**Course key**
- `C1` GitHub Actions: The Big Picture
- `C2` Authoring and Maintaining GitHub Actions Workflows
- `C3` Consuming GitHub Actions Workflows
- `C4` Authoring and Maintaining GitHub Actions
- `C5` Managing GitHub Actions

**Honesty note on my ratings:** the `❌ Gap` calls were each verified by searching the transcripts. The `🟡 Partial` calls are inferred from lesson titles plus sampled transcript content, not a minute-by-minute reading of every course — so a `🟡` could occasionally be a `✅` if the topic got more demo time than the title suggests. Flag any that look off to you. The "Your confidence" column is blank for you to fill in (1 = no idea, 5 = could teach it).

---

## Domain 1 — Author and manage workflows (20–25%)

### Configure workflow triggers and events
| ID | Objective | Coverage | Where | Notes | Your confidence (1–5) |
|---|---|---|---|---|---|
| 1.1 | Scheduled, manual, webhook, and repository events | ✅ | C2 | schedule, `workflow_dispatch`, push, `issues` trigger all demoed | |
| 1.2 | Choose appropriate scope, permissions, and events | 🟡 | C2 | permissions/events shown; the *decision-making* ("which event/scope fits this need") is lighter | |
| 1.3 | `workflow_dispatch` inputs (types/required/defaults) + pass inputs to reusable workflows via `workflow_call` (inputs & secrets mapping) | 🟡 | C2, C3, C5 | dispatch trigger shown; **typed input validation** and explicit `workflow_call` inputs/secrets mapping are thin | |

### Design and implement workflow structure
| ID | Objective | Coverage | Where | Notes | Your confidence (1–5) |
|---|---|---|---|---|---|
| 1.4 | Jobs, steps, and conditional logic | ✅ | C2 | "Jobs Have Steps", "Conditional Jobs with If" | |
| 1.5 | Dependencies between jobs (`needs`) | ✅ | C2 | "Passing Outputs between Dependent Jobs" | |
| 1.6 | Workflow commands and environment variables | ✅ | C2, C3, C4 | grouping logs, `GITHUB_ENV`, default + custom env vars | |
| 1.7 | Service containers (`services:`), ports, health checks, options | ✅ | C2 | MySQL service container demo; health-check options shown lightly | |
| 1.8 | `strategy`/`matrix`: include/exclude, fail-fast, max-parallel, optimize size; runner image changes (Ubuntu 20.04 deprecation, Windows Server 2025 for `windows-latest`) | 🟡 | C2 | matrix **basics** covered; include/exclude, fail-fast, max-parallel and the **2025 runner-image facts** are thin/absent | |
| 1.9 | YAML anchors & aliases (`&`, `*`, merge `<<`) within one file | ❌ | — | **Verified not covered.** New Jan-2026 objective | |
| 1.10 | Predefined contexts (github, runner, env, **vars**, secrets, inputs, matrix, needs, strategy, job, steps, github.event, github.ref) + immutable actions behavior + version pinning | 🟡 | C2, C3 | many contexts used in passing; **no systematic treatment**; `vars` context + immutable actions absent | |
| 1.11 | Expressions `${{ }}`; static (parse) vs runtime evaluation; prevent secret leakage in logs | 🟡 | C2 | expressions used throughout; **static-vs-runtime distinction** and leakage prevention thin | |
| 1.12 | Editor tooling (Actions VS Code extension, YAML schema completion, IntelliSense, validation) | 🟡 | C2 | C2 monitors runs in VS Code; **authoring-assist features** barely shown | |

### Manage workflow execution and outputs
| ID | Objective | Coverage | Where | Notes | Your confidence (1–5) |
|---|---|---|---|---|---|
| 1.13 | Pass data between jobs/steps (artifacts, outputs, `GITHUB_ENV`, `GITHUB_OUTPUT`, reusable-workflow outputs) | ✅ | C2, C3 | strong; confirm `GITHUB_OUTPUT` (not the deprecated `set-output`) | |
| 1.14 | Job summaries via `GITHUB_STEP_SUMMARY` (Markdown reports) | ❌ | — | **Verified not covered.** New Jan-2026 objective | |
| 1.15 | Workflow status badges + environment protections | ✅ | C2, C5 | badges; environment approval; environment deployments | |
| 1.16 | Caching & artifact management; retention policies via **REST API** (logs/artifacts/runs) at org/repo | 🟡 | C2 | caching + artifacts ✅; **programmatic retention via REST API** absent | |

---

## Domain 2 — Consume and troubleshoot workflows (15–20%)

### Interpret workflow behavior and results
| ID | Objective | Coverage | Where | Notes | Your confidence (1–5) |
|---|---|---|---|---|---|
| 2.1 | Identify triggers and effects from config and logs | ✅ | C3 | "Describe a Workflow's Effects…", "Identify the Event…" | |
| 2.2 | Diagnose failed runs using logs and run history | ✅ | C3, C2 | logs + step debug logging | |
| 2.3 | Expand/interpret YAML anchors, aliases, merged mappings when analyzing | ❌ | — | **Verified not covered** (same YAML gap as 1.9) | |
| 2.4 | Interpret matrix expansions, correlate job names to axes, analyze variant failures, **selectively rerun individual matrix jobs** | 🟡 | C2 | matrix basics ✅; rerunning a single failed matrix job / axis correlation thin | |
| 2.5 | Locate workflows, logs, artifacts in UI **and via API** | ✅ | C3 | UI + REST API (download logs via curl/PAT) demoed | |
| 2.6 | Download and manage workflow artifacts | ✅ | C2, C3 | upload/download/delete | |

### Use and manage workflow templates
| ID | Objective | Coverage | Where | Notes | Your confidence (1–5) |
|---|---|---|---|---|---|
| 2.7 | Consume org-level and reusable workflows | ✅ | C3, C5 | reusable workflow in shared repo | |
| 2.8 | Consume non-public org workflow templates | ✅ | C3 | "Organization Templated Workflows" | |
| 2.9 | Starter workflows (public + private/non-public), customize/adapt, distinguish from reusable & composite | ✅ | C3 | "Create a Starter Workflow" | |
| 2.10 | Differentiate starter vs reusable vs composite | ✅ | C3, C4, C5 | spread across courses — worth consolidating in your head | |
| 2.11 | Contrast disabling vs deleting workflows | ✅ | C3 | "Disabling vs. Deleting Workflows" | |

---

## Domain 3 — Author and maintain actions (15–20%)

### Create and troubleshoot custom actions
| ID | Objective | Coverage | Where | Notes | Your confidence (1–5) |
|---|---|---|---|---|---|
| 3.1 | Define action structure and metadata | ✅ | C4 | directory structure + `action.yml` syntax | |
| 3.2 | Action types (JS/Docker/composite) + **immutable actions rollout** + version pinning/registry sources | 🟡 | C4 | the three types ✅ with demos; **immutable actions rollout** + registry-source implications absent | |
| 3.3 | Troubleshoot action execution and errors | ✅ | C4 | troubleshooting per action type | |
| 3.4 | Required files, directory structure, metadata | ✅ | C4 | | |
| 3.5 | Access workflow artifacts and logs | ✅ | C3, C4 | | |
| 3.6 | Implement workflow commands within actions | ✅ | C4 | "Implementing Workflow Commands" | |

### Distribute and maintain actions
| ID | Objective | Coverage | Where | Notes | Your confidence (1–5) |
|---|---|---|---|---|---|
| 3.7 | Distribution models (public/private/marketplace) | ✅ | C4 | | |
| 3.8 | Publish to GitHub Marketplace | ✅ | C4 | full publish demo (incl. removing a listing) | |
| 3.9 | Versioning and release strategies | ✅ | C4, C2 | tagging an action; releases; confirm major-version tag (`v1`) convention | |
| 3.10 | Define/manage reusable components and templates | ✅ | C5 | reusable workflows + composite actions | |

---

## Domain 4 — Manage GitHub Actions for the enterprise (20–25%)

### Distribute and govern actions and workflows
| ID | Objective | Coverage | Where | Notes | Your confidence (1–5) |
|---|---|---|---|---|---|
| 4.1 | Control access to actions/workflows within the enterprise | ✅ | C5 | teams + repository access; **enterprise-tier** (vs org) nuance is lighter | |
| 4.2 | Configure organizational use policies | ✅ | C5 | third-party action access / allow lists | |

### Manage runners at scale
| ID | Objective | Coverage | Where | Notes | Your confidence (1–5) |
|---|---|---|---|---|---|
| 4.3 | Configure and monitor GitHub-hosted and self-hosted runners | ✅ | C5, C2 | runner types, set up/build self-hosted; monitoring lighter | |
| 4.4 | Apply IP allow lists and networking settings | ❌ | — | **Verified not covered** | |
| 4.5 | Manage runner groups and troubleshoot runner issues | ✅ | C5 | runner groups ✅; troubleshooting lighter | |
| 4.6 | Preinstalled software/tool versions (image release notes, **toolcache**) + install at runtime (`setup-*`, package managers, caching, container images, **custom self-hosted images**) | 🟡 | C2 | preinstalled software + `setup-go` ✅; toolcache/release-notes/custom images thin | |

### Manage encrypted secrets and variables
| ID | Objective | Coverage | Where | Notes | Your confidence (1–5) |
|---|---|---|---|---|---|
| 4.7 | Define/scope encrypted secrets **and variables** at org/repo/environment | 🟡 | C5, C2 | **secrets** ✅ at all levels; **configuration variables (`vars`)** as a distinct feature is thin | |
| 4.8 | Access/use secrets and variables; manage **programmatically via REST APIs** | 🟡 | C2, C5 | usage in workflows ✅; variables + **REST API management** of secrets/vars absent | |

---

## Domain 5 — Secure and optimize automation (10–15%)

### Implement security best practices
| ID | Objective | Coverage | Where | Notes | Your confidence (1–5) |
|---|---|---|---|---|---|
| 5.1 | Environment protections and approval gates | ✅ | C2, C5 | production approval; environment deployments | |
| 5.2 | Identify/use trustworthy Marketplace actions | ✅ | C3 | "Indications of Trustworthy Actions" | |
| 5.3 | Mitigate **script injection** (sanitize/validate inputs, least-privilege, avoid untrusted data in `run:`, shell quoting, prefer vetted actions) | ❌ | — | **Verified not covered.** High-value security objective | |
| 5.4 | `GITHUB_TOKEN` lifecycle (ephemeral, scoped), granular permissions, contrast with PAT, restrict write scopes | 🟡 | C2, C3 | token permissions ✅; PAT shown for API (C3); **ephemeral lifecycle + explicit PAT-vs-token contrast** thin | |
| 5.5 | OIDC token (`id-token`) for cloud-provider federation (kill long-lived cloud secrets) | ❌ | — | **Verified not covered** — courses authenticate to Azure via secrets/PAT, not OIDC | |
| 5.6 | Pin third-party actions to full **commit SHAs**; immutable actions enforcement; avoid floating `@main`/`@v*` | 🟡 | C3 | using a *specific version* ✅ conceptually; **SHA pinning** + immutable enforcement thin | |
| 5.7 | Enforce action usage policies (allow/deny lists, **required reviewers for unverified actions**) | ✅ | C5 | allow lists ✅; required-reviewer flow lighter | |
| 5.8 | Generate/verify **artifact attestations / provenance** (SLSA, build metadata) + deployment verification | ❌ | — | **Verified not covered.** New Jan-2026 objective | |

### Optimize workflow performance and cost
| ID | Objective | Coverage | Where | Notes | Your confidence (1–5) |
|---|---|---|---|---|---|
| 5.9 | Caching & artifact retention for efficiency; retention via **REST APIs** | 🟡 | C2 | caching ✅; **programmatic retention** absent (overlaps 1.16) | |
| 5.10 | Recommend strategies for scaling/optimizing workflows | 🟡 | C2, C5 | ingredients exist (matrix, caching, runner choice) but **no consolidated optimization framework** | |

---

## Priority gap summary

**Hard gaps — not in the courses at all (verified):**
1. YAML anchors / aliases / merge keys — both authoring (1.9) and *reading/analyzing* them (2.3)
2. Job summaries via `GITHUB_STEP_SUMMARY` (1.14)
3. Script-injection mitigation (5.3)
4. OIDC federation to cloud providers (5.5)
5. Artifact attestations / provenance / SLSA (5.8)
6. IP allow lists & runner networking (4.4)

**Partial gaps clustering around newer / enterprise topics:**
- **Security hardening:** SHA pinning + immutable actions (5.6, 3.2, 1.10)
- **REST API management:** retention policies, secrets/variables programmatically (1.16, 4.8, 5.9)
- **Configuration variables (`vars`)** as distinct from secrets (4.7, 1.10)
- **Runner image currency:** Ubuntu 20.04 deprecation, Windows Server 2025, toolcache (1.8, 4.6)
- **Matrix depth:** include/exclude, fail-fast, max-parallel, rerunning single jobs (1.8, 2.4)
- **Authoring ergonomics:** VS Code Actions extension (1.12); static-vs-runtime expression evaluation (1.11)

**Strategic read:** the courses are strong on Domains 2 and 3 and the core of Domain 1. The gaps cluster in **Domain 5 (Secure & optimize)** and the **newer security/enterprise objectives** added in the January 2026 refresh — exactly what you'd expect when an older course path meets a freshly-reworded exam. Domain 5 is only 10–15% of the exam by weight, but it's the densest pocket of uncovered material, so it has an outsized study-cost-per-objective.

*All "current state" items (runner images, immutable actions, REST API specifics) should be confirmed against live GitHub docs before relying on them, since they may have changed since January 2026.*
