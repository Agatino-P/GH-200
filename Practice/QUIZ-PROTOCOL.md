# GH-200 Quiz Protocol (session recipe)

Scripts live in `Practice/scripts/`; run them from `Practice/` as `python3 scripts/<name>.py`. Data (`attempts.jsonl`, the banks, `sessions/`) stays in `Practice/` — the scripts resolve it via their parent dir, so the working directory doesn't matter. `attempts.jsonl` is the append-only system of record — never edit it by hand. The answer key lives only in each session's `manifest.json`, written at generation time and read only by `log_answer.py`.

## 1. Setup

```
python3 scripts/report.py                       # last scores, exclusion count, --after candidate
python3 scripts/make_session.py [--after Qnnn]
python3 scripts/validate_session.py <id>        # optional: confirm the new session matches the bank
```

`make_session.py` skips questions whose last 2 graded attempts were correct (`--exclude-recent-correct 2` is the default; `0` disables). It prints the session id and writes `sessions/<id>/questions.md`.

Sessions are **open-ended**: generate all eligible questions (no `--limit`) and quiz until the learner says stop — session length is never known in advance. Stopping mid-file is fine; unanswered questions have no log entry and stay eligible for the next session.

Hard rules for the quizmaster:
- Never open `manifest.json` or the master bank during a session.
- Never reuse or inspect a seed.

## 2. Present

Read `sessions/<id>/questions.md` **incrementally** (a chunk at a time, in order — not the whole file; it can hold the full bank). **One question per turn**: stem + options verbatim, plus the Type line (single / multi-select N correct). Then wait. The learner may ask clarifying questions before committing. No hints, no discussing options before commitment. Keep going until the learner says stop, then close (§6).

## 3. Grade

The instant the learner commits:

```
python3 scripts/log_answer.py --session <id> --qid Qnnn --answer X[,Y]
```

The script's output is the **only** source of the verdict and correct letters — never compute or guess a grade. Reveal and rationale come after the command, from the option texts already in `questions.md`.

## 4. Miss triage

Discuss each miss, agree a bucket — (a) careless, (b) fundamentals gap, (c) retention hole, (d) bad question — then:

```
python3 scripts/log_answer.py --session <id> --qid Qnnn --set-bucket b --note "..."
```

## 5. Mishaps

Leaked or garbled presentation: `--void "reason"`, move on. A duplicate log for the same question is refused; `--force` supersedes an erroneous entry (last record wins).

## 6. Close

```
python3 scripts/report.py
```

State the session's raw and adjusted score (adjusted = raw / (scored − bucket-b/d misses), target ≥77%). Commit `attempts.jsonl` + `sessions/<id>/` to git. Update the §6 session row and resume point in `GH-200_Practice_Protocol_and_Progress.md`.

## Tooling map

| File | Role |
|---|---|
| `make_session.py` | filter bank by history, shuffle (via `shuffle_bank.py`), write `questions.md` + `manifest.json` |
| `log_answer.py` | grade letter-vs-letter against the manifest, append to `attempts.jsonl` |
| `report.py` | per-session raw/adjusted scores, failed-last list, exclusion preview, per-question history |
| `validate_session.py` | post-generation integrity check: confirms a session's options + correct-answer maps match the bank exactly (`validate_session.py [session-id]`) |
| `backfill_pass1.py` | one-off, already run — Pass 1 drill log → `attempts.jsonl` (sessions `pass1-*`) |
| `quiz_log.py` | shared attempts reader (amendment/supersession merge) |
