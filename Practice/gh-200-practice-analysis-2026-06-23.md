# Practice Assessment Analysis — June 23, 2026 (MS Learn, 27/30)
**Question-by-question mapping against the current (Jan-2026) GH-200 objectives, plus a deep-dive on the 3 misses.**

> Companion to `gh-200-practice-full-questions-2026-06-23.md` and `gh-200-practice-results-2026-06-23.md`.
> Objective IDs (1.1–5.10) are from `GH-200_Coverage_Map.md`, which is built from the official study guide.

---

## ★ Headline findings (read first)

1. **All 3 misses were off-syllabus or outdated — not core-objective failures.** Q22 (GitHub Script) and Q30 (GHAS) test topics that are **not in the GH-200 objective list at all**; Q8 (Azure access) is an **old secret-based framing that ignores OIDC** — the modern, studied approach.
2. **Even the ~20 "on-syllabus" questions test only the foundational layer.** None exercised the depth the study guide implies — no OIDC, no artifact attestations, no runner networking, no REST-API management, no matrix include/exclude/fail-fast, no YAML anchors, no `GITHUB_STEP_SUMMARY`. The deep Domain 4/5 material you studied **was not tested here**.
3. **So 27/30 neither validates nor threatens your readiness on the reworded exam.** It's an easy, foundational, partly-dated assessment. Your "surprise" reaction was correct — those surprises were the assessment drifting off-syllabus, not a hole in your prep.

**Verdict legend:** ✅ on-syllabus (objective) · 🟡 on-syllabus but foundational-only / quirky framing · 🔵 background-familiarity only (not a measured objective) · ❌ off-syllabus (not an objective) · ⚠️ outdated / arguably wrong by current objectives

---

## 30-question mapping

| Q | Topic | Maps to | Verdict | Your result |
|---|---|---|---|---|
| 1 | `if: contains(... labels ...)` purpose | 1.4 + 1.10/1.11 (if + contexts + expressions) | ✅ legit (modest depth) | ✓ |
| 2 | What can NOT trigger a workflow | 1.1 (events) | ✅ foundational | ✓ |
| 3 | "What can trigger an Azure deploy workflow" → any event | 1.1 | 🟡 quirky Azure framing; point = any event triggers | ✓ |
| 4 | Trigger on push (`on: push`) | 1.1 | ✅ foundational | ✓ |
| 5 | `echo "::error::…"` workflow command | 1.6 (workflow commands) | ✅ foundational *(question says "debug" but answer is an error command — sloppy wording)* | ✓ |
| 6 | What is a step | 1.4 | ✅ foundational | ✓ |
| 7 | What the `jobs` section is for | 1.4 | ✅ foundational | ✓ |
| 8 | Grant repo access to Azure → GitHub Secrets | 5.4/5.5 (auth) | ⚠️ **outdated** — ignores OIDC (see deep-dive) | ✗ **MISS** |
| 9 | Keep Azure creds out of plain text → Secrets | 4.7 (secrets) | ✅ foundational | ✓ |
| 10 | What is Dependabot | — | 🔵 not a measured objective (dependency tooling, tangential) | ✓ |
| 11 | What Secrets do NOT protect → log output | 1.11 (secret-leakage) | ✅ legit | ✓ |
| 12 | How `env` works | 1.6 (env vars) | ✅ foundational | ✓ |
| 13 | What Actions is used for → all of these | — (C1 overview) | 🟡 intro-level; no specific objective | ✓ |
| 14 | What Actions can NOT do → "upload a new secret" | 4.8 (secrets REST API) | ⚠️ **borderline-wrong** — with the secrets REST API a workflow *can* create secrets (see note) | ✓ |
| 15 | Reference a reusable workflow → `uses` | 1.3 / 2.7 | ✅ foundational | ✓ |
| 16 | Create a workflow → YAML in `.github/workflows/` | structure | ✅ foundational | ✓ |
| 17 | What matrix allows → parallel across configs | 1.8 (matrix) | ✅ **foundational only** — no include/exclude/fail-fast/max-parallel | ✓ |
| 18 | Purpose of caching → reduce run time | 1.16 / 5.9 | ✅ foundational | ✓ |
| 19 | Save artifacts → `actions/upload-artifact` | 1.13 / 2.6 | ✅ foundational | ✓ |
| 20 | Access repo code → `actions/checkout` | structure | ✅ foundational | ✓ |
| 21 | What GitHub Packages is for | — | 🔵 background-familiarity (study guide lists Packages as assumed background, not a skill) | ✓ |
| 22 | What is GitHub Script | — | ❌ **off-syllabus** — `actions/github-script` is not a GH-200 objective (see deep-dive) | ✗ **MISS** |
| 23 | GitHub Script vs GitHub Actions | — | ❌ off-syllabus (GitHub Script again) | ✓ |
| 24 | Custom action in Ruby → Docker container action | 3.2 (action types) | ✅ legit | ✓ |
| 25 | Three action types | 3.2 | ✅ legit | ✓ |
| 26 | Required `action.yml` keys → name/runs/description | 3.1 / 3.4 | ✅ legit | ✓ |
| 27 | Essential file for an action → `action.yml` | 3.1 / 3.4 | ✅ foundational | ✓ |
| 28 | NOT an Actions feature → repository metrics | — | 🟡 general; no specific objective | ✓ |
| 29 | Self-hosted vs GitHub-hosted runner | 4.3 (runners) | ✅ foundational | ✓ |
| 30 | What is GHAS | — | ❌ **off-syllabus** — GHAS is a separate product / GH-500 cert (see deep-dive) | ✗ **MISS** |

