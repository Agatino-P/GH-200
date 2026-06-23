# GH-200 — Topic 5B Recap: OIDC Keyless Cloud Auth

**Domain 5 (Secure & optimize, 10–15% weight) · Objective 5.5 (OIDC federation to cloud providers).**
Verified live against official GitHub Docs (OpenID Connect concept page, OpenID Connect reference, Configuring OIDC in cloud providers / AWS / Azure / GCP, Using OIDC with reusable workflows) on 2026-06-23. Current-state; re-verify near exam time.

Cheat file companion: `GH-200_Cheat_5B_-_OIDC_Keyless_Cloud_Auth.md`.

---

## Bit 1 — Concept & flow (5.5)

### The problem OIDC solves
A workflow that deploys to AWS/Azure/GCP needs to authenticate. The old way: create a cloud credential, **duplicate it** into GitHub as a long-lived secret, and present it every run. That static secret is the liability — it sits in GitHub indefinitely, must be rotated by hand, and if leaked it's valid until someone revokes it.

### The OIDC alternative — keyless
Instead of storing a cloud credential, the workflow proves *who it is* at runtime and gets a **short-lived** token back. Nothing long-lived **of the cloud's** is stored in GitHub. (Authentication still happens — but with ephemeral, GitHub-provisioned tokens, not a secret you keep. "Keyless" means no key *you own and store*, not "no auth.")

### Two tokens — keep them straight (the crux)
- **Token A — the request token** (`ACTIONS_ID_TOKEN_REQUEST_TOKEN`): GitHub injects it into the runner for the job (gated by `id-token: write`). Its only job is to authenticate the call *to GitHub's own OIDC endpoint* to mint Token B. GitHub is both ends of that exchange; **the cloud never sees Token A.** Ephemeral, per-job, never stored. Same family of machinery as `GITHUB_TOKEN`.
- **Token B — the OIDC JWT**: what GitHub mints and signs, and what actually gets sent to the cloud. It is an **identity assertion** — it carries claims (repo, ref, environment, actor…) but **no permissions**.

Mental model: Token A authenticates you *to GitHub*; Token B authenticates GitHub's *assertion about you* to the cloud.

### The flow — end to end
1. GitHub dispatches the job and injects **Token A** into the runner (requires `id-token: write`).
2. The job uses Token A to call GitHub's OIDC provider at `https://token.actions.githubusercontent.com` → GitHub signs and returns **Token B**, a JWT unique to that job.
3. The job sends **Token B** to the cloud (via the cloud's login action).
4. The cloud validates Token B (see validation order below), then returns a **short-lived access token scoped to that job**, carrying the assumed role's permissions.

The clean summary: GitHub never sees your cloud credentials; the cloud never sees any GitHub secret — the only thing crossing the wall is a signed, scoped, short-lived JWT.

### How the cloud accepts the JWT — asymmetric crypto, no shared secret
GitHub signs the JWT with its **private** key (RS256). The cloud verifies it with GitHub's **public** keys, published at the issuer's JWKS endpoint (discoverable via `https://token.actions.githubusercontent.com/.well-known/openid-configuration` → `jwks_uri`). Only GitHub's private key could produce a signature that verifies against GitHub's published public key, so a valid signature is cryptographic proof the token is authentically from GitHub and untampered. No password or shared secret ever passes between GitHub and the cloud — that's why it's keyless in both directions.

### Validation order (issuer → signature → claims)
The cloud can't "check against the public key" until it knows *whose* key set to fetch. Correct sequence:
1. Read the **`iss`** claim ("claims to be GitHub").
2. Confirm `iss` is a **trusted, registered issuer** (the one-time provider registration). If not on the trust list → reject.
3. Fetch **that issuer's** public keys from its JWKS endpoint.
4. **Verify the signature** with those keys.
5. Check **`aud`/`sub`** against the role's trust policy (Bit 2).

The issuer check is **not** redundant with the signature check — they answer different questions. Signature = *"is it real / untampered?"*. Issuer = *"is it from a signer I decided to trust?"*. The issuer step also *selects* which key set to verify against, so it must come first. (Two attacks, two defenses: a forged token claiming `iss: github` fails at signature; a genuinely-signed token from an untrusted IdP fails at the issuer/trust check.)

### The one YAML change — `id-token: write` (and its trap)
```yaml
permissions:
  id-token: write
  contents: read
```
`id-token: write` does **not** grant write to any resource. It only lets the job **request and use** the OIDC token (mint Token B). Pure identity permission. Missing it is the #1 OIDC failure. (Per the 5A rule, naming this one permission sets all others to `none` except `metadata` — add back `contents: read` if you check out code.)

### Who controls scope (since the token carries none)
Entirely the **cloud side**: authN (identity) is GitHub's; authZ (access) is the cloud's.
- **Trust policy / condition** = *who* may assume the role (claim matching — Bit 2).
- **Permission policy on the role** = *what* the assumed credentials can do (ordinary cloud IAM, nothing to do with GitHub).

Contrast with `GITHUB_TOKEN`, whose scope is set *inside* GitHub via `permissions:` because the resource being accessed *is* GitHub. With OIDC, the resource is the cloud's, so the cloud owns authZ; GitHub's only scope-side levers are whether the token is minted (`id-token: write`) and what identity claims it carries.

### Mechanics
Normally done by the cloud's official login action — `aws-actions/configure-aws-credentials`, `azure/login`, `google-github-actions/auth`. No official action? Fetch the JWT manually via the runner env vars `ACTIONS_ID_TOKEN_REQUEST_URL` + `ACTIONS_ID_TOKEN_REQUEST_TOKEN` (the toolkit's `getIDToken()` helper wraps exactly that).

