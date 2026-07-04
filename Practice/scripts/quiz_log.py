#!/usr/bin/env python3
"""Shared reader for attempts.jsonl, the append-only quiz system of record.

Two record kinds share the file:

    attempt   {ts, session, qid, map_old_to_new, correct, given, result,
               bucket, bucket_raw, note}
    amendment {ts, session, qid, amend: true, bucket, note}

Per (session, qid) the LAST attempt record wins (a --force re-log supersedes
earlier ones), then the last amendment's bucket/note overlay it. Amendments
exist because bucket triage happens after the grade reveal, while the file
must stay append-only.
"""

import json

RESULTS = {"correct", "incorrect", "void", "gap", "excluded"}
SCOREABLE = {"correct", "incorrect"}


class LogError(Exception):
    pass


def read_records(path):
    records = []
    with open(path, encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError as e:
                raise LogError(f"{path}:{lineno}: bad JSON: {e}")
            if not isinstance(rec, dict) or "session" not in rec or "qid" not in rec:
                raise LogError(f"{path}:{lineno}: record missing session/qid")
            records.append(rec)
    return records


def merge_attempts(records):
    """One merged dict per (session, qid), in first-seen (chronological) order."""
    merged = {}
    order = []
    for rec in records:
        key = (rec["session"], rec["qid"])
        if rec.get("amend"):
            if key not in merged:
                raise LogError(f"amendment for {key} with no prior attempt")
            if rec.get("bucket") is not None:
                merged[key]["bucket"] = rec["bucket"]
            if rec.get("note") is not None:
                merged[key]["note"] = rec["note"]
        else:
            if rec.get("result") not in RESULTS:
                raise LogError(f"{key}: bad result {rec.get('result')!r}")
            if key not in merged:
                order.append(key)
            merged[key] = dict(rec)
    return [merged[k] for k in order]


def load_attempts(path):
    return merge_attempts(read_records(path))


def history_by_qid(attempts):
    history = {}
    for a in attempts:
        history.setdefault(a["qid"], []).append(a)
    return history


def recently_correct(history, n):
    """True if the last n scoreable attempts exist and were all correct."""
    scoreable = [a for a in history if a["result"] in SCOREABLE]
    return len(scoreable) >= n and all(a["result"] == "correct" for a in scoreable[-n:])
