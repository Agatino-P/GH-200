# GH-200 Cheat — Topic 1C: Matrix Strategy In Depth

*Trap-grade keepers only. Full explanation in the matching recap: `GH-200_Topic_1C_-_Matrix_Strategy_In_Depth.md`.*

### Where keys live ⚠️ (don't confuse levels)
- `matrix` / `fail-fast` / `max-parallel` → **only under `strategy:`**.
- `continue-on-error` → on a **JOB** or a **STEP** (NOT under `strategy:`).
- `runs-on` / `needs` → **JOB** level.

### Resolution order
- **EXPAND → EXCLUDE → INCLUDE.** `include` runs **last** and can **re-add** an excluded combo. (A common blog states this backwards — it's wrong.)
- `exclude`/`include` entries **don't accept arrays** — one scalar set per list item.

### include behavior
- Entry's matrix keys **match** an existing combo → **AUGMENT** (add extra keys).
- Keys **don't match** any combo → **NEW combo**.
- **Original axis values never overwritten**; include-added keys **can** be overwritten by a later include.
- **include-only** (no base axes) = explicit hand-picked combo list.

### fail-fast / max-parallel / continue-on-error
- **`fail-fast` default = `true`** → first failing combo **cancels** all in-progress + queued. Set `false` for full reports.
- `max-parallel` = cap on **simultaneous** combos (default = max allowed). A **count**, not an axis.
- **Swallow vs preserve** (THE distinction):
  - `continue-on-error: true` → **SWALLOWS** failure: run not failed, **downstream `needs:` sees SUCCESS**.
  - `fail-fast: false` → **PRESERVES** failure (still counts, blocks `needs:`), just doesn't cancel siblings.
- `fail-fast: true` + **flat** `continue-on-error: true` = **pointless** (fail-fast inert). Meaningful only as `continue-on-error: ${{ matrix.experimental }}` (per-combo carve-out).

### Dynamic matrix via fromJSON
- Matrix is fixed at **setup** → can't build from a **same-job** step output. Use a **PRIOR job** + `needs:` + `fromJSON`.
- Producer: set a **single-line JSON string** job output (`jq -c`). Consumer: `matrix: ${{ fromJSON(needs.<job>.outputs.<key>) }}`.
- **object** → whole matrix (keys become axes) · **array** → one axis OR the `include` list.
- `needs:` mandatory · malformed JSON → matrix won't expand · **empty array → ZERO jobs** (skipped, not failed).

### Runner images & -latest (verified June 2026; mappings DRIFT)
- `-latest` labels **float** — GitHub migrates them to newer OS gradually (~1–2 months) → **non-deterministic over time**. **Pin** a version label for reproducibility.
- Current: `ubuntu-latest`=**Ubuntu 24.04** · `windows-latest`=**Windows Server 2025** (=`windows-2025`) · `macos-latest`=**macOS 15 Arm64** (gotcha: Apple silicon).
- **Ubuntu 20.04 retired** (unsupported since **2025-04-01**) → `runs-on: ubuntu-20.04` **fails**.
- ⚠️ **Pinning stops silent migration, NOT deprecation** — a pinned old label still dies when the image is retired.
- (Newer, likely post-exam: `ubuntu-26.04` = public preview; `windows-latest` moving to "Server 2025 + VS 2026" toolset, June 2026.)
