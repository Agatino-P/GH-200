# GH-200 Cheat — 4C: Variables & Secrets REST API

*Last-week review. Full notes: `GH-200_Topic_4C_-_Variables_and_Secrets_REST_API.md`. (Domain 4 · 4.7, 4.8)*

---

### ★ Variable precedence — MOST SPECIFIC wins
`environment > repository > organization`. Docs say "lowest level takes precedence" = closest to the job.

### ★ Env-level timing trap
Environment-level variables land on the runner **only after the job starts** ⇒ they do **NOT** overwrite `env`/`vars` during **pre-job processing**. So an env-level var can't feed `runs-on` / early-evaluated keys. Distractor bait: "set the runner via an environment variable."

### ★ Reusable-workflow trap
A called (reusable) workflow uses the **CALLER's** repository variables. The called workflow's **own** repo variables are **NOT** available to it.

### ★ 256 KB combined — env excluded
Combined **org+repo** variables = **256 KB / workflow run** (GitHub.com/GHEC; **GHES = 10 MB**). Over the cap → only org vars under it served (after repo vars, alphabetical). **Environment vars don't count** → push overflow into environments. (Other limits: 48 KB/var; 1000 org / 500 repo / 100 env.)

### ★ Variables = PLAINTEXT, Secrets = ENCRYPTED
Variables: visible in settings, **not masked**, for non-sensitive config. Secrets: libsodium-sealed + masked. Never put sensitive data in a variable.

---

### Secrets via REST — 3-step encrypt-first
1. **GET** `…/actions/secrets/public-key` → `{ key_id, key }`
2. **Encrypt** plaintext with that key via **libsodium sealed box**, Base64 it
3. **PUT** `…/actions/secrets/{name}` body `{ "encrypted_value", "key_id" }`
- Org adds `"visibility":"selected"` + `"selected_repository_ids":[...]` ← **IDs, not names**.
- Encryption is **client-side, before it reaches GitHub** → plaintext never in GitHub logs; GitHub decrypts server-side at runtime.
- Sealed box = recipient-only (GitHub) anonymous PK encryption; function `crypto_box_seal`. (Concept, not a memorize-item.)

### ★ API read-back contrast (trap)
- **GET a secret = NO value** — metadata only (name/timestamps). Values can **never** be read back via API.
- **GET a variable = returns the value** (plaintext CRUD: `POST`/`GET`/`PATCH`/`DELETE` on `/actions/variables`).

### Scopes
- repo/env secrets: collaborator access (classic `repo` scope).
- org secrets: `admin:org`.

### gh CLI
`gh secret set NAME` (does GET-key → seal → PUT for you); `gh variable set NAME` (plaintext).

---

### ⚠ Unverified / version-specific (calibrate vs practice exams)
- **256 KB** = cloud; **10 MB** = GHES.
- Variable **creation naming rules** (no spaces, no leading digit, no `GITHUB_` prefix, case-insensitive) — standard rules, not re-pulled verbatim.
- **Variables REST endpoints** stated from parallel structure (secrets API verified live; variables API page not re-pulled).
- **gh CLI** commands from knowledge, not re-pulled.
