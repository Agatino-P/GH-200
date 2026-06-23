# GH-200 Practice (Testing) Protocol & Progress Tracker

**Last updated: 2026-06-23 21:21 UTC** *(bump this timestamp on every edit — same convention as the study protocol §3.7)*

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
- **Practice question sources / providers → §10 (in this file).** *(Absorbed from the former standalone `gh-200-practice-providers.md`, which is now retired — this protocol is the single source of truth for providers.)*
- The **free official Microsoft Learn practice assessment** is the anchor. **Caveat (see §7):** in the June 23 run it tested *foundational* material and did **not** touch the hard reworded objectives studied (OIDC, attestations, runner networking, enforcement). It is **necessary-not-sufficient** — supplement with banks that reflect the Jan-2026 reworded objectives.
- Study-phase **recaps + per-topic cheats** (on the learner's HD + repo `Agatino-P/gh-200` → `Study material/`) — the remediation source whenever a miss maps to a studied topic. Ask the learner to upload the relevant one when needed.
- `GH-200_Coverage_Map.md` and `GH-200_Study_Protocol_and_Progress.md` — objective list + teaching-phase record (for cross-referencing a miss back to where it was taught).

## 4. Testing protocol (how we run the phase)
1. **Anchor on the free official MS Learn assessment; supplement** from the provider list (the unofficial banks — Tutorials Dojo, GHCertified, SkillCertPro, ITExams — better reflect the reworded enterprise/security objectives, but accuracy is not guaranteed; treat their "correct" answers skeptically and verify against `docs.github.com`).
2. **Per attempt, capture two files** (naming convention already in use):
   - `gh-200-practice-full-questions-YYYY-MM-DD.md` — every question **with all options** (the distractors are the learning surface; the results page often hides them — re-open the assessment to capture them).
   - `gh-200-practice-results-YYYY-MM-DD.md` — score, per-section breakdown, per-question answer summary + rationale.
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
9. **Three-source sync discipline (study protocol §8):** the project holds only the operating set (this protocol, the study protocol, coverage map, source PDFs/indexes, and the per-attempt practice files). The provider list now lives **in this protocol (§10)** — the standalone `gh-200-practice-providers.md` is retired and can be deleted from the project. Recaps/cheats stay on HD + repo. Keep repo / project / HD aligned; verify by fresh clone when in doubt.

## 5. Readiness criteria / targets
- **Learner's working target: consistently 77%+ across multiple attempts** (set in the June 23 results file).
- **Honesty note on the target:** practice-bank raw % ≠ the exam's scaled 700/1000, and the official practice assessment under-represents the hard objectives (§7). So a high anchor-assessment score is **necessary, not sufficient**. Real readiness signal = passing the official practice **and** at least one reworded-objective bank, **with no domain consistently below the others** — especially the high-weight Domain 1 and Domain 4 (20–25% each) and the dense Domain 5.
- Stop-condition for "ready": multiple attempts comfortably clear of the line, misses are only bucket (a)/(d), and the parked calibration flags (§8) are resolved.

## 6. Attempt log
*(Claude appends a row + a short prose analysis per attempt.)*

| # | Date | Provider | Raw score | By section (as reported) | Misses | Bucket(s) |
|---|---|---|---|---|---|---|
| 1 | 2026-06-23 | MS Learn official practice assessment | 27/30 (90%) | S1 94% · S2 100% · S3 86% · S4 50% | Q8, Q22, Q30 | **all (d)** — off-syllabus ×2, outdated ×1 (see analysis file) |

**Attempt 1 analysis (logged retroactively — predates this protocol; capture files in the project; full per-question mapping in `gh-200-practice-analysis-2026-06-23.md`):**
- 13-minute completion; banner said "passed all sections" which sits **oddly** against the reported 50% on Section 4 — noted in the source file, treated as a display quirk.
- **Full 30-question → objective mapping done (analysis file).** Result: ~20 questions map to current objectives but only at the **foundational layer**; 3 are quirky/overview; 2 are background-familiarity only; **3 are off-syllabus**; 2 are outdated/arguably-wrong by current objectives. **None of the deep Domain 4/5 material studied (OIDC, attestations, runner networking, REST API, matrix depth, anchors, step summaries) was tested.**
- **All three misses are off-syllabus or outdated — NOT core-objective failures:**
  - **Q8** — "grant repo access to Azure" → assessment wants **GitHub Secrets**; the option picked ("authenticate to Azure with GitHub") reads like the **OIDC** model studied in 5B. The question predates/ignores OIDC → **bucket (d) outdated**. (Wording is also genuinely clumsy.)
  - **Q22** — **GitHub Script** (`actions/github-script`) is a real action but **not a GH-200 objective** → **bucket (d) off-syllabus**.
  - **Q30** — **GHAS** is a separate product with its own cert (GH-500), **not a GH-200 objective** → **bucket (d) off-syllabus**.
- ⚠ **Q14** ("Actions can't upload a secret") was scored correct but **conflicts with the secrets REST API (4.8)** studied — don't internalize the bank's framing.
- **Key calibration finding:** this 30-item assessment is markedly **easier, more foundational, and partly dated** vs the Jan-2026 reworded exam. **Zero targeted review owed** from this attempt. **Do not read 90% here as exam-ready.** Next attempts must use banks that exercise the reworded objectives.

## 7. Miss ledger (running gap feedback → review)
*(Confirmed weak spots harvested from attempts, with the bucket and the review action. Bucket (a)/(d) items are recorded for awareness but don't drive review.)*

| From | Item | Bucket | Maps to | Action |
|---|---|---|---|---|
| Attempt 1 | Q8 — repo→Azure access "via GitHub Secrets" vs OIDC | **(d)** outdated | 5B (OIDC) | None owed — dated question; know the bank's answer, keep OIDC as the real best practice |
| Attempt 1 | Q22 — GitHub Script = `actions/github-script` action, not a language | **(d)** off-syllabus | — (not an objective) | None owed — off-syllabus |
| Attempt 1 | Q30 — GHAS = application-security suite (GH-500 territory) | **(d)** off-syllabus | — (not an objective) | None owed — off-syllabus |

*Net from Attempt 1: **zero (b)/(c) items → no targeted review owed.** All misses were (d).*

**Standing watch-items (not yet triggered by a miss, but where the studied material is most likely to be tested by harder banks):** Domain 4 (highest weight; runner networking / images / variables / REST) and Domain 5 (OIDC, attestations, enforcement, optimization). Watch their per-section scores closely once a reworded-objective bank is run.

## 8. Parked calibration flags (carried from the teaching phase — resolve against real practice questions)
*(Confirm or refute each as it surfaces in a bank; update the relevant cheat/recap if a question settles it.)*
1. **`fromJSON` dynamic-matrix exam weight** — open since Topic 1C; gauge frequency.
2. **Immutable-action *publishing* GA status** (3A/5C) — README "not for public use" vs a GA-labeled roadmap card.
3. **SLSA baseline level + exact per-level wording** (5C) — stated unverified.
4. **Exact per-plan concurrency numbers + matrix-combination cap** (5D) — secondary-sourced.
5. **"No REST endpoint to *set* the retention period" conclusion** (5D/1E) — revisit if a question contradicts it.
6. **Exact item count / type mix of the reworded exam** (new this phase) — Microsoft doesn't publish it; refine from booking page + bank structure.

## 9. Progress tracker

| Item | Status |
|---|---|
| Teaching phase (Domains 1–5) | ✅ complete (see study protocol) |
| This practice protocol | ✅ created 2026-06-23 20:36 UTC |
| Attempt 1 — MS Learn official practice | ✅ logged (27/30, 90%) — foundational, under-tests gap areas |
| Attempt 1 — full question-vs-objective analysis | ✅ done — `gh-200-practice-analysis-2026-06-23.md`; all 3 misses bucket (d), zero review owed |
| Reworded-objective bank (Domain 4/5 depth) | ⬜ not yet run |
| Parked calibration flags | ⬜ open (6 items, §8) |
| Readiness (§5 stop-condition) | ⬜ not met — one easy attempt only |

---

## 10. Practice question sources (providers) — single source of truth
*(Absorbed 2026-06-23 from the retired standalone `gh-200-practice-providers.md`. **All costs, counts, and freshness lines are the providers' own self-descriptions — approximate; verify on the provider page before buying.** Unofficial banks get current-state details wrong → always verify any "correct" answer against `docs.github.com` (Attempt 1 showed even the official one can be dated). Verified live where noted.)*

| Provider | Cost | Volume | Official? | Freshness (their claim) | Notes |
|---|---|---|---|---|---|
| **[Microsoft Learn practice assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/gh-200)** | Free | 30 | ✅ official | aligned to current study guide | The anchor. **But Attempt 1 showed it's foundational + partly dated** — under-tests the reworded Domain 4/5 depth. Necessary-not-sufficient. |
| **[GHCertified](https://ghcertified.com/en/practice-tests/actions)** | Free | 178 | ❌ community | — | **Recommended next** — free first probe of reworded-objective depth. |
| **[Tutorials Dojo](https://portal.tutorialsdojo.com/courses/gh-200-github-actions-practice-exams/)** | ~$10–15 (sales common) | 140+ full; **free 30-Q sampler** | ❌ unofficial | "continuously refined / aligned with official objectives" + 1-yr updates — **general claim, no dated post-Jan-2026 guarantee** (verified live 2026-06-23) | Detailed explanations + official doc links; 4 modes + flashcards. [Free sampler](https://portal.tutorialsdojo.com/product/free-gh-200-github-actions-practice-exams-sampler/) = low-risk quality probe before paying. |
| **[MeasureUp](https://www.measureup.com/microsoft-gh-200-github-actions-practice-test.html)** | $99 | — | ✅ official simulator | — | Timed Certification + Practice modes; priciest. |
| **[SkillCertPro](https://skillcertpro.com/product/github-actions-certification-exam-questions/)** | ~$20 | 540 / 9 mocks | ❌ unofficial | claims "weekly updates / 2026 latest" | Bug-bounty accuracy claims; verify answers. |
| **[ITExams](https://www.itexams.com/info/GH-200)** | Free | 110 user-submitted | ❌ unofficial (dumps) | none | **Most skepticism** — user-submitted, accuracy not guaranteed. |

**Also seen in searches (unvetted, not curated in):** Udemy GH-200 banks (one claims 240 Q "regularly updated," another 6 exams / 390 Q); certificationpractice.com (free, self-described "reviewed up to date June 2026"). Capture here only if a future attempt uses one.

**Exam logistics corroboration (Tutorials Dojo + others, 2026-06-23):** 100 min · ~65 questions (approximate, not officially published) · 700/1000 scaled pass mark — consistent with §2.

---

## ▶ RESUME POINT (start here next session)

**STATUS:** Testing phase initialized. **One attempt logged + fully analyzed** — MS Learn official practice, **27/30 (90%)**, June 23. Foundational and partly dated; did **not** exercise the studied gap areas. Full mapping in `gh-200-practice-analysis-2026-06-23.md`; **all 3 misses bucket (d) (off-syllabus/outdated), zero review owed.** Necessary-not-sufficient.

**Do this first:** read this protocol to reload state. Recaps/cheats are on the learner's HD + repo — ask the learner to upload any needed for a targeted review.

**Next decisions / actions:**
1. **Next bank = GHCertified (free, 178 Q)** — decided by learner 2026-06-23 as the first reworded-objective probe (Domain 4/5 depth). Provider details in **§10**. Fallback if it's thin/low-quality: Tutorials Dojo (free 30-Q sampler first, then ~$10–15 full). **Verify "correct" answers against `docs.github.com` before trusting them.**
2. **Run → capture both files** (`full-questions` + `results`, dated) → **triage misses into the four buckets (§4.4)** → log in §6/§7 → route (b)/(c) to targeted review.
3. **Settle parked flags (§8)** opportunistically as questions surface them.
4. **Re-sync** after each session (project + repo + HD); bump the header timestamp.

*(Filename chosen as `GH-200_Practice_Protocol_and_Progress.md` to mirror the study protocol. Tell me if you'd prefer "Testing" or a different name — easy to rename.)*
