# GH-200 Practice (Testing) Protocol & Progress Tracker

**Last updated: 2026-06-28 20:52 UTC** *(bump this timestamp on every edit — same convention as the study protocol §3.7. Use `date -u`; this value is the real system clock.)*

*This file is the operating agreement and running state for the **testing/practice phase** of GH-200 preparation. It is the companion to `GH-200_Study_Protocol_and_Progress.md`, which is now the historical **teaching-phase** record (Domains 1–5 gap-complete). Paste this into the project so any future session has full context. Claude updates the **Session log (§6)**, **Coverage ledger (§6b)**, and **Miss ledger (§7)** at the end of every session, then re-syncs all three sources (project + repo + HD).*

---

## 0. Key definitions & the no-data-loss rule (read first)

- **Session** — one working sitting, of whatever size the learner has time and energy for (could be 10 questions, could be 50). Variable. **A session is not a unit of scoring** — its raw % is too small-n to read on its own (§5).
- **Pass** — every usable question answered **exactly once**: GHCertified **178** + Tutorials Dojo **29** (excluding off-syllabus TD Q26) = **~207**, accumulated across **as many sessions as it takes**. The pass — not the session — is the unit of scoring and readiness.
- **Gap study** — working the accumulated gap list (§7 miss ledger + §7b gap agenda). Happens **only after a pass completes**, never mid-pass. During a pass we keep drilling and keep *recording* gaps; we don't stop to study them.
- **Pass 2 / next pass** — a fresh full run of all ~207, started **only after** the previous pass's gap study is done.

