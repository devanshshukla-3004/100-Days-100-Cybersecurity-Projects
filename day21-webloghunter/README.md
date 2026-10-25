# Day 21 — WebLogHunter

A lightweight, defensive web-log analyzer that flags suspicious HTTP requests and noisy clients from access logs. It works offline on log files you are authorized to inspect.

## Features
- Apache/Nginx combined access-log parsing (common format subset)
- Detection rules for SQL injection, XSS, path traversal, suspicious HTTP methods, repeated authentication failures, and HTTP error bursts
- Evidence-backed findings with severity, source IP, rule ID, and matched request
- JSON and CSV report export
- No network scanning, exploitation, or automatic blocking

## Requirements
Python 3.10+; standard library only.

## Run
```bash
python webloghunter.py --input samples/access.log --json-out findings.json --csv-out findings.csv
python webloghunter.py --input samples/access.log --threshold 5
python -m unittest discover -s tests -v
```

## Input
One Apache/Nginx combined-style access log entry per line, e.g.
```
192.0.2.10 - - [26/Oct/2026:10:15:00 +0000] "GET /index.html HTTP/1.1" 200 123 "-" "ExampleBrowser/1.0"
```

## Detection notes
These are heuristic indicators, not proof of compromise. URL-encoded payloads are decoded for inspection; results depend on log format and rule thresholds. Validate findings manually and tune for your environment. Use only on logs you are authorized to analyze.
