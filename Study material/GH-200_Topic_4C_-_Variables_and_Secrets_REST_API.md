# GH-200 — Topic 4C Recap: Configuration Variables & Managing Secrets/Variables via REST API

**Domain 4 (Enterprise, highest weight 20–25%) · Objectives 4.7 (variables) + 4.8 (programmatic secrets/variables).**
Verified live against official GitHub Docs (Variables reference, Contexts reference, REST API for Actions secrets, Encrypting secrets for the REST API, Secrets concept) on 2026-06-22. Current-state; re-verify near exam time.

Cheat file companion: `GH-200_Cheat_4C_-_Variables_and_Secrets_REST_API.md`.

---

## Bit 1 — Configuration variables (`vars`)

Non-secret, **plaintext** config values, defined once and reused, read via the `vars` context. Three levels: **organization, repository, environment**. Secrets are the encrypted sibling (Bit 2).

### Precedence — most specific wins
Docs phrase it "the variable at the lowest level takes precedence":
```
environment  >  repository  >  organization
```
Same name at multiple levels → the closest-to-the-job level wins.

### ★ Env-level timing trap
Environment-level variables only become available on the runner **after the job starts executing**, so they do **not** overwrite values in the `env` and `vars` contexts during the **pre-job processing** phase (the part GitHub evaluates before dispatching to a runner). A var consumed in an early-evaluated spot (e.g. `runs-on`) won't pick up the env-level override.

### ★ Reusable-workflow trap
For a called (reusable) workflow, the variables used come from the **caller's** repository. The called workflow's **own** repo variables are **not** made available to it.

### Limits (GitHub.com / GHEC)
- 48 KB per individual variable
- 1,000 org · 500 per repo · 100 per environment
- **Combined org+repo total: 256 KB per workflow run.** Past that, only the org variables under the cap are served (after repo variables, sorted alphabetically). **Environment variables do not count toward the 256 KB** → push overflow config into environments.
- *(Version note: GHES uses a 10 MB combined limit instead of 256 KB.)*

### `vars` context
A name→value map of org/repo/env configuration variables, usable in expressions — including early-evaluated places like `runs-on`, `name`, `if`, `environment`:
```yaml
jobs:
  build:
    if: ${{ vars.DEPLOY_ENABLED == 'true' }}
    runs-on: ${{ vars.RUNNER }}
    environment: ${{ vars.ENV_STAGE }}
```

### Org access policy
An org-level variable (or secret) can be scoped by repository access: **all repos / private repos only / a selected list**.

### vars vs secrets (4.7 headline)
Variables are **plaintext** — visible in settings, **not** masked in logs — for non-sensitive config. Secrets are **encrypted + masked**. Same three-level structure; never put sensitive data in a variable.

### Naming
`vars.NAME` dereference requires a name starting with a letter or `_`, containing only alphanumerics / `-` / `_`. (Stricter variable-*creation* rules — no spaces, can't start with a number, `GITHUB_` prefix forbidden, case-insensitive — are the standard documented rules; not re-pulled verbatim this session.)

### Q&A outcomes (Bit 1) — 5/5
Confirmed: precedence (env wins), env-timing trap (env var can't feed `runs-on`), the 256 KB combined / env-excluded rule, reusable-workflow var sourcing (caller's repo), org access scoping. Flagged keepers: env-timing trap, reusable-workflow trap, 256 KB-combined/env-excluded.

---

## Bit 2 — Managing secrets & variables via REST API

Headline contrast (4.8): **variables = plaintext CRUD; secrets = encrypt-before-send.**

### Variables — plain CRUD, value readable
Standard REST on `/actions/variables` (no encryption):
- repo: `POST/GET /repos/{owner}/{repo}/actions/variables`, `GET/PATCH/DELETE …/variables/{name}`
- org: `/orgs/{org}/actions/variables` (+ repository-access scoping)
- env: `/repos/{owner}/{repo}/environments/{env}/variables`
- A `GET` on a variable **returns its value** in plaintext.

### Secrets — three-step encrypt-first dance
1. **GET the public key** for the target scope:
   ```bash
   GET /repos/{owner}/{repo}/actions/secrets/public-key
   # → { "key_id": "...", "key": "<base64 public key>" }
   ```
2. **Encrypt** the plaintext with that key using a **libsodium sealed box** (`crypto_box_seal`), then Base64-encode.
3. **PUT** the secret with ciphertext + key id:
   ```bash
   PUT /repos/{owner}/{repo}/actions/secrets/{name}
   { "encrypted_value": "<base64 sealed box>", "key_id": "..." }
   ```
   Org-level adds `"visibility"` + `"selected_repository_ids"` (IDs, not names).

### Why client-side encryption
The sealed box is created **before the value reaches GitHub** (same for UI and API), so the plaintext never lands in GitHub's request/exception logs; GitHub decrypts server-side only to inject it into the runtime. TLS protects transit; the sealed box adds defence against accidental logging *inside* GitHub.

### What a sealed box is (background, not a memorize-item)
libsodium public-key encryption where only the **recipient** (GitHub) has a key pair. Each call generates a throwaway **ephemeral** key pair, derives a shared key against GitHub's public key, encrypts, prepends the ephemeral public key, and discards the ephemeral private key → only GitHub can decrypt; it's "anonymous" (sender not cryptographically identified — your API token already proves who you are). Per-language wrappers: PyNaCl `SealedBox`, RbNaCl `Boxes::Sealed`, Sodium.Core `SealedPublicKeyBox`, JS `crypto_box_seal`.

### ★ The big API contrast (trap)
- **`GET` a secret never returns its value** — metadata only (name, timestamps). Values can't be read back via API (even an admin can't exfiltrate stored secret values this way).
- **`GET` a variable returns the value.**

### Scopes
repo/environment secret endpoints need collaborator access (classic token `repo` scope); org secret endpoints need `admin:org`.

### gh CLI shortcut
`gh secret set NAME` runs the whole dance (fetch public key → seal → PUT); `gh variable set NAME` for plaintext. (Stated from knowledge; CLI docs not re-pulled this session.)

### Q&A outcomes (Bit 2) — 5/5
Confirmed: create-secret order (GET key → encrypt → PUT), secret-vs-variable GET behaviour, secrets unreadable via API, client-side-encryption rationale, org `selected` visibility with repo IDs.

---

## Honesty flags (carried from teaching)
- **256 KB combined limit** is GitHub.com/GHEC; **GHES = 10 MB** — version-specific.
- **Variable naming creation rules** (no spaces, no leading digit, `GITHUB_` prefix forbidden, case-insensitive) stated as standard rules, not re-pulled verbatim this session.
- **Variables REST endpoints** (`/actions/variables` paths, PATCH-to-update, GET-returns-value) stated from the parallel API structure; the *secrets* API page was verified live, the *variables* API page was not re-pulled this turn.
- **gh CLI** commands stated from knowledge, not re-pulled this session.
- Current-state only: older docs reference `tweetsodium`; current is libsodium — taught current only.

## Cross-refs
- `vars`/`secrets`/`env` contexts & `${{ }}` setup-time vs runtime evaluation ↔ Topic 1B.
- Secret masking (raw + common encodings incl. Base64) ↔ Topic 1B.
- Environments & deployment protection ↔ Domain 5 (5.7 required reviewers).
- Next domain: Domain 5 — security/optimize (script injection, `GITHUB_TOKEN` vs PAT, OIDC, SHA pinning/immutable enforcement, required reviewers, artifact attestations/SLSA, optimization).
