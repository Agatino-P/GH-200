# GH-200 · Cheat 3A — Immutable Releases & Version Pinning

*Terse last-week-review keepers for objective 3.2. Fuller note: `GH-200_Topic_3A_-_Immutable_Releases_and_Version_Pinning.md`. Enforcement specifics → see 5.6.*

---

## ⭐ HEADLINE TRAP — a Release is NOT automatically immutable
Two independent checks; a tag ref is locked only if **BOTH** pass:
1. **Is it a release at all?** Bare tag (no release) → movable.
2. **Is that release _immutable_?** Publishing a release does **NOT** lock it. Immutable **only if** the repo/org had immutable releases **enabled at publish time**. Setting off (or an older release) → **mutable release = still movable** (assets + tag changeable).

Three states of any tag: **bare tag → movable** · **mutable release → still movable** · **immutable release → locked**.

> **The exam trap:** "it's a Release on a clean `v3.4.0` tag, so it's locked." ❌ WRONG. A Release ≠ an immutable Release. The version string *and even the existence of a release* tell you nothing — only the **immutable** status does.
>
> **Don't get fooled by the semver tag alone** — `@v3.4.0` can be a bare tag, a mutable release, OR an immutable release. Lock comes from the **immutable status** (or a full SHA), never the version text.

### How a consumer checks immutability
- **Release page:** **"Immutable" label** below the title (no label ⇒ not immutable).
- **REST:** `GET /repos/{o}/{r}/releases/tags/{TAG}` → release object's **`immutable` boolean** (404 ⇒ no release / bare tag).
- **CLI:** `gh release verify <tag>` (succeeds + loads attestation ⇒ immutable).
- *(GitHub's own user-facing "how to check" docs are still an open issue — under-documented.)*

### ⭐ Better-safe-than-sorry rule
**A full commit SHA is immutable by construction** — no audit of the author's release/setting needed. When in doubt, **pin the SHA**.

---

## Immutable releases — the lock
- **= assets locked + Git tag locked** (+ tag name unreusable after deletion + auto signed attestation). ← don't drop the **tag** lock.
- It's a **repo/org setting** (UI or REST API) — **NOT** a workflow-YAML key. No `immutable: true` in YAML. (spot-the-mistake)
- **Disabling it later does NOT un-freeze** already-immutable releases.
- Publishing locks instantly → author flow: **draft → attach assets → publish**.
- Attestation = **Sigstore bundle**; verify with `gh release verify` / `gh release verify-asset`.
- Immutability attaches to the **release, not a bare tag** → author keeps a tag movable by **not creating a release** for it.

## Pinning spectrum (consumer)  — least → most safe
`@main` (branch, worst) → `@v4` (floating major) → `@v4.1.0` (plain version tag) → `@<full 40-char SHA>` (best)
- Tags = **movable pointers**; full SHA = **content-addressed, can't be re-pointed**.
- **Full 40-char SHA** only — short SHAs are ambiguous / not accepted.
- On an immutable-releases repo: best readable option = a version tag `@v4.1.0` **that is itself a published immutable release** ≈ a SHA.
- **`@v4` floating stays movable as long as no immutable release is published on it** (authors keep it release-free so it can advance). The name `v4` decides nothing.

## ⚠️ Flags (uncertain — calibrate vs practice exams)
- **OCI/`ghcr.io` publishing** of actions: status conflicting; first-party publish action README says **not for public use**. Treat as **not confirmed GA**.
- **Dependabot + SHA-pinning alerting** interference: **unverified**. (Updates of SHA-pinned actions = confirmed.)

## ⚠️ Do not confuse
- **Immutable *subject claims*** = an **OIDC token format** change (→ 5.5). **Different feature**, not immutable releases.
