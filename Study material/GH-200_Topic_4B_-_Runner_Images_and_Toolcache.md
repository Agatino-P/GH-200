# GH-200 — Topic 4B Recap: Runner Images & Toolcache

**Domain 4 (Enterprise, highest weight 20–25%) · Objective 4.6 — runner images, tool-cache, custom images, self-hosted customization.**
Verified live against official GitHub Docs + the `actions/runner-images` `ubuntu-24.04` README on 2026-06-22. This area is current-state and still evolving (custom images GA'd ~April 2026); re-verify specifics near exam time.

Cheat file companion: `GH-200_Cheat_4B_-_Runner_Images_and_Toolcache.md`.

---

## Bit 1 — Runner images & the tool-cache

### Mental model: three sources + one store

- **Source 1 — preinstalled (baked into the image)**, two layers:
  - (a) ordinary **system-wide** software on `PATH` (git, docker, a default Node/Python, apt packages);
  - (b) **Cached Tools** — extra runtime *versions* staged into the tool-cache (on `ubuntu-24.04`: Go, Node.js, Python, PyPy, Ruby).
- **Source 2 — `setup-*` actions** (run during the job).
- **Source 3 — your own installs** (`apt-get` / `brew` / `pip` / manual download).
- **The store — the tool-cache (`_work/_tool`)**: filled by Source 1b and Source 2; **ignored** by Source 3.

Key structural point: the tool-cache is the **shelf**, not a third source. "Preinstalled" and "`setup-*`" put things *on* the shelf; direct installs don't.

### Table 1 — sources & where the tool-cache sits

| Thing | Role | Lives where | Filled by | `setup-*` sees it? |
|---|---|---|---|---|
| Preinstalled — system-wide (git, docker, default Node/Python, apt pkgs) | ready-to-use OS/app software | normal paths (`/usr/bin`, …) | image build | No |
| Preinstalled — Cached Tools (Go, Node.js, Python, PyPy, Ruby) | extra runtime *versions* | tool-cache (`_work/_tool`) | image build | Yes |
| tool-cache (the shelf) | storage, **not** a source | `_work/_tool` | preinstall + `setup-*` misses | it **is** the shelf |
| `setup-*` (setup-node / setup-python / …) | the picker | — (reads/writes the shelf) | — | — |
| Your installs (`apt-get` / `pip` / `brew` / manual) | runtime additions | normal paths | you, mid-job | No |

### Table 2 — available right away / fast installable / persisted

| Source | Speed | Persist across jobs — HOSTED | Persist across jobs — SELF-HOSTED |
|---|---|---|---|
| Preinstalled (system-wide + Cached Tools) | instant, ~0 cost | re-provided fresh each job (new VM) | yes, while on the machine |
| `setup-*` → version **is** preinstalled/cached | instant (PATH switch) | switch re-runs each job (cheap) | cached version stays |
| `setup-*` → version **not** preinstalled | one-time download | **NOT** persisted; re-downloads each job unless `actions/cache` | persisted in tool-cache → later jobs hit |
| Your manual install (`apt-get`/`pip`/`brew`) | installer speed | not persisted | persists (and risks drift) |

### The two different "caches" (the fuzzy part)

| Cache | Holds | Filled by | On HOSTED runners |
|---|---|---|---|
| tool-cache (`_work/_tool`) | tool/runtime **binaries** | preinstall + `setup-*` | per-VM — wiped each job (gives **speed**, not persistence) |
| `actions/cache` (Topic 1E) | your **dependencies** (npm/pip/…) | you, via the action | GitHub-side cache service — **survives** across jobs |

**Persistence cut:** HOSTED = fresh VM every job (tool-cache does not persist). SELF-HOSTED = same machine reused (`_work/_tool` survives → `setup-*` downloads stick for later jobs).

### How `setup-*` behaves
- Requested version already on the shelf (common hosted case) → just prepend to `PATH`. Near-zero cost.
- Not there → the `setup-LANGUAGE` action downloads the binary into the tool-cache, then activates it (needs internet).

### Where to find the exact image software
Workflow log → expand **Set up job → Runner Image →** the "Included Software" link = the precise manifest for that run. The image set is maintained in `actions/runner-images` and refreshed ~weekly (rollout takes a few days). Don't assume a tool/version is present — pin with `setup-*` + explicit version.

### Q&A outcomes (Bit 1)
- **The apt-get vs `setup-python` trap:** a direct `apt-get install python3.12` is **invisible** to `setup-python`. setup-python does its normal thing regardless — uses a cached 3.12 if present, otherwise downloads it into the tool-cache. The apt result never enters the picture. (No need to memorize per-image version lists; the point is that direct installs don't touch the tool-cache.)
- Clarified that "preinstalled" is **two layers**, not one (system-wide + Cached Tools), confirmed against the `ubuntu-24.04` README's separate `Installed Software` and `Cached Tools` sections.

---

## Bit 2 — Custom images (larger runners) & self-hosted customization

Spectrum of *how much you bake ahead of time*: install-at-runtime (Bit 1) → **custom image** → **self-hosted fully-custom VM**.

### A) Custom images — for GitHub-hosted *larger* runners
Start from a GitHub-curated base image and build your own VM image with tools, dependencies, certificates, binaries, and prepulled container images already in place — a "pre-warmed" runner.

- **Headline limit:** custom images work **only on larger runners → GitHub Team or GitHub Enterprise Cloud**. Not standard runners, not Free. GA'd ~April 2026 (public preview from Oct 2025).
- **Three steps:** (1) set up an **image-generation runner**; (2) **generate** the image with the `snapshot` keyword; (3) **install/use** — assign to a runner group and point `runs-on` at it.
- **Platform/size rules:** the image-generation runner's platform must match the target image (**Linux x64, Linux ARM64, or Windows x64**); run the resulting image on a runner of the **same size or larger**.
- **`snapshot` — two syntaxes:**

  String form (name only; GitHub versions it entirely):
  ```yaml
  jobs:
    build:
      runs-on: my-image-generation-runner
      snapshot: my-custom-image      # captures the VM after the LAST step succeeds
      steps:
        - run: ./install-deps.sh
  ```
  Mapping form (name **and** optional major version):
  ```yaml
  jobs:
    build:
      runs-on: my-image-generation-runner
      snapshot:
        image-name: my-custom-image
        version: 1                   # MAJOR only; minor auto-increments, no patch
      steps:
        - run: ./install-deps.sh
  ```
- **Success-only:** a new image version is created **only when the job completes successfully**. A failed/incomplete run produces no new version.
- **Stays GitHub's, not yours:** still runs on GitHub infra; the image lives in the org's Actions settings under **"Custom images,"** *not* in your own container registry (`ghcr.io`); not reusable across other CI providers; not a general-purpose VM pipeline.
- **Billing/governance:** jobs billed at the larger-runner per-minute rate; **storage billed separately** through Actions storage; each successful snapshot = a new version, so frequent rebuilds + retained old versions grow storage fast; enterprise owners manage access and set **retention policies** in Actions policy settings. Regenerating ~weekly is recommended (patches/updates) → another artifact to manage.
- **Security best practices:** dedicated runner groups for image generation; **don't share runner groups between production and dev/test** (dev/test access ⇒ injection path into prod images); images can be built from **any branch**, so write access alone can trigger generation → least privilege. Permissions: org/enterprise owner, CI/CD Admin role, or equivalent fine-grained perms.

### B) Self-hosted — full customization (the other end)
You own the machine, so you customize everything: full OS image (e.g. Packer/AMIs), **any distro**, persistent tool-cache, pre/post-job hooks. Cost: you own maintenance, patching, security, drift. GitHub explicitly points you to self-hosted (or Docker) for non-Ubuntu Linux distros, since hosted Linux is Ubuntu-only.

### C) Where each is allowed
```
runtime install   → any runner, ephemeral, re-done every job
custom image      → LARGER hosted runners only (Team/GHEC), pre-warmed, GitHub-managed
self-hosted VM    → total control + total responsibility, any distro
```

### Q&A outcomes (Bit 2)
- **Mapping-form correction:** my first example showed only the string form. The mapping form is the one that lets you set the version (`image-name:` + `version:`); that `version` is the **major** segment, with the minor auto-incrementing per snapshot and no patch versions.

---

## Quiz outcomes
- **Bit 1:** Q2–Q5 correct (4/4). Q1 wasn't scored as a miss — it was a fair push on a loosely-worded item; the underlying concept (direct installs invisible to `setup-*`) landed.
- **Bit 2:** 5/5. Cleanly rejected the distractors that (C) custom images make you own OS patching like self-hosted [false] and (E) custom images are reusable on other CI providers [false].

## Honesty flags (carried from teaching)
- **Tool-cache path/env var:** the documented default is `_work/_tool`; the hosted-Ubuntu path (commonly cited as `/opt/hostedtoolcache`) and the `RUNNER_TOOL_CACHE` env-var name were **not** re-verified this session.
- **Custom images GA timing:** GA'd ~April 2026 (preview from Oct 2025). Pre-GA write-ups describe it as preview and may be stale; some limits/UI could still shift.
- **Retention numbers:** the *existence* of a retention policy is solid; a community report cites a **60-day default / 90-day maximum**, but those exact numbers were **not** found in official docs this session — treat as unverified.
- **Pre/post-job hook env-var names** (`ACTIONS_RUNNER_HOOK_JOB_STARTED` / `_COMPLETED`) come from a community blog this session, not re-verified against official docs.

## Cross-refs
- `actions/cache` (dependency cache) ↔ Topic 1E (caching vs artifacts + retention).
- Larger runners ↔ Topic 4A (static-IP larger runners, Azure VNET, runner groups).
- Next: Topic 4C — configuration variables (`vars`) hierarchy + managing secrets/variables via REST API (4.7, 4.8).
