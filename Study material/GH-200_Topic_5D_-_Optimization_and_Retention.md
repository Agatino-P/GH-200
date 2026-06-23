# GH-200 — Topic 5D: Optimizing Workflows & Managing Retention

**Domain 5 (Secure & Optimize). Objectives: 5.10 (scaling/optimization strategies) + 5.9 (programmatic retention).**
Verified live against `docs.github.com` (incl. Enterprise Cloud) and GitHub billing/limits reference, session 2026-06-23. Final gap topic of Domain 5.

> Companion cheat file: `GH-200_Cheat_5D_-_Optimization_and_Retention.md`

---

## Bit 1 — The cost & limits model and how to optimize against it

The objective is "recommend strategies" — conceptual. But you recommend against a model: *what you pay for* and *what constrains you*.

### What you pay for

| Factor | Detail |
|---|---|
| Billable minutes | Only for **GitHub-hosted runners on private repos**. **Public repos and self-hosted runners are free** (no billable minutes). |
| ★ Rounding | Each job rounded **up to the nearest whole minute**. 1s and 59s both bill as 1 min — hurts with many tiny jobs. |
| ★ OS multiplier | **Linux 1× · Windows 2× · macOS 10×.** A 10-min macOS job consumes 100 minutes. Moving to Linux is the biggest single lever. Formula: **billed = round-up(minutes) × OS-multiplier.** |
| Larger runners | Higher per-minute rate scaling with vCPU; **no charge while idle**; static IP adds no cost; included free minutes **can't** be used on them; **not free even for public repos**. |
| Storage | Artifacts + Packages storage billed separately from minutes. |

### What constrains you

| Limit | Value |
|---|---|
| ★ Job execution time | **6 hours max per job** — killed if exceeded. |
| Concurrency | Capped per plan (Free lowest → Enterprise highest; larger-runner + macOS caps separate). Support can raise on request. |
| Matrix size | A single matrix capped at a max number of job combinations (commonly cited 256). |
| Schedule | `schedule:` no more often than every 5 min; can be delayed/dropped under load. |

⚠ **Confidence split:** the 6-hour limit, OS multipliers, round-up rule, and public/self-hosted=free are confirmed in GitHub docs. Exact per-plan concurrency numbers and the matrix-combination cap are from secondary sources — know they *exist* and scale by plan; verify the figures on a practice exam.

### Optimization levers — and the critical speed-vs-cost distinction

**★ Parallelization optimizes TIME, not billed minutes — and can increase them.** Billed minutes are *summed across jobs*. 18 min of work as one job = 18 billed min / 18 min wall-clock; split into 3 parallel jobs of 6 min = still 18 billed min but ~6 min wall-clock. Add per-job setup (re-checkout, re-install) + per-job round-up and the split often bills *more*. Parallelism buys latency/throughput, not a cheaper bill.

The genuine **cost** levers:

1. **Run less.** Path filters (skip doc-only changes), branch filters, `if:` conditions.
```
on:
  push:
    paths: ['src/**', 'package.json']
    paths-ignore: ['**/*.md', 'docs/**']   # use ONE of paths/paths-ignore per event
```
2. **Stop wasted in-flight work — the two cheapest wins.**
```
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true      # cancel a run superseded by a new push
```
```
jobs:
  build:
    timeout-minutes: 15          # without it, a hung job runs to the 6h ceiling
```
3. **Cache & reuse.** `actions/cache` keyed on lockfile hash + `restore-keys`; Docker layer cache (`type=gha`); reusable workflows / composite actions. **1E distinction: cache = deps/build-acceleration (7-day default, 10 GB LRU); artifact = results you keep (90-day default).** Different features.
4. **Right-size — bigger isn't automatically cheaper.** 8-core finishing a 20-min build in 12 min = ~4× rate for ~1.67× speed = net more expensive. Pick the knee of the curve; prefer Linux over 2×/10× platforms.
5. **`needs:` as a fast-fail gate (this is where the dependency graph saves *minutes*).** Put cheap checks (lint/unit) in a job the expensive job `needs:`; a failure kills the run before the costly job starts. This is "run less" wearing a dependency-graph costume — *this* saves minutes, not parallelism per se.
6. **Trim storage** (Bit 2): lower `retention-days`, upload only what's needed, compress.

### Measuring

