# GH-200 — Topic 5C: Action Enforcement Policies & Build Provenance

**Domain 5 (Secure & Optimize). Objectives: 5.6 action-usage enforcement + light 5.7 (pinning/immutable enforcement) + 5.8 (artifact attestations / provenance / SLSA).**
Verified live against `docs.github.com` (Enterprise Cloud) and the GH-200 study guide (skills measured Jan 2026), session date 2026-06-23.

> Companion cheat file: `GH-200_Cheat_5C_-_Action_Enforcement_Policies_and_Build_Provenance.md`
> Boundary reminder: Topic 3A taught *what* pinning/immutability are and *why* to pin. Topic 5C is the **enforcement machinery** (Bit 1) and the **provenance proof** (Bit 2) — not a re-teach of 3A concepts.

---

## Bit 1 — Enforcing safe action consumption

These controls make safe consumption *mandatory* for everyone in a repo/org/enterprise, rather than relying on each developer to choose well.

### Where the controls live (same block, three signposts)

| Level | How to get there | Section label once there |
|---|---|---|
| Repository | Settings → Actions → General | "Actions permissions" |
| Organization | Settings → Actions → General | "Policies" |
| Enterprise | Policies (top nav) → Actions | "Policies" |

**Override direction (the load-bearing cross-tier fact):** enterprise → organization → repository. A lower level can only *tighten*, never loosen, a policy set above it. A `!` carve-out in an allow list is "partially override" in the sense of subtracting an exception — both entries coexist; block wins on overlap.

### Lever 1 — "Actions permissions" policy (the allow/deny list)

Four mutually-exclusive options:

| Option | Allows | Note |
|---|---|---|
| Allow all actions and reusable workflows | Anything, any author | Default |
| Allow `<owner>` actions and reusable workflows | *Local only* | **Blocks GitHub's own actions** — `actions/checkout` becomes inaccessible |
| Allow `<owner>`, and select non-`<owner>` | Local + sub-toggles below | Only tier that unlocks finer control |
| Disable | Nothing runs | — |

Sub-toggles under the "select" tier:

| Sub-toggle | Effect |
|---|---|
| Allow actions created by GitHub | Everything in the `actions` and `github` orgs (this restores `actions/checkout`) |
| Allow Marketplace actions by verified creators | Any action with the verified-creator badge |
| Allow or block specified actions and reusable workflows | Explicit list — **max 1000 entries** |

List syntax (same `@ref` grammar as `uses:`):

```
actions/checkout@v4      # exact ref
monalisa/*               # all repos under an owner
monalisa/my-action@*     # any ref of one action
*, !evil-org/*           # allow all, block one owner
```

- `!` entries are denies layered over allows; **block wins on overlap**.
- **Local actions (`uses: ./path`) are never restricted by any policy** — the list only governs remote refs.
- The **verified-creator badge confirms publisher *identity* only** — GitHub verified the org is a genuine partner, not impersonator. It does **not** mean the code was reviewed or audited, and a verified account can itself be compromised. Trusting the toggle = trusting *who* wrote it, not *what the code does*. GitHub's own guidance still says review the source and pin to a SHA even for verified creators.

### Lever 2 — Require actions to be pinned to a full-length commit SHA

A dedicated checkbox inside the same allowed-actions policy, at repo/org/enterprise. When on, **every action ref must be a full 40-char SHA** — including your own org's actions and GitHub's. This is the *enforcement* of the 3A pinning concept (3A = voluntary; this = compulsory org-wide).

- **★ Reusable workflows are EXEMPT — still referenceable by tag.** The rule applies to `uses:` *actions*, not to `uses: owner/repo/.github/workflows/x.yml@ref`. "Forces reusable workflows onto SHAs too" → false.
- **A SHA pin freezes the action's source tree, not its runtime behavior.** A pinned action can still be mutable underneath via an unpinned Docker base image, an unpinned nested composite action, or a script it `curl`s at runtime. Reproducible *source*, not reproducible *behavior*.

### Lever 3 — Approval gate for untrusted contributors' workflows

Settings → Actions → General → "Fork pull request workflows" / "Approval for running fork pull request workflows from contributors." This gates on *who triggers*, not on which actions are used.

| Setting | Who must wait for approval |
|---|---|
| First-time contributors who are new to GitHub | Brand-new GitHub accounts only |
| First-time contributors | Anyone with no merged commit/PR in *this* repo |
| All outside collaborators / external contributors | Anyone not a member/owner of the repo or org |

A write-access maintainer approves before the fork-PR workflow runs. **Both the PR author and the triggering actor are checked.** A run awaiting approval for >30 days is auto-deleted.

