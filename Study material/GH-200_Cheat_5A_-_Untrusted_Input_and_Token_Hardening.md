# GH-200 — Cheat 5A: Untrusted Input & Token Hardening

*Full notes: `GH-200_Topic_5A_-_Untrusted_Input_and_Token_Hardening.md`. Domain 5 · objectives 5.3 + 5.4. Verified live 2026-06-23.*

---

## TRAPS FIRST

- **The half-fix.** Moving an untrusted value into an `env:` var is pointless if you then read it back as `${{ env.VAR }}`. That's still an expression → substituted into the script source at template time → still injectable. Read it the shell way: `$VAR` / `"$VAR"`.
- **Quoting ≠ a fix.** `"${{ github.event.* }}"` in a `run:` block is still vulnerable — substitution happens before the shell exists, so quotes are just text to break out of.
- **Double-quoting shell vars** is general hygiene (word-splitting), NOT the GitHub script-injection mitigation. Don't pick it as *the* fix.
- **`permissions:` — name one, lose the rest.** Naming any permission sets all unspecified ones to `none`; **`metadata` always stays read**. Unnamed perms do NOT keep their defaults.
- **Self-hosted lifetime trap.** Job ceiling is 5 days, but `GITHUB_TOKEN` only refreshes up to **24h**. Don't pick "lasts 5 days."
- **Run vs trigger.** A push/PR via `GITHUB_TOKEN` does **not trigger** a new run — the commit still **lands**, the event is suppressed at the trigger stage (no run created/queued/skipped). It's not "rejected" and not "held."
- **System fields aren't untrusted.** `pull_request.number`, `run_id`, `sha` = system-generated, not attacker-controlled. Distractors.

---

## Bit 1 — Script injection (5.3)

- **Mechanism:** `run:` builds a temp shell script with `${{ }}` substituted in **before execution** → untrusted context becomes script *source*.
- **Fix hierarchy:**
  1. Intermediate `env:` var, read as `"$VAR"` (the preferred inline-script fix).
  2. Pass the value as an action `with:` argument (also safe).
- **Untrusted sources:** issue/PR `title`, `body`, **branch/ref names** (`head_ref`), **email addresses**, `label`, `message`, `name`. Branch-name PoC: `zzz";echo${IFS}"hello";#`.
- **Defense-in-depth:** least-privilege `permissions:`, input validation, vetted/SHA-pinned actions, CodeQL / Scorecards.

## Bit 2 — `GITHUB_TOKEN` vs PAT (5.4)

- **What it is:** a **GitHub App installation token**, minted **per job**, auto-injected, never stored. Read via `secrets.GITHUB_TOKEN` or `github.token`. NOT user-bound (that's why it's safer than a PAT).
- **Three traits:** ephemeral (dies at job end) · repo-scoped (can't reach other repos) · permission-tunable.
- **Lifetime cap:** 6h hosted · self-hosted refreshable only to 24h.
- **Recursion guard:** `GITHUB_TOKEN`-pushed commits/PRs don't trigger downstream runs. Need them to? Use a **PAT or GitHub App token** — same swap that gives cross-repo reach also lifts the guard.
- **PATs:** fine-grained (recommended, repo-restrictable) > classic (every repo the user can access). Flaw = user-bound + long-lived.
- **Escalation order:** `GITHUB_TOKEN` → **GitHub App** token (cross-repo / short-lived) → **PAT** (last resort, set expiry).
