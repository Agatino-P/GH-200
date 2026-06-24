# GH-200 Practice (Testing) Protocol & Progress Tracker

**Last updated: 2026-06-24 16:37 UTC** *(bump this timestamp on every edit — same convention as the study protocol §3.7. Use `date -u`; this value is the real system clock.)*

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
- Study-phase **recaps + per-topic cheats** (on the learner's HD + repo `Agatino-P/gh-200` → `Study material/`) — the remediation source whenever a miss maps to a studied topic. Ask the learner to upload the relevant one when needed.
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
9. **Three-source sync discipline (study protocol §8):** the project holds only the operating set (this protocol, the study protocol, coverage map, source PDFs/indexes, and the GHCertified raw + verified bank files). Recaps/cheats stay on HD + repo. Keep repo / project / HD aligned; verify by fresh clone when in doubt.
10. **Quizzing from banks — ALWAYS shuffle option order.** Several banks (confirmed for **GHCertified**, 2026-06-24) list the correct option(s) first, so the answer-position is heavily skewed: ~67% of GHCertified items are a bare `A` and ~89% have `A` among the correct answers. Un-shuffled, the learner could score ~89% by reflexively picking A while testing nothing. **Rule:** whenever Claude quizzes from any captured bank, randomize the option order per question (and within multi-selects) and re-letter, keeping the original key mapped internally. The stored verification files keep the *original* letters (so they stay diffable against the raw bank) — the shuffle happens only at quiz time.
11. **Project-contents manifest (§11) — keep current + verify at every session start.** Whenever a file is added to or removed from the project, update the §11 manifest in the same edit. At the **start of every session** (first read), verify the actual project against §11 and report missing/extra — the learner requests this on every restart. The `/mnt/project` mirror is a cross-check only; the claude.ai project UI is authoritative.

## 5. Readiness criteria / targets
- **Learner's working target: consistently 77%+ across multiple attempts.**
- **Honesty note on the target:** practice-bank raw % ≠ the exam's scaled 700/1000. Real readiness signal = passing reworded-objective bank(s) **with no domain consistently below the others** — especially the high-weight Domain 1 and Domain 4 (20–25% each) and the dense Domain 5.
- Stop-condition for "ready": multiple attempts comfortably clear of the line, misses are only bucket (a)/(d), and the parked calibration flags (§8) are resolved.

## 6. Attempt log
*(Claude appends a row + a short prose analysis per attempt.)*

| # | Date | Provider | Raw score | By section | Misses | Bucket(s) |
|---|---|---|---|---|---|---|
| — | — | — | *(no attempts logged yet — first will be a GHCertified drill batch)* | — | — | — |



## 7. Miss ledger (running gap feedback → review)
*(Confirmed weak spots harvested from attempts, with the bucket and the review action. Bucket (a)/(d) items are recorded for awareness but don't drive review.)*

| From | Item | Bucket | Maps to | Action |
|---|---|---|---|---|
| — | *(empty — no (b)/(c) gaps logged yet)* | — | — | — |

**Standing watch-items (not yet triggered by a miss, but where the studied material is most likely to be tested by harder banks):** Domain 4 (highest weight; runner networking / images / variables / REST) and Domain 5 (OIDC, attestations, enforcement, optimization). Watch their per-section scores closely as GHCertified drill batches are run.

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

**Expected set — 18 files, nothing else:**
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
```

**Deliberately NOT in the project (flag if any reappear):** the MS Learn practice files (`gh-200-practice-full-questions / -results / -analysis-2026-06-23.md`); the 7 per-block GHCertified verified files (superseded by the consolidated `-verified-full-` file); the retired `gh-200-practice-providers.md`.

**Pending additions:** none outstanding. The Tutorials Dojo sampler landed 2026-06-24 (its 2 files are in the set above); the TD full 140+ bank is paid and not collected.

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
