# GH-200 Gap-Study Plan — Pass 1 → Pass 2 bridge

*Created 2026-06-29. Companion to `GH-200_Practice_Protocol_and_Progress.md`. Pass 1 (GHCertified, 178 Q) is COMPLETE; the Tutorials Dojo sampler was retired. This plan governs the **gap-study phase** before Pass 2.*

---

## §0 What drives this plan

**The signal is your own performance, not course coverage.** Two primary drivers:

1. **Errors you made** in Pass 1 — especially the ones that turned out to be *reference gaps* (you'd seen a fragment but picked the wrong event/function when a different one came up).
2. **Topics you explicitly flagged as unknown** ("giant gap", "first time reading", "don't know anything about X", "no point guessing").

Course-coverage analysis is **demoted to a secondary check** — it only contributes the *untested blind-spots tail* (Phase 1-C): real Jan-2026 objectives no question tested and you never flagged, so the error/flag signal is silent on them. We are **not** re-running the courses.

**Order:** build broad understanding first (Phase 1 — catalogs, unknowns, blind-spots), then re-drill the genuine retention slips (Phase 2).

## §1 How each topic runs

Per topic: **compact, doc-grounded recap -> a few check questions -> fold any confirmed keeper into `GH-200_Combined_Cheat_Sheets.md`.** One question at a time, shuffled, mechanical grading.

- **Check questions are ephemeral — not logged as Q&A.** Only outcomes are kept: keepers -> cheat sheet, any new gap -> §7b, progress -> the §3 checklist.
- **Integrity:** gap-topic checks are **authored + verified against `docs.github.com`** at write time and are **never written into the GHCertified bank or `gh-200-drill-log.md`** (stays GHCertified-only). Error re-drill (Phase 2) re-draws the **actual missed questions verbatim** from the bank.
- **Current-state facts** (SLSA wording, runner images, reusable limits, REST paths, immutable-actions status) are re-verified against live docs when studied.
- **Goal everywhere: the whole catalog, not the instances you saw** — so a swapped event or function on the exam doesn't catch you.

## §2 On "bits"

No formal `Bit` structure. Single-concept topics get one recap + checks; the two catalog-heavy ones (R1 triggers, R2 functions) and the runner cluster (R6) get light sub-points. Split further only if a topic proves heavy when we reach it.

---

## Phase 1 — Build broad understanding

### 1-A · Reference catalogs *(you saw only fragments — learn the whole list)*

#### R1 · Triggers & events — full reference
**Driver:** errors Q108 (`types:` keyword), Q138 (`workflow_run`), Q153 (which events run non-default-branch workflows), Q165 (dispatch endpoints); + your direct request for "the list of triggers / the events content."
**Scope:**
- Full common-event list: `push`, `pull_request`, `pull_request_target`, `issues`, `issue_comment`, `workflow_dispatch`, `repository_dispatch`, `workflow_run`, `workflow_call`, `schedule`, `release`, `deployment`, `check_run`/`check_suite`, `registry_package`, `star`, `discussion`...
- **Activity `types:`** per event (opened/closed/synchronize/reopened/labeled/edited/published...).
- Rule: **only `push` & `pull_request` run a workflow from a non-default branch; all others use the default branch.** Merged-PR pattern = `types: [closed]` + `if github.event.pull_request.merged == true`.
- `branches:`/`paths:` filter the **base/target** branch.
- Dispatch endpoints (both `POST`): `repository_dispatch` -> `/repos/O/R/dispatches`; `workflow_dispatch` -> `/repos/O/R/actions/workflows/<id>/dispatches`; `workflow_dispatch` input types (string/boolean/choice/number/environment).
**Checks:** ~4 — each deliberately picks an event/type you did **not** see in Pass 1.

#### R2 · Expression functions & operators — full reference
**Driver:** errors Q101 (status-function gate), Q140 (`startsWith`), Q164 (`if:` levels); + your direct request for "the list of functions."
**Scope:**
- Functions: `contains()`, `startsWith()`, `endsWith()`, `format()`, `join()`, `toJSON()`, `fromJSON()`, `hashFiles()`.
- **Status functions:** `success()`, `failure()`, `always()`, `cancelled()` — and the implicit `if: success()` gate they lift.
- Operators (`==`, `!=`, `&&`, `||`, `!`, comparisons), object filters (`*`), `${{ }}` optional in `if:`, truthiness (e.g. `'false'` is a truthy *string*).
- `if:` is **job + step only** (no workflow-level).
**Checks:** ~4 — mix functions you never saw (`contains`, `format`, `join`) with status-function gating.

#### R3 · Contexts & default variables — full reference
**Driver:** errors Q146/Q148 + TD (`github.ref` / `GITHUB_REF`), Q121 (default vars), Q122/Q125 (`env:` scopes).
**Scope:**
- `github.*` context essentials; default env vars (`GITHUB_*`, `RUNNER_*`); `GITHUB_TOKEN` is a *secret*, not a default env var.
- Ref family: `github.ref` (full, varies by event), `github.ref_name` (short), `github.ref_type`, `github.sha`, `github.head_ref`/`github.base_ref` (PR-only). `github.ref` by event: push `refs/heads/<b>`; tag `refs/tags/<t>`; PR unmerged `refs/pull/<n>/merge`; PR merged `refs/heads/<base>`.
- `env:` scopes = workflow / job / **step**; environment-scoped vars are a separate feature (`vars`/`secrets` contexts).
**Checks:** ~3.

### 1-B · Flagged-unknown topics *(you told me you didn't know these)*

#### R4 · GHEC vs GHES / GitHub Connect / `actions-sync` — *you: "giant gap"*
GHEC (hosted SaaS) vs GHES (self-hosted appliance); GHES has no GitHub.com/Marketplace action access by default; **GitHub Connect** = automatic access; **`actions-sync`** = manual/air-gapped; enterprise- vs org-level action access control. **Checks:** ~3.

#### R5 · GitHub Apps + installation tokens + OIDC two-token flow — *you: "first time reading" / "forgot temp creds"*
App registration vs installation; installation access token (short-lived, per-installation, not user-bound); `actions/create-github-app-token`; `GITHUB_TOKEN` *is* an installation token; escalation order. **OIDC:** identity JWT -> exchanged for **separate, short-lived cloud credentials** (the second token you keep forgetting); `id-token: write`; trust-policy `sub` conditions; cloud-login actions. **Checks:** ~4.

#### R6 · Self-hosted runners — *you: "don't know anything about runner labels"*
- **Labels & groups:** default labels (`self-hosted`/OS/arch), custom labels, `runs-on` array = match **ALL** (AND); **groups = access control**, **labels = routing**.
- **Troubleshooting:** `config.sh`/`run.sh --check`; connectivity logs in the **`_diag` folder on the runner**; `ACTIONS_RUNNER_DEBUG`.
- **Networking / IP allow lists:** add runner egress IPs; ephemeral runners need a fixed NAT/proxy IP.
- **Service containers** (`services:`) and **toolcache** (self-hosted starts empty).
**Checks:** ~4.

#### R7 · `pull_request` vs `pull_request_target` security (+ script injection) — *you: "no point guessing"*
`pull_request` (merge-commit context, no fork secrets, SAFE) vs `pull_request_target` (base context, full secrets incl. forks, DANGEROUS — "pwn request"); script-injection mitigation: **never interpolate `${{ github.event.* }}` into `run:`** — route through a quoted `env:` var; least-privilege `GITHUB_TOKEN`. **Checks:** ~3.

#### R8 · GitHub Packages publishing — *you: "not so sure"*
Publish = `write:packages` + registry config (`npm.pkg.github.com` etc.) + a publish step; `registry_package` event *reacts to* a publish; org/internal package scope. **Checks:** ~2.

### 1-C · Untested blind-spots *(NOT surfaced by errors or flags — real Jan-2026 objectives; your call: yes)*

> These didn't show up in the error/flag signal because no question tested them and you never hit them — but they're genuine exam objectives and total blind spots, so they carry real (just unmeasured) risk.

#### U1 · Artifact attestations / provenance / SLSA — `[5.8]` — highest blind-spot risk
Double gap (zero bank + not in course). `actions/attest-build-provenance`; `id-token: write` + `attestations: write`; SLSA framework + build levels (verify wording vs docs); generate vs **verify** (`gh attestation verify`). **Checks:** ~3. *(Worth doing despite being untested — a whole objective you've never touched.)*

#### U2 · YAML anchors / aliases / merge keys — `[1.9 / 2.3]`
Writing **and** reading `&` / `*` / `<<` within a file. New Jan-2026 objective, not in the course. **Checks:** ~2.

#### U3 · Minor — `[1.12 / 1.11]`
Editor tooling (VS Code Actions extension, schema completion); static-vs-runtime expression evaluation. Light pass. **Checks:** ~2.

---

## Phase 2 — Error re-drill *(genuine retention slips on material you HAD studied)*

*Check questions = the actual missed GHCertified questions, re-drawn verbatim from the bank.*

- **E1 · Reusable workflows vs composite actions + permissions** — step-vs-job/secrets-block contrast, **downgrade-only** permissions, `secrets: inherit`, full `uses:` path. *(Q040, Q130, Q131, Q174)*
- **E2 · Secrets & masking** — `::add-mask::` for derived/encoded values (auto-mask covers the secret + common encodings incl. base64, best-effort). *(Q147, Q040)*
- **E3 · Environments** — required reviewers (>=read access, 1 approval, self-review preventable, teams ok), deployment protection rules vs the repo/org retention setting. *(Q059, Q178)*
- **E4 · Concurrency & re-run** — `concurrency.group` + `cancel-in-progress`; re-run `github.actor` (original) vs `github.triggering_actor` (re-runner). *(Q171; §7b#10/#6)*
- **E5 · Cache / artifacts / retention / checkout** — cache vs artifact scoping, `retention-days` on `upload-artifact`, no official `delete-artifact`, **no `actions/checkout` => empty workspace**. *(Q144, Q156, Q175)*

---

## §3 Progress checklist *(the only state kept)*

```
Phase 1-A — Reference catalogs
[ ] R1  Triggers & events (full list + types + payloads)
[ ] R2  Expression functions & operators (full list + status fns)
[ ] R3  Contexts & default variables (github.ref family, env scopes)

Phase 1-B — Flagged-unknown topics
[ ] R4  GHEC vs GHES / GitHub Connect / actions-sync
[ ] R5  GitHub Apps + installation tokens + OIDC two-token
[ ] R6  Self-hosted runners (labels/groups/_diag/IP/service containers)
[ ] R7  pull_request vs pull_request_target + script injection
[ ] R8  GitHub Packages publishing

Phase 1-C — Untested blind-spots (real objectives, no error/flag signal)
[ ] U1  Artifact attestations / provenance / SLSA   (highest blind-spot risk)
[ ] U2  YAML anchors / aliases / merge keys
[ ] U3  Editor tooling + static-vs-runtime expressions (light)

Phase 2 — Error re-drill (verbatim missed questions)
[ ] E1  Reusable vs composite + permissions
[ ] E2  Secrets & masking
[ ] E3  Environments
[ ] E4  Concurrency & re-run
[ ] E5  Cache / artifacts / retention / checkout
```

*Per topic, one line on completion: date + result (pass / keeper added / new gap). Enough to resume across sessions.*

## §4 Exit -> Pass 2

Done when every R/U topic has a recap + passed checks and every E topic's re-drawn questions pass clean, with keepers folded into the cheat sheet. **Then Pass 2** — fresh verbatim re-drill of GHCertified Q001->Q179 (Q157 absent), same regime; readiness judged on the full-pass per-domain breakdown.

---
*Suggested order: R1 -> R2 -> R3 (catalogs unlock the rest and are the most error-dense), then R4-R8, then U1-U3, then Phase 2. U1 (attestations) can jump earlier if you'd rather front-load the one total blind spot. No gap-study Q-log; sync state to project + repo + HD at session end.*
