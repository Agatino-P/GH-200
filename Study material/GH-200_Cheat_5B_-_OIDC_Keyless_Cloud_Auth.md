# GH-200 — Cheat 5B: OIDC Keyless Cloud Auth

*Full notes: `GH-200_Topic_5B_-_OIDC_Keyless_Cloud_Auth.md`. Domain 5 · objective 5.5. Verified live 2026-06-23.*

---

## TRAPS FIRST

- **`id-token: write` ≠ resource write.** It only lets the job request/use the OIDC token. Missing it = #1 OIDC failure. (Names one permission → all others `none` except `metadata` read.)
- **Two tokens, don't merge them.** `ACTIONS_ID_TOKEN_REQUEST_TOKEN` (request token) authenticates the runner *to GitHub* to mint the JWT — **the cloud never sees it.** Only the **JWT** goes to the cloud.
- **The JWT carries identity, not permissions.** Scope is 100% cloud-side. AuthN = GitHub; authZ = cloud.
- **Validation order = issuer → signature → claims.** Read `iss` → confirm trusted/registered issuer → fetch *that* issuer's public keys → verify signature → check `aud`/`sub`. Issuer check is NOT redundant with signature: it *selects* the key set ("is it a signer I trust?") vs signature ("is it real?").
- **`sub` precedence: environment > pull_request > branch/tag.** A job referencing an environment gets `:environment:NAME` even on a PR trigger. No composite form. Condition for `:ref:refs/heads/main` breaks the moment a job declares an environment.
- **PR job referencing `production` → `sub` matches `:environment:production`.** The cloud condition does NOT stop it — **environment protection rules** (GitHub-side, before token issue) do. Scope-to-environment + protection-rules are a **pair**.
- **`StringEquals` + `*` fails CLOSED.** `*` is literal under `StringEquals` → matches nothing → too-restrictive bug, not exposure. Danger appears under `StringLike` (wildcard expands). Distinguish too-restrictive (broken) from too-permissive (hole).
- **Immutable subject claims ≠ immutable releases (3A).** Same word, unrelated feature.

---

## Bit 1 — Concept & flow

- **Why:** swap a **long-lived stored cloud secret** for a **short-lived token fetched at runtime**. Nothing durable in GitHub.
- **Flow:** job (with `id-token: write`) → request token mints a **signed JWT** from `https://token.actions.githubusercontent.com` → JWT sent to cloud → cloud validates → returns **short-lived, job-scoped** cloud creds.
- **Acceptance = asymmetric crypto.** GitHub signs with private key (RS256); cloud verifies with GitHub's **public** keys (JWKS via `.well-known/openid-configuration`). No shared secret. Trust anchored by one-time provider registration (issuer URL).
- **Scope:** trust policy = *who may assume the role*; role permission policy = *what it can do*. GitHub's only levers = `id-token: write` + the identity claims.
- **Mechanics:** cloud's official login action (`aws-actions/configure-aws-credentials`, `azure/login`, `google-github-actions/auth`), or manual fetch via `ACTIONS_ID_TOKEN_REQUEST_URL` + `ACTIONS_ID_TOKEN_REQUEST_TOKEN` (`getIDToken()` helper).

## Bit 2 — Trust config & claims

- **`sub` format:** `repo:<owner>/<repo>:<ref-type>:<ref>`. Forms: `ref:refs/heads/<branch>`, `ref:refs/tags/<tag>`, `environment:<name>`, `pull_request`.
- **`pull_request` sub is stable, no PR number** → conditioning on it trusts ALL PRs incl. forks. Never for production.
- **`aud`:** defaults to owner URL; cloud actions set it (AWS `sts.amazonaws.com`). Condition on `aud` AND `sub`.
- **AWS condition keys:** `token.actions.githubusercontent.com:aud` / `:sub`. Azure = federated credential; GCP = workload identity pool. Same concept.
- **Four misconfigs:** (1) `aud`-only = all of GitHub; (2) `repo:org/*` (wildcard-eval) = whole org incl. forks/dependabot/new repos; (3) wildcard under `StringEquals` = matches nothing, use `StringLike`; (4) production on `pull_request` = any PR author incl. forks.
- **Best pattern:** scope to `:environment:NAME` (stable across triggers) **+ environment protection rules** (the actual gate).
- **Granularity:** customize `sub` template via REST (`include_claim_keys`); condition on `repository_id`, `repository_visibility`, `repo_property_*`; `job_workflow_ref` for reusable workflows.
- **⚠ Immutable subject claims:** repos created after **2026-07-15** default to `sub` with owner_id + repo_id → `repo:org@123456/repo@456789:...` (anti namespace-recycling). Old repos opt in (settings UI / REST). **Not** on GHES. Trust policy must match the repo's actual format.
