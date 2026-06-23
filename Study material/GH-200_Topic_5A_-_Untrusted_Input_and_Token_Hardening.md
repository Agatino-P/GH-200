# GH-200 — Topic 5A Recap: Untrusted Input & Token Hardening

**Domain 5 (Secure & optimize, 10–15% weight) · Objectives 5.3 (script injection) + 5.4 (`GITHUB_TOKEN` vs PAT).**
Verified live against official GitHub Docs (Script injections concept page, Security hardening guide / Enterprise Cloud, Automatic token authentication, `GITHUB_TOKEN` concept page, Managing your personal access tokens) on 2026-06-23. Current-state; re-verify near exam time.

Cheat file companion: `GH-200_Cheat_5A_-_Untrusted_Input_and_Token_Hardening.md`.

---

## Bit 1 — Script injection (5.3)

### The core mechanism (this *is* the topic)
A step's `run:` block is **not** handed to the shell directly. GitHub first **builds a temporary shell script**, substituting every `${{ }}` expression into the script *text* at **template/parse time** — before the shell starts. Only then is the generated script executed.

Consequence: if an untrusted value is interpolated straight into `run:`, the attacker's text becomes **part of the script source**, not data the script reads. That is the injection. (Same parse-time-vs-runtime split as Topic 1B — here it's the security fallout.)

### Vulnerable pattern
```yaml
- name: Check title
  run: |
    title="${{ github.event.issue.title }}"
    echo "$title"
```
An issue title containing shell metacharacters is spliced into the generated script and executed.

### Why quoting in the YAML does NOT save you
The substitution happens at template-build time, before the shell exists. The quotes you typed are just more script text the attacker can close and break out of. Even a branch/ref name suffices: `zzz";echo${IFS}"hello";#` is a valid Git ref and is enough to break out and inject.

### Preferred fix — intermediate environment variable
```yaml
- name: Check title
  env:
    TITLE: ${{ github.event.issue.title }}
  run: |
    echo "$TITLE"
```
Why safe: the value is placed into the **process environment** as a data value and read at **runtime** via `$TITLE`. It never becomes part of the generated script's source, so the shell treats it as a string, not commands.

> **Critical sub-point (the "half-fix"):** setting an `env:` var is pointless if you then read it back as an expression — `${{ env.TITLE }}` — instead of as a real shell variable `$TITLE`. `${{ env.TITLE }}` is still an expression, so it's substituted into the script source at template time, exactly like the original vuln. The whole protection is "the shell reads it at runtime," so reference it the shell way (`$VAR` / `"$VAR"`).

### Alternative safe shape — pass as an action argument
```yaml
- uses: org/title-checker@v3
  with:
    title: ${{ github.event.issue.title }}
```
Not vulnerable: the value is passed to the action as an argument, not used to generate a shell script.

### Defense-in-depth (supporting, not the primary fix)
- Least-privilege `permissions:` so a successful injection has a weak `GITHUB_TOKEN` to abuse.
- Input validation.
- Prefer vetted / SHA-pinned actions.
- CodeQL (ExpressionInjection query) and OpenSSF Scorecards to detect injection patterns.
- Double-quoting shell variables avoids word-splitting but is **general shell hygiene**, not the GitHub-specific mitigation. Don't let an exam answer dress it up as *the* fix.

### Non-obvious untrusted sources (classic distractors)
Not just issue/PR `title` and `body`. Also **branch/ref names** and **email addresses**. Untrusted fields cluster on those ending in `body`, `*_ref` (`head_ref`), `label`, `message`, `name`, `page_name`, `title`. System-generated fields (`pull_request.number`, `run_id`, `sha`) are **not** attacker-controlled.

### Quiz outcomes (Bit 1)
- **5/5.** Correctly identified the only directly-interpolated `run:` as vulnerable; correctly separated attacker-controlled fields (title, `head_ref`, author email) from system fields (PR number, run_id); confirmed quoting is not a fix; chose the env-var indirection as the primary fix.
- **Keeper that caught the trap:** the half-fix — `env:` var defeated by re-reading it as `${{ env.VAR }}`.

---

## Bit 2 — `GITHUB_TOKEN` vs PAT (5.4)

