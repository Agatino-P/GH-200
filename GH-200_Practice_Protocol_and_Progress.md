# GH-200 Practice (Testing) Protocol & Progress Tracker

**Last updated: 2026-06-24 22:06 UTC** *(bump this timestamp on every edit — same convention as the study protocol §3.7. Use `date -u`; this value is the real system clock.)*

*This file is the operating agreement and running state for the **testing/practice phase** of GH-200 preparation. It is the companion to `GH-200_Study_Protocol_and_Progress.md`, which is now the historical **teaching-phase** record (Domains 1–5 gap-complete). Paste this into the project so any future session has full context. Claude updates the **Attempt log** and **Miss ledger** at the end of each session.*

---

## 1. Mission
The teaching/remediation phase is complete (all five domains, 14 recaps + 14 cheats). We are now in the **testing phase**: run practice exams as the real diagnostic, convert every miss into targeted review, and track readiness attempt-over-attempt until the learner can pass **GH-200 (700/1000)** with margin and no domain consistently weak.

## 2. Exam logistics *(current-state — re-confirm on the official page before booking; details have a Jan-2026 rewording behind them)*
- **Pass mark: 700 / 1000** — a *scaled* score, not a raw percentage (so a raw practice % is **not** directly comparable to the pass line). Consistent with the study protocol and standard Microsoft convention.
- **Time: 100 minutes** (per Microsoft Learn). Confirm at booking.
- **Item count: not officially published.** Microsoft does not list an exact count on the public exam page; community/third-party figures cluster around **~60–65 items** (some report ~60 scored + 10–15 unscored pretest). **Treat as approximate — flagged, not fact.**
- **Question types:** multiple-choice, multiple-response (multi-select), and scenario/case-study items; **interactive components possible** (per Microsoft Learn). Recognition-based, not free-recall.
- **Delivery:** proctored, online or in-person via Pearson VUE.
- **Content currency:** exam **reworded significantly in January 2026** (new/removed/moved objectives). Mostly GA features; may include commonly-used Preview features. Source: official MS Learn study guide.
- **Validity:** reported as **2 years** (third-party sources — unverified against the official page; confirm if it matters).

## 3. Source materials for this phase (already in the project / on HD)
- **Practice question sources / providers → §10 (in this file).**
- The **verified GHCertified bank** (`gh-200-ghcertified-verified-full-2026-06-24.md`) is the **primary drill source** — 178 questions, fully verified (0 wrong keys), covering Domain 1–5 incl. real Domain 4/5 depth (OIDC, GHES, REST, runner groups, packages). Drill it shuffled (§4.10).
- Study-phase **recaps + cheats** — **consolidated 2026-06-24 into two combined files**, `GH-200_Combined_Recaps.md` (all 14 topic recaps) and `GH-200_Combined_Cheat_Sheets.md` (all 14 cheats). These now live in **all three sources** (project + repo `Agatino-P/gh-200` → `Study material/` + HD); the 28 per-topic files were retired from the repo. They are the remediation source whenever a miss maps to a studied topic.
- `GH-200_Coverage_Map.md` and `GH-200_Study_Protocol_and_Progress.md` — objective list + teaching-phase record (for cross-referencing a miss back to where it was taught).

