# 🧠 Learning Log

Record practical lessons from the challenge. Keep entries specific: what was attempted, what happened, what was learned, and what remains unverified.

## Day 01 — LogSentinel

**Focus:** Defensive security and authentication log analysis.

**Built:** A Streamlit dashboard that summarizes authentication activity and presents rule-based findings, including brute-force bursts, password-spraying patterns, failure-followed-by-success sequences, and off-hours authentication.

**Learning themes:** Turning authentication events into useful summaries; designing explainable detections; presenting evidence and transparent risk scores; communicating findings through a dashboard.

**Evidence:** [Repository](https://github.com/devanshshukla-3004/LogSentinel) · [Live dashboard](https://logsentinel-xon2pv6gnpi2cs7rtnj7ur.streamlit.app/)

**Follow-up:** Continue improving presentation and verify changes against the deployed application. Treat recreated visuals as previews, not proof of live execution.

## Day 02 — NetRecon

**Focus:** Network security and reconnaissance.

**Built so far:** A Python command-line tool with TCP connect scanning, concurrent port checks, basic service labels, optional banner collection, target resolution, and JSON reporting.

**Learning themes:** Socket programming and timeouts; thread-pool concurrency; parsing port ranges; structuring results and JSON reports; responsible-use boundaries.

**Evidence:** [Repository](https://github.com/devanshshukla-3004/NetRecon)

**Verification still to record:** Run locally against an owned system or lab, execute tests, capture genuine output, and document issues. Until then, do not describe the implementation as fully tested.

## Day 03 — FileSentry

**Focus:** Host security and file integrity monitoring.

**Built:** A Python CLI that uses SHA-256 baselines to detect modified, deleted, and newly created files, with JSON reporting and path exclusions.

**Verification:** The user ran `python -m unittest discover -s tests -v`; all 8 tests passed. Manual CLI checks verified baseline creation, a clean scan, detection of a modified file, detection of a deleted file, and detection of a new file.

**Learning themes:** Hash-based integrity checks; baseline-driven comparison; distinguishing expected changes from clean scans; reporting scan outcomes; designing CLI exit codes and tests.

**Limitations to remember:** A baseline must be protected; scans are point-in-time; hash changes do not identify who changed a file; excluded paths are not monitored.

**Evidence:** [Repository](https://github.com/devanshshukla-3004/FileSentry)

## Day 04 — PhishLens

**Focus:** Defensive security, phishing indicators, and explainable analysis.

**Built:** An offline Python CLI that applies transparent heuristics to URL structure and email text, returning a capped score, risk band, rule codes, explanations, and JSON output.

**Verification:** The user ran `python -m unittest discover -s tests -v`; all 8 tests passed. The URL-analysis command and sample-email analysis command both executed successfully and returned structured JSON.

**Observed behavior:** `https://example.com/account/login` received a low score of 10 because an account-related keyword matched. The included suspicious email sample received a high score of 66 with findings for urgency language, a password reference, an action-link prompt, and a generic greeting.

**Learning themes:** Explainable rule-based analysis; JSON CLI design; false positives; communicating uncertainty; distinguishing a heuristic score from a probability or definitive verdict.

**Limitations to remember:** No DNS, reputation checks, redirect analysis, HTML or attachment inspection, or machine-learning model. Heuristics can miss threats and flag benign content.

**Evidence:** [Repository](https://github.com/devanshshukla-3004/PhishLens-Explainable-Phishing-URL-Email-Analyzer) · [Demo guide](https://github.com/devanshshukla-3004/PhishLens-Explainable-Phishing-URL-Email-Analyzer/blob/main/docs/DEMO_GUIDE.md)

## Day 05 — AuthShield (planned)

**Focus:** Authentication log analysis and brute-force detection.

**Goal:** Build a command-line analyzer for synthetic authentication events, with explainable detections for repeated failures, failures across multiple accounts from one source, and successful logins following repeated failures.

**Status:** Planned only; implementation and verification have not started.

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

*Record real observations. Failed attempts and unresolved issues are valuable parts of the learning process.*