# GH-200 — Combined Cheat Sheets (All 14 Topics)

*Assembled 2026-06-24 20:18 UTC from repo `Agatino-P/gh-200` @ `0f2dd86`, folder `Study material/`. Each section is the per-topic cheat reproduced verbatim, with its headings nested one level under the section title; content is not edited. The matching full recap for any topic is `GH-200_Topic_<code>_...` in the same folder.*

## Contents


**Domain 1 — Author & maintain workflows**
- [Topic 1A — Triggers, Permissions, Inputs, Reusable Workflows](#topic-1a--triggers-permissions-inputs-reusable-workflows)
- [Topic 1B — Contexts, Expressions & Secret Leakage](#topic-1b--contexts-expressions--secret-leakage)
- [Topic 1C — Matrix Strategy In Depth](#topic-1c--matrix-strategy-in-depth)
- [Topic 1D — YAML Anchors, Aliases & Merge Keys](#topic-1d--yaml-anchors-aliases--merge-keys)
- [Topic 1E — Outputs, Summaries & Retention](#topic-1e--outputs-summaries--retention)

**Domain 2 — Troubleshoot**
- [Topic 2A — Troubleshooting Matrix Runs](#topic-2a--troubleshooting-matrix-runs)

**Domain 3 — Consume workflows & actions**
- [Topic 3A — Immutable Releases & Version Pinning](#topic-3a--immutable-releases--version-pinning)

**Domain 4 — Author & maintain actions / runners**
- [Topic 4A — Runner Networking & Access Boundaries](#topic-4a--runner-networking--access-boundaries)
- [Topic 4B — Runner Images & Toolcache](#topic-4b--runner-images--toolcache)
- [Topic 4C — Variables & Secrets REST API](#topic-4c--variables--secrets-rest-api)

**Domain 5 — Secure & optimize**
- [Topic 5A — Untrusted Input & Token Hardening](#topic-5a--untrusted-input--token-hardening)
- [Topic 5B — OIDC Keyless Cloud Auth](#topic-5b--oidc-keyless-cloud-auth)
- [Topic 5C — Action Enforcement Policies & Build Provenance](#topic-5c--action-enforcement-policies--build-provenance)
- [Topic 5D — Optimization & Retention](#topic-5d--optimization--retention)


---

## Topic 1A — Triggers, Permissions, Inputs, Reusable Workflows

*Source: `GH-200_Cheat_1A_-_Triggers_Permissions_Inputs_Reusable_Workflows.md`*

*Trap-grade keepers only. Full explanation in the matching recap: `GH-200_Topic_1A_-_Triggers_Permissions_Inputs_Reusable_Workflows.md`.*

#### Triggers
- `workflow_dispatch` = **internal** (UI / `gh` CLI / API; typed inputs). `repository_dispatch` = **external** POST to dispatches endpoint with custom `event_type`.
- `schedule`: **min 5 min**, **default branch only**, best-effort (delayed under load; avoid top-of-hour).
- Narrow events with: `types:`, `branches:`/`branches-ignore:`, `paths:`/`paths-ignore:`, `tags:`. `tags:` is for `push`, not `pull_request`.

#### permissions / GITHUB_TOKEN
- Token is **per-job + ephemeral** (expires when the job ends).
- **Job-level `permissions:` REPLACES workflow-level (not merge).** Any **unlisted scope → `none`**.
- `{}` = no access; `read-all` / `write-all` = shortcuts.
- **Default read-only** for new repos/orgs/enterprises (`contents`+`packages` read). **Repo ← org ← enterprise** inheritance.
- **Fork PR token = read-only** unless admin enabled "Send write tokens to workflows from pull requests."
- `403: Resource not accessible by integration` = missing scope → add it to `permissions:`.

#### Input types  ⚠️ MEMORIZE THE TWO SETS
- `workflow_dispatch`: **string, boolean, choice, number, environment** (5). `type` **OPTIONAL** (defaults `string`).
- `workflow_call`: **string, number, boolean** (3). `type` **REQUIRED**. **No `choice`, no `environment`.**
- `choice` **requires `options:`**.
- `description`: **required** in `action.yml` inputs; **NOT** required in `workflow_dispatch` inputs.
- `github.event.inputs.*` = **always strings** (`"false"` is truthy!). `inputs.*` = **typed**.
- `type: environment` = **picker only**; protection + env-secrets apply **only when a job sets `environment:`**.
- dispatch limits: **10 inputs max**, **65,535-char** payload.
- `workflow_call` unset defaults: **`false` / `0` / `""`**.

#### Reusable workflows (`workflow_call`)
- Called at **JOB level**: `jobs.<id>.uses: owner/repo/.github/workflows/x.yml@REF` (**ref required**).
- `secrets: inherit` = **all** caller secrets (**org + repo**), **same org/enterprise only**.
- **Can't** reference `secrets.*` in caller `with:` (**parse-time error**). `with:` = inputs channel; `secrets:` = secrets channel.
- Environment secrets **not passable** via `workflow_call`; set `environment:` on the reusable job instead.
- Nesting allowed; **permissions only reduce down the chain, never elevate.**


---

## Topic 1B — Contexts, Expressions & Secret Leakage

*Source: `GH-200_Cheat_1B_-_Contexts_Expressions_Secret_Leakage.md`*

*Trap-grade keepers only. Full explanation in the matching recap: `GH-200_Topic_1B_-_Contexts_Expressions_Secret_Leakage.md`.*

#### Context — what the term means HERE
- A **context** = a **read-only bag of runtime data**, read via `${{ }}`. NOT the vague English "situation." A named object you index into; only holds data that exists at that moment.
  - `github` → event/actor/ref/sha/repo · `needs` → upstream job outputs · `matrix` → this job's axis values · `steps` → id'd step outputs in **same** job.

#### env vs vars vs secrets  ⚠️ THE contrast
- `env` = inline in YAML; **auto-exposed as shell `$NAME`**; not masked.
- `vars` = UI/API config; **read only via `${{ vars.X }}`**; **NOT masked**; **must map to env: for the shell.**
- `secrets` = UI/API sensitive; **read only via `${{ secrets.X }}`**; **auto-masked**; must map to env: for the shell.
- **secrets masked / vars NOT masked** ← the whole exam point. Sensitive value in `vars` = leak.
- Precedence (both): **environment > repository > organization.**
- `env:` blocks **don't self-reference** (one entry can't use another from the same block).

#### Matrix (primer; depth = 1C)
- `strategy.matrix` is **per JOB**; runs the job once per **cross-product** combo, **parallel** by default.
- Throttle with **`max-parallel`** (1 = sequential). It caps a **count**, not an "axis." Combo order = don't rely on it.
- `needs: <matrix-job>` waits for **ALL** combos — matrix job = **one graph node**.
- **Matrix outputs:** all combos write the **same** output names → overwrite (**last wins, unreliable**). Fix: unique names via `matrix` context, e.g. `result_${{ matrix.x }}`.

#### Expression evaluation — two phases
- **Setup phase** (before runners): job graph, **matrix expansion**, names, concurrency, `needs`.
- **Execution phase** (on runner): `if:`, `run:`, `with:`, env interpolation, step/job outputs.
- **Context availability by location:** top-of-file = ~nothing · job-level `if:`/`strategy` = `github`/`needs`/`vars` (**NO `steps`, NO `runner`**) · step-level = **everything**.
- ❌ `jobs.x.if: ${{ steps.y.outputs.z }}` fails — `steps` not available at job level.
- Matrix is **fixed at setup** → dynamic matrix = **`fromJSON(needs.<prior>.outputs.list)`**, never from a same-job step. (`fromJSON` = real built-in; full treatment 1C.)

#### Secret leakage — masking is best-effort
- Masking catches the **raw secret + common encodings (notably Base64)** — so `base64(secret)` IS masked. But **NOT guaranteed**:
  - `echo "${{ secrets.T }}"` → `***`  ·  `echo "${{ secrets.T }}" | base64` → `***` (Base64 handled)  ·  `... | rev` → **CLEAR TEXT** (uncommon transform).
  - Leaks via: **structured/JSON secrets**, splitting/substringing, odd transforms, and `base64(secret+suffix)` padding edge case.
- Derived sensitive values → register with **`::add-mask::$VALUE`** (real workflow command). Never store structured data (JSON/XML) as a secret.
- **Outputs are NOT a secret channel** — they flow to GitHub + downstream as ordinary data. (A real registered secret in an output *is* redacted on the runner; a self-minted value is not.)
- **Script injection** (also 5.3): never interpolate untrusted `${{ }}` (PR title / branch / issue body / commit msg) straight into `run:`. **Bind to `env:`, then use `"$VAR"` quoted.**

#### Passing secrets — where & how
- Already a registered secret? → read **`${{ secrets.X }}`** in the later job. Available run-wide; **no passing.**
- Calling a reusable workflow? → hand it over via the **`secrets:`** block (or **`secrets: inherit`**). Separate trust boundary; secrets don't cross automatically.
- A value you generated & must reuse downstream? → **`::add-mask::`** it, OR better: **don't pass the credential** — write the artifact/result it protects, not the secret.


---

## Topic 1C — Matrix Strategy In Depth

*Source: `GH-200_Cheat_1C_-_Matrix_Strategy_In_Depth.md`*

*Trap-grade keepers only. Full explanation in the matching recap: `GH-200_Topic_1C_-_Matrix_Strategy_In_Depth.md`.*

#### Where keys live ⚠️ (don't confuse levels)
- `matrix` / `fail-fast` / `max-parallel` → **only under `strategy:`**.
- `continue-on-error` → on a **JOB** or a **STEP** (NOT under `strategy:`).
- `runs-on` / `needs` → **JOB** level.

#### Resolution order
- **EXPAND → EXCLUDE → INCLUDE.** `include` runs **last** and can **re-add** an excluded combo. (A common blog states this backwards — it's wrong.)
- `exclude`/`include` entries **don't accept arrays** — one scalar set per list item.

#### include behavior
- Entry's matrix keys **match** an existing combo → **AUGMENT** (add extra keys).
- Keys **don't match** any combo → **NEW combo**.
- **Original axis values never overwritten**; include-added keys **can** be overwritten by a later include.
- **include-only** (no base axes) = explicit hand-picked combo list.

#### fail-fast / max-parallel / continue-on-error
- **`fail-fast` default = `true`** → first failing combo **cancels** all in-progress + queued. Set `false` for full reports.
- `max-parallel` = cap on **simultaneous** combos (default = max allowed). A **count**, not an axis.
- **Swallow vs preserve** (THE distinction):
  - `continue-on-error: true` → **SWALLOWS** failure: run not failed, **downstream `needs:` sees SUCCESS**.
  - `fail-fast: false` → **PRESERVES** failure (still counts, blocks `needs:`), just doesn't cancel siblings.
- `fail-fast: true` + **flat** `continue-on-error: true` = **pointless** (fail-fast inert). Meaningful only as `continue-on-error: ${{ matrix.experimental }}` (per-combo carve-out).

#### Dynamic matrix via fromJSON
- Matrix is fixed at **setup** → can't build from a **same-job** step output. Use a **PRIOR job** + `needs:` + `fromJSON`.
- Producer: set a **single-line JSON string** job output (`jq -c`). Consumer: `matrix: ${{ fromJSON(needs.<job>.outputs.<key>) }}`.
- **object** → whole matrix (keys become axes) · **array** → one axis OR the `include` list.
- `needs:` mandatory · malformed JSON → matrix won't expand · **empty array → ZERO jobs** (skipped, not failed).

#### Runner images & -latest (verified June 2026; mappings DRIFT)
- `-latest` labels **float** — GitHub migrates them to newer OS gradually (~1–2 months) → **non-deterministic over time**. **Pin** a version label for reproducibility.
- Current: `ubuntu-latest`=**Ubuntu 24.04** · `windows-latest`=**Windows Server 2025** (=`windows-2025`) · `macos-latest`=**macOS 15 Arm64** (gotcha: Apple silicon).
- **Ubuntu 20.04 retired** (unsupported since **2025-04-01**) → `runs-on: ubuntu-20.04` **fails**.
- ⚠️ **Pinning stops silent migration, NOT deprecation** — a pinned old label still dies when the image is retired.
- (Newer, likely post-exam: `ubuntu-26.04` = public preview; `windows-latest` moving to "Server 2025 + VS 2026" toolset, June 2026.)


---

## Topic 1D — YAML Anchors, Aliases & Merge Keys

*Source: `GH-200_Cheat_1D_-_YAML_Anchors_Aliases_Merge_Keys.md`*

*Trap-grade keepers only. Full explanation in the matching recap: `GH-200_Topic_1D_-_YAML_Anchors_Aliases_Merge_Keys.md`.*

#### Support matrix ⚠️ THE whole topic
- `&` anchor + `*` alias → **SUPPORTED** (shipped **2025-09-18**, auto-enabled all repos). Before that: errored.
- `<<` **merge key → NOT SUPPORTED.** GitHub shipped "half the feature." Official docs document only `&`/`*`.
- ❌ Don't generalize: "anchors supported" ≠ "merge keys supported." They are **not** the same feature.

#### Anchors / aliases mechanics
- Alias copies the **WHOLE node** — **all-or-nothing**, NO partial override.
- **Define before use** — anchor must appear **above** any alias to it (top-to-bottom). Alias-before-anchor = error.
- **Same file only** — NOT a cross-file/cross-repo reuse tool (that's composite actions / reusable workflows).
- Can anchor any node: scalar, sequence (e.g. shared `paths:` across triggers), mapping, or a whole job.

#### Merge keys — the trap
- `<<: *base` in a workflow = **broken/invalid**, not inherit-and-override. (Exact failure mode — hard error vs literal `<<` key — unverified; either way the merge does NOT happen.)
- Want **base + override one key**? → **composite action or reusable workflow.** Anchors = exact duplication only.
- `<<: *base` is a classic **"spot the mistake"** distractor (objective 2.3 reading/analysis).
- Trivia: merge keys are YAML **1.1** optional type, never in core 1.2 → inconsistent parser support generally.

#### Exam weight ⚠️ uncertain
- Feature shipped Sept 2025, exam reworded Jan 2026 → weight/form **not verified**. Likely tested as *read-and-analyze* / *spot-invalid-`<<`* rather than authoring. Calibrate vs practice exams.


---

## Topic 1E — Outputs, Summaries & Retention

*Source: `GH-200_Cheat_1E_-_Outputs_Summaries_Retention.md`*

*Trap-grade keepers only. Full explanation in the matching recap: `GH-200_Topic_1E_-_Outputs_Summaries_Retention.md`.*

#### Job summaries — `GITHUB_STEP_SUMMARY`
- It's an **environment FILE** (variable = a file path). Append **GFM Markdown**; renders on the run summary page.
- `>>` appends (auto-newline each append); `>` overwrites **the current step's** buffer only.
- **1 MiB per step** limit → exceeding it **aborts** that step's summary (error "1024k"), not silent truncation.
- Renders GFM: tables, Mermaid, alerts (`> [!NOTE]`). `<details>` must stay within ONE step (isolation breaks cross-step tags).

#### Job summaries — step isolation ⚠️ (flagged keeper)
- `GITHUB_STEP_SUMMARY` is a **SEPARATE file PER STEP**. Steps are isolated.
- `>>` appends to the CURRENT step's file; `>` overwrites ONLY the current step's buffer.
- `>` can **NEVER** wipe another step's summary. At job end all step files are grouped into one job summary.
- Across jobs: summaries ordered by **job completion time**, not definition order.
- (Trap: assuming `>` in a later step clears the whole job summary — it doesn't.)

#### The four environment-file siblings (all use `>>`)
```
GITHUB_STEP_SUMMARY -> Markdown for HUMANS (run summary page)
GITHUB_OUTPUT       -> step OUTPUT for machines (steps.<id>.outputs.*)
GITHUB_ENV          -> env var for LATER STEPS ($NAME)
::warning:: / ::error:: -> annotations (inline highlights, not rich content)
```

#### Artifacts vs cache ⚠️
- **Artifact** = persist a run's OUTPUTS (share between jobs, download, inspect). Reliable & retained.
- **Cache** = SPEED (restore deps across runs by key). **Best-effort, can be EVICTED, NOT guaranteed.**
- Cross-job: FILE/binary → **artifact**; small STRING/metadata → **job output** (`needs.<job>.outputs.X`). Cache is NOT a transfer tool.
- Anti-patterns: cache to pass build output between jobs (unreliable); artifacts as a dep cache (slow/costly).

#### Retention numbers ⚠️ TWO DIFFERENT SETS (easy to confuse)
```
ARTIFACTS/LOGS: default 90d | public ≤90 | private/internal ≤400
CACHE:          default  7d | public ≤90 | private/internal ≤365
CACHE size cap: 10 GB/repo default, LRU eviction over limit
```
- Per-artifact override: `retention-days:` on `upload-artifact` (capped by repo/org/enterprise). Applies to NEW artifacts only.
- `upload-artifact@v4` / `download-artifact@v4` current; **v3 deprecated & stopped working**. (v4: artifact names must be unique within a run.)

#### Retention via REST API (verified)
```
GET    /repos/{o}/{r}/actions/artifacts                  # list repo artifacts
GET    /repos/{o}/{r}/actions/runs/{run_id}/artifacts    # list a run's artifacts
DELETE /repos/{o}/{r}/actions/artifacts/{artifact_id}    # delete one  <- retention workhorse
GET    /repos/{o}/{r}/actions/artifacts/{id}/{format}    # download (format=zip; URL expires in 1 MIN)
```
- "Enforce retention" programmatically = **list + DELETE** on a schedule.
- ⚠️ `PUT .../actions/retention` is **UNVERIFIED / likely not official** — do NOT trust it. Default-retention config is UI/org-policy.

#### VS Code GitHub Actions extension (`GitHub.vscode-github-actions`)
- Two halves: (1) **authoring** — schema validation + completion, incl. smart checks of job/step references and event-payload validation from `on:`; (2) **run management** — view/cancel/re-run/trigger runs, drill runs→jobs→steps, view logs.
- ⚠️ **No remote repos** — github.dev / vscode.dev unsupported; use a local clone. GHES support = experimental beta.
- NOT the same as "GitHub Local Actions" (third-party, runs workflows locally via `act`).


---

## Topic 2A — Troubleshooting Matrix Runs

*Source: `GH-200_Cheat_2A_-_Troubleshooting_Matrix_Runs.md`*

*Trap-grade keepers only. Full explanation in the matching recap: `GH-200_Topic_2A_-_Troubleshooting_Matrix_Runs.md`.*

#### Reading matrix job labels
- Auto-label = `<job_name> (val1, val2, ...)`, values in **matrix-key DECLARATION order**, comma-separated.
- e.g. `matrix: {arch:[x64,arm64], node:[18,20]}` → `arch=arm64,node=18` shows as `build (arm64, 18)`.
- Decode a label using the YAML's key order — NOT by finish order (**run order is not guaranteed**).
- Custom label: `jobs.<job_id>.name` (job attribute, sibling of `runs-on`/`strategy`/`steps`), can use `${{ matrix.* }}`.

#### fail-fast: cancelled ≠ failed ⚠️
- Default `fail-fast: true` → one failed leg **cancels** all other in-progress/queued legs.
- Cancelled legs are **collateral**, true result UNKNOWN — the culprit is the leg that actually FAILED.
- `fail-fast: false` + re-run = clean per-variant pass/fail map (is the failure one combo or broad?).

#### Rerun scopes & surfaces
- Three scopes: **Re-run all** | **Re-run failed** (failed + downstream dependents) | **Re-run single job** (each matrix leg = its own job).
- UI: "Re-run jobs" dropdown / per-job hover icon / logs view.
- CLI: `gh run rerun <id>` | `gh run rerun <id> --failed` | `gh run rerun --job <job_id>` (`--debug` for debug logging).
- REST: `POST .../runs/{run_id}/rerun` | `.../runs/{run_id}/rerun-failed-jobs` | `.../jobs/{job_id}/rerun`.
- Re-runs create a **new ATTEMPT** (old run preserved; attempt navigation; reuses original SHA).

#### KEEPER GOTCHA — single-job API rerun archives the attempt ⚠️
- `POST .../actions/jobs/{job_id}/rerun` creates a NEW attempt → remaining old failures are now in the ARCHIVED attempt.
- Trying to individually rerun a second old failure → **HTTP 403 "Only jobs from the current attempt can be re-run."**
- **No endpoint to rerun a SUBSET** of jobs in one call. Options: `rerun-failed-jobs` (ALL) or one-at-a-time.
- To retry several specific legs: use `rerun-failed-jobs`, or rerun them before a new attempt archives them.

#### Edge bug (not the rule)
- Matrixed **reusable** workflows: "Re-run failed jobs" may restart the failed leg but NOT its downstream dependents inside the reusable workflow. (Documented behavior = failed + dependents; this is a reported bug.)


---

## Topic 3A — Immutable Releases & Version Pinning

*Source: `GH-200_Cheat_3A_-_Immutable_Releases_and_Version_Pinning.md`*

*Terse last-week-review keepers for objective 3.2. Fuller note: `GH-200_Topic_3A_-_Immutable_Releases_and_Version_Pinning.md`. Enforcement specifics → see 5.6.*

---

### ⭐ HEADLINE TRAP — a Release is NOT automatically immutable
Two independent checks; a tag ref is locked only if **BOTH** pass:
1. **Is it a release at all?** Bare tag (no release) → movable.
2. **Is that release _immutable_?** Publishing a release does **NOT** lock it. Immutable **only if** the repo/org had immutable releases **enabled at publish time**. Setting off (or an older release) → **mutable release = still movable** (assets + tag changeable).

Three states of any tag: **bare tag → movable** · **mutable release → still movable** · **immutable release → locked**.

> **The exam trap:** "it's a Release on a clean `v3.4.0` tag, so it's locked." ❌ WRONG. A Release ≠ an immutable Release. The version string *and even the existence of a release* tell you nothing — only the **immutable** status does.
>
> **Don't get fooled by the semver tag alone** — `@v3.4.0` can be a bare tag, a mutable release, OR an immutable release. Lock comes from the **immutable status** (or a full SHA), never the version text.

#### How a consumer checks immutability
- **Release page:** **"Immutable" label** below the title (no label ⇒ not immutable).
- **REST:** `GET /repos/{o}/{r}/releases/tags/{TAG}` → release object's **`immutable` boolean** (404 ⇒ no release / bare tag).
- **CLI:** `gh release verify <tag>` (succeeds + loads attestation ⇒ immutable).
- *(GitHub's own user-facing "how to check" docs are still an open issue — under-documented.)*

#### ⭐ Better-safe-than-sorry rule
**A full commit SHA is immutable by construction** — no audit of the author's release/setting needed. When in doubt, **pin the SHA**.

---

### Immutable releases — the lock
- **= assets locked + Git tag locked** (+ tag name unreusable after deletion + auto signed attestation). ← don't drop the **tag** lock.
- It's a **repo/org setting** (UI or REST API) — **NOT** a workflow-YAML key. No `immutable: true` in YAML. (spot-the-mistake)
- **Disabling it later does NOT un-freeze** already-immutable releases.
- Publishing locks instantly → author flow: **draft → attach assets → publish**.
- Attestation = **Sigstore bundle**; verify with `gh release verify` / `gh release verify-asset`.
- Immutability attaches to the **release, not a bare tag** → author keeps a tag movable by **not creating a release** for it.

### Pinning spectrum (consumer)  — least → most safe
`@main` (branch, worst) → `@v4` (floating major) → `@v4.1.0` (plain version tag) → `@<full 40-char SHA>` (best)
- Tags = **movable pointers**; full SHA = **content-addressed, can't be re-pointed**.
- **Full 40-char SHA** only — short SHAs are ambiguous / not accepted.
- On an immutable-releases repo: best readable option = a version tag `@v4.1.0` **that is itself a published immutable release** ≈ a SHA.
- **`@v4` floating stays movable as long as no immutable release is published on it** (authors keep it release-free so it can advance). The name `v4` decides nothing.

### ⚠️ Flags (uncertain — calibrate vs practice exams)
- **OCI/`ghcr.io` publishing** of actions: status conflicting; first-party publish action README says **not for public use**. Treat as **not confirmed GA**.
- **Dependabot + SHA-pinning alerting** interference: **unverified**. (Updates of SHA-pinned actions = confirmed.)

### ⚠️ Do not confuse
- **Immutable *subject claims*** = an **OIDC token format** change (→ 5.5). **Different feature**, not immutable releases.


---

## Topic 4A — Runner Networking & Access Boundaries

*Source: `GH-200_Cheat_4A_-_Runner_Networking_and_Access_Boundaries.md`*

*Last-week review. Full notes: `GH-200_Topic_4A_-_Runner_Networking_and_Access_Boundaries.md`. (Domain 4 · 4.4)*

---

#### ★ MASTER DISTINCTION — egress identity vs private reachability
- **Egress identity** = predictable *source IP* the runner presents → for **IP allow lists** / target firewalls. Tools: **self-hosted** or **static-IP larger runners**.
- **Private reachability** = getting onto/into a network with **no public endpoint** → DB, Artifactory, on-prem API. Tools: **Azure VNET**, **WireGuard**, **API gateway + OIDC**.
- **Don't cross them:** a static IP does NOT grant reachability; a VNET does NOT (by default) give an allow-listable egress IP.

#### ★ NO "Actions" toggle on an IP allow list
Only two controls exist:
1. **Enable IP allow list** (enforcement on/off)
2. **Enable IP allow list configuration for installed GitHub Apps** (auto-imports App-declared IPs; happens even if the list isn't enabled)

Actions is gated **purely by the runner's IP**. Distractor bait: *"...for Actions runners"*, *"...for Actions and Pages."*

#### ★ Static IP ⊕ Azure VNET = mutually exclusive
- VNET runners use **dynamic IPs**; can't also assign static IP.
- VNET + **Azure default outbound** ⇒ egress IPs **unpredictable**, **not** allow-listable → need **NAT gateway / stable outbound IP**.

---

#### IP allow list — fast facts
- **GHEC only.** Gates **PRIVATE** resources (public stays open).
- **Role-blind** — applies to owners, repo admins, outside collaborators too → **lockout risk**, keep ≥2 owners.
- **Adding entries ≠ enforcing** — must tick *Enable IP allow list*.
- Org-level **or** enterprise-level (enterprise entries inherited; org can add but not edit inherited).
- CIDR notation.

#### Hosted-runner conflict
- Standard hosted runners = **wide + shared + weekly-rotating Azure IPs** ⇒ can't practically allow-list (and it weakens control).
- Under an allow list, use **self-hosted** OR **static-IP larger runners**; add the runner IP/range to the list. (Standard runner ⇒ `checkout` 403.)

#### Carve-outs / exemptions (distractors)
- **Dependabot** = exempt (first-party App).
- **GitHub App server-to-server installation tokens** = not currently restricted.
- **Codespaces** = unusable for org repos when an org allow list is set.

#### Private networking paths
- **Static IP larger runner** → egress identity; fixed range; usable *with* allow list; dual ranges, scales past 500 concurrency.
- **Azure VNET** → reachability; **VNET injection** = NIC in your subnet, **VM stays GitHub-side**; inherits NSG / ExpressRoute / VPN; **2–64 vCPU Ubuntu + Windows only**; setup = Azure resources first → network config → runner group; size subnet > max concurrency.
- **API gateway + OIDC** and **WireGuard overlay** → reachability, **work with standard runners** (patterns you build).

#### OS/size exclusions
- **macOS larger runners** = **no** Azure VNET, **no** static IP.

---

#### Watch-outs (uncertain / evolving — don't over-commit)
- "Artifacts exempt from allow list" = **community claim, unverified**.
- GHES docs say hosted runners wholly incompatible (older/absolute); GHEC adds the static-IP exception.
- VNET NICs moving to a GitHub service subscription; **VNET failover** in public preview.
- Subnet buffer %: docs ~30% vs GitHub Learn 20% — know the *principle* (size > max concurrency), not the number.


---

## Topic 4B — Runner Images & Toolcache

*Source: `GH-200_Cheat_4B_-_Runner_Images_and_Toolcache.md`*

*Last-week review. Full notes: `GH-200_Topic_4B_-_Runner_Images_and_Toolcache.md`. (Domain 4 · 4.6)*

---

#### ★ Three SOURCES + one STORE (don't make the tool-cache a "source")
- **Preinstalled** (baked) = TWO layers: (a) system-wide on `PATH` (git, docker, default Node/Python, apt pkgs); (b) **Cached Tools** = extra runtime *versions* in the tool-cache (ubuntu-24.04: Go, Node, Python, PyPy, Ruby).
- **`setup-*` actions** (run-time picker).
- **Your installs** (`apt-get`/`pip`/`brew`/manual).
- **tool-cache (`_work/_tool`)** = the SHELF. Filled by preinstall + `setup-*` only. **Direct installs never touch it.**

#### ★ Direct installs are INVISIBLE to `setup-*`
`apt-get install python3.12` → `setup-python` does NOT see it. setup-python uses a cached version if present, else downloads into the tool-cache. The apt result is irrelevant in all cases.

#### ★ HOSTED = speed, not persistence
- Tool-cache on hosted = **per-VM**, wiped every job. Preinstalled versions give *fast starts*, but nothing you download mid-job survives.
- What persists across **hosted** jobs = **`actions/cache`** (deps), a *different* cache. ← don't confuse the two.
- **SELF-HOSTED** = same machine ⇒ `_work/_tool` survives ⇒ a `setup-*` download sticks for later jobs (manual installs persist too → drift risk).

#### ★ Custom images = LARGER runners ONLY → Team/GHEC
Not standard runners, not Free. GA ~April 2026 (was preview Oct 2025).

#### ★ Custom image ≠ self-hosted
- Still **GitHub's infra**. Image lives in org Actions → **"Custom images"** catalog — **NOT** `ghcr.io`, **NOT** your registry. No cross-CI reuse. Not a general VM pipeline.
- Distractor bait: "pushed to ghcr.io", "reuse on CircleCI", "you patch the OS like self-hosted."

---

#### Custom images — fast facts
- **3 steps:** image-generation runner → generate via `snapshot` → assign to runner group + `runs-on`.
- **Platform match:** gen-runner platform = target (Linux x64 / Linux ARM64 / Windows x64). Run image on **same size or larger**.
- **`snapshot` syntax:**
  - String (`snapshot: name`) = name only, GitHub versions it.
  - Mapping (`image-name:` + `version:`) = name + **major** version; **minor auto-increments, NO patch**.
- **Version created ONLY on job success.** Fail/incomplete ⇒ no new version.
- **Storage billed separately** (Actions storage); each snapshot = new version ⇒ storage grows. Enterprise owners set **retention policy**.
- **Security:** dedicated runner group for image gen; **don't share prod with dev/test** (injection); buildable from **any branch** ⇒ write access = trigger ⇒ least privilege.

#### Self-hosted — fast facts
- Full OS/image control, **any distro**, persistent tool-cache, pre/post-job hooks — but you own maintenance/security/drift.
- **Hosted Linux = Ubuntu ONLY.** Other distros ⇒ Docker, or self-hosted custom VM.

#### Find the exact image software
Log → **Set up job → Runner Image → "Included Software"** link. Source = `actions/runner-images`, refreshed ~weekly. Don't assume presence/version — pin `setup-*` + explicit version.

---

#### ⚠ Unverified (calibrate vs practice exams)
- Hosted tool-cache **path** `/opt/hostedtoolcache` + env var `RUNNER_TOOL_CACHE` — not re-verified (documented default = `_work/_tool`).
- Custom-image **retention 60-day default / 90-day max** — community-reported, not docs-confirmed.
- Hook env-var names `ACTIONS_RUNNER_HOOK_JOB_STARTED`/`_COMPLETED` — from a community blog.


---

## Topic 4C — Variables & Secrets REST API

*Source: `GH-200_Cheat_4C_-_Variables_and_Secrets_REST_API.md`*

*Last-week review. Full notes: `GH-200_Topic_4C_-_Variables_and_Secrets_REST_API.md`. (Domain 4 · 4.7, 4.8)*

---

#### ★ Variable precedence — MOST SPECIFIC wins
`environment > repository > organization`. Docs say "lowest level takes precedence" = closest to the job.

#### ★ Env-level timing trap
Environment-level variables land on the runner **only after the job starts** ⇒ they do **NOT** overwrite `env`/`vars` during **pre-job processing**. So an env-level var can't feed `runs-on` / early-evaluated keys. Distractor bait: "set the runner via an environment variable."

#### ★ Reusable-workflow trap
A called (reusable) workflow uses the **CALLER's** repository variables. The called workflow's **own** repo variables are **NOT** available to it.

#### ★ 256 KB combined — env excluded
Combined **org+repo** variables = **256 KB / workflow run** (GitHub.com/GHEC; **GHES = 10 MB**). Over the cap → only org vars under it served (after repo vars, alphabetical). **Environment vars don't count** → push overflow into environments. (Other limits: 48 KB/var; 1000 org / 500 repo / 100 env.)

#### ★ Variables = PLAINTEXT, Secrets = ENCRYPTED
Variables: visible in settings, **not masked**, for non-sensitive config. Secrets: libsodium-sealed + masked. Never put sensitive data in a variable.

---

#### Secrets via REST — 3-step encrypt-first
1. **GET** `…/actions/secrets/public-key` → `{ key_id, key }`
2. **Encrypt** plaintext with that key via **libsodium sealed box**, Base64 it
3. **PUT** `…/actions/secrets/{name}` body `{ "encrypted_value", "key_id" }`
- Org adds `"visibility":"selected"` + `"selected_repository_ids":[...]` ← **IDs, not names**.
- Encryption is **client-side, before it reaches GitHub** → plaintext never in GitHub logs; GitHub decrypts server-side at runtime.
- Sealed box = recipient-only (GitHub) anonymous PK encryption; function `crypto_box_seal`. (Concept, not a memorize-item.)

#### ★ API read-back contrast (trap)
- **GET a secret = NO value** — metadata only (name/timestamps). Values can **never** be read back via API.
- **GET a variable = returns the value** (plaintext CRUD: `POST`/`GET`/`PATCH`/`DELETE` on `/actions/variables`).

#### Scopes
- repo/env secrets: collaborator access (classic `repo` scope).
- org secrets: `admin:org`.

#### gh CLI
`gh secret set NAME` (does GET-key → seal → PUT for you); `gh variable set NAME` (plaintext).

---

#### ⚠ Unverified / version-specific (calibrate vs practice exams)
- **256 KB** = cloud; **10 MB** = GHES.
- Variable **creation naming rules** (no spaces, no leading digit, no `GITHUB_` prefix, case-insensitive) — standard rules, not re-pulled verbatim.
- **Variables REST endpoints** stated from parallel structure (secrets API verified live; variables API page not re-pulled).
- **gh CLI** commands from knowledge, not re-pulled.


---

## Topic 5A — Untrusted Input & Token Hardening

*Source: `GH-200_Cheat_5A_-_Untrusted_Input_and_Token_Hardening.md`*

*Full notes: `GH-200_Topic_5A_-_Untrusted_Input_and_Token_Hardening.md`. Domain 5 · objectives 5.3 + 5.4. Verified live 2026-06-23.*

---

### TRAPS FIRST

- **The half-fix.** Moving an untrusted value into an `env:` var is pointless if you then read it back as `${{ env.VAR }}`. That's still an expression → substituted into the script source at template time → still injectable. Read it the shell way: `$VAR` / `"$VAR"`.
- **Quoting ≠ a fix.** `"${{ github.event.* }}"` in a `run:` block is still vulnerable — substitution happens before the shell exists, so quotes are just text to break out of.
- **Double-quoting shell vars** is general hygiene (word-splitting), NOT the GitHub script-injection mitigation. Don't pick it as *the* fix.
- **`permissions:` — name one, lose the rest.** Naming any permission sets all unspecified ones to `none`; **`metadata` always stays read**. Unnamed perms do NOT keep their defaults.
- **Self-hosted lifetime trap.** Job ceiling is 5 days, but `GITHUB_TOKEN` only refreshes up to **24h**. Don't pick "lasts 5 days."
- **Run vs trigger.** A push/PR via `GITHUB_TOKEN` does **not trigger** a new run — the commit still **lands**, the event is suppressed at the trigger stage (no run created/queued/skipped). It's not "rejected" and not "held."
- **System fields aren't untrusted.** `pull_request.number`, `run_id`, `sha` = system-generated, not attacker-controlled. Distractors.

---

### Bit 1 — Script injection (5.3)

- **Mechanism:** `run:` builds a temp shell script with `${{ }}` substituted in **before execution** → untrusted context becomes script *source*.
- **Fix hierarchy:**
  1. Intermediate `env:` var, read as `"$VAR"` (the preferred inline-script fix).
  2. Pass the value as an action `with:` argument (also safe).
- **Untrusted sources:** issue/PR `title`, `body`, **branch/ref names** (`head_ref`), **email addresses**, `label`, `message`, `name`. Branch-name PoC: `zzz";echo${IFS}"hello";#`.
- **Defense-in-depth:** least-privilege `permissions:`, input validation, vetted/SHA-pinned actions, CodeQL / Scorecards.

### Bit 2 — `GITHUB_TOKEN` vs PAT (5.4)

- **What it is:** a **GitHub App installation token**, minted **per job**, auto-injected, never stored. Read via `secrets.GITHUB_TOKEN` or `github.token`. NOT user-bound (that's why it's safer than a PAT).
- **Three traits:** ephemeral (dies at job end) · repo-scoped (can't reach other repos) · permission-tunable.
- **Lifetime cap:** 6h hosted · self-hosted refreshable only to 24h.
- **Recursion guard:** `GITHUB_TOKEN`-pushed commits/PRs don't trigger downstream runs. Need them to? Use a **PAT or GitHub App token** — same swap that gives cross-repo reach also lifts the guard.
- **PATs:** fine-grained (recommended, repo-restrictable) > classic (every repo the user can access). Flaw = user-bound + long-lived.
- **Escalation order:** `GITHUB_TOKEN` → **GitHub App** token (cross-repo / short-lived) → **PAT** (last resort, set expiry).


---

## Topic 5B — OIDC Keyless Cloud Auth

*Source: `GH-200_Cheat_5B_-_OIDC_Keyless_Cloud_Auth.md`*

*Full notes: `GH-200_Topic_5B_-_OIDC_Keyless_Cloud_Auth.md`. Domain 5 · objective 5.5. Verified live 2026-06-23.*

---

### TRAPS FIRST

- **`id-token: write` ≠ resource write.** It only lets the job request/use the OIDC token. Missing it = #1 OIDC failure. (Names one permission → all others `none` except `metadata` read.)
- **Two tokens, don't merge them.** `ACTIONS_ID_TOKEN_REQUEST_TOKEN` (request token) authenticates the runner *to GitHub* to mint the JWT — **the cloud never sees it.** Only the **JWT** goes to the cloud.
- **The JWT carries identity, not permissions.** Scope is 100% cloud-side. AuthN = GitHub; authZ = cloud.
- **Validation order = issuer → signature → claims.** Read `iss` → confirm trusted/registered issuer → fetch *that* issuer's public keys → verify signature → check `aud`/`sub`. Issuer check is NOT redundant with signature: it *selects* the key set ("is it a signer I trust?") vs signature ("is it real?").
- **`sub` precedence: environment > pull_request > branch/tag.** A job referencing an environment gets `:environment:NAME` even on a PR trigger. No composite form. Condition for `:ref:refs/heads/main` breaks the moment a job declares an environment.
- **PR job referencing `production` → `sub` matches `:environment:production`.** The cloud condition does NOT stop it — **environment protection rules** (GitHub-side, before token issue) do. Scope-to-environment + protection-rules are a **pair**.
- **`StringEquals` + `*` fails CLOSED.** `*` is literal under `StringEquals` → matches nothing → too-restrictive bug, not exposure. Danger appears under `StringLike` (wildcard expands). Distinguish too-restrictive (broken) from too-permissive (hole).
- **Immutable subject claims ≠ immutable releases (3A).** Same word, unrelated feature.

---

### Bit 1 — Concept & flow

- **Why:** swap a **long-lived stored cloud secret** for a **short-lived token fetched at runtime**. Nothing durable in GitHub.
- **Flow:** job (with `id-token: write`) → request token mints a **signed JWT** from `https://token.actions.githubusercontent.com` → JWT sent to cloud → cloud validates → returns **short-lived, job-scoped** cloud creds.
- **Acceptance = asymmetric crypto.** GitHub signs with private key (RS256); cloud verifies with GitHub's **public** keys (JWKS via `.well-known/openid-configuration`). No shared secret. Trust anchored by one-time provider registration (issuer URL).
- **Scope:** trust policy = *who may assume the role*; role permission policy = *what it can do*. GitHub's only levers = `id-token: write` + the identity claims.
- **Mechanics:** cloud's official login action (`aws-actions/configure-aws-credentials`, `azure/login`, `google-github-actions/auth`), or manual fetch via `ACTIONS_ID_TOKEN_REQUEST_URL` + `ACTIONS_ID_TOKEN_REQUEST_TOKEN` (`getIDToken()` helper).

### Bit 2 — Trust config & claims

- **`sub` format:** `repo:<owner>/<repo>:<ref-type>:<ref>`. Forms: `ref:refs/heads/<branch>`, `ref:refs/tags/<tag>`, `environment:<name>`, `pull_request`.
- **`pull_request` sub is stable, no PR number** → conditioning on it trusts ALL PRs incl. forks. Never for production.
- **`aud`:** defaults to owner URL; cloud actions set it (AWS `sts.amazonaws.com`). Condition on `aud` AND `sub`.
- **AWS condition keys:** `token.actions.githubusercontent.com:aud` / `:sub`. Azure = federated credential; GCP = workload identity pool. Same concept.
- **Four misconfigs:** (1) `aud`-only = all of GitHub; (2) `repo:org/*` (wildcard-eval) = whole org incl. forks/dependabot/new repos; (3) wildcard under `StringEquals` = matches nothing, use `StringLike`; (4) production on `pull_request` = any PR author incl. forks.
- **Best pattern:** scope to `:environment:NAME` (stable across triggers) **+ environment protection rules** (the actual gate).
- **Granularity:** customize `sub` template via REST (`include_claim_keys`); condition on `repository_id`, `repository_visibility`, `repo_property_*`; `job_workflow_ref` for reusable workflows.
- **⚠ Immutable subject claims:** repos created after **2026-07-15** default to `sub` with owner_id + repo_id → `repo:org@123456/repo@456789:...` (anti namespace-recycling). Old repos opt in (settings UI / REST). **Not** on GHES. Trust policy must match the repo's actual format.


---

## Topic 5C — Action Enforcement Policies & Build Provenance

*Source: `GH-200_Cheat_5C_-_Action_Enforcement_Policies_and_Build_Provenance.md`*

> Last-week review. Fuller note: `GH-200_Topic_5C_-_Action_Enforcement_Policies_and_Build_Provenance.md`
> 5C = **enforcement** (Bit 1) + **provenance proof** (Bit 2). NOT a re-teach of 3A concepts.

---

### ⚠ THE BIG ONE — "artifact" is two unrelated features (exam won't name the domain)

| Verbs in the question | It's… | Domain |
|---|---|---|
| `upload-artifact`/`download-artifact`, "between jobs," "retention," "90 days" | **workflow artifact** | 1 (Topic 1E) |
| `attest`, "provenance," "Sigstore," "`gh attestation verify`," "SLSA," "verify before deploy" | **build output under an attestation** | 5 (5.8) |

Same word, unrelated mechanics. Read the verbs, not the noun.

---

### Bit 1 — enforcement keepers

- **Override direction:** enterprise → org → repo. Lower level can only **tighten**, never loosen.
- **Section labels differ by scope:** repo = "Actions permissions"; org & enterprise = "Policies." (Concept identical; recognize, don't memorize.)
- **Local-only policy blocks GitHub's own actions** → `actions/checkout` becomes inaccessible. Re-enable via "Allow actions created by GitHub."
- **Local actions (`uses: ./path`) are NEVER restricted by the allow/deny list.** Remote refs only.
- **`!` in the allow list** = subtract an exception; both entries coexist; **block wins on overlap**. `*, !evil-org/*` = allow all except that owner. List capped at **1000 entries**.
- **Verified-creator badge = publisher IDENTITY only**, not code review/audit. Verified accounts can be compromised. Still review source + pin SHA.
- **★ SHA-pinning enforcement applies to ACTIONS only — reusable workflows are EXEMPT (still tag-referenceable).** "Forces reusable workflows onto SHAs too" → FALSE.
- **SHA pin freezes source, not behavior** — a pinned action can still pull an unpinned Docker image / nested composite / `curl`ed script. Reproducible *source*, not *behavior*.
- **★ "Required reviewers for unverified actions" is NOT a real feature.** It's a loose umbrella over: (a) fork-PR contributor-approval gate (keys off *who triggers*) + (b) environment "Required reviewers" protection rules (gate a *job* hitting a protected env). No setting inspects action-verified-status and demands a reviewer.
- Fork-PR approval: maintainer (write access) approves before run; **both PR author AND triggering actor checked**; run awaiting approval **>30 days → auto-deleted**.
- Immutable actions: **consuming = live/transparent** (OCI packages from GitHub Packages, host `pkg.actions.githubusercontent.com` under `*.actions.githubusercontent.com` → 4A allow-list). **Publishing your own = ⚠ not confidently GA** (README "not for public use" vs roadmap "GA"). Verify on practice exam.

---

### Bit 2 — attestation keepers

- **Attestation = signed claim binding SUBJECT (name + SHA-256 digest) → PREDICATE (provenance facts) in in-toto format.** Digest = hash of the actual bytes.
- **3 permissions to generate:** `id-token: write` (OIDC signing identity — the 5B tie-in, NOT for deploy), `contents: read`, `attestations: write`. (+ `packages: write` for container images.)
- **Action naming:** `actions/attest-build-provenance` (historic) is, as of v4, a **wrapper around `actions/attest`**. New code → `actions/attest@v4`. **Recognize BOTH names.** `@v1` in old material = drift, not wrong.
- **Keyless signing via Sigstore:** public repo → **Public Good** instance (has transparency log); private/internal → GitHub **private** Sigstore (no transparency log, federates only with Actions).
- **Generating alone = no security benefit. Value only on verification** (`gh attestation verify`, needs `--owner` OR `--repo`).
  - Container image → `oci://ghcr.io/...` prefix, not a file path.
  - SBOM → must pass `--predicate-type` (else it verifies provenance, not the SBOM).
  - `--signer-workflow` / `--signer-repo` → require a *specific* signing workflow/repo.

- **★ CHECK ORDER (Q2 keeper):** verify runs **bytes → signature → identity**.
  - A **plain file-swap fails at step 1 (digest/bytes lookup)** — the swapped bytes hash to a different digest, so **no attestation exists for them**, before any signature is examined.
  - The **signature check** defeats a **forged/invalid attestation that has a matching digest**.
  - The **identity check** rejects a validly-signed output from a *different* owner/repo than you demanded.
  - Exam can split these: "what catches a swapped artifact?" (bytes) vs "what catches a forged attestation?" (signature).

- **★ MONOTONIC — state it precisely:** verify passes when **≥1 attestation satisfies the SPECIFIC CLAIMS YOU ASKED TO VERIFY** (`--owner`/`--repo` + `--signer-workflow`/`--predicate-type` if given) — NOT the generic "an attestation passes." Junk/non-matching attestations are **inert** (can't substitute, can't veto). Monotonic = once it passes, later additions can't flip it to fail (anti-DOS).
  - **Looseness lives in YOUR query:** `--owner acme` only proves "*someone* in acme signed it," not "`release.yml` did." Tighten with `--repo`/`--signer-workflow`. **Owner ≠ workflow.**
  - Verifying provenance ≠ verifying SBOM (different predicate).

- **SLSA** = "Supply-chain Levels for Software Artifacts" ("salsa"), industry framework, not a GitHub feature. GitHub provenance is in SLSA build-provenance format. **Attestations + reusable workflows → SLSA v1.0 Build Level 3.** (⚠ baseline level of a plain attestation + exact per-level wording = unverified; objective lists SLSA as an *example* only.)
- Deploy gate: run `gh attestation verify` before consuming a build output; proceed only on pass. K8s **admission controller** can enforce at the cluster (know it exists).


---

## Topic 5D — Optimization & Retention

*Source: `GH-200_Cheat_5D_-_Optimization_and_Retention.md`*

> Last-week review. Fuller note: `GH-200_Topic_5D_-_Optimization_and_Retention.md`
> 5D = cost/limits/optimization (5.10) + retention/storage (5.9). Final Domain 5 topic.

---

### Cost model (Bit 1)

- **Billed = round-up(minutes) × OS-multiplier.** Round each job **UP to the whole minute** (1s and 59s both = 1 min).
- **OS multiplier: Linux 1× · Windows 2× · macOS 10×.** macOS 10-min job = 100 min. Move to Linux = biggest lever.
- **Public repos + self-hosted runners = FREE** (no billable minutes). 10× only bites on **private** (or larger runners, never free even on public).
- **Larger runners:** higher rate by vCPU; **free while idle**; static IP no extra cost; included free minutes can't be used on them.
- **★ Job limit = 6 hours** (killed if exceeded). Concurrency capped per plan (Free→Enterprise). Matrix cap commonly cited **256**. `schedule:` ≥ 5-min spacing, can be delayed/dropped.

### Optimization levers (Bit 1)

- **★ Parallelization cuts TIME, not billed minutes — can INCREASE them.** Minutes are summed across jobs; split adds per-job setup + per-job round-up. Exam answer: "splitting into a parallel matrix reduces wall-clock, NOT billed minutes, and may raise them."
- **Real minute-savers:** path/branch filters + `if:` (run less); `concurrency` + **`cancel-in-progress: true`** (cheapest win — kills runs superseded by a new push); **`timeout-minutes`** (else hung job runs to the 6h ceiling); right-sizing (bigger ≠ cheaper — 4× rate for 1.67× speed = net loss); **`needs:` fast-fail gate** (cheap lint job gates the expensive job → failure stops the run before costly work = where the dependency graph actually saves minutes).
- **cache vs artifact (1E):** cache = deps/build-accel, **7-day default**, 10 GB LRU; artifact = results, **90-day default**. Don't swap their roles.
- **★ Usage metrics show RAW minutes (NO multiplier applied)** → dashboard number ≠ bill. Metrics = "where minutes go"; billing page/spending limits = actual cost.

### Retention & storage (Bit 2)

- **Defaults: artifact/log = 90 days; cache = 7 days.** *Understand why* (cache = disposable/churns fast + size-capped LRU; artifact = retrievable results). Don't memorize in isolation.
- **Range: artifacts 1–400 days** (private/internal/Enterprise); **public capped at 90**. Cache: public ≤ 90, private/internal ≤ 365.
- **★ Period change is NOT retroactive** — applies to NEW objects only; old artifacts keep their original lifespan (by design, not a bug). To reclaim now → delete explicitly.
- Per-artifact override: `retention-days:` in `upload-artifact` (capped by repo/org max); `compression-level: 0–9`.
- **★ Programmatic retention — precise meaning:** = per-artifact `retention-days` (declarative) + programmatic **deletion** via REST/`gh`. There is **NO confirmed REST endpoint to SET the retention period** (`PUT .../actions/retention` unverified/likely not official). REST does **get / list / delete** only.
  - `DELETE /repos/{owner}/{repo}/actions/artifacts/{artifact_id}` (+ `GET` to list); `DELETE .../actions/runs/{run_id}`; `gh cache delete`.
- **★ Quota recalculation lags** (commonly 6–24h). A "storage quota exceeded" error persists *after* a successful delete — deletion didn't fail; just wait + lower retention going forward.


---

## Drill-Surfaced Keepers — Pass 1 (added 2026-06-25)

*Trap-grade items surfaced while drilling the GHCertified bank (Pass 1). Each was checked against the live material; most fill gaps the courses never covered. Distribute into the topic sections above on the next cleanup pass — kept together here for now.*


**Topic 1A**
- Run a job **only on a merged PR**: there is **no `merged` activity type** — use `pull_request: types: [closed]` + `if: github.event.pull_request.merged == true`.
- Reusable-workflow limits: **max 50** reusable workflows callable per file (raised from 20); **nesting depth 10** levels (raised from 4). *(current-state — re-verify)*
- `pull_request` `branches:`/`paths:` filters match the **base (target) branch** (where the PR merges INTO), NOT the source/head branch. `!pattern` excludes; a later negative line removes earlier matches. (`tags:` is push-only.)

**Topic 1B**
- Status-check functions (used in `if:`): `success()` (implicit default), `failure()`, `always()`, `cancelled()`. NOT functions: completed/state/status.
- **Secrets NOT usable in `if:`** (job or step) — validation error. To gate on a secret: map to job-level `env:` then `if: ${{ env.X != '' }}` (unset secret → empty string).
- `if:` — the surrounding `${{ }}` is **optional** (`if: success()` == `if: ${{ success() }}`). `github.repository` = full **`owner/repo`**; owner alone = `github.repository_owner` (no `github.org`/`github.organization`).
- Runner default **env vars** use `RUNNER_` prefix: `RUNNER_OS` (Linux/Windows/macOS), `RUNNER_ARCH` (X86/X64/ARM/ARM64), `RUNNER_NAME`, `RUNNER_TEMP`, `RUNNER_TOOL_CACHE` — mirror the `runner` context (`runner.os` ↔ `RUNNER_OS`). NOT `GITHUB_RUNNER_OS`. `GITHUB_` = repo/event/workflow data; `RUNNER_` = runner machine.

**Topic 1C**
- You CAN parallelize an **entire reusable workflow**: put `strategy.matrix` on a job whose body is `jobs.<id>.uses: <reusable-wf>@ref` → runs that whole reusable workflow once per matrix combo. (Matrix itself is still job-scoped; this is the mechanism.)

**Topic 1E**
- `actions/cache`: `key` = exact key; `path` = files to cache; **`restore-keys`** = ordered **fallback prefixes** — on exact-key miss, restore the most recent **partial** match (still `cache-hit:false`). `enableCrossOsArchive` = cross-OS; `cache-hit` output = hit/miss.

**Topic 2A**
- Re-run actor split: `github.actor`/`GITHUB_ACTOR` = **original** triggerer (unchanged on re-run; re-run uses its privileges); `github.triggering_actor`/`GITHUB_TRIGGERING_ACTOR` = whoever **re-ran** (changes). Re-run also reuses the **original SHA/ref**.

**Topic 4C**
- Scope levels = **organization / repository / environment**. An environment is **repo-scoped** — there is NO environment shared across repositories (common distractor).

**Topic 1A/2A**
- Skip a run: put `[skip ci]` `[ci skip]` `[no ci]` `[skip actions]` `[actions skip]` (or a `skip-checks: true` trailer) in **any commit message of a push**, or in the **HEAD commit of a PR**. Applies ONLY to push & pull_request (not pull_request_target). `ci` tokens = cross-tool convention (Travis/GitLab); `actions` tokens = GitHub-specific.

**Topic 4C/5**
- Org-level **shareable/reusable** components (4): **Secrets, Configuration Variables, Self-Hosted Runners, Workflow Templates**. NOT shareable: **Environment Variables** (inline env:), **Cache**, **Artifacts** (run/repo-scoped). Trap = Configuration Variables (yes) vs Environment Variables (no).

**Topic 1B/5A**
- Default env vars (GITHUB_ prefix): GITHUB_WORKFLOW, GITHUB_REPOSITORY, GITHUB_ACTOR, GITHUB_SHA, GITHUB_REF, GITHUB_RUN_ID/NUMBER, GITHUB_JOB, GITHUB_EVENT_NAME, GITHUB_WORKSPACE, GITHUB_API_URL... **GITHUB_TOKEN is NOT one** — it's a secret (`secrets.GITHUB_TOKEN`/`github.token`), map it to env yourself. Runner machine defaults = `RUNNER_*`.

**Topic 1E/5D**
- CACHE access scope = own branch + default branch (+ PR base); **siblings isolated**. Default-branch caches shared to all. (Retention: cache 7d / artifact 90d.) ARTIFACT scope = the RUN, not branch; cross-branch/run download via `actions/download-artifact` w/ run-id + `actions: read`.

---

## Drill-Surfaced Keepers — Pass 1, Session 3 (added 2026-06-29)

**Variables — disambiguation heuristic (exam-critical):** when a stem says "variables" ambiguously, let the OPTIONS disambiguate.
- `env:` / `.env` keys in YAML → **custom environment variables**. Scopes: **workflow / job / step ONLY**. Inheritance flows parent→child, innermost wins; siblings never see each other.
- `${{ vars.X }}` → **configuration variables** (set in settings UI). Scopes: **enterprise / org / repo / environment**.
- Cross-step data sharing is NOT a sibling reference → write `$GITHUB_ENV` (later steps) or step outputs `$GITHUB_OUTPUT` → `steps.<id>.outputs.X`.

**if: + status functions (HIGH VALUE — bit repeatedly):** every step/job carries an implicit `if: success()`. After a failure, later steps are SKIPPED unless their `if:` contains a status fn (`failure()` / `always()` / `cancelled()`). To run a step only when a specific prior step failed: `if: failure() && steps.<id>.outcome == 'failure'` (the bare outcome check alone gets skipped). A failing step DOES stop the job by default.

**REST verbs:** download run logs = `GET .../runs/{id}/logs`; create-or-update a secret = `PUT .../secrets/{name}` (idempotent, not POST).

**Actions cleanup hooks:** JavaScript action → `runs.post`; Docker container action → `runs.post-entrypoint`.

**Self-hosted runners:** attach at repository / organization / enterprise. Validate connectivity with the runner app's `config.sh`/`run.sh --check`; connectivity logs in the runner's `_diag` folder. Definition: a machine you deploy & manage to run Actions jobs.

**GHES + GitHub.com actions:** GitHub Connect = AUTO access; `actions-sync` = MANUAL (air-gapped); none by default.

**Misc keepers:** scheduled workflows → LATEST commit on the DEFAULT branch · re-run uses the ORIGINAL commit SHA (not the fixed commit) · re-running workflows + deleting logs both need WRITE · default job timeout = 360 min · cron weekdays = `0 0 * * 1-5` · custom action metadata always in `action.yml`/`action.yaml` (required even if private) · `concurrency` limits concurrent runs / `max-parallel` throttles matrix · env-var names are case-sensitive regardless of OS/shell.

**Correction to earlier keeper (artifact scope):** "ARTIFACT scope = the RUN" is the DEFAULT reach, not a hard wall — with `actions: read` + `run-id` (+`repository`), `download-artifact` v4+ pulls from OTHER runs and repos. Cache's branch scope IS a hard isolation boundary; artifact's run scope is a soft default permissions can open.

**Matrix-include counting (settles §8#1 partially):** base = product of axes; each `include` entry merges into an existing combination only if it doesn't OVERWRITE an original matrix value, else it adds a NEW combination. (Q073: 2×2 + 1 unmergeable include = 5.)