## 4. Testing protocol (how we run the phase)
1. **Drill the verified GHCertified bank as the primary diagnostic** (already captured + fully verified). Optionally supplement with the free Tutorials Dojo 30-Q sampler for an independent cross-check. Any unofficial bank's keys are treated skeptically and verified against `docs.github.com` before trusting them (GHCertified is already done).
2. **For drilling, work from the verified bank file directly** (no capture needed — GHCertified is already captured + verified). If a *new external* assessment is ever run, capture its questions-with-options and results into dated `.md` files and verify keys against `docs.github.com` before trusting them.
3. **Score and break down by section/domain.** Note small-n sections (a "50%" on a 2-item section is one miss — don't over-read).
4. **Triage every miss into one of four buckets:**
   - **(a) careless / misread** — no review needed; note it for pacing discipline.
   - **(b) fundamentals gap** — a basic concept the courses should have covered; quick targeted fix.
   - **(c) studied-topic retention hole** — maps to a recap/cheat; re-review that artifact + live docs.
   - **(d) bad/ambiguous question or source error** — the bank is wrong or the question is malformed; record *why* and move on (do not "learn" a wrong answer).
   Route **(b)** and **(c)** to targeted review; log all four in the **Miss ledger (§7)**.
5. **Update this tracker** (Attempt log + Miss ledger + calibration flags) at session end, then re-sync (project + repo + HD).
6. **Accuracy rules inherited from study protocol §4** (non-negotiable — learner prioritizes truth over helpfulness): verify current-state against official GitHub docs and cite; never invent action names / inputs / REST endpoints / CLI flags / YAML keys; state uncertainty plainly; flag anything that may have changed since the Jan-2026 cutoff.
7. **Timestamp every edit** — bump the header `Last updated` to current `YYYY-MM-DD HH:MM UTC`.
8. **Formatting (study protocol §3.8):** in chat, small fenced blocks only; anything wide/long → a downloadable `.md` file with real markdown tables.
9. **Three-source sync discipline (study protocol §8):** the project holds the operating set (this protocol, the study protocol, coverage map, source PDFs/indexes, the GHCertified + Tutorials Dojo bank files) **plus the two combined study-material files** (`GH-200_Combined_Recaps.md`, `GH-200_Combined_Cheat_Sheets.md`). **Convention change (2026-06-24):** recaps/cheats were consolidated from 28 per-topic files into these two combined files and now live in **all three** sources (project + repo + HD) — superseding the earlier "recaps/cheats stay on HD + repo, not project / cheats are per-topic not monolithic" rule. Keep repo / project / HD aligned; verify by fresh clone when in doubt.
10. **Quizzing from banks — ALWAYS shuffle option order.** Several banks (confirmed for **GHCertified**, 2026-06-24) list the correct option(s) first, so the answer-position is heavily skewed: ~67% of GHCertified items are a bare `A` and ~89% have `A` among the correct answers. Un-shuffled, the learner could score ~89% by reflexively picking A while testing nothing. **Rule:** whenever Claude quizzes from any captured bank, randomize the option order per question (and within multi-selects) and re-letter, keeping the original key mapped internally. The stored verification files keep the *original* letters (so they stay diffable against the raw bank) — the shuffle happens only at quiz time.
11. **Project-contents manifest (§11) — keep current + verify at every session start.** Whenever a file is added to or removed from the project, update the §11 manifest in the same edit. At the **start of every session** (first read), verify the actual project against §11 and report missing/extra — the learner requests this on every restart. The `/mnt/project` mirror is a cross-check only; the claude.ai project UI is authoritative.
12. **Quiz delivery — ONE QUESTION AT A TIME (critical, learner-mandated 2026-06-24).** Present **exactly one** question, options only (answer + rationale hidden), then **wait**. The learner may answer **or ask a clarifying question first** — never batch multiple questions or rush ahead. Only after the learner commits: reveal the marked answer, give the rationale, and **shuffle still applies (§4.10)**. Alongside each question, Claude **verifies in the background which objective it really maps to** (objective ID + a one-line why) and **records it** so the per-question objective map accumulates over the phase. **Per-question tracking** (so we always know what was asked / passed / failed): keep a running record of source Q-ID, the shuffled→original letter map, the learner's answer, correct/incorrect, the four-bucket triage (§4.4) on any miss, and the mapped objective. Summarize the running tally on request and roll confirmed (b)/(c) gaps into the Miss ledger (§7).

## 5. Readiness criteria / targets
- **Learner's working target: consistently 77%+ across multiple attempts.**
- **Honesty note on the target:** practice-bank raw % ≠ the exam's scaled 700/1000. Real readiness signal = passing reworded-objective bank(s) **with no domain consistently below the others** — especially the high-weight Domain 1 and Domain 4 (20–25% each) and the dense Domain 5.
- Stop-condition for "ready": multiple attempts comfortably clear of the line, misses are only bucket (a)/(d), and the parked calibration flags (§8) are resolved.

## 6. Attempt log
*(Claude appends a row + a short prose analysis per attempt.)*

| # | Date | Provider | Raw score | By section | Misses | Bucket(s) |
|---|---|---|---|---|---|---|
| 1 | 2026-06-25 | GHCertified (verified bank, shuffled, one-at-a-time) | **20/35 = 57% raw** · **20/25 = 80% adjusted** | spans D1–D5 | 15 | (b)×9 (c)×5 (d)×1 |

**Attempt 1 analysis:** First real GHCertified drill (35 Qs, partial bank, one-at-a-time per §4.12). **Raw 57% but adjusted 80%** once justified misses are set aside. **10 of 15 misses were bucket (b) material gaps + (d) bad wording — i.e. the reworded exam reaching past the course material, not recall failures; only ~5 were genuine (c) retention slips** (and one of those, Q068, exposed a material *error*). Key signal: command of *studied* material is solid (~80%); the raw gap is uncovered breadth, now captured (15 cheat keepers added to the Combined Cheat Sheets + 1 recap correction + the §12 gap agenda). Scoring convention adopted: report **raw AND adjusted** (adjusted excludes (b)+(d)), with the four-bucket breakdown.



## 7. Miss ledger (running gap feedback → review)
*(Confirmed weak spots harvested from attempts, with the bucket and the review action. Bucket (a)/(d) items are recorded for awareness but don't drive review.)*

| From | Item | Bucket | Maps to | Action |
|---|---|---|---|---|
| A1·Q100 | status-check functions success()/failure()/always()/cancelled() | (b) | 1.11 | Added to cheat (1B); cover in expressions ref |
| A1·Q050 | env is repo-scoped (no cross-repo env) | (c) | 4.7 | Cheat emphasis (4C) added |
| A1·Q158 | merged-PR idiom: types:[closed] + if merged==true (no 'merged' type) | (b) | 1.1 | Cheat (1A) + triggers ref |
| A1·Q076 | reusable-wf limits: 50/file, nesting 10 (was 20/4) | (b) | 1.3/2.7 | Cheat (1A); re-verify near exam |
| A1·Q068 | secrets NOT usable in if: (map to env) — **recap had this WRONG** | (c)+err | 1.11 | **Recap corrected** + cheat (1B) |
| A1·Q118 | skip-run keywords [skip ci] etc.; push=any commit / PR=HEAD | (b) | 2.x/1.1 | Cheat (1A/2A) |
| A1·Q072 | env-vars vs config-vars; workflow templates are org-shareable | (c) | 4.1/4.7 | Cheat (4C/5) |
| A1·Q031 | ${{ }} optional in if:; github.repository=owner/repo | (b) | 1.11/1.10 | Cheat (1B) + contexts ref |
| A1·Q018 | pull_request branches: filters BASE (target) branch | (b) | 1.1 | Cheat (1A) + triggers ref |
| A1·Q096 | RUNNER_ default env vars (RUNNER_OS etc.) | (b) | 1.6 | Cheat (1B) + env-var ref |
| A1·Q171 | re-run: actor=original vs triggering_actor=re-runner; reuses SHA | (c)+(b) | 2.4 | Cheat (2A); actor split was a gap |
| A1·Q043 | cache branch scope (own+default+PR-base; siblings isolated) | (b) | 1.16/5.9 | Cheat (1E/5D) |
| A1·Q106 | restore-keys = fallback prefixes for partial cache match | (b) | 1.16 | Cheat (1E) |
| A1·Q061 | default env-var list; GITHUB_TOKEN is a SECRET not a default env var | (c) | 1.6 | Cheat (1B/5A) |

**Standing watch-items (not yet triggered by a miss, but where the studied material is most likely to be tested by harder banks):** Domain 4 (highest weight; runner networking / images / variables / REST) and Domain 5 (OIDC, attestations, enforcement, optimization). Watch their per-section scores closely as GHCertified drill batches are run.


## 7b. Pass-1 drill gap agenda — COVER BEFORE PASS 2

*Concepts the bank tested that the course material does NOT cover (or got wrong). Work through these (verify each against `docs.github.com`) before re-drilling. All have cheat keepers queued in `GH-200_Combined_Cheat_Sheets.md` → 'Drill-Surfaced Keepers — Pass 1'.*

1.  [1.11 (expressions) / 1.4 (if:)] status-check functions: success()/failure()/always()/cancelled()
2. **BUILD TASK** [1.1 / 1.2 triggers, events, scope] TRIGGERS & EVENTS — systematic reference MISSING: (1) full list of common trigger events (push, pull_request, pull_request_target, issues, issue_comment, workflow_dispatch, repository_dispatch, workflow_run, workflow_call, schedule, release, deployment, discussion, check_run/check_suite, registry_package); (2) their activity `types:` (opened/closed/synchronize/reopened/labeled/edited...); (3) key `github.event.*` payload properties. Specific keeper: merged PR = types:[closed] + if github.event.pull_request.merged==true (no 'merged' type). | ALSO: pull_request branches:/paths: filter the BASE/target branch, not source/head. | ALSO: default ENV VARS — RUNNER_ family (RUNNER_OS/ARCH/NAME/TEMP/TOOL_CACHE) vs GITHUB_ family; map to runner context. | ALSO: GITHUB_ default env-var list (GITHUB_WORKFLOW/REPOSITORY/ACTOR/SHA/REF/RUN_ID...); GITHUB_TOKEN is NOT a default env var (it's a secret).
3.  [1.3 / 2.7 reusable workflows] reusable-workflow limits: max 50 callable per file (was 20); nesting depth 10 levels (was 4). Current-state — re-verify near exam.
4.  [2.x manage runs / 1.1 triggers] skip a workflow run: [skip ci]/[ci skip]/[no ci]/[skip actions]/[actions skip] in ANY commit msg of a push, or the HEAD commit of a PR. Only push & pull_request (NOT pull_request_target). Also skip-checks trailer. (ci-based tokens = cross-tool convention shared w/ GitLab/Travis; actions-based = GitHub-specific.)
5.  [1.11 expressions / 1.10 contexts] In `if:` the `${{ }}` wrapper is OPTIONAL — `if: success()` == `if: ${{ success() }}`. Plus github.repository = full owner/repo (owner alone = github.repository_owner; no github.org/github.organization).
6.  [2.4 re-run / 1.10 contexts] On re-run: github.actor (GITHUB_ACTOR) = ORIGINAL triggerer, unchanged (re-run uses its privileges); github.triggering_actor (GITHUB_TRIGGERING_ACTOR) = whoever re-ran, changes.
7.  [1.16 / 5.9 caching & artifacts] CACHE branch scoping: a run restores caches from its OWN branch + DEFAULT branch (+ PR BASE branch); sibling feature branches isolated (anti-poisoning). Default-branch caches shared to all. vs ARTIFACT: scoped to the RUN, not branch; cross-run/branch download via actions/download-artifact (run-id + actions:read; cross-repo token).

## 8. Parked calibration flags (carried from the teaching phase — resolve against real practice questions)
*(Confirm or refute each as it surfaces in a bank; update the relevant cheat/recap if a question settles it.)*
1. **`fromJSON` dynamic-matrix exam weight** — open since Topic 1C; gauge frequency. *(GHCertified note: no `fromJSON` dynamic-matrix items, but matrix-`include` counting is tested 3× — Q073, Q124, Q137. Drill the include algorithm.)*
2. **Immutable-action *publishing* GA status** (3A/5C) — README "not for public use" vs a GA-labeled roadmap card.
3. **SLSA baseline level + exact per-level wording** (5C) — stated unverified.
4. **Exact per-plan concurrency numbers + matrix-combination cap** (5D) — secondary-sourced. *(GHCertified verification corroborated the **256 matrix-combination cap** and **360-min/6-h default job timeout**; reusable-workflow cap = **50/file**, nesting depth = **10 levels** (was 4). Per-plan concurrency numbers still not independently confirmed.)*
5. **"No REST endpoint to *set* the retention period" conclusion** (5D/1E) — revisit if a question contradicts it.
6. **Exact item count / type mix of the reworded exam** (new this phase) — Microsoft doesn't publish it; refine from booking page + bank structure.

## 9. Progress tracker

| Item | Status |
|---|---|
| Teaching phase (Domains 1–5) | ✅ complete (see study protocol) |
| This practice protocol | ✅ created 2026-06-23 20:36 UTC |
| Primary drill bank | ✅ GHCertified captured + **fully verified** (178 Q, 0 wrong keys, `gh-200-ghcertified-verified-full-2026-06-24.md`) — **not yet drilled** |
| Parked calibration flags | 🟡 partially informed by GHCertified (matrix cap 256, job timeout 360 min, reusable cap 50 / nesting 10 confirmed; see §8) — concurrency per-plan numbers still open |
| Readiness (§5 stop-condition) | ⬜ not met — no drill attempts logged yet |

---

## 10. Practice question sources (providers)
*(Costs/counts are providers' own self-descriptions — approximate; verify before buying. Unofficial bank keys are verified against `docs.github.com` before trusting.)*

**Active + candidate sources:**

| Provider | Cost | Volume | Status |
|---|---|---|---|
| **GHCertified** | Free | 178 | ✅ **Primary drill bank.** Captured + fully verified 2026-06-24 (0 wrong keys). Raw = `gh-200-ghcertified-bank-full-2026-06-24.md`; verified = `gh-200-ghcertified-verified-full-2026-06-24.md` (method/legend/traps inside). ⚠ Answer-position bias → **shuffle when quizzing** (§4.10). |
| **Tutorials Dojo** | Free sampler (~$10–15 full) | 30 sampler / 140+ full | ✅ **Sampler collected + verified 2026-06-24** (30 Q, **0 wrong keys**). Raw = `gh-200-tutorialsdojo-sampler-bank-2026-06-24.md`; verified = `gh-200-tutorialsdojo-sampler-verified-2026-06-24.md`. ⚠ **Q26 is off-syllabus** (a Microsoft Sentinel/KQL item, bucket d — skip it); soft flags on Q3/Q27/Q29 (Q29 = dated, OIDC not offered). Good secondary cross-check; no position bias but shuffle anyway (§4.10). **Links:** free sampler `https://portal.tutorialsdojo.com/product/free-gh-200-github-actions-practice-exams-sampler/` · full course `https://portal.tutorialsdojo.com/product/gh-200-github-actions-practice-exams/`. (TD markets it as "not exam dump.") Full 140+ bank not yet collected. |

**Not pursuing** (recorded so we don't reconsider them each session): **ITExams** (marketed "free" but a freemium paywall — ~10 free Qs then ~$50/mo for one exam, figures approximate; user reports of wrong answers + stale content; lowest-trust dumps, not justified vs the verified GHCertified bank); **MS Learn practice assessment** (foundational + partly dated — under-tests Domain 4/5; the prior 30-Q sitting added no value); **MeasureUp** ($99) and **SkillCertPro** (~$20) — paid, not justified unless GHCertified results show a real gap. Various Udemy/certificationpractice.com banks — unvetted, ignore unless a specific need arises.

## 11. Expected project contents (manifest)

**Maintenance rule:** keep this list exact. Whenever a file is added to or removed from the project, update this manifest **in the same edit** and bump the header timestamp. **This manifest must be verified at the start of every session** (it's the first item under "Do this first" in the Resume Point): list the actual project files, diff against the set below, and report anything missing or extra.

**Reliability note (important):** the `/mnt/project` view Claude reads is a **mirror that can lag or shift** — it has disagreed with the prompt's own file list and changed mid-session before. It is a **cross-check, not ground truth.** The authoritative source is the **file panel in the claude.ai project UI**. Agreement between the two = confirmed; a mismatch = "check the UI." Claude must not assert the project is correct on its own listing alone.

**Expected set — 20 files, nothing else:**
```
# Course materials (11) — stable, rarely change
1_-_GitHub_Actions_The_Big_Picture_-_Index.md
2_-_Authoring_and_Maintaining_GitHub_Actions_Workflows_-__Index.md
3_-_Consuming_GitHub_Actions_Workflows_-_Index.md
4_-Authoring_and_Maintaining_GitHub_Actions_-_Index.md
5_-_Managing_GitHub_Actions_-_Index.md
1__GitHub_Actions_The_Big_Picture.pdf
2__Authoring_and_Maintaining_GitHub_Actions_Workflows.pdf
3__Consuming_GitHub_Actions_Workflows.pdf
4_Authoring_and_Maintaining_GitHub_Actions.pdf
5_Managing_GitHub_Actions.pdf
Study_guide_for_Exam_GH200__GitHub_Actions___Microsoft_Learn__20_June_2026.pdf

# Working docs (3)
GH-200_Coverage_Map.md
GH-200_Study_Protocol_and_Progress.md
GH-200_Practice_Protocol_and_Progress.md          # this file

# Practice banks (4)
gh-200-ghcertified-bank-full-2026-06-24.md        # raw capture
gh-200-ghcertified-verified-full-2026-06-24.md    # verified + enriched
gh-200-tutorialsdojo-sampler-bank-2026-06-24.md   # TD free sampler, raw capture (30 Q)
gh-200-tutorialsdojo-sampler-verified-2026-06-24.md # TD free sampler, verified + enriched

# Combined study material (2) — consolidated 2026-06-24 from the 28 per-topic files
GH-200_Combined_Recaps.md                         # all 14 topic recaps
GH-200_Combined_Cheat_Sheets.md                   # all 14 cheats
```

**Deliberately NOT in the project (flag if any reappear):** the MS Learn practice files (`gh-200-practice-full-questions / -results / -analysis-2026-06-23.md`); the 7 per-block GHCertified verified files (superseded by the consolidated `-verified-full-` file); the retired `gh-200-practice-providers.md`; **the 28 per-topic recap/cheat files** (`GH-200_Topic_*` / `GH-200_Cheat_*`) — consolidated 2026-06-24 into the two combined files and removed from the repo's `Study material/` (which now holds only those two).

**Pending additions:** none outstanding. The two combined study-material files (`GH-200_Combined_Recaps.md`, `GH-200_Combined_Cheat_Sheets.md`) landed 2026-06-24 in project + repo + HD. The TD full 140+ bank is paid and not collected.

---

## ▶ RESUME POINT (start here next session)

**STATUS:** Testing phase active. **GHCertified bank: captured + fully verified (2026-06-24).** All 178 questions checked → **0 wrong keys**; consolidated verdicts/enrichment in `gh-200-ghcertified-verified-full-2026-06-24.md`. The bank is trustworthy and current — **ready to drill, shuffled** (§4.10). No drill attempts logged yet.

**Do this first:**
1. **Verify project contents against the §11 manifest** (the learner asks for this on every restart): list the actual project files, diff against §11, and report missing/extra. Remember the `/mnt/project` view is only a cross-check — confirm against the claude.ai project UI; if they disagree, the UI wins. If files were added/removed, update the §11 manifest in the same session.
2. Read the rest of this protocol to reload state. Recaps/cheats are on the learner's HD + repo — ask the learner to upload any needed for a targeted review.

**⭐ TONIGHT:** Drill the verified GHCertified bank (the main activity → action 1 below), shuffled (§4.10).

**Next decisions / actions:**
1. **Drill the verified GHCertified bank** — pull from `gh-200-ghcertified-verified-full-2026-06-24.md`, **shuffle option order per question** (§4.10) so position carries no signal, and run in batches. Source-answer accuracy is already settled (0 wrong keys); the residual mild-doubt items (Q116, Q174, Q178, Q066) are flagged in that file if a question bites.
2. **Score each batch → triage misses into the four buckets (§4.4)** → log a row in §6 + any (b)/(c) gaps in §7 → route to targeted review. (Misses here are genuine knowledge/recall signal, since the keys are trustworthy.) Fallback bank if more breadth is wanted: Tutorials Dojo (free 30-Q sampler, then ~$10–15 full).
3. **Settle parked flags (§8)** opportunistically as questions surface them.
4. **Re-sync** after each session (project + repo + HD); bump the header timestamp.

*(Filename chosen as `GH-200_Practice_Protocol_and_Progress.md` to mirror the study protocol. Tell me if you'd prefer "Testing" or a different name — easy to rename.)*
