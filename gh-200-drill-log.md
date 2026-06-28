# GH-200 — Drill Log (per-question audit)

**Last updated: 2026-06-28 20:52 UTC** *(bump on every edit; `date -u`)*

*Per-question audit trail for the practice phase, mandated by practice-protocol §4.15. One entry per question, recording the four things grading needs so it is **mechanical and auditable**, never reconstructed from memory:*
*(a) the exact shuffled question as presented · (b) the source Q-ID · (c) the correct option in the shuffled frame (presented letter + content) + the shuffled→original map · (d) the grading (learner's answer + ✓/✗ by letter-vs-letter).*

**Rules (from §4.15):**
- The correct option's **shuffled letter** is written here **at presentation time**, before the learner answers.
- Grading compares the learner's letter to the recorded correct letter. **Never** glue the bank's original-answer word onto the learner's letter.
- This file is synced with project + repo + HD (§4.9) and is the audit trail behind the §6b coverage-ledger pass/fail column.

**Status:** Pass 1 reset to Q000 on 2026-06-28 (prior Q001–Q020 voided for integrity failures — see protocol §6). Next question to draw = **GHCertified Q001**. No valid entries yet.

---

## Entry format (template)

```
### <Q-ID> · <bank> · <date>
Stem: <question stem as presented>
Options (shuffled, as presented):
  A. <text>
  B. <text>
  C. <text>
  D. <text>
Shuffle map (presented → original): A→<o>, B→<o>, C→<o>, D→<o>
Correct (shuffled frame): <letter> = <content>
Learner answer: <letter> = <content>
Grade: <✓|✗>   Bucket (if ✗): <a|b|c|d>   Objective: <id>
Note: <one line, only if needed>
```

---

## Pass 1 — entries

*(none yet — begins at GHCertified Q001)*