Org Actions usage metrics show where minutes go. ★ **Keeper trap: usage metrics do NOT apply minute multipliers** — they show *raw* minutes, so a macOS/Windows-heavy org's metric ≠ its bill. Purpose = "where are minutes spent," not "what's the invoice." Use the billing page + spending limits for actual cost.

---

## Bit 2 — Retention & storage management (5.9)

Storage is the other paid axis. Two distinct controls people conflate: the retention **period** (default lifespan for *new* objects) vs **deletion** (removing existing objects). Different mechanisms.

### The retention period (a setting, not really an API)

| | Artifacts & logs | Caches |
|---|---|---|
| Default | **90 days** | **7 days** |
| Range | **1–400 days** (private/internal/Enterprise); **public capped at 90** | public ≤ 90; private/internal ≤ 365 |
| Set where | Ent/org/repo → Settings → Actions → General → "Artifact and log retention" | same settings area |
| ★ Retroactive? | **No** — applies only to *new* objects, never existing ones | same |
| Hierarchy | Lower level can't exceed the cap set above it | same |

★ **Why the defaults differ (the understanding, not the numbers):** cache is disposable build-acceleration that should churn fast → short 7-day clock + size cap (10 GB default, up to 10,000 GB) with **LRU eviction** when exceeded. Artifacts are results you may retrieve later → long 90-day clock.

Per-artifact override at authoring time (capped by the repo/org max):
```
- uses: actions/upload-artifact@v4
  with:
    name: build-output
    path: dist/
    retention-days: 7         # overrides the 90-day default for this artifact
    compression-level: 6      # 0 (none) – 9 (max); artifacts compressed by default
```

### Programmatic management — what's actually real (resolves parked 5.9)

**Programmatic DELETION — verified, official:**
```
DELETE /repos/{owner}/{repo}/actions/artifacts/{artifact_id}   # delete one artifact
GET    /repos/{owner}/{repo}/actions/artifacts                 # list to find IDs
DELETE /repos/{owner}/{repo}/actions/runs/{run_id}             # delete a workflow run
```
Often scripted via `actions/github-script` (`github.rest.actions.listArtifactsForRepo` + `deleteArtifact`) or `gh api`. Caches: `gh cache list` / `gh cache delete <id>`.

**⚠ Setting the retention PERIOD via REST — NOT confirmed official.** No documented REST endpoint sets the retention-days value; a `PUT .../actions/retention`-style endpoint is unverified/likely not official (resolves the flag carried since 1E). Setting the period is a **settings/UI** operation + the per-artifact `retention-days` in YAML.

**★ Precise, exam-safe framing of "programmatic retention":**
> = (a) declarative per-artifact `retention-days` in `upload-artifact`, plus (b) programmatic *deletion* via the REST artifacts API / `gh`. It does **not** mean an API that sets the account-wide retention period — that's a setting. Verified path is **list + DELETE**; treat "set the period via REST" as not-confirmed.

### Operational gotcha

After deleting artifacts/caches, the **storage-quota figure lags** — recalculation can take several hours (commonly 6–24h). A "storage quota exceeded" error does **not** clear instantly after a successful cleanup. Recognize this so you don't assume deletion failed; wait for recalculation and set lower retention going forward.

---

## Quiz outcomes (this session)

**Bit 1 — 5/5** (one item was a typo, not a miss). Solid on: round-up × OS-multiplier (macOS 10×); public-repo standard runners are free regardless of OS; **parallelism cuts wall-clock, not billed minutes** (and can raise them via setup + rounding) — the real minute-saver is **fast-fail `needs:` gating**; `cancel-in-progress` as the cheapest, zero-risk win; usage metrics show **raw** minutes (no multiplier) so dashboard ≠ bill.

**Bit 2 — 5/5** (on substance). Solid on: 90-day artifact vs 7-day cache defaults + override behavior; retention-period change is **not retroactive** (by design, not a bug); **no REST endpoint sets the retention period** — REST does get/list/delete only; cache over size cap → **LRU eviction**; post-deletion **quota recalculation lag** explains a persisting quota error (deletion didn't fail).

**Learner-driven calibration:** quiz format moving to contrasts/scenarios, not recall drills (raw-number recitation has no value for a recognition exam — understand *why* cache=7/artifact=90, don't memorize in isolation).

**Status: Topic 5D complete → Domain 5 gap-complete → Domains 1–5 all done.** Next phase = practice exams (+ settle the long-parked `fromJSON` dynamic-matrix exam-weight question there). A new testing-phase protocol will govern from the next session.
