# GH-200 Cheat — 4B: Runner Images & Toolcache

*Last-week review. Full notes: `GH-200_Topic_4B_-_Runner_Images_and_Toolcache.md`. (Domain 4 · 4.6)*

---

### ★ Three SOURCES + one STORE (don't make the tool-cache a "source")
- **Preinstalled** (baked) = TWO layers: (a) system-wide on `PATH` (git, docker, default Node/Python, apt pkgs); (b) **Cached Tools** = extra runtime *versions* in the tool-cache (ubuntu-24.04: Go, Node, Python, PyPy, Ruby).
- **`setup-*` actions** (run-time picker).
- **Your installs** (`apt-get`/`pip`/`brew`/manual).
- **tool-cache (`_work/_tool`)** = the SHELF. Filled by preinstall + `setup-*` only. **Direct installs never touch it.**

### ★ Direct installs are INVISIBLE to `setup-*`
`apt-get install python3.12` → `setup-python` does NOT see it. setup-python uses a cached version if present, else downloads into the tool-cache. The apt result is irrelevant in all cases.

### ★ HOSTED = speed, not persistence
- Tool-cache on hosted = **per-VM**, wiped every job. Preinstalled versions give *fast starts*, but nothing you download mid-job survives.
- What persists across **hosted** jobs = **`actions/cache`** (deps), a *different* cache. ← don't confuse the two.
- **SELF-HOSTED** = same machine ⇒ `_work/_tool` survives ⇒ a `setup-*` download sticks for later jobs (manual installs persist too → drift risk).

### ★ Custom images = LARGER runners ONLY → Team/GHEC
Not standard runners, not Free. GA ~April 2026 (was preview Oct 2025).

### ★ Custom image ≠ self-hosted
- Still **GitHub's infra**. Image lives in org Actions → **"Custom images"** catalog — **NOT** `ghcr.io`, **NOT** your registry. No cross-CI reuse. Not a general VM pipeline.
- Distractor bait: "pushed to ghcr.io", "reuse on CircleCI", "you patch the OS like self-hosted."

---

### Custom images — fast facts
- **3 steps:** image-generation runner → generate via `snapshot` → assign to runner group + `runs-on`.
- **Platform match:** gen-runner platform = target (Linux x64 / Linux ARM64 / Windows x64). Run image on **same size or larger**.
- **`snapshot` syntax:**
  - String (`snapshot: name`) = name only, GitHub versions it.
  - Mapping (`image-name:` + `version:`) = name + **major** version; **minor auto-increments, NO patch**.
- **Version created ONLY on job success.** Fail/incomplete ⇒ no new version.
- **Storage billed separately** (Actions storage); each snapshot = new version ⇒ storage grows. Enterprise owners set **retention policy**.
- **Security:** dedicated runner group for image gen; **don't share prod with dev/test** (injection); buildable from **any branch** ⇒ write access = trigger ⇒ least privilege.

### Self-hosted — fast facts
- Full OS/image control, **any distro**, persistent tool-cache, pre/post-job hooks — but you own maintenance/security/drift.
- **Hosted Linux = Ubuntu ONLY.** Other distros ⇒ Docker, or self-hosted custom VM.

### Find the exact image software
Log → **Set up job → Runner Image → "Included Software"** link. Source = `actions/runner-images`, refreshed ~weekly. Don't assume presence/version — pin `setup-*` + explicit version.

---

### ⚠ Unverified (calibrate vs practice exams)
- Hosted tool-cache **path** `/opt/hostedtoolcache` + env var `RUNNER_TOOL_CACHE` — not re-verified (documented default = `_work/_tool`).
- Custom-image **retention 60-day default / 90-day max** — community-reported, not docs-confirmed.
- Hook env-var names `ACTIONS_RUNNER_HOOK_JOB_STARTED`/`_COMPLETED` — from a community blog.
