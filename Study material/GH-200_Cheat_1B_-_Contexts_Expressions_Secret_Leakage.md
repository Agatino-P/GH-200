# GH-200 Cheat — Topic 1B: Contexts, Expressions, Secret Leakage

*Trap-grade keepers only. Full explanation in the matching recap: `GH-200_Topic_1B_-_Contexts_Expressions_Secret_Leakage.md`.*

### Context — what the term means HERE
- A **context** = a **read-only bag of runtime data**, read via `${{ }}`. NOT the vague English "situation." A named object you index into; only holds data that exists at that moment.
  - `github` → event/actor/ref/sha/repo · `needs` → upstream job outputs · `matrix` → this job's axis values · `steps` → id'd step outputs in **same** job.

### env vs vars vs secrets  ⚠️ THE contrast
- `env` = inline in YAML; **auto-exposed as shell `$NAME`**; not masked.
- `vars` = UI/API config; **read only via `${{ vars.X }}`**; **NOT masked**; **must map to env: for the shell.**
- `secrets` = UI/API sensitive; **read only via `${{ secrets.X }}`**; **auto-masked**; must map to env: for the shell.
- **secrets masked / vars NOT masked** ← the whole exam point. Sensitive value in `vars` = leak.
- Precedence (both): **environment > repository > organization.**
- `env:` blocks **don't self-reference** (one entry can't use another from the same block).

### Matrix (primer; depth = 1C)
- `strategy.matrix` is **per JOB**; runs the job once per **cross-product** combo, **parallel** by default.
- Throttle with **`max-parallel`** (1 = sequential). It caps a **count**, not an "axis." Combo order = don't rely on it.
- `needs: <matrix-job>` waits for **ALL** combos — matrix job = **one graph node**.
- **Matrix outputs:** all combos write the **same** output names → overwrite (**last wins, unreliable**). Fix: unique names via `matrix` context, e.g. `result_${{ matrix.x }}`.

### Expression evaluation — two phases
- **Setup phase** (before runners): job graph, **matrix expansion**, names, concurrency, `needs`.
- **Execution phase** (on runner): `if:`, `run:`, `with:`, env interpolation, step/job outputs.
- **Context availability by location:** top-of-file = ~nothing · job-level `if:`/`strategy` = `github`/`needs`/`vars` (**NO `steps`, NO `runner`**) · step-level = **everything**.
- ❌ `jobs.x.if: ${{ steps.y.outputs.z }}` fails — `steps` not available at job level.
- Matrix is **fixed at setup** → dynamic matrix = **`fromJSON(needs.<prior>.outputs.list)`**, never from a same-job step. (`fromJSON` = real built-in; full treatment 1C.)

### Secret leakage — masking is best-effort
- Masking catches the **raw secret + common encodings (notably Base64)** — so `base64(secret)` IS masked. But **NOT guaranteed**:
  - `echo "${{ secrets.T }}"` → `***`  ·  `echo "${{ secrets.T }}" | base64` → `***` (Base64 handled)  ·  `... | rev` → **CLEAR TEXT** (uncommon transform).
  - Leaks via: **structured/JSON secrets**, splitting/substringing, odd transforms, and `base64(secret+suffix)` padding edge case.
- Derived sensitive values → register with **`::add-mask::$VALUE`** (real workflow command). Never store structured data (JSON/XML) as a secret.
- **Outputs are NOT a secret channel** — they flow to GitHub + downstream as ordinary data. (A real registered secret in an output *is* redacted on the runner; a self-minted value is not.)
- **Script injection** (also 5.3): never interpolate untrusted `${{ }}` (PR title / branch / issue body / commit msg) straight into `run:`. **Bind to `env:`, then use `"$VAR"` quoted.**

### Passing secrets — where & how
- Already a registered secret? → read **`${{ secrets.X }}`** in the later job. Available run-wide; **no passing.**
- Calling a reusable workflow? → hand it over via the **`secrets:`** block (or **`secrets: inherit`**). Separate trust boundary; secrets don't cross automatically.
- A value you generated & must reuse downstream? → **`::add-mask::`** it, OR better: **don't pass the credential** — write the artifact/result it protects, not the secret.
