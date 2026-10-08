# 🧠 Learning Log

Record practical lessons from the challenge. Keep entries specific: what was attempted, what happened, what was learned, and what remains unverified.

## Day 01 — LogSentinel

**Focus:** Defensive security and authentication log analysis.

**Built:** A Streamlit security analytics dashboard that validates authentication events, detects brute-force bursts, password spraying, failure→success sequences, and off-hours authentication, then presents explainable findings and risk scores.

**Learning themes:** Turning raw authentication events into useful detections; designing transparent rule logic; separating evidence from risk scoring; communicating security findings through a dashboard.

**Evidence:** [Repository](https://github.com/devanshshukla-3004/LogSentinel) · [Live dashboard](https://logsentinel-xon2pv6gnpi2cs7rtnj7ur.streamlit.app/)

---

## Day 02 — NetRecon

**Focus:** Network security and reconnaissance.

**Built:** A Python CLI with TCP connect scanning, concurrent port checks, basic service identification, optional banner collection, target resolution, and JSON reporting.

**Learning themes:** Socket programming; connection timeouts; concurrency with thread pools; port-range parsing; structured reconnaissance output; responsible-use boundaries.

**Verification note:** The repository is published, but local verification was not recorded in the central log. Treat the project as built/published rather than fully verified.

**Evidence:** [Repository](https://github.com/devanshshukla-3004/NetRecon)

---

## Day 03 — FileSentry

**Focus:** Host security and file integrity monitoring.

**Built:** A Python CLI that creates SHA-256 baselines and detects modified, deleted, and newly created files, with JSON reporting and path exclusions.

**Verification:** 8 unit tests passed. Manual CLI checks verified baseline creation, clean scans, modified-file detection, deleted-file detection, and new-file detection.

**Learning themes:** Hash-based integrity checking; baseline comparison; scan-state modeling; CLI exit behavior; testing security utilities.

**Limitations:** A baseline must be protected; scans are point-in-time; hashes identify change rather than the actor; excluded paths are not monitored.

**Evidence:** [Repository](https://github.com/devanshshukla-3004/FileSentry)

---

## Day 04 — PhishLens

**Focus:** Defensive security, phishing indicators, and explainable analysis.

**Built:** An offline Python CLI that applies deterministic heuristics to URL structure and email text, returning a capped risk score, risk band, rule codes, explanations, and JSON output.

**Verification:** 8 unit tests passed. URL and sample-email CLI analysis were manually executed successfully.

**Observed behavior:** The included benign-looking example URL produced a low heuristic score, while the included suspicious email sample produced a high-risk result with multiple explainable findings.

**Learning themes:** Explainable security heuristics; false positives; communicating uncertainty; JSON CLI design; distinguishing a heuristic score from a probability or definitive verdict.

**Limitations:** No DNS/reputation lookup, redirect analysis, HTML/attachment inspection, or machine-learning model.

**Evidence:** [Repository](https://github.com/devanshshukla-3004/PhishLens-Explainable-Phishing-URL-Email-Analyzer) · [Demo guide](https://github.com/devanshshukla-3004/PhishLens-Explainable-Phishing-URL-Email-Analyzer/blob/main/docs/DEMO_GUIDE.md)

---

## Day 05 — AuthShield

**Focus:** Authentication security and SOC-style detection logic.

**Built:** An offline Python CLI that parses synthetic authentication logs and detects brute-force bursts, password spraying, failure→success sequences, repeated failures, off-hours activity, account-targeting patterns, and high-risk source behavior.

**Verification:** The repository README records a verified local run with **9 tests passing** and a sample analysis of 13 events producing 6 findings.

**Learning themes:** Sliding time windows; detection-rule thresholds; correlation of authentication events; explainable risk scoring; security report generation.

**Key engineering lesson:** Detection rules need evidence, clear thresholds, and bounded claims. A risk score is a triage aid, not proof of compromise.

**Evidence:** [Repository](https://github.com/devanshshukla-3004/AuthShield)

---

## Day 06 — IOC Inspector

**Focus:** Threat intelligence and incident-response triage.

**Built:** An offline-first IOC extraction and analysis utility supporting IPv4 addresses, domains, URLs, emails, MD5/SHA-1/SHA-256 hashes, defanged indicators, normalization, deduplication, classification, heuristic risk scoring, JSON/CSV export, and recursive text/log analysis.

**Learning themes:** Defanged IOC restoration before extraction; normalization and deduplication; deterministic heuristic scoring; machine-readable security reporting; designing security tools without mandatory external threat-intelligence APIs.

**Engineering note:** URL extraction and email punctuation handling caused CI failures during development. The issues were fixed and the final CI run passed across Python 3.10–3.13.

**Evidence:** [Repository](https://github.com/devanshshukla-3004/IOC-Inspector)

---

## Day 07 — SecureConfig

**Focus:** Host hardening and security configuration auditing.

**Built:** A read-only Windows/Linux auditor covering Windows Firewall, Microsoft Defender real-time protection, UAC, Linux SSH root-login policy, and firewall-tool visibility, with evidence, remediation guidance, status/severity models, posture scoring, JSON/CSV reports, tests, and CI.

**Learning themes:** Reading security configuration safely; separating auditing from remediation; platform-specific checks; normalized posture scoring; defensive design.

**Important limitation:** SecureConfig is a practical security-auditing utility, not a full CIS compliance scanner or enterprise hardening platform.

**Verification:** CI is green across Python 3.10–3.13.

**Evidence:** [Repository](https://github.com/devanshshukla-3004/SecureConfig)

---

## Day 08 — HTTPShield

**Focus:** Web security posture and HTTP hardening.

**Built:** A defensive HTTP analyzer that checks HTTPS transport, redirects, HSTS, CSP, X-Content-Type-Options, clickjacking protections, Referrer-Policy, Permissions-Policy, technology disclosure, and cookie security attributes including Secure, HttpOnly, SameSite, and cookie prefixes.

**Learning themes:** Translating browser security guidance into deterministic checks; parsing response headers and cookies safely; evidence-backed findings; security scoring; defensive HTTP client design.

**Verification:** GitHub Actions CI is green on the current repository.

**Important limitation:** HTTPShield is not a replacement for a full web application security assessment and does not claim OWASP compliance or certification.

**Evidence:** [Repository](https://github.com/devanshshukla-3004/HTTPShield-HTTP-Security-Header-Analyzer)

---

## Day 09 — DNSGuard

**Focus:** DNS security and infrastructure configuration analysis.

**Built:** A defensive DNS analyzer that collects A/AAAA, MX, NS, SOA, CNAME, TXT, CAA and DNSSEC-related records, follows CNAME chains, evaluates DNSSEC signals, SPF, DMARC, nameserver redundancy, and resolver visibility, and exports structured JSON/CSV reports.

**Learning themes:** Treating DNS as a security trust layer; interpreting DNSSEC signals; analyzing mail-security records; separating observable configuration from full cryptographic validation; deterministic testing of DNS-dependent logic.

**Engineering note:** Early CI failures exposed two important design problems: DMARC analysis was performing an independent network query, and a resolver finding used an invalid status enum. Both were corrected. The final CI run is green.

**Important limitation:** DNSGuard does not claim full DNSSEC chain validation, CIS/NIST compliance, or a complete DNS penetration test.

**Evidence:** [Repository](https://github.com/devanshshukla-3004/DNSGuard)

---

## Day 10 — ProcHunt (planned)

**Focus:** Endpoint process threat hunting and detection engineering.

**Planned direction:** Analyze structured process telemetry for suspicious parent/child relationships, LOLBins, encoded commands, script interpreters, privilege abuse, temporary-directory execution, and other behavioral indicators. Findings will include evidence, risk scoring, and MITRE ATT&CK mappings.

**Goal:** Move from configuration and indicator analysis into **behavioral detection engineering**.

**Status:** Planned; implementation has not started.

---

## 🧩 Cross-project lessons so far

### 1. Security tooling needs evidence

A score without evidence is difficult to investigate. The challenge is increasingly using findings that explain **what triggered, why it matters, and what to inspect next**.

### 2. Determinism matters

Network-dependent checks can make tests flaky. DNSGuard reinforced the importance of collecting external data once and passing deterministic fixtures into the analyzer.

### 3. Status is not the same as compliance

A useful MVP can be fully functional without being enterprise-grade or a compliance certification tool. Claims should match the implemented scope.

### 4. CI is part of the engineering process

Several projects exposed real bugs through CI. Fixing those failures is part of the learning outcome, not something to hide from the project history.

### 5. The challenge is becoming a security-engineering portfolio

The first nine days now cover logs, networking, host integrity, phishing, authentication, threat intelligence, host configuration, HTTP security, and DNS security. Day 10 begins the transition into endpoint detection engineering.

---

## Weekly reflection template

### Week __ — Days __ to __

**Projects built:**  
**Projects tested:**  
**Projects published:**  

**Most useful thing I learned:**  
**Most challenging issue:**  
**How I investigated or resolved it:**  
**What I would improve next time:**  
**Next week's focus:**  

---

*Record real observations. Failed attempts and unresolved issues are valuable parts of the engineering record.*
