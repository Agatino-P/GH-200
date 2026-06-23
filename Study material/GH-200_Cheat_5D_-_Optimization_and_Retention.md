# GH-200 Cheat — Topic 5D: Optimization & Retention

> Last-week review. Fuller note: `GH-200_Topic_5D_-_Optimization_and_Retention.md`
> 5D = cost/limits/optimization (5.10) + retention/storage (5.9). Final Domain 5 topic.

---

## Cost model (Bit 1)

- **Billed = round-up(minutes) × OS-multiplier.** Round each job **UP to the whole minute** (1s and 59s both = 1 min).
- **OS multiplier: Linux 1× · Windows 2× · macOS 10×.** macOS 10-min job = 100 min. Move to Linux = biggest lever.
- **Public repos + self-hosted runners = FREE** (no billable minutes). 10× only bites on **private** (or larger runners, never free even on public).
- **Larger runners:** higher rate by vCPU; **free while idle**; static IP no extra cost; included free minutes can't be used on them.
- **★ Job limit = 6 hours** (killed if exceeded). Concurrency capped per plan (Free→Enterprise). Matrix cap commonly cited **256**. `schedule:` ≥ 5-min spacing, can be delayed/dropped.

## Optimization levers (Bit 1)

- **★ Parallelization cuts TIME, not billed minutes — can INCREASE them.** Minutes are summed across jobs; split adds per-job setup + per-job round-up. Exam answer: "splitting into a parallel matrix reduces wall-clock, NOT billed minutes, and may raise them."
- **Real minute-savers:** path/branch filters + `if:` (run less); `concurrency` + **`cancel-in-progress: true`** (cheapest win — kills runs superseded by a new push); **`timeout-minutes`** (else hung job runs to the 6h ceiling); right-sizing (bigger ≠ cheaper — 4× rate for 1.67× speed = net loss); **`needs:` fast-fail gate** (cheap lint job gates the expensive job → failure stops the run before costly work = where the dependency graph actually saves minutes).
- **cache vs artifact (1E):** cache = deps/build-accel, **7-day default**, 10 GB LRU; artifact = results, **90-day default**. Don't swap their roles.
- **★ Usage metrics show RAW minutes (NO multiplier applied)** → dashboard number ≠ bill. Metrics = "where minutes go"; billing page/spending limits = actual cost.

## Retention & storage (Bit 2)

- **Defaults: artifact/log = 90 days; cache = 7 days.** *Understand why* (cache = disposable/churns fast + size-capped LRU; artifact = retrievable results). Don't memorize in isolation.
- **Range: artifacts 1–400 days** (private/internal/Enterprise); **public capped at 90**. Cache: public ≤ 90, private/internal ≤ 365.
- **★ Period change is NOT retroactive** — applies to NEW objects only; old artifacts keep their original lifespan (by design, not a bug). To reclaim now → delete explicitly.
- Per-artifact override: `retention-days:` in `upload-artifact` (capped by repo/org max); `compression-level: 0–9`.
- **★ Programmatic retention — precise meaning:** = per-artifact `retention-days` (declarative) + programmatic **deletion** via REST/`gh`. There is **NO confirmed REST endpoint to SET the retention period** (`PUT .../actions/retention` unverified/likely not official). REST does **get / list / delete** only.
  - `DELETE /repos/{owner}/{repo}/actions/artifacts/{artifact_id}` (+ `GET` to list); `DELETE .../actions/runs/{run_id}`; `gh cache delete`.
- **★ Quota recalculation lags** (commonly 6–24h). A "storage quota exceeded" error persists *after* a successful delete — deletion didn't fail; just wait + lower retention going forward.
