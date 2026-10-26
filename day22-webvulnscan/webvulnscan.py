#!/usr/bin/env python3
"""WebVulnScan: passive checks for common web security misconfigurations.

Only sends a single ordinary GET request to the explicitly supplied URL.
Use only on systems you own or are authorized to assess.
"""
from __future__ import annotations
import argparse
import csv
import json
import ssl
import sys
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

CHECKS = {
    "content-security-policy": ("MEDIUM", "Consider a Content-Security-Policy appropriate for your application."),
    "strict-transport-security": ("MEDIUM", "Enable HSTS on HTTPS sites after confirming HTTPS works across the domain."),
    "x-content-type-options": ("LOW", "Set X-Content-Type-Options: nosniff."),
    "referrer-policy": ("LOW", "Set a deliberate Referrer-Policy, such as strict-origin-when-cross-origin."),
    "permissions-policy": ("INFO", "Consider restricting browser features that the application does not need."),
}
DISCLOSURE_HEADERS = ("server", "x-powered-by", "x-aspnet-version", "x-generator")

def validate_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ValueError("Target must be a complete http:// or https:// URL.")
    if parsed.username or parsed.password:
        raise ValueError("Credentials in target URLs are not supported.")
    return url

def analyze_response(url: str, status: int, headers) -> dict:
    normalized = {str(k).lower(): str(v) for k, v in headers.items()}
    findings = []
    for header, (severity, recommendation) in CHECKS.items():
        if header == "strict-transport-security" and urlparse(url).scheme != "https":
            continue
        if not normalized.get(header):
            findings.append({
                "severity": severity,
                "category": "Missing security header",
                "evidence": header,
                "recommendation": recommendation,
            })
    for header in DISCLOSURE_HEADERS:
        if normalized.get(header):
            findings.append({
                "severity": "INFO",
                "category": "Potential information disclosure",
                "evidence": f"{header}: {normalized[header]}",
                "recommendation": "Review whether this server or framework detail needs to be exposed.",
            })
    if urlparse(url).scheme == "http":
        findings.append({
            "severity": "HIGH",
            "category": "Unencrypted transport",
            "evidence": "Target URL uses HTTP",
            "recommendation": "Serve the application over HTTPS and redirect HTTP to HTTPS.",
        })
    return {
        "target": url,
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "http_status": status,
        "finding_count": len(findings),
        "findings": findings,
        "limitations": "Passive, single-response checks only; not proof of exploitability or a full vulnerability assessment.",
    }

def scan(url: str, timeout: float = 8.0) -> dict:
    validate_url(url)
    request = Request(url, headers={"User-Agent": "WebVulnScan/1.0 (passive security review)"}, method="GET")
    try:
        with urlopen(request, timeout=timeout, context=ssl.create_default_context()) as response:
            return analyze_response(response.geturl(), response.status, response.headers)
    except HTTPError as exc:
        return analyze_response(exc.geturl(), exc.code, exc.headers)
    except (URLError, TimeoutError, OSError) as exc:
        raise RuntimeError(f"Request failed: {exc}") from exc

def write_report(report: dict, output: str) -> None:
    if output.lower().endswith(".csv"):
        with open(output, "w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=["target", "http_status", "severity", "category", "evidence", "recommendation"])
            writer.writeheader()
            for finding in report["findings"]:
                writer.writerow({"target": report["target"], "http_status": report["http_status"], **finding})
    else:
        with open(output, "w", encoding="utf-8") as handle:
            json.dump(report, handle, indent=2)

def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Passive web security configuration checker")
    parser.add_argument("url", help="URL you own or are authorized to assess")
    parser.add_argument("--output", default="webvulnscan-report.json", help="Output .json or .csv report")
    parser.add_argument("--timeout", type=float, default=8.0, help="Request timeout in seconds")
    args = parser.parse_args(argv)
    try:
        report = scan(args.url, args.timeout)
        write_report(report, args.output)
    except (ValueError, RuntimeError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(f"Target: {report['target']}")
    print(f"HTTP status: {report['http_status']}")
    print(f"Findings: {report['finding_count']}")
    for item in report["findings"]:
        print(f"[{item['severity']}] {item['category']}: {item['evidence']}")
    print(f"Report saved: {args.output}")
    print("Note: passive checks only; findings require manual validation.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
