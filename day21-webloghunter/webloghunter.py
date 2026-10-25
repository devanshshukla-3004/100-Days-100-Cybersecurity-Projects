#!/usr/bin/env python3
"""WebLogHunter: offline, heuristic web access-log triage."""
from __future__ import annotations
import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from urllib.parse import unquote

LOG_RE = re.compile(r'^(?P<ip>\\S+) \\S+ \\S+ \\[(?P<time>[^]]+)\\] "(?P<method>[A-Z]+) (?P<target>.*?) HTTP/[^"]+" (?P<status>\\d{3}) (?P<size>\\S+)(?: "(?P<referer>[^"]*)" "(?P<ua>[^"]*)")?.*$')
@dataclass
class AccessEvent:
    line: int
    ip: str
    timestamp: str
    method: str
    target: str
    status: int
    user_agent: str
@dataclass
class Finding:
    rule_id: str
    severity: str
    source_ip: str
    count: int
    evidence: str
    recommendation: str

def parse_line(raw: str, line_no: int):
    m = LOG_RE.match(raw.strip())
    if not m:
        return None
    d = m.groupdict()
    return AccessEvent(line_no, d["ip"], d["time"], d["method"], d["target"], int(d["status"]), d.get("ua") or "")

def analyze(events, threshold=5):
    findings = []
    by_ip = defaultdict(list)
    patterns = [
        ("WEB_SQLI", re.compile(r"(union(?:%20|\\s)+select|select.+from|or(?:%20|\\s)+1=1|sleep\\()", re.I), "HIGH", "Review the request and validate input handling."),
        ("WEB_XSS", re.compile(r"(<script|%3cscript|javascript:|onerror=)", re.I), "HIGH", "Inspect output encoding and request context."),
        ("WEB_PATH_TRAVERSAL", re.compile(r"(\\.\\./|%2e%2e%2f|%2e%2e\\\\)", re.I), "HIGH", "Review path normalization and file-access controls."),
    ]
    for e in events:
        by_ip[e.ip].append(e)
        decoded = unquote(e.target)
        for rule, pattern, severity, rec in patterns:
            if pattern.search(decoded) or pattern.search(e.target):
                findings.append(Finding(rule, severity, e.ip, 1, f"line {e.line}: {e.method} {e.target} [{e.status}]", rec))
                break
        if e.method in {"TRACE", "TRACK", "CONNECT"}:
            findings.append(Finding("WEB_RARE_METHOD", "MEDIUM", e.ip, 1, f"line {e.line}: method={e.method} target={e.target}", "Confirm this method is required and disable it if not."))
    for ip, rows in by_ip.items():
        auth_fails = [e for e in rows if e.status in (401, 403) and re.search(r"login|signin|auth|admin", e.target, re.I)]
        if len(auth_fails) >= threshold:
            findings.append(Finding("WEB_AUTH_FAILURE_BURST", "HIGH", ip, len(auth_fails), f"{len(auth_fails)} 401/403 responses on authentication-related paths; example: {auth_fails[0].target}", "Correlate with identity-provider logs and rate-limit abusive attempts."))
        errors = [e for e in rows if e.status >= 400]
        if len(errors) >= threshold:
            findings.append(Finding("WEB_HTTP_ERROR_BURST", "MEDIUM", ip, len(errors), f"{len(errors)} HTTP 4xx/5xx responses; example: {errors[0].target}", "Check for broken clients, scanning, or application errors before concluding malicious activity."))
    return findings

def main():
    p = argparse.ArgumentParser(description="Analyze authorized Apache/Nginx access logs for suspicious patterns.")
    p.add_argument("--input", required=True, help="Path to access log")
    p.add_argument("--threshold", type=int, default=5, help="Minimum per-IP count for burst rules (default: 5)")
    p.add_argument("--json-out", default="findings.json")
    p.add_argument("--csv-out", default="findings.csv")
    args = p.parse_args()
    if args.threshold < 1:
        p.error("--threshold must be >= 1")
    events, skipped = [], 0
    for i, raw in enumerate(Path(args.input).read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        event = parse_line(raw, i)
        if event: events.append(event)
        elif raw.strip(): skipped += 1
    findings = analyze(events, args.threshold)
    Path(args.json_out).write_text(json.dumps([asdict(f) for f in findings], indent=2), encoding="utf-8")
    with Path(args.csv_out).open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(Finding.__dataclass_fields__))
        writer.writeheader()
        writer.writerows(asdict(f) for f in findings)
    print(f"WebLogHunter: parsed={len(events)} skipped={skipped} findings={len(findings)}")
    print(f"Reports: {args.json_out}, {args.csv_out}")
    for f in findings:
        print(f"[{f.severity}] {f.rule_id} | {f.source_ip} | {f.evidence}")

if __name__ == "__main__":
    main()
