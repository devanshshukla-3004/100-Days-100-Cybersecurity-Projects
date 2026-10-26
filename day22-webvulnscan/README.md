# WebVulnScan — Day 22/100

A lightweight Python tool for **passive web security configuration checks**. It inspects a single HTTP response for missing security headers, plain-HTTP transport, and potentially revealing server headers.

## Checks
- Content-Security-Policy, HSTS (HTTPS only), X-Content-Type-Options, Referrer-Policy, and Permissions-Policy
- Plain HTTP transport
- Potentially revealing Server / X-Powered-By / framework-version headers
- JSON or CSV report output

## Requirements
Python 3.10+; standard library only.

## Usage
```bash
python webvulnscan.py https://your-authorized-domain.example
python webvulnscan.py https://your-authorized-domain.example --output report.csv
python -m unittest discover -s tests -v
```

Only run this against systems you own or have explicit permission to assess. The scanner sends one ordinary GET request, does not send attack payloads, crawl paths, brute-force, or attempt exploitation. A missing header is not automatically a vulnerability; review each finding in the context of the application. This is not a replacement for a full security assessment.

## Detection approach
The tool uses a small transparent ruleset and gives each finding a severity label and a recommendation. The checks are based on common defensive guidance such as the [OWASP HTTP Headers Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html).

## Project status
Code and unit tests are committed; run the test suite locally or in CI before reporting test results.