**★ Exam-wording honesty flag:** the objective says *"required reviewers for unverified actions,"* but **no GitHub feature gates on whether an *action* is verified and demands a reviewer.** The phrase is a loose umbrella over two real, separate features: (a) this contributor-approval gate (keys off *who triggers*), and (b) **environment "Required reviewers"** protection rules (gate a *job* targeting a protected environment — same protection-rule pairing as 5B's OIDC). Recognize both; don't hunt for a literal "unverified-actions reviewer" setting.

### Backdrop — immutable actions on hosted runners (registry-source shift)

| Aspect | Status |
|---|---|
| Consuming immutable actions | Live/transparent — hosted runners resolve actions as immutable OCI packages from GitHub Packages where one exists, else classic Git-ref resolution. No workflow change needed |
| Download host | `pkg.actions.githubusercontent.com` (under required `*.actions.githubusercontent.com`); publishing uses `ghcr.io` → **4A allow-list tie-in** |
| Publishing your own immutable action | ⚠ **Not confidently GA** — `actions/publish-immutable-action` README still says "not ready for public use," yet a roadmap card is labeled GA. Conflicting signals (flag carried from 3A); verify against a practice exam |

---

## Bit 2 — Artifact attestations & build provenance (5.8)

### ⚠ Terminology warning — "artifact" is two unrelated features

The exam will not tell you which domain a question belongs to. Read the verbs.

| If the question is about… | "Artifact" means… | Clues |
|---|---|---|
| Moving files between jobs / keeping run outputs (Domain 1, Topic 1E) | a **workflow artifact** | `upload-artifact`, `download-artifact`, "between jobs," "retention," "90 days," "download from the run" |
| Proving where/how a published thing was built (Domain 5, 5.8) | a **build output you publish & someone else consumes** (release binary, container image, package) | `attest`, `attest-build-provenance`, "provenance," "Sigstore," "`gh attestation verify`," "SLSA," "verify before deploy" |

| | Workflow artifact (1E) | Thing an attestation is *about* (5.8) |
|---|---|---|
| Created by | `actions/upload-artifact` | your build step (the file/image) |
| Purpose | hand a file between jobs / retrieve after run | ship a verifiable build output to consumers |
| Stored | Actions artifact service, tied to the **run** | output lives where you publish it; the *attestation* lives in GitHub's attestations API, tied to the **repo** |
| Lifetime | retention-bound (90-day default, 1–400 range — per 1E) | persists with the repo, independent of the run |

They can touch (a build output is sometimes also uploaded as a workflow artifact to move between jobs), but the attestation is about the *published output's provenance*, not the inter-job transfer. Below, "build output" = the 5.8 sense.

### The problem 5.8 solves

A published build output is linked to the consumer only by *name and location*, not identity. Anyone who can write to a point in the chain (compromised registry creds, hijacked Release asset, poisoned CDN/mirror, typosquat) can swap your file for a malicious one of the same name + version. The version string proves nothing about the bytes. (Distinct from Bit 1: SHA-pinning protects the *action source pulled into* your build; this protects the *build output shipped out of* it.)

### What an attestation is

A cryptographically signed claim binding a **subject** to a **predicate**, in the **in-toto** format:

- **Subject** = the build output's name + its **SHA-256 digest** (hash of the actual bytes; one byte changed → different digest).
- **Predicate** = build-provenance facts: link to the workflow, repository, organization, environment, commit SHA, triggering event, and other claims from the **OIDC token** used during the build.

5B tie-in: the signing identity comes from OIDC — `id-token: write` exists precisely to mint the identity that signs.

### Why "swapped in" is *detected* (the real mechanic)

Verification checks three things; the **order matters**:

1. **Bytes (digest lookup).** CLI hashes the file the consumer holds, then fetches the attestation *by that digest*. A swapped file has a different digest → **no attestation exists for those bytes** → fails here, before any signature is examined.
2. **Signature.** Catches a *forged/invalid* attestation that has a matching digest — checked against the Sigstore certificate chain.
3. **Identity.** Confirms the signing cert's claims match the `--owner`/`--repo` you demanded. A validly-signed output from a *different* repo still fails if you demanded yours.

So a **plain file-swap dies at step 1 (bytes)**; the **signature check defends against a forged attestation on a matching digest**. The attestation doesn't block the swap — it makes it detectable before the bytes are used.

### Generating an attestation

```
permissions:
  id-token: write       # OIDC identity used to sign (keyless)
  contents: read
  attestations: write   # upload the attestation to GitHub
```

```
- name: Generate provenance attestation
  uses: actions/attest@v4
  with:
    subject-path: 'path/to/your/build-output'
```

Container images additionally need `packages: write`.

**⚠ Naming precision:** the historically-named action is **`actions/attest-build-provenance`**; as of its v4 it's a thin **wrapper around `actions/attest`**. Existing workflows can keep using `attest-build-provenance`; new ones should use `actions/attest`. Recognize **both names**. Older GA material shows `attest-build-provenance@v1` vs current `actions/attest@v4` — version drift, not a contradiction.

### How signing works (keyless, via Sigstore)

Short-lived Sigstore-issued signing certificate; no long-lived key you manage — same keyless philosophy as 5B OIDC.

| Repository type | Sigstore instance | Transparency log? |
|---|---|---|
| Public | Sigstore **Public Good** instance | Yes |
| Private / internal | GitHub's **private** Sigstore instance | **No** — same codebase, no public transparency log, federates only with GitHub Actions |

Signed attestation is uploaded to GitHub's attestations API, associated with the repo, visible in the Actions tab.

### Verifying

**Generating alone gives no security benefit — the value only materializes on verification.** Done with the GitHub CLI:

```
gh attestation verify path/to/build-output --owner my-org
gh attestation verify path/to/build-output --repo my-org/my-repo
```

Must supply `--owner` (`-o`) *or* `--repo` (`-R`). Specifics:

- **Container images:** point at the image with an `oci://` prefix — `gh attestation verify oci://ghcr.io/my-org/my-image:tag -R my-org/my-repo` (after `docker login ghcr.io`).
- **SBOM attestations:** pass `--predicate-type` explicitly (otherwise it verifies build provenance, not the SBOM).
- **Reusable-workflow signing:** `--signer-repo` points at the repo holding the signing workflow when it differs from the caller; `--signer-workflow` requires a *specific* workflow file did the signing.

**★ Monotonic verification — stated precisely:** verification passes when **at least one attestation satisfies the specific claims you asked to verify** (the identity in `--owner`/`--repo`, plus `--signer-workflow`/`--predicate-type` if supplied) — *not* the vague "at least one attestation passes." Non-matching/junk attestations in the set are **inert**: they can't substitute for your demand and can't veto an attestation that already met it. Monotonic = once it passes, later additions can't flip it to failing (anti-DOS). Corollary: looseness lives in *your query* — `--owner` only proves "someone in the org," so tighten with `--repo`/`--signer-workflow` for a specific builder; and verifying provenance ≠ verifying an SBOM (different predicate).

Why a set can hold multiple attestations for one digest: different predicate types (provenance + SBOM), re-runs/re-publishes of the same bytes, or reusable-workflow signing — plus, maliciously, junk anyone could add.

### Where SLSA fits

**SLSA** ("Supply-chain Levels for Software Artifacts," said "salsa") is an industry framework (not a GitHub feature) defining graded supply-chain integrity levels. GitHub's provenance predicate *is* in SLSA build-provenance format, so producing these attestations is how you meet SLSA's provenance requirement on GitHub.

Verified claim to hold: **artifact attestations + reusable workflows → SLSA v1.0 Build Level 3** (provenance generated by a hardened, controlled platform — a centrally-managed reusable workflow — rather than by the build about itself).

⚠ Honesty flag: the "reusable workflows → Build L3" statement is straight from the docs (confident). I'm *not* certain of the baseline level a plain attestation reaches, nor the exact requirement wording per level — verify against a practice exam. The objective lists SLSA as an example only ("e.g., SLSA, build metadata") → conceptual familiarity, not reciting the level table.

### Integrating into deployment verification

Run `gh attestation verify` before a deploy step consumes a build output; proceed only on success → provenance becomes a deploy gate. GitHub also offers a **Kubernetes admission controller** that validates attestations at the cluster so only properly-attested images deploy. (Know it exists; not a deep-dive.)

---

## Quiz outcomes (this session)

**Bit 1 — effectively solid.** Both genuine traps landed: reusable-workflow exemption from SHA enforcement, local-only policy blocking `actions/checkout`, and local-action (`./path`) exemption from the allow list. Misses were *wording*, not concept:
- The `!`-block keeper was reasoned correctly during teaching but dropped on the multiple-choice; reframed as "subtracts an exception, block wins on overlap."
- Marked "required reviewers for unverified actions" as a real setting (the worded trap) — corrected: it's a loose umbrella, not a feature.

**Bit 2 — 4/5.** Clean on: missing `id-token: write` and its signing role; SBOM ≠ provenance (different predicate); the artifact-term collision (correctly classified both scenarios); `--owner` overclaim (owner ≠ workflow; tighten with `--signer-workflow`/`--repo`).
- **The one real miss:** check *order*. A plain **file-swap fails at the digest/bytes lookup** (no attestation exists for those bytes), *before* any signature check. The **signature check** is what defeats a forged/bad attestation on a *matching* digest. → cheat-file keeper.

Learner-driven refinements incorporated: the artifact-collision note (read the verbs, exam won't name the domain); monotonic verification stated as "satisfies the specific claims you asked to verify," not generic "an attestation passes."
