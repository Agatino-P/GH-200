# GH-200 Cheat — Topic 1D: YAML Anchors, Aliases & Merge Keys

*Trap-grade keepers only. Full explanation in the matching recap: `GH-200_Topic_1D_-_YAML_Anchors_Aliases_Merge_Keys.md`.*

### Support matrix ⚠️ THE whole topic
- `&` anchor + `*` alias → **SUPPORTED** (shipped **2025-09-18**, auto-enabled all repos). Before that: errored.
- `<<` **merge key → NOT SUPPORTED.** GitHub shipped "half the feature." Official docs document only `&`/`*`.
- ❌ Don't generalize: "anchors supported" ≠ "merge keys supported." They are **not** the same feature.

### Anchors / aliases mechanics
- Alias copies the **WHOLE node** — **all-or-nothing**, NO partial override.
- **Define before use** — anchor must appear **above** any alias to it (top-to-bottom). Alias-before-anchor = error.
- **Same file only** — NOT a cross-file/cross-repo reuse tool (that's composite actions / reusable workflows).
- Can anchor any node: scalar, sequence (e.g. shared `paths:` across triggers), mapping, or a whole job.

### Merge keys — the trap
- `<<: *base` in a workflow = **broken/invalid**, not inherit-and-override. (Exact failure mode — hard error vs literal `<<` key — unverified; either way the merge does NOT happen.)
- Want **base + override one key**? → **composite action or reusable workflow.** Anchors = exact duplication only.
- `<<: *base` is a classic **"spot the mistake"** distractor (objective 2.3 reading/analysis).
- Trivia: merge keys are YAML **1.1** optional type, never in core 1.2 → inconsistent parser support generally.

### Exam weight ⚠️ uncertain
- Feature shipped Sept 2025, exam reworded Jan 2026 → weight/form **not verified**. Likely tested as *read-and-analyze* / *spot-invalid-`<<`* rather than authoring. Calibrate vs practice exams.