Minimal AWS example (the action handles steps 1–4):
```yaml
permissions:
  id-token: write
  contents: read
steps:
  - uses: aws-actions/configure-aws-credentials@<sha>
    with:
      role-to-assume: arn:aws:iam::123456789012:role/my-deploy-role
      aws-region: us-east-1
```

---

## Bit 2 — Trust config & claims (5.5)

Step 4 in detail: once the signature proves the token is from GitHub, **the claims decide whether *this specific workflow* may assume the role.** Two claims do almost all the work — `sub` and `aud`.

### The `sub` (subject) claim — the main gate
Default format, a concatenation of metadata:
```
repo:<owner>/<repo>:<ref-type>:<ref>
```
Common forms:
```
repo:octo-org/octo-repo:ref:refs/heads/main       # a branch
repo:octo-org/octo-repo:ref:refs/tags/v1.2.3       # a tag
repo:octo-org/octo-repo:environment:production     # a job referencing an environment
repo:octo-org/octo-repo:pull_request               # a pull_request-triggered job
```

### `sub` precedence — environment > pull_request > branch/tag
The ref/tag form appears only if the job references no environment **and** wasn't PR-triggered. Resolution order:
- Job references an **environment** → `:environment:NAME`, **regardless of trigger** (including PR). Always wins.
- No environment, **PR-triggered** → `:pull_request`.
- No environment, not a PR → `:ref:refs/heads/<branch>` or `:ref:refs/tags/<tag>`.

There is **no composite `pull_request + environment` form** — the environment form replaces the others. Most common "it worked until I added an environment" failure: a condition written for `:ref:refs/heads/main` stops matching the moment the job declares an environment.

The **`pull_request` sub is stable and has no PR number** (the PR ref lives in `ref`/`job_workflow_ref`, not `sub`), so conditioning on `:pull_request` trusts **every** PR, including forks.

### The `aud` (audience) claim — secondary condition
Defaults to the owner URL (e.g. `https://github.com/octo-org`). Cloud login actions override it to the cloud's expected value (AWS `sts.amazonaws.com`). Condition on **both** `aud` and `sub`.

### Writing the condition (AWS shape)
```json
"Condition": {
  "StringEquals": {
    "token.actions.githubusercontent.com:aud": "sts.amazonaws.com",
    "token.actions.githubusercontent.com:sub": "repo:octo-org/octo-repo:ref:refs/heads/main"
  }
}
```
Azure = **federated credential** (issuer + subject match); GCP = **workload identity pool** attribute conditions. Different syntax, identical concept.

### The four classic misconfigurations
1. **`aud` only, no `sub`** — opens the role to all of GitHub.com. No scenario where correct.
2. **`repo:org/*` wildcard (under a wildcard-evaluating operator)** — whole org, incl. forks landing in the org, dependabot branches, new repos by any member.
3. **Wildcard value under `StringEquals`** — `StringEquals` does not evaluate `*`; `:ref:refs/heads/release/*` matches a branch *literally named* `release/*`. Use `StringLike` when the value contains a wildcard.
4. **Production trust on `pull_request`** — PR workflows run with the PR author's token; anyone who can open a PR (incl. external contributors on public repos) runs under that trust.

### `StringEquals` vs `StringLike` cuts both ways (refined point)
Under `StringEquals`, `*` is **literal** → a wildcard pattern matches *nothing* → the role is assumable by no one. That's a **fail-closed / too-restrictive bug, not an exposure.** The danger appears only under `StringLike`, where `*` expands and a loose pattern can grant the whole org. So "wildcard in the sub condition" is genuinely *unsafe* only when the operator evaluates wildcards. Distinguish **too-restrictive (broken)** from **too-permissive (exposure)** — they fail in opposite directions, and the `StringEquals→StringLike` "fix" is exactly the move that can flip a fail-closed bug into a real hole.

