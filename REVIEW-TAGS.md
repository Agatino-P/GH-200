# Study-doc review tags

A lightweight triage scheme for reviewing the long study docs without forking the file
(git is the safety net — checkpoint-commit, then mark/cut freely and `git restore` to undo).

## The extension

**Todo Tree** — surfaces the tags below in a sidebar tree + highlights them in the editor.

- Marketplace: <https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree>
- Extension ID: `Gruntfuggly.todo-tree`
- Quick install on another PC: `code --install-extension Gruntfuggly.todo-tree`
  (or just open this repo — VS Code will prompt to install the recommended extension).

The workspace config lives in `.vscode/settings.json`; it activates automatically once the
extension is installed.

## First-time setup — what actually had to be installed/changed (2026-07-01)

Getting Todo Tree working took more than installing the extension. If it shows **"Nothing
found"** or its commands are **"not found"**, work through these — in the order they bit us:

1. **Install the extension** — `Gruntfuggly.todo-tree` (see links above).
2. **Trust the workspace.** Todo Tree declares no untrusted-workspace support, so in
   **Restricted Mode** VS Code disables it entirely → commands "not found" + nothing scanned.
   `Cmd+Shift+P` → **Workspaces: Manage Workspace Trust** → Trust.
3. **Install ripgrep — this was the real blocker.** Todo Tree searches with `rg`; VS Code's
   bundled copy was not found on this machine and no standalone `rg` was installed, so it
   errored with **"Failed to find vscode-ripgrep."** Fix:
   ```
   brew install ripgrep
   ```
   (Apple Silicon → `/opt/homebrew/bin/rg`; Intel Mac → `/usr/local/bin/rg`; Linux → `which rg`.)
   Do **not** install the unrelated "vscode-ripgrep" Marketplace extension — that is not the fix.
4. **Point Todo Tree at that binary** — already set in `.vscode/settings.json`:
   `"todo-tree.ripgrep.ripgrep": "/opt/homebrew/bin/rg"`. On a different machine, update this
   path to match that machine's `rg`.
5. **Fully relaunch** (`Cmd+Q`, not just "Reload Window") so the `onStartupFinished` activation
   fires cleanly after installing/enabling.

Sanity check when stuck: `View → Output` (`Cmd+Shift+U`) → **Todo Tree** channel shows the exact
ripgrep command + any error. If "Todo Tree" isn't even in that dropdown, the extension never
activated (→ trust / relaunch).

## The tags

Drop one at the **end of a line or section** while reading. They sit inside an HTML comment,
so they are **invisible in the rendered / GitHub view** — visible only in the editor source.

| Tag | Meaning | Colour | Paste this |
|-----|---------|--------|------------|
| CUT | take it out | 🔴 red | `<!-- CUT -->` |
| TBC | to be confirmed — not so sure about it | 🟡 yellow | `<!-- TBC -->` |
| TBD | to be defined — needs more info | 🔵 blue | `<!-- TBD -->` |
| IMPORTANT | high relevance — revisit on a focused pass | 🟢 green | `<!-- IMPORTANT -->` |

## Workflow

1. Commit a checkpoint (so anything is recoverable via git).
2. Read and mark — no deleting yet. The Todo Tree panel shows every mark, grouped, with counts.
3. Review a whole tag at once from the panel (e.g. all `CUT`), or `grep -n "CUT" <file>`.
4. Act in bulk — e.g. ask Claude *"remove everything tagged CUT"*, review the diff, commit.
   (Splits the judgement — yours, per line — from the mechanical deletion — bulk.)

> This file is excluded from Todo Tree scanning (see `todo-tree.filtering.excludeGlobs`),
> so the example tags above don't show up as real marks.
