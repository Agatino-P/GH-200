#!/usr/bin/env python3
"""One-off: convert gh-200-drill-log.md (Pass 1) into attempts.jsonl records.

The drill log has two hand-written entry formats (old: Q001-Q031 from
2026-06-28; new: Q032-Q179 from 2026-06-29, with both `→` and `->` arrow
spellings) and five outcomes: correct, incorrect, VOID, GAP (not scored),
and Q042's correct-but-EXCLUDED (leaked during a refresh). Drill-log maps
are presented<-original and get inverted to the manifest's old->new form.

Records are tagged session pass1-<date> so the protocol §6 per-session
numbers stay verifiable; a reconciliation summary is printed for checking
against §6 (session 2: raw 28/31, adjusted 28/29; 2026-06-29: 100/141).

Usage:
    backfill_pass1.py [--drill-log PATH] [--out PATH]    # refuses existing --out
"""

import argparse
import json
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.dirname(SCRIPT_DIR)  # Practice/
REPO_ROOT = os.path.dirname(DATA_DIR)
DEFAULT_LOG = os.path.join(REPO_ROOT, "gh-200-drill-log.md")
DEFAULT_OUT = os.path.join(DATA_DIR, "attempts.jsonl")

ENTRY_RE = re.compile(r"^### GHCertified (Q\d+)\b.*$", re.M)
TS_RE = re.compile(r"\(presented (2026-\d\d-\d\dT[\d:]+Z)\)")
MAP_LABEL_RE = re.compile(
    r"(?:shuffle map \(presented<-original\):|\*\*shuffle(?:→|->)orig map:\*\*)(.*)$", re.M)
PAIR_RE = re.compile(r"([A-G])<-([A-G])")
CORRECT_RE = re.compile(
    r"^(?:- \*\*Correct \(shuffled frame\):\*\*|correct \(shuffled frame\):)\s*"
    r"([A-G](?:\s*,\s*[A-G])*)", re.M)
LEARNER_RE = re.compile(
    r"^(?:- \*\*Learner answer:\*\*|learner answer:)\s*"
    r"([A-G](?:\s*,\s*[A-G])*)?(?=[\s(]|$)", re.M)
GRADE_RE = re.compile(r"^(?:- \*\*Grade:\*\*|.*\bgrade:)\s*(.+)$", re.M)
BUCKET_RE = re.compile(r"bucket[ :]*\(([a-d])\)")


def letters(group):
    return [s.strip() for s in group.split(",")] if group else []


def classify(grade_text):
    if grade_text.startswith("VOID"):
        return "void"
    if grade_text.startswith("GAP"):
        return "gap"
    if grade_text.startswith(("✓", "OK-correct")):
        return "excluded" if "EXCLUDED" in grade_text else "correct"
    if grade_text.startswith(("✗", "X-wrong")):
        return "incorrect"
    return None


def parse_entry(qid, chunk, problems):
    def fail(msg):
        problems.append(f"{qid}: {msg}")

    ts = TS_RE.search(chunk)
    if not ts:
        return fail("no presented timestamp")

    grade_m = GRADE_RE.search(chunk)
    if not grade_m:
        return fail("no grade line")
    grade_text = grade_m.group(1).strip()
    result = classify(grade_text)
    if result is None:
        return fail(f"unclassifiable grade: {grade_text!r}")
    scoreable = result in ("correct", "incorrect", "excluded")

    map_m = MAP_LABEL_RE.search(chunk)
    pairs = PAIR_RE.findall(map_m.group(1)) if map_m else []
    map_old_to_new = {orig: pres for pres, orig in pairs}
    if len(map_old_to_new) != len(pairs):
        return fail("duplicate letters in shuffle map")

    correct_m = CORRECT_RE.search(chunk)
    correct = letters(correct_m.group(1)) if correct_m else []
    learner_m = LEARNER_RE.search(chunk)
    given = letters(learner_m.group(1)) if learner_m and learner_m.group(1) else []

    if scoreable:
        if not map_old_to_new:
            return fail("no shuffle map")
        if not correct:
            return fail("no correct letters")
        if not given:
            return fail("no learner letters")
        frame = set(map_old_to_new.values())
        stray = [x for x in correct + given if x not in frame]
        if stray:
            return fail(f"letters {stray} not in presented frame {sorted(frame)}")
        expected = "correct" if set(given) == set(correct) else "incorrect"
        if result in ("correct", "incorrect") and result != expected:
            return fail(f"grade says {result} but letters say {expected} "
                        f"(correct {correct}, given {given})")

    bucket_m = BUCKET_RE.search(grade_text)
    date = ts.group(1)[:10]
    return {
        "ts": ts.group(1),
        "session": f"pass1-{date}",
        "qid": qid,
        "map_old_to_new": map_old_to_new,
        "correct": correct,
        "given": given,
        "result": result,
        "bucket": bucket_m.group(1) if bucket_m else None,
        "bucket_raw": grade_text if bucket_m else None,
        "note": None,
    }


def reconcile(records):
    sessions = {}
    for rec in records:
        sessions.setdefault(rec["session"], []).append(rec)
    for sid in sorted(sessions):
        recs = sessions[sid]
        scored = [r for r in recs if r["result"] in ("correct", "incorrect")]
        raw = sum(1 for r in scored if r["result"] == "correct")
        misses = [r for r in scored if r["result"] == "incorrect"]
        buckets = {}
        for r in misses:
            buckets[r["bucket"] or "?"] = buckets.get(r["bucket"] or "?", 0) + 1
        bd = sum(1 for r in misses if r["bucket"] in ("b", "d"))
        denom = len(scored) - bd
        others = {k: sum(1 for r in recs if r["result"] == k)
                  for k in ("void", "gap", "excluded")}
        print(f"{sid}: {len(recs)} entries — raw {raw}/{len(scored)}, "
              f"adjusted {raw}/{denom}"
              f" — miss buckets {buckets or '{}'}"
              f" — void {others['void']}, gap {others['gap']}, "
              f"excluded {others['excluded']}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--drill-log", default=DEFAULT_LOG)
    ap.add_argument("--out", default=DEFAULT_OUT)
    args = ap.parse_args()

    if os.path.exists(args.out):
        sys.exit(f"refusing to overwrite existing {args.out}")

    with open(args.drill_log, encoding="utf-8") as f:
        text = f.read()

    headers = list(ENTRY_RE.finditer(text))
    if len(headers) != 178:
        sys.exit(f"expected 178 drill-log entries, found {len(headers)}")

    problems = []
    records = []
    for m, nxt in zip(headers, headers[1:] + [None]):
        chunk = text[m.start(): nxt.start() if nxt else len(text)]
        rec = parse_entry(m.group(1), chunk, problems)
        if rec:
            records.append(rec)

    if problems:
        sys.exit("backfill aborted, nothing written:\n  " + "\n  ".join(problems))

    with open(args.out, "w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    print(f"wrote {len(records)} records to {args.out}")
    reconcile(records)


if __name__ == "__main__":
    main()