### What `GITHUB_TOKEN` actually is
When you enable Actions on a repo, GitHub silently installs a **GitHub App** on it. `GITHUB_TOKEN` is an **installation access token** for that App, minted **fresh per job**. You never create or store it; it appears in the job and is read via `${{ secrets.GITHUB_TOKEN }}` or the `github.token` context (available even if you don't explicitly pass it to an action).

### Three defining properties (and the PAT contrast)
1. **Ephemeral** — expires when the job finishes (or at its max lifetime). Per-**job**, not per-workflow. A PAT lives until its expiry date (or forever if none set) and works from anywhere.
2. **Repo-scoped** — permissions limited to the repo containing the workflow; it cannot reach other repos. This is the headline reason to escalate to a PAT or App token.
3. **Permission-tunable (least privilege)** — shaped via the `permissions:` key at workflow or job level.

### The `permissions:` rule (exam-critical)
```yaml
permissions:
  contents: read
  issues: write
```
Naming **any** permission sets **all unspecified permissions to `none`** — with the **sole exception of `metadata`, which always gets read**. Job-level `permissions:` overrides workflow-level for that job. GitHub's recommended default posture is `contents: read` (enough to clone and build).

### Maximum lifetime depends on runner type
- **GitHub-hosted:** max job time 6 hours → token lives up to **6 hours**.
- **Self-hosted:** max job time is 5 days, **but** because it's an installation access token it can only be refreshed for up to **24 hours**. Jobs running longer than 24h must switch to a PAT or other auth. (Don't conflate the 5-day job ceiling with the token's 24h refresh cap.)

### The recursion guard (favorite trap — mind the wording)
A push or PR made **with `GITHUB_TOKEN`** does **not trigger** a new workflow run. Precise mechanics: the **commit still lands** in the repo; the event is suppressed **at the trigger stage** — no run is created, queued, or skipped; nothing downstream fires. Purpose: prevent recursive/infinite workflow runs.

This is **`GITHUB_TOKEN`-specific**. If you *need* downstream workflows to fire, authenticate the push/PR with a **PAT or a GitHub App installation token** instead — then the events trigger normally. So the same swap that grants cross-repo reach also lifts the recursion guard: one mechanism, two consequences.

### PATs — two flavors, when each fits
- **Fine-grained PAT (recommended):** restrictable to specific repositories, with fine-grained permissions.
- **PAT (classic):** broad — can access every repository the owning user can access.
- Defining weakness of *any* PAT: tied to a **user account** (carries that user's reach) and **long-lived**. GitHub's guidance: prefer the built-in `GITHUB_TOKEN`; if you need more, prefer a **GitHub App** installation token (short-lived, not user-bound) over a PAT.

### Decision frame
Default to **`GITHUB_TOKEN`** → need cross-repo, or need to trigger downstream workflows → prefer a **GitHub App** token → use a **PAT** (fine-grained > classic, with expiry) only when an App is impractical.

### Quiz outcomes (combined 5A quiz)
- **5/5.** Identified `GITHUB_TOKEN` as a per-job App installation token (not user-bound); applied the "name one → others `none`, metadata read" rule; got the recursion guard right including run-vs-trigger and the PAT/App escape hatch; chose the 24h self-hosted refresh cap over the 5-day red herring.
- **Crossover question nailed:** for "read untrusted PR title in `run:` AND push a commit that should trigger CI," chose env-var-read-as-`$TITLE` **plus** a PAT/App token — and rejected the sabotage option that re-broke the injection fix via `${{ env.TITLE }}`.

---

## Cross-references
- 5.3 ↔ Topic 1B (expression evaluation: static/parse-time vs runtime; untrusted `${{ }}`).
- 5.4 ↔ Topic 4C (secrets/variables, `permissions`) and ↔ Topic 5B next (OIDC as the keyless alternative to long-lived PAT secrets).

## Honesty / verification flags
- The full list of `permissions:` scopes (`actions`, `checks`, `contents`, `deployments`, `issues`, `packages`, `pull-requests`, `repository-projects`, `security-events`, `statuses`, plus `metadata`) is stated from a GitHub changelog + community sources; the **`metadata`-always-read** rule and the **unspecified→`none`** rule are confirmed in docs/community. The canonical current permissions-reference table was not re-pulled line-by-line this session — verify exact scope names if an item hinges on one.
- Lifetime figures (6h hosted, 24h self-hosted refresh) are from the current `GITHUB_TOKEN` concept page.
- "Default to `contents: read`" is GitHub's stated good practice, not a hard requirement.