**▶ NO-DATA-LOSS RULE (non-negotiable, added 2026-06-28):** session state — which Q-IDs have been answered, the misses, the four-bucket triage — lives in **THIS FILE** (§6 session log + §6b coverage ledger + §7 miss ledger), is written **at the end of every session**, and is synced to all three sources (§4.9). **Chat history is NOT a reliable store of progress and must never be relied on to reconstruct it.** *(Learned the hard way: Attempt 1's per-question draw was logged only as misses, and its passed-question IDs could not be recovered from chat history — checked 2026-06-28. The ledger below now prevents a repeat.)*

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
5. **Update this tracker** (Session log §6 + Coverage ledger §6b + Miss ledger §7 + calibration flags §8) at session end, then re-sync (project + repo + HD).
6. **Accuracy rules inherited from study protocol §4** (non-negotiable — learner prioritizes truth over helpfulness): verify current-state against official GitHub docs and cite; never invent action names / inputs / REST endpoints / CLI flags / YAML keys; state uncertainty plainly; flag anything that may have changed since the Jan-2026 cutoff.
7. **Timestamp every edit** — bump the header `Last updated` to current `YYYY-MM-DD HH:MM UTC`.
8. **Formatting (study protocol §3.8):** in chat, small fenced blocks only; anything wide/long → a downloadable `.md` file with real markdown tables.
9. **Three-source sync discipline (study protocol §8):** the project holds the operating set (this protocol, the study protocol, coverage map, source PDFs/indexes, the GHCertified + Tutorials Dojo bank files) **plus the two combined study-material files** (`GH-200_Combined_Recaps.md`, `GH-200_Combined_Cheat_Sheets.md`). **Convention change (2026-06-24):** recaps/cheats were consolidated from 28 per-topic files into these two combined files and now live in **all three** sources (project + repo + HD) — superseding the earlier "recaps/cheats stay on HD + repo, not project / cheats are per-topic not monolithic" rule. Keep repo / project / HD aligned; verify by fresh clone when in doubt.
10. **Quizzing from banks — ALWAYS shuffle option order.** Several banks (confirmed for **GHCertified**, 2026-06-24) list the correct option(s) first, so the answer-position is heavily skewed: ~67% of GHCertified items are a bare `A` and ~89% have `A` among the correct answers. Un-shuffled, the learner could score ~89% by reflexively picking A while testing nothing. **Rule:** whenever Claude quizzes from any captured bank, randomize the option order per question (and within multi-selects) and re-letter, keeping the original key mapped internally. The stored verification files keep the *original* letters (so they stay diffable against the raw bank) — the shuffle happens only at quiz time.
11. **Project-contents manifest (§11) — keep current + verify at every session start.** Whenever a file is added to or removed from the project, update the §11 manifest in the same edit. At the **start of every session** (first read), verify the actual project against §11 and report missing/extra — the learner requests this on every restart. The `/mnt/project` mirror is a cross-check only; the claude.ai project UI is authoritative.
12. **Quiz delivery — ONE QUESTION AT A TIME (critical, learner-mandated 2026-06-24).** Present **exactly one** question, options only (answer + rationale hidden), then **wait**. The learner may answer **or ask a clarifying question first** — never batch multiple questions or rush ahead. Only after the learner commits: reveal the marked answer, give the rationale, and **shuffle still applies (§4.10)**. Alongside each question, Claude **verifies in the background which objective it really maps to** (objective ID + a one-line why) and **records it** so the per-question objective map accumulates over the phase. **Per-question tracking** (so we always know what was asked / passed / failed): keep a running record of source Q-ID, the shuffled→original letter map, the learner's answer, correct/incorrect, the four-bucket triage (§4.4) on any miss, and the mapped objective. Summarize the running tally on request, roll confirmed (b)/(c) gaps into the Miss ledger (§7), and **persist every answered Q-ID to the §6b coverage ledger at session end — never leave it only in chat (§0 no-data-loss rule).**
13. **Draw order within a pass — IN BANK ORDER (added 2026-06-28).** Draw questions **sequentially by source Q-ID** — GHCertified Q001→Q179 (Q157 absent), then Tutorials Dojo Q1→Q30 **skipping Q26** — never random question selection. **Option order is still shuffled per §4.10**; the in-order rule governs *which question*, not *option position*. Sequencing makes the §6b coverage ledger a simple **high-water mark** ("done through Q-N"), so resume across sessions is unambiguous and no question is drawn twice within a pass.
14. **Durable per-question logging — the no-data-loss guarantee (added 2026-06-28).** Every question drawn is recorded in the **§6b coverage ledger** as part of wrapping the session: source Q-ID, pass/fail, four-bucket on any miss, mapped objective. **This file — not the chat transcript — is the system of record (§0).** At session end the ledger is updated and all three sources re-synced (§4.9). If a session is cut short, the ledger still reflects every question committed up to that point, so the next session resumes exactly where this one stopped.
15. **Drill log — the exact shuffled question + answer + grade in a SEPARATE FILE (added 2026-06-28, learner-mandated, NON-NEGOTIABLE).** A dedicated file `gh-200-drill-log.md` records, **per question**, the four things grading needs so it is *mechanical and auditable*, never reconstructed from memory:
    - **(a) the exact shuffled question as presented** — stem + the shuffled, re-lettered options exactly as the learner saw them;
    - **(b) the reference number** — the source Q-ID (e.g. GHCertified Q019);
    - **(c) the answer** — the correct option **in the shuffled frame** (its presented letter) AND its content, plus the shuffled→original letter map;
    - **(d) the grading** — the learner's answer, and ✓/✗ obtained by comparing the learner's letter to the recorded correct letter from (c).
    **Order is mandatory:** the correct option's *shuffled letter* is written to the drill log **at the moment the question is presented** (before the learner answers) — grading then compares letters mechanically. **Claude must never grade by gluing the bank's original answer word onto the learner's letter** (the 2026-06-28 inversion bug: presented `A=regex / B=glob`, learner answered `A`, Claude wrote "correct — A, glob" — fusing original-answer *content* with shuffled *letter*. Banned.). The drill log is synced with the other three sources (§4.9) and is itself the audit trail behind the §6b ledger's pass/fail column.

## 5. Readiness criteria / targets
- **Learner's working target: consistently 77%+ across multiple attempts.**
- **Report both per-session and per-pass scores.** Each session's raw/adjusted score is reported so the learner sees how the sitting went — but **readiness is anchored on the full ~207-question pass** (per-domain breakdown taken across the whole pass), because a single small session's % is noisy (a "50%" on a 4-question sitting is just two misses). Per-session = progress feedback; per-pass = the readiness signal.
- **Honesty note on the target:** practice-bank raw % ≠ the exam's scaled 700/1000. Real readiness signal = passing reworded-objective bank(s) **with no domain consistently below the others** — especially the high-weight Domain 1 and Domain 4 (20–25% each) and the dense Domain 5.
- Stop-condition for "ready": multiple passes comfortably clear of the line, misses are only bucket (a)/(d), and the parked calibration flags (§8) are resolved.

## 6. Session log (current pass)
*(Claude appends a row + a short prose analysis per session. A pass spans many of these; see the high-water mark below and the per-question detail in §6b.)*

**▶ Pass 1 progress:** restarting clean from Q001 in bank order under ID-tracking (§4.13/§6b). **⚠ Attempt-1 caveat (2026-06-28):** A1 (below) drilled ~35 questions but logged only its **misses** (§7), not the full answered-list; its **passed-question IDs are unrecoverable** (chat history checked 2026-06-28, not retrievable). So Pass 1 is counted fresh from this session; up to ~35 A1 questions may resurface once when reached in order — **accepted overlap**, the price of the lost A1 draw. The §6b ledger prevents any repeat of this loss.

| # | Date | Provider | Raw score | By section | Misses | Bucket(s) |
|---|---|---|---|---|---|---|
| 1 | 2026-06-25 | GHCertified (verified bank, shuffled, one-at-a-time) — *passed-IDs unlogged, see caveat above* | **20/35 = 57% raw** · **20/25 = 80% adjusted** | spans D1–D5 | 15 | (b)×9 (c)×5 (d)×1 |
| — | 2026-06-28 | GHCertified Q001–Q020 — **RESULTS VOIDED** (see analysis) | *not counted* | D1 | — | — |

**2026-06-28 session — VOIDED, gaps kept.** Ran GHCertified Q001–Q020 but the session hit three integrity failures: (1) Q003–Q014 were initially **fabricated from memory** instead of pulled from the bank file; (2) redacted-pull receipts twice **leaked the answer** (source-order echo; a `grep` hint that included the answer line); (3) a **grading inversion** on Q019 (presented `A=regex / B=glob`; learner answered `A`; graded "correct — A, glob" by fusing the bank's original-answer *word* to the shuffled *letter*). Because the shuffle→content map was never persisted, the other ✓ grades can't be re-audited either. **Decision (learner): void the entire question log for this session, reset Pass 1 to Q000, and keep only the validated gaps (→ §7).** Fixes added same day: §4.15 drill log (exact shuffled question + Q-ID + answer-in-shuffled-frame + grade, written at presentation time; mechanical letter-vs-letter grading; no memory grading).

**Attempt 1 analysis:** First real GHCertified drill (35 Qs, partial bank, one-at-a-time per §4.12). **Raw 57% but adjusted 80%** once justified misses are set aside. **10 of 15 misses were bucket (b) material gaps + (d) bad wording — i.e. the reworded exam reaching past the course material, not recall failures; only ~5 were genuine (c) retention slips** (and one of those, Q068, exposed a material *error*). Key signal: command of *studied* material is solid (~80%); the raw gap is uncovered breadth, now captured (15 cheat keepers added to the Combined Cheat Sheets + 1 recap correction + the §7b gap agenda). Scoring convention adopted: report **raw AND adjusted** (adjusted excludes (b)+(d)), with the four-bucket breakdown. **Bookkeeping note:** A1 predates the §6b coverage ledger and in-order draw rule (both added 2026-06-28 after its passed-IDs proved unrecoverable); precise ID-tracking begins at Q001 (the next question drawn).



## 6b. Coverage ledger (per-question record — the system of record)
*(Updated every session per §4.12/§4.14. This — not chat history — is how we know what has been answered (§0). In-order draw (§4.13) means the GHCertified line is effectively a high-water mark; the table records the detail. The audit trail behind each pass/fail is the drill log `gh-200-drill-log.md`, §4.15.)*

**▶ Pass 1 high-water mark:** **GHCertified — through Q000** (next question to draw = **Q001**). **TD — 0 / 29.** *(Excluded from the count: A1's ~35 questions — passed-IDs unrecoverable, see §6 caveat; AND the 2026-06-28 session's Q001–Q020 — grades VOIDED for integrity failures, see §6 row. The valid **gaps** from both are preserved in §7; only the question results were reset.)*

**How to read/maintain this:** one row per question actually drawn, appended live during the session and saved at session end. `Result` = ✓ pass / ✗ miss. On a miss, `Bucket` is the §4.4 triage and the item also goes to §7. `Obj` = the objective it really maps to (§4.12 background check). When resuming, the next question = the lowest un-drawn Q-ID in bank order (§4.13).

| Source Q-ID | Result | Bucket | Obj | Session |
|---|---|---|---|---|
| *(none logged yet — Pass 1 ID-tracking begins at Q001)* | | | | |

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

**Gaps preserved from the VOIDED 2026-06-28 session** *(question results were reset, but these surfaced real, valid gaps — content stands regardless of the grading chaos):*
1. **[1.3 reusable wf]** Token perms to a reusable workflow = **downgrade-only** (caller's perms can only be narrowed, never elevated). Three-way contrast to keep straight: *reusable workflow* → caller's perms, downgrade-only · *fork `pull_request`* → read-only token + no secrets by default · *`workflow_run`* → independent workflow, own `permissions:`, privileged base-repo context, decoupled from the trigger.
2. **[1.4 / 1.11 status fns — RECONFIRMS A1·Q100]** A needed job carries an implicit `if: success()`; lifted by **any** status function (`failure()`/`always()`/`cancelled()`), not only `failure()`. If A fails → dependents are **skipped** (skipped ≠ failed), independent jobs keep running, nothing is "cancelled." *Bit twice now → high-value review target.*
3. **[1.1 triggers]** `workflow_dispatch` = **manual** (UI/API run button); `repository_dispatch` = **external** webhook/REST. *Mixed up twice in one session — keep the pair straight.*
4. **[1.1 `pull_request` — RECONFIRMS A1·Q018] VOCAB FIX (root cause):** learner maps "base" → "source"; correct is **base = target = destination = the merge-INTO branch**; head = source = compare = come-FROM. `branches:`/`paths:` on `pull_request` filter the **base/target**. Not a concept gap — a naming inversion to drill.
5. **[calibration → §8]** matrix-over-reusable-workflow **is** a real bank pattern (Q014); the stem's "parallelize entire workflows" wording is loose (no "workflow matrix" keyword — it's `strategy.matrix` on a job whose step is `uses:` a reusable workflow).


## 7b. Gap agenda — accumulates DURING Pass 1; study AFTER Pass 1 completes (before Pass 2)

*Concepts the bank tested that the course material does NOT cover (or got wrong). **Timing (clarified 2026-06-28 — this had been misread): these are studied AFTER Pass 1 COMPLETES, NOT before continuing Pass 1.** This agenda keeps accumulating every session as new gaps surface, all the way through the ~207-question pass; only once the pass is done do we work the list (verify each against `docs.github.com`), and only then run Pass 2. All items have cheat keepers queued in `GH-200_Combined_Cheat_Sheets.md` → 'Drill-Surfaced Keepers — Pass 1'.*

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
| Primary drill bank | ✅ GHCertified captured + **fully verified** (178 Q, 0 wrong keys) — **Pass 1 in progress** (A1 drilled 35 Q on 2026-06-25; per-question draw not recovered, see §6/§6b; restarting clean Q001 in bank order) |
| Parked calibration flags | 🟡 partially informed by GHCertified (matrix cap 256, job timeout 360 min, reusable cap 50 / nesting 10 confirmed; see §8) — concurrency per-plan numbers still open |
| Readiness (§5 stop-condition) | ⬜ not met — Pass 1 underway, no completed pass yet |

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

**Expected set — 21 files, nothing else:**
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

# Working docs (4)
GH-200_Coverage_Map.md
GH-200_Study_Protocol_and_Progress.md
GH-200_Practice_Protocol_and_Progress.md          # this file
gh-200-drill-log.md                                # per-question audit: shuffled Q + Q-ID + answer + grade (§4.15)

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

**STATUS:** Testing phase active — **Pass 1 in progress.** GHCertified bank captured + fully verified (178 Q, 0 wrong keys); TD sampler verified (29 usable, Q26 off-syllabus). **Attempt 1** (35 Q, 2026-06-25) is logged in §6 but its passed-question IDs were unrecoverable from chat history (checked 2026-06-28), so **Pass 1 is restarting clean from Q001 in bank order** with full per-question tracking (§6b). New conventions added 2026-06-28: **session vs pass definitions (§0)**, **no-data-loss rule (§0)**, **in-order draw (§4.13)**, **durable per-question logging (§4.14 → §6b)**.

**Do this first:**
1. **Verify project contents against the §11 manifest** (the learner asks for this on every restart): list the actual project files, diff against §11, and report missing/extra. Remember the `/mnt/project` view is only a cross-check — confirm against the claude.ai project UI; if they disagree, the UI wins. If files were added/removed, update the §11 manifest in the same session.
2. Read the rest of this protocol to reload state — especially **§0 (definitions + no-data-loss rule)** and the **§6b coverage ledger** (the high-water mark = where to resume). Recaps/cheats are in `Study material/` (repo + HD) — ask the learner to upload any needed for a targeted review.

**Next decisions / actions:**
1. **Drill the verified GHCertified bank IN ORDER** — next question = lowest un-drawn Q-ID per the §6b high-water mark (Pass 1 starts at Q001). **Shuffle option order per question (§4.10)**; sequencing is question-order only. **One question at a time (§4.12)** — options shown, answer/rationale hidden until the learner commits. Source-answer accuracy is settled (0 wrong keys); residual mild-doubt items (Q116, Q174, Q178, Q066) are flagged in the verified file if a question bites.
2. **Per question:** record it in §6b *as you go* (Q-ID, ✓/✗, bucket on a miss, mapped objective); roll confirmed (b)/(c) gaps into §7. Report each session's raw **and** adjusted score (§5) — readiness itself is judged on the completed pass, not the session.
3. **At session end (NO-DATA-LOSS — §0):** write §6 (session row) + §6b (every Q-ID drawn) + §7 (new gaps), bump the timestamp, and re-sync project + repo + HD. Never leave progress only in chat.
4. **Gap study is for AFTER Pass 1 completes (§7b)** — keep accumulating gaps during the pass; don't stop to study mid-pass.
5. **Settle parked flags (§8)** opportunistically as questions surface them.

*(Filename `GH-200_Practice_Protocol_and_Progress.md` mirrors the study protocol.)*
