# GH-200 · Topic 3A — Immutable Releases & Version Pinning

*Recap note. Objective **3.2** (immutable actions rollout + registry-source implications + version pinning). Standalone Domain 3 topic; the **enforcement** side (org rulesets, required SHA pinning, blocking disallowed actions) is deliberately deferred to **5.6**. Paired cheat file: `GH-200_Cheat_3A_-_Immutable_Releases_and_Version_Pinning.md`.*

*Verified live (June 2026) against GitHub Docs + Changelog. Items I could not confirm are flagged ⚠️ rather than asserted.*

---

## Bit 1 — Immutable releases: what it locks, how it's enabled

### The problem it solves
By default a **Git tag is movable** and **release assets are editable**. So a compromised maintainer account — or a careless maintainer — can re-point `v1.2.0` to a different commit, or swap an uploaded binary, *after* you've already pinned to it. You'd run different code under the same reference and never notice. Immutable releases removes that attack surface.

### What it is
A **repository setting**, also settable at the **organization** level, and toggleable via **REST API**. It is a **GitHub Releases** supply-chain feature — *not* actions-specific — but action authors enable it on their action's repo. When on, **every new release is immutable**.

> Key framing: it's a **setting**, not a workflow-YAML key. There is no `immutable: true` in `.github/workflows`. (Spot-the-mistake bait.)

### What gets locked once a release is immutable
- **Assets** — files attached to the release can't be added, modified, or deleted.
- **The Git tag** — locked to its specific commit; can't be moved or deleted while the release exists. *(This is the lock that actually defeats the re-pointing attack — easy to forget alongside the asset lock.)*
- **Resurrection protection** — if you delete the immutable release you may delete the tag, but you **cannot reuse that tag name** afterward — even in a freshly recreated repo of the same name.

### Attestation
Creating an immutable release **auto-generates a signed release attestation** (a verifiable record of the release tag, commit SHA, and assets). Format = **Sigstore bundle**. Verify with:

```
gh release verify <tag>
gh release verify-asset <tag> <asset>
```

### Two behaviors worth memorizing
- **Disabling immutability later does NOT un-freeze** releases created while it was on — those stay immutable.
- Publishing locks everything immediately, so the recommended authoring flow is: **create as draft → attach all assets → publish**.

### Tie to action versioning (the lever into Bit 2)
Immutability attaches to the **release**, not to a bare tag. So if an author *wants* a movable tag — e.g. keeping `v1` floating to the newest `v1.x` — the docs are explicit: **don't create a release for it**, just push/move the bare tag.

That single authoring choice ("no release = movable") is exactly what leaves a floating tag **unprotected for the consumer**. Same coin, two sides.

```yaml
# Author side: a release published from this workflow is immutable
# ONLY IF the repo/org has immutable releases enabled.
on:
  release:
    types: [published]
# the enable/disable toggle lives in repo/org settings or the REST API,
# NOT in workflow YAML.
```

### ⚠️ Honesty flag — the OCI / ghcr.io publishing path
Objective 3.2 mentions "registry-source implications." There is a concept of publishing an action as an **OCI artifact to GitHub Packages / `ghcr.io`**, consumed by SemVer. **Status is conflicting and unconfirmed:** a roadmap card labels "Immutable Actions" GA, but the first-party `actions/publish-immutable-action` README *currently* still states it is **not ready for public use** and uploads won't work until fully released. Treated here as **NOT confirmed usable** — mechanics not drilled. **Calibrate its exam weight against practice exams.**

### ⚠️ Do not confuse with — immutable *subject claims* (OIDC)
A separate feature, "**immutable subject claims**," changes the **OIDC token subject format** (auto-enforced for new repos from ~July 15 2026). It is unrelated to immutable releases. Belongs to **OIDC (objective 5.5)**, not here.

---

## Bit 2 — The version-pinning spectrum (consumer side)

When you write `uses: owner/action@REF`, the `REF` decides how much can change under you. Least → most resistant to silent change:

```yaml
uses: owner/act@main          # branch    — moves on EVERY push          (worst)
uses: owner/act@v4            # major tag — floats to latest v4.x
uses: owner/act@v4.1.0        # version tag — specific, but still a movable pointer
uses: owner/act@<40-char-sha> # full commit SHA — content-addressed       (best)
```

### Why the ordering
- A **branch** ref changes on every push, with no version signal — most dangerous.
- A **tag** (`v4` or `v4.1.0`) is just a **movable pointer to a commit**. It can be re-pointed by the maintainer or an attacker. `v4` is *designed* to float (newest `v4.x`), so it's looser than `v4.1.0`, but **both are mutable pointers in principle**.
- A **full 40-char commit SHA** is **content-addressed**: it names an exact tree and **can't be re-pointed** (changing content changes the SHA). Guarantees byte-for-byte the same action every run. GitHub's standard recommendation for third-party actions.

### Full vs short SHA
Use the **full 40-character** SHA. Short SHAs are ambiguous and are not accepted where full-SHA pinning is expected. *(Enforcement details — org policy that can require full-SHA pinning — are in 5.6.)*

### Trade-offs of SHA pinning (so it's not treated as free)
- Loss of readability — `a1b2c3…` doesn't tell you it's "v4.1.0 with the fix."
- You stop auto-receiving patch updates — you bump the SHA yourself, typically via Dependabot.
- ⚠️ **Unverified caveat:** a claim circulates that SHA-pinning can interfere with Dependabot's vulnerability **alerting** on actions. Confirmed: Dependabot can *update* SHA-pinned actions (and annotates the version in a comment). **Not confirmed:** the alerting nuance — verify before relying on it.