### Recommended pattern — scope to an environment (plus the consequence)
`repo:org/repo:environment:production` is the cleanest production pattern: the `sub` is **stable across all triggers**, and you can layer GitHub **environment protection rules** on top.

But mind the precedence interaction: a **PR-triggered job that references `production`** also produces `sub: ...:environment:production`, so its token **would match** a `:environment:production` cloud condition. The real defense is **not** the cloud condition — it's the **environment protection rules**, which run GitHub-side *before* the job executes. If `production` is protected (deploy restricted to `main`, required reviewers, etc.), a PR-triggered job can't enter the environment, so it never gets a token with that `sub` to begin with.

**Pairing rule:** `:environment:NAME` in a cloud trust policy is only as safe as the protection rules on that environment. Scope-to-environment and environment-protection-rules are a **pair** — neither does the job alone. A production environment with no protection rules + a trust condition on `:environment:production` is exactly the hole.

### Going more granular — customizing claims
- **Customize the `sub` template** via REST API (`PUT .../actions/oidc/customization/sub` with `include_claim_keys`) to fold in `actor`, `event_name`, `workflow`, `job_workflow_ref`, etc.
- Condition directly on standalone claims: `repository_id`, `repository_visibility`, `repo_property_*` (repository custom properties → attribute-based access control).
- For **reusable workflows**, the `job_workflow_ref` claim identifies the *called* workflow — how you scope trust to a shared central workflow.

### ⚠ Current-state flag: immutable subject claims
GitHub is moving to an **immutable `sub` format** adding owner ID and repo ID, to satisfy the OIDC rule that subjects must be unique and never reassigned (closing a namespace-recycling hole where a recycled org/repo name could reproduce an old `sub`):
```
Previous:  repo:octo-org/octo-repo:ref:refs/heads/main
Immutable: repo:octo-org@123456/octo-repo@456789:ref:refs/heads/main
```
The `@` separator is used because `@` can't appear in usernames or repo names. Per docs: repositories created after **2026-07-15** use this format by default; older repos keep the previous format unless they opt in (org/repo OIDC settings UI or REST API); renames/transfers after that date also migrate. **Not available on GitHub Enterprise Server.**

Honesty notes: (a) that date sits just ahead of "today" (2026-06-23), so whether the exam reflects it depends on when the question bank was written — the durable point is that the format *can* differ and **your trust policy must match the format the repo actually uses.** (b) "Immutable subject claims" is a **different feature** from "immutable releases/actions" (Topic 3A) — same adjective, unrelated mechanism. Don't conflate them.

---

## Quiz outcomes
- **Bit 1 quiz: 5/5.** Clean on identity-vs-permissions, `id-token: write` trap, JWT acceptance via public-key crypto + one-time provider registration, scope living cloud-side, and the two-token distinction. One refinement surfaced and resolved: JWT validation is **issuer → signature → claims**, and the issuer check is not redundant with the signature (it selects the key set and confirms a trusted signer).
- **Bit 2 / combined 5B quiz: effectively 6/6.** Correct on `sub` precedence (environment wins), the environment-protection pairing as the real PR gate, validation order, token roles, and immutable claims. The "which configs are unsafe" item exposed the refined point that `StringEquals`+wildcard fails *closed* (too restrictive), not open — recognition of all four misconfig patterns was correct; the strict "genuinely unsafe = too permissive" reading is A (aud-only) and E (pull_request).

## Cross-references
- 5B ↔ 5A (`permissions:` / `id-token: write` follows the "name one → others none except metadata" rule; OIDC is the keyless alternative to the long-lived-PAT-secret pattern).
- 5B ↔ environment protection rules (5.1, already course-covered) — the GitHub-side gate that makes environment-scoped trust safe.
- Immutable subject claims ↔ NOT the same as immutable releases (3A).

## Honesty / verification flags
- RS256, the `jwks_uri`, and the `.well-known/openid-configuration` shape are confirmed against GitHub's live discovery document.
- AWS trust-policy condition syntax (`token.actions.githubusercontent.com:sub`/`:aud`) is current and verified; Azure (federated credentials) and GCP (workload identity pools) achieve the same gate with different syntax — concept identical, exact syntax not re-pulled per provider this session.
- Immutable-subject-claims rollout date (2026-07-15) is from the current OIDC reference; treat as imminent/forward-dated relative to study time.
- AWS short-lived credential default (~1 hour, configurable up to 12h) is provider-/config-dependent — verify a specific figure before relying on it.
