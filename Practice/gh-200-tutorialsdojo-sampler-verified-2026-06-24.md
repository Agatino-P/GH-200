# GH-200 — Tutorials Dojo FREE Sampler (verified + enriched)

**Companion to:** `gh-200-tutorialsdojo-sampler-bank-2026-06-24.md` (raw capture, 30 Q)
**Source:** Tutorials Dojo free GH-200 sampler, Review Mode export · captured 2026-06-24
**Method:** every marked answer checked against settled GH-200 knowledge; doc-anchored items cross-checked against `docs.github.com`. Same two-tier honesty as the GHCertified file — **Settled** = stable, well-established behaviour; **🔎 Live-checked** = confirmed against docs in this/most-recent pass. This is reasoned verification, **not** a fetch-per-question.
**Last updated: 2026-06-24 16:23 UTC**

---

## Headline

**0 wrong keys — all 30 marked answers are correct or defensible.** But the sampler is *not* flawless:

- **Q26 is OFF-SYLLABUS (bucket d):** it's a Microsoft Sentinel / Kusto (KQL) question about Entra ID sign-in monitoring — nothing to do with GitHub Actions. The marked answer (`bin`) is right *as KQL*, but the item does not belong in a GH-200 bank. **Do not study it; treat as junk.** This is a real quality ding for the free sampler.
- **3 soft flags (⚑):** Q3 (two near-identical org-repo options), Q27 (a second option is arguably valid too), Q29 (correct among the options offered, but OIDC — the current best practice — isn't one of them; same dated framing as the old MS-Learn Q8).

Otherwise the sampler is solid and current: good spread across all four domains, and the keys agree with everything established in the GHCertified verification. Verdict for the keep/discard decision (§10): **worth keeping as a secondary cross-check**, with the explicit caveat that ≥1 question is mis-filed from another exam.

Domain spread (TD's own labels): Author & Manage Workflows ×8, Consume & Troubleshoot Workflows ×12, Author & Maintain Actions ×7 (incl. the off-topic Q26), Manage for Enterprise ×5 (×4 valid by topic).

---

## Verdict table

| Q | Marked | Verdict | Tier | Note |
|---|--------|---------|------|------|
| 1 | Repository, Organization, Enterprise | ✅ correct | Settled | Three runner registration scopes; Team/Workflow/Project are not execution scopes. |
| 2 | `GET …/actions/runs/:run_id/logs` | ✅ correct | 🔎 Live-checked | Confirmed earlier (GHCertified Q069). POST/DELETE/run-only are wrong. |
| 3 | Repos that belong to the organization | ✅ correct ⚑ | Settled | **⚑ Ambiguous:** option C ("internal repositories within the org's namespace") overlaps heavily. "Internal" is a visibility level; the marked "belong to the organization" is the broader org-owned answer TD treats as right. Both describe org-owned repos — a sloppy distractor pair. |
| 4 | `echo "::debug::…"` | ✅ correct | Settled | `::warning::`/`::add-mask::`/`$GITHUB_STEP_SUMMARY` don't emit debug. |
| 5 | Workflow that runs only the action | ✅ correct | Settled | Real runner context needs a workflow; local Node run can't reproduce Actions context/inputs. |
| 6 | Organization owner | ✅ correct | Settled | Org-level secrets + repo access policy = org owner; repo admin is repo-scoped. |
| 7 | `actions/upload-artifact` | ✅ correct | Settled | `download-artifact` retrieves; `setup-node`/`stale` unrelated. |
| 8 | `.github/workflows` | ✅ correct | Settled | Canonical discovery path. |
| 9 | Composite action | ✅ correct | Settled | Packages a *series of steps* as one action; reusable workflow packages *jobs*. |
| 10 | `env:` mapping form | ✅ correct | Settled | `vars:`/`with:` invalid for step env; `env:` as a list is malformed — must be a mapping. |
| 11 | `runs.using: composite` in `action.yml` | ✅ correct | Settled | Type is derived from `action.yml`, not repo name/keywords. |
| 12 | "Caching for reused/rarely-changing files" + "Artifacts = files created by a job, available after the run" | ✅ correct | Settled | Distractor A ("cache retained 30 days") is wrong — cache eviction is ~7 days of no access (or 10 GB cap), not 30. Package-registry options are wrong. |
| 13 | SHA-pin + semantic-version tag | ✅ correct | Settled | Matches the publishing best-practices (GHCertified Q034/Q133). Moving branch / no version = anti-patterns. |
| 14 | `runs-on: [self-hosted, windows, x64]` | ✅ correct | Settled | `runs-on` + cumulative labels; OS and arch are separate labels, not `win-x64`. |
| 15 | Read | ✅ correct | Settled | Minimum *repository access level* to download artifacts is Read; Write over-grants. ("Actions Read" is a fine-grained-PAT scope, not a repo access level — distractor.) |
| 16 | Required reviewers on a deployment environment | ✅ correct | Settled | The environment approval gate; CODEOWNERS/branch-protection don't gate job execution this way. |
| 17 | `workflow_run` | ✅ correct | Settled | Chains off another workflow's completion without editing it; `workflow_call`=reusable, `dispatch`=manual, `schedule`=cron. |
| 18 | 30 days | ✅ correct | Settled | A run pending approval is auto-failed after 30 days (also the max environment wait-timer). |
| 19 | Service container | ✅ correct | Settled | `services:` provides ephemeral DBs per job — on the official objective list. |
| 20 | Latest commit on default/base branch | ✅ correct | Settled | Scheduled runs use the default branch's latest commit (GHCertified Q079). |
| 21 | `GITHUB_REF` | ✅ correct | Settled | Fully-formed ref that triggered the run; `GITHUB_HEAD_REF` is PR-source only; `GITHUB_BRANCH` isn't a thing. |
| 22 | Finished runs can be removed | ✅ correct | Settled | Completed runs are deletable regardless of age; **write** (not admin) suffices; in-progress can't be deleted; no 30-day rule. |
| 23 | Define Production env + required reviewers; reference the env in the deploy job | ✅ correct | Settled | Two-part environment gate. Repo-admin assignment / branch protection / "register VMs in env config" are wrong. |
| 24 | Reusable workflows (`workflow_call`) | ✅ correct | Settled | Needs *multiple jobs* reusable across repos → reusable workflow, not composite action. |
| 25 | `uses: octo-org/another-repo/.github/workflows/workflow.yml@v1` | ✅ correct | Settled | Must be `uses:` + full `.github/workflows/` path + `@ref`; `implements:`/`imports:` and the owner-less form are wrong. |
| 26 | `bin` (KQL) | ⚠️ **OFF-SYLLABUS** | bucket (d) | **Not a GitHub Actions question** — it's a Microsoft Sentinel/KQL item (Entra ID sign-ins, time-chart bucketing). `bin()` is the right KQL operator, but this is mis-filed from another exam. **Skip it.** |
| 27 | Required approvals gate access to environment secrets | ✅ correct ⚑ | Settled | **⚑ Mild ambiguity:** option B ("authenticate workflows with Entra ID") is also a plausibly valid use of env secrets. TD's answer is the *most distinctive* use case (approval-gating is unique to environment secrets), so it's defensible — but the stem could be read to fit B. |
| 28 | Composite run steps action | ✅ correct | Settled | Composite `run:` steps execute shell natively; JS/TS/Docker add overhead. |
| 29 | Manage SP credentials via GitHub Secrets | ✅ correct ⚑ | Settled | **⚑ Dated framing:** correct *among the offered options* (commit/hardcode/PAT are all insecure or wrong), but **OIDC federation — the current recommended approach (no long-lived secrets)** — is not offered. Same family as the retired MS-Learn Q8. If quizzing, mention OIDC as the better real-world answer. |
| 30 | Multi-OS (Linux/Win/macOS) managed runners + automatic patching/maintenance | ✅ correct | Settled | GitHub-hosted advantages. "Long-lived runner persistence via Environments" is wrong — hosted runners are ephemeral. |

---

## Notes for drilling

- **Shuffle (§4.10) still applies.** Unlike GHCertified, TD's sampler shows no answer-position bias (correct options appear in varied slots), but randomise on quiz anyway so position never becomes a crutch.
- **Hold out Q26 entirely** — it's not GH-200 material.
- **Q29 is a teaching moment, not a miss:** if it comes up, drill the OIDC-vs-stored-secret distinction (Domain 5 / security objective) rather than just accepting the keyed answer.
- The four ⚑/⚠ items are all bucket (d)-adjacent (bad/ambiguous/dated question), **not** knowledge gaps — so a miss on them shouldn't be triaged as a (b)/(c) gap.
