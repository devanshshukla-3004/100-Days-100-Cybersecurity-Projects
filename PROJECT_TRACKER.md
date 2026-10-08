# 📋 100-Day Project Tracker

This is the **source of truth** for project scope and status. A repository existing does not automatically mean a project is tested or complete.

## Status definitions

- **Planned** — idea and learning objective selected; implementation has not started.
- **In progress** — active development.
- **Built** — primary functionality implemented.
- **Tested** — relevant automated tests and/or manual verification completed.
- **Published** — repository documentation and supporting evidence are publicly available.
- **Complete** — the current planned scope is built, tested, documented, and published.

## Project tracker

| Day | Project | Cybersecurity area | Main learning objective | Repository / demo | Current status |
|---:|---|---|---|---|---|
| 01 | [LogSentinel](https://github.com/devanshshukla-3004/LogSentinel) | Defensive security, authentication logs | Turn authentication events into explainable detections and an investigation dashboard | [Repository](https://github.com/devanshshukla-3004/LogSentinel) · [Live dashboard](https://logsentinel-xon2pv6gnpi2cs7rtnj7ur.streamlit.app/) | **Built & published** |
| 02 | [NetRecon](https://github.com/devanshshukla-3004/NetRecon) | Network security, reconnaissance | Implement TCP connect scanning, concurrency, service labels, optional banners, and JSON reporting | [Repository](https://github.com/devanshshukla-3004/NetRecon) | **Built & published; verification to be recorded** |
| 03 | [FileSentry](https://github.com/devanshshukla-3004/FileSentry) | Host security, file integrity | Use SHA-256 baselines to detect modified, deleted, and newly created files | [Repository](https://github.com/devanshshukla-3004/FileSentry) | **Tested & manually verified** |
| 04 | [PhishLens](https://github.com/devanshshukla-3004/PhishLens-Explainable-Phishing-URL-Email-Analyzer) | Defensive security, phishing analysis | Apply transparent heuristics to URL structure and email text | [Repository](https://github.com/devanshshukla-3004/PhishLens-Explainable-Phishing-URL-Email-Analyzer) · [Demo guide](https://github.com/devanshshukla-3004/PhishLens-Explainable-Phishing-URL-Email-Analyzer/blob/main/docs/DEMO_GUIDE.md) | **Tested & manually verified** |
| 05 | [AuthShield](https://github.com/devanshshukla-3004/AuthShield) | Defensive security, authentication monitoring | Detect brute-force bursts, password spraying, failure→success sequences, repeated failures, and off-hours activity | [Repository](https://github.com/devanshshukla-3004/AuthShield) | **Tested & published; 9 tests passed** |
| 06 | [IOC Inspector](https://github.com/devanshshukla-3004/IOC-Inspector) | Threat intelligence, incident-response triage | Extract, defang, normalize, classify, score, and export IOCs | [Repository](https://github.com/devanshshukla-3004/IOC-Inspector) | **Tested & published; CI green** |
| 07 | [SecureConfig](https://github.com/devanshshukla-3004/SecureConfig) | Host security, configuration auditing | Perform read-only Windows/Linux configuration checks with evidence, remediation, and posture scoring | [Repository](https://github.com/devanshshukla-3004/SecureConfig) | **Tested & published; CI green** |
| 08 | [HTTPShield](https://github.com/devanshshukla-3004/HTTPShield-HTTP-Security-Header-Analyzer) | Web security, HTTP hardening | Analyze HTTPS, redirects, security headers, technology disclosure, and cookie security | [Repository](https://github.com/devanshshukla-3004/HTTPShield-HTTP-Security-Header-Analyzer) | **Tested & published; CI green** |
| 09 | [DNSGuard](https://github.com/devanshshukla-3004/DNSGuard) | DNS security, infrastructure security | Analyze DNS records, DNSSEC signals, SPF/DMARC, CNAME topology, nameserver redundancy, and resolver visibility | [Repository](https://github.com/devanshshukla-3004/DNSGuard) | **Tested & published; CI green** |
| 10 | ProcHunt | Endpoint security, detection engineering | Analyze process telemetry for suspicious execution chains, LOLBins, encoded commands, privilege abuse, and MITRE ATT&CK techniques | Repository to be created | **Planned** |
| 11–100 | Future projects | Varied | One clearly scoped, progressively harder cybersecurity learning objective per project | — | **Planned** |

## 🧠 Current capability progression

```text
Day 01  Log analytics
   ↓
Day 02  Network reconnaissance
   ↓
Day 03  Host integrity
   ↓
Day 04  Phishing analysis
   ↓
Day 05  Authentication detection
   ↓
Day 06  Threat-intelligence triage
   ↓
Day 07  Host configuration auditing
   ↓
Day 08  Web security posture
   ↓
Day 09  DNS security posture
   ↓
Day 10  Endpoint detection engineering
```

The objective is to move from **single-purpose utilities** toward **correlated security systems and SOC workflows**.

## ✅ Completion checklist

Before treating a project as complete, check the items that apply:

- [ ] Scope and learning outcome are clear.
- [ ] Core functionality is implemented.
- [ ] Relevant automated tests are passing.
- [ ] Manual verification is performed when useful.
- [ ] Setup and usage instructions are documented.
- [ ] Known limitations are stated honestly.
- [ ] Genuine screenshot, sample output, or demo is included when useful.
- [ ] Repository is linked from this tracker.
- [ ] CI is green when CI is part of the project.
- [ ] LinkedIn update is published, if planned.
- [ ] Responsible-use notes are included for security-sensitive tools.

## 📅 Weekly review

At the end of each seven-day period, summarize:

- Projects built, tested, and published
- New security concepts learned
- Bugs and failed approaches
- What was improved
- What remains unverified
- Next week's technical focus

**Note:** This is a learning and portfolio tracker, not a claim of certification or professional expertise.