### Where immutable releases changes the calculus
A reference to a tag that **is** a published **immutable** release (e.g. `@v4.1.0` where that release was published with immutability on) is **locked** — nearly as trustworthy as a SHA, while staying human-readable. **But mind the gaps:**
- It only helps for tags that are **immutable releases** — see the two-level trap below.
- A floating **`@v4`** is movable **as long as no immutable release is published on it** — and authors deliberately keep it that way (no release ⇒ free to advance to newest `v4.x`). Nothing about the *name* `v4` decides this; an author *could* publish an immutable release on `v4`, but then it stops floating.
- It depends on the **author** having enabled the setting; the consumer doesn't control it.

### ⭐ The two-level trap (a release is NOT automatically immutable)
This is the highest-value exam trap in the topic. Two independent questions, and you must clear **both** before a tag ref is locked:

1. **Is the tag even a release?** A bare tag (no release object) is just a movable pointer.
2. **Is that release _immutable_?** Publishing a release does **NOT** make it immutable. Immutability applies **only if the repo/org had immutable releases enabled at publish time.** A release published while the setting was off — or an older pre-existing release — is **fully mutable** (assets and tag still changeable).

So a tag can be in three states:
- bare tag (no release) → **movable**
- **mutable** release (setting was off) → **still movable**
- **immutable** release (setting was on) → **locked**

The trap a student falls for: "it's a Release on a clean `v3.4.0` tag → locked." **Wrong.** A Release ≠ an immutable Release. The version string and even the *existence of a release* tell you nothing about the lock — only the **immutable** status does.

### How a consumer actually checks (verified)
- **Release page:** an immutable release shows an **"Immutable" label below the title**. No label ⇒ not immutable.
- **REST API:** `GET /repos/{owner}/{repo}/releases/tags/{TAG}` → the release object has an explicit **`immutable` boolean**. A **404** means there's no release on that tag at all (bare tag).
- **CLI:** `gh release verify <tag>` confirms a release exists **and is immutable** (it loads the auto-generated signed attestation; immutable releases have one, others don't).
- *Honest caveat:* GitHub has an **open docs issue** asking for a proper "how to tell if a release is immutable, as a user" guide — so this check is real but under-documented today.

### ⭐ The "better safe than sorry" rule
You shouldn't have to audit each action's release setup. A **full commit SHA is immutable by construction** (content-addressed) — independent of whether the author made a release, enabled immutability, or later toggled it off. **When in doubt, pin the SHA and you never have to check any of the above.**

### Practical ranking
`branch` (worst) → `@v4` floating major → `@v4.1.0` plain tag → **`@v4.1.0` immutable-release tag ≈ `@<full-sha>`** (best; readable-vs-opaque is the tiebreaker).

### Forward pointer
*Requiring* SHA pinning or blocking disallowed actions org-wide (rulesets / Actions policy) = enforcement → **taught in 5.6**, not here.

---

## Q&A outcomes (what the quizzes surfaced)

**Bit 1 quiz — 4/5.** Misses/keepers:
- The one miss was forgetting that immutability locks **two** things: **assets AND the tag**. The tag-lock (tag pinned to its commit, can't move/delete while the release exists) is the part that actually stops the re-pointing attack. **Keeper:** *immutable release = assets locked + tag locked (+ name unreusable after deletion + auto-attestation).*
- Confirmed cold: movable tag ⇒ don't create a release; disabling never un-freezes; draft→attach→publish; no `immutable:` YAML key (it's a setting).

**Bit 2 quiz — 3/5.** Both misses were the **same misconception**, so it's the headline keeper:
- Treating "immutable releases enabled on the repo" as "**every tag** on that repo is locked." It is **per-release, not per-repo-wide-tag**. `@main` and a floating `@v4` (no release behind them) stay **mutable** even on an immutable-releases repo; only `@v4.1.0`-as-a-published-immutable-release is locked; a full SHA is always pinned regardless of any setting.
- **Don't get fooled by the semver tag alone:** `@v3.4.0` looking precise does *not* make it safe — the same string can be a bare movable tag, a *mutable* release, or a *published immutable* release. Safety comes from the **immutable status** (or a full SHA), never from how specific the version string looks.
- **A release is NOT automatically immutable** (the two-level trap): clearing "is it a release?" is not enough — you must also clear "is that release *immutable*?" Publishing while the setting was off (or an older release) leaves it mutable. This is the single highest-value trap in the topic.
- Short-SHA point reasoned out from first principles (good) rather than memorized.

---

## Cross-references
- **Bit 1 ↔ Bit 2:** "no release = movable tag" is the author's feature *and* the consumer's hazard — the same fact appears in both bits.
- **→ 5.6:** SHA-pinning enforcement, org Actions policy / rulesets, blocking disallowed actions, full-SHA requirement specifics.
- **→ 5.5:** OIDC — and the *different* "immutable subject claims" feature (keep separate).
- **↔ 1.10 / Topic 1B:** version pinning was foreshadowed alongside the contexts material.

## Open / to-calibrate against practice exams
1. Exam weight of the **OCI/ghcr publishing** path (status unconfirmed).
2. The **Dependabot SHA-pinning alerting** caveat (unverified).
3. Whether the exam phrases this as "immutable **actions**" vs "immutable **releases**."
