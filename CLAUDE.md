# GH-200 exam prep

Study repo for the GH-200 (GitHub Actions) certification. Master question bank and quiz tooling live in `Practice/`.

- To quiz the learner, follow `Practice/QUIZ-PROTOCOL.md` exactly — script-graded, one question per turn.
- `Practice/attempts.jsonl` is the append-only system of record for all quiz results; never edit it by hand.
- Never open `Practice/sessions/*/manifest.json` or the master bank while a quiz session is running (answer leak).
- Progress narrative and session log: `GH-200_Practice_Protocol_and_Progress.md` (§6, resume point at the bottom).
