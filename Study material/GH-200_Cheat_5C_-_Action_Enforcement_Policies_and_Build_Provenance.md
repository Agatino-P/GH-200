# GH-200 Cheat — Topic 5C: Action Enforcement Policies & Build Provenance

> Last-week review. Fuller note: `GH-200_Topic_5C_-_Action_Enforcement_Policies_and_Build_Provenance.md`
> 5C = **enforcement** (Bit 1) + **provenance proof** (Bit 2). NOT a re-teach of 3A concepts.

---

## ⚠ THE BIG ONE — "artifact" is two unrelated features (exam won't name the domain)

| Verbs in the question | It's… | Domain |
|---|---|---|
| `upload-artifact`/`download-artifact`, "between jobs," "retention," "90 days" | **workflow artifact** | 1 (Topic 1E) |
| `attest`, "provenance," "Sigstore," "`gh attestation verify`," "SLSA," "verify before deploy" | **build output under an attestation** | 5 (5.8) |

Same word, unrelated mechanics. Read the verbs, not the noun.

---

## Bit 1 — enforcement keepers

- **Override direction:** enterprise → org → repo. Lower level can only **tighten**, never loosen.
- **Section labels differ by scope:** repo = "Actions permissions"; org & enterprise = "Policies." (Concept identical; recognize, don't memorize.)
- **Local-only policy blocks GitHub's own actions** → `actions/checkout` becomes inaccessible. Re-enable via "Allow actions created by GitHub."
- **Local actions (`uses: ./path`) are NEVER restricted by the allow/deny list.** Remote refs only.
- **`!` in the allow list** = subtract an exception; both entries coexist; **block wins on overlap**. `*, !evil-org/*` = allow all except that owner. List capped at **1000 entries**.
- **Verified-creator badge = publisher IDENTITY only**, not code review/audit. Verified accounts can be compromised. Still review source + pin SHA.
- **★ SHA-pinning enforcement applies to ACTIONS only — reusable workflows are EXEMPT (still tag-referenceable).** "Forces reusable workflows onto SHAs too" → FALSE.
- **SHA pin freezes source, not behavior** — a pinned action can still pull an unpinned Docker image / nested composite / `curl`ed script. Reproducible *source*, not *behavior*.
- **★ "Required reviewers for unverified actions" is NOT a real feature.** It's a loose umbrella over: (a) fork-PR contributor-approval gate (keys off *who triggers*) + (b) environment "Required reviewers" protection rules (gate a *job* hitting a protected env). No setting inspects action-verified-status and demands a reviewer.
- Fork-PR approval: maintainer (write access) approves before run; **both PR author AND triggering actor checked**; run awaiting approval **>30 days → auto-deleted**.
- Immutable actions: **consuming = live/transparent** (OCI packages from GitHub Packages, host `pkg.actions.githubusercontent.com` under `*.actions.githubusercontent.com` → 4A allow-list). **Publishing your own = ⚠ not confidently GA** (README "not for public use" vs roadmap "GA"). Verify on practice exam.

---

## Bit 2 — attestation keepers

- **Attestation = signed claim binding SUBJECT (name + SHA-256 digest) → PREDICATE (provenance facts) in in-toto format.** Digest = hash of the actual bytes.
- **3 permissions to generate:** `id-token: write` (OIDC signing identity — the 5B tie-in, NOT for deploy), `contents: read`, `attestations: write`. (+ `packages: write` for container images.)
- **Action naming:** `actions/attest-build-provenance` (historic) is, as of v4, a **wrapper around `actions/attest`**. New code → `actions/attest@v4`. **Recognize BOTH names.** `@v1` in old material = drift, not wrong.
- **Keyless signing via Sigstore:** public repo → **Public Good** instance (has transparency log); private/internal → GitHub **private** Sigstore (no transparency log, federates only with Actions).
- **Generating alone = no security benefit. Value only on verification** (`gh attestation verify`, needs `--owner` OR `--repo`).
  - Container image → `oci://ghcr.io/...` prefix, not a file path.
  - SBOM → must pass `--predicate-type` (else it verifies provenance, not the SBOM).
  - `--signer-workflow` / `--signer-repo` → require a *specific* signing workflow/repo.

- **★ CHECK ORDER (Q2 keeper):** verify runs **bytes → signature → identity**.
  - A **plain file-swap fails at step 1 (digest/bytes lookup)** — the swapped bytes hash to a different digest, so **no attestation exists for them**, before any signature is examined.
  - The **signature check** defeats a **forged/invalid attestation that has a matching digest**.
  - The **identity check** rejects a validly-signed output from a *different* owner/repo than you demanded.
  - Exam can split these: "what catches a swapped artifact?" (bytes) vs "what catches a forged attestation?" (signature).

- **★ MONOTONIC — state it precisely:** verify passes when **≥1 attestation satisfies the SPECIFIC CLAIMS YOU ASKED TO VERIFY** (`--owner`/`--repo` + `--signer-workflow`/`--predicate-type` if given) — NOT the generic "an attestation passes." Junk/non-matching attestations are **inert** (can't substitute, can't veto). Monotonic = once it passes, later additions can't flip it to fail (anti-DOS).
  - **Looseness lives in YOUR query:** `--owner acme` only proves "*someone* in acme signed it," not "`release.yml` did." Tighten with `--repo`/`--signer-workflow`. **Owner ≠ workflow.**
  - Verifying provenance ≠ verifying SBOM (different predicate).

- **SLSA** = "Supply-chain Levels for Software Artifacts" ("salsa"), industry framework, not a GitHub feature. GitHub provenance is in SLSA build-provenance format. **Attestations + reusable workflows → SLSA v1.0 Build Level 3.** (⚠ baseline level of a plain attestation + exact per-level wording = unverified; objective lists SLSA as an *example* only.)
- Deploy gate: run `gh attestation verify` before consuming a build output; proceed only on pass. K8s **admission controller** can enforce at the cluster (know it exists).
