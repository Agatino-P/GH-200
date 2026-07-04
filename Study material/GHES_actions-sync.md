# `actions/actions-sync` — a CLI, not a workflow action

The `actions/` prefix just means "the `actions-sync` repo in GitHub's `actions` org" (same org as `actions/checkout`). Despite the name, **you never write `uses: actions/actions-sync`** — it's a standalone command-line tool an admin runs to copy GitHub.com actions onto a GitHub Enterprise Server (GHES) instance. It's the **manual** method, used when GHES is offline/air-gapped.

Runs as `pull` → `push` (or `sync` for both at once):

```
actions-sync pull --cache-dir ./cache --repo-name actions/checkout
actions-sync push --cache-dir ./cache --destination-url https://ghes.example.com
```

**Vs GitHub Connect:** GitHub Connect = automatic, live access to GitHub.com actions; `actions-sync` = manual CLI, the option when there's no live connection.