**Tally:** ✅ on-syllabus 20 · 🟡 quirky/overview 3 · 🔵 background-only 2 · ❌ off-syllabus 3 · ⚠️ outdated/borderline 2 (= 30; misses fall in the ❌/⚠️ rows).

---

## The 3 misses — what went wrong (and whether it matters)

### Q8 — "How do you grant your repo access to Azure?" → **GitHub Secrets** (you picked "Authenticate to Azure with GitHub")
- **Why the assessment marks Secrets correct:** the basic model stores an Azure service-principal credential as a GitHub Secret, which `azure/login` then reads. The option you chose is vague and isn't a concrete mechanism, so the assessment rejects it.
- **Why this is an outdated question:** the current best practice — and exactly what you studied in **5B** — is **OIDC federation**: GitHub mints a short-lived token, Azure trusts it via a federated credential, and **no secret is stored at all**. The assessment's "correct" answer is the older secret-based approach and doesn't offer OIDC as an option.
- **Likely cause for you:** "authenticate to Azure with GitHub" reads like the OIDC mental model (GitHub authenticating to Azure), so you may have reasoned *toward* the modern approach and got dinged by a dated question. That's the opposite of a knowledge gap.
- **Takeaway:** for this dated assessment, recognize the Secrets answer; for the reworded exam and reality, OIDC (5B) is preferred. **Bucket (d)** — outdated question, no review needed.

### Q22 — "What is GitHub Script?" → the **`actions/github-script` action** (you picked "a programming language that compiles to JavaScript")
- **Correct meaning:** GitHub Script is an **action** (`actions/github-script`) that lets you run JavaScript inside a workflow step with the GitHub API pre-wired (the script has `github`, `context`, and `core` available). The option you picked describes something like TypeScript, not this.
- **Why it doesn't matter for GH-200:** `actions/github-script` is a real, popular action but is **not in the objective list** — it's not a measured skill. Missing it reflects nothing about your exam readiness.
- **Takeaway:** optional to learn; genuinely off-syllabus. **Bucket (d)** — irrelevant to objectives.

### Q30 — "What is GitHub Advanced Security (GHAS)?" → a **broad application-security solution** (you picked "a tool for analyzing source code for vulnerabilities")
- **Correct meaning:** GHAS is a **product suite** (code scanning, secret scanning, dependency review, etc.). Your answer described just **code scanning** — one component, not the whole.
- **Why it doesn't matter for GH-200:** GHAS is its own product with its own certification (**GH-500**). It is **not a GH-200 objective**.
- **Takeaway:** off-syllabus. **Bucket (d)** — different exam's territory.

---

## Note on Q14 (got it "right," but the question is shaky)
The assessment says Actions "cannot upload a new secret to GitHub Secrets." By the current objectives that's **arguably wrong**: the **secrets REST API** (objective **4.8**, which you studied) lets a workflow create/update secrets programmatically (fetch the repo public key → libsodium sealed box → `PUT`). The assessment treats secret *creation* as out-of-scope for Actions, which reflects an older, narrower view. Don't internalize the assessment's framing here.

---

## Bottom line
- **Misses:** 3, all **bucket (d)** (off-syllabus ×2, outdated ×1). **Zero** map to a current objective → no targeted review owed from this attempt.
- **Coverage gap of the assessment itself:** it tested the foundational slice of Domains 1–3 and basic runners/secrets; it did **not** test the reworded Domain 4/5 depth (OIDC, attestations, enforcement, runner networking, REST API, optimization/retention, matrix depth, anchors, step summaries).
- **Action:** treat this attempt as a warm-up only. Next, run a bank that actually exercises the reworded objectives (GHCertified free, or Tutorials Dojo), verifying its "correct" answers against `docs.github.com`.

### Miss-ledger reclassification (for the practice protocol §7)
| Item | Old bucket | New bucket (after analysis) |
|---|---|---|
| Q8 — Azure access via Secrets vs OIDC | (b)/(d) | **(d)** outdated question |
| Q22 — GitHub Script | (b) | **(d)** off-syllabus |
| Q30 — GHAS scope | (b) | **(d)** off-syllabus |
