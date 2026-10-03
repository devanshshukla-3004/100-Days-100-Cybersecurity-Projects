# 🧠 Learning Log

Use this file to record practical lessons from the challenge. Keep entries specific: what was attempted, what happened, what was learned, and what remains unverified.

## Day 01 — LogSentinel

**Focus:** Defensive security and authentication log analysis.

**Built:** A Streamlit dashboard that summarizes authentication activity and presents rule-based findings, including brute-force bursts, password-spraying patterns, failure-followed-by-success sequences, and off-hours authentication.

**Learning themes:**
- Turning authentication events into useful security summaries
- Designing explainable, rule-based detections
- Presenting findings with evidence and transparent risk scores
- Communicating defensive security findings through a dashboard

**Evidence:** [Repository](https://github.com/devanshshukla-3004/LogSentinel) · [Live dashboard](https://logsentinel-xon2pv6gnpi2cs7rtnj7ur.streamlit.app/)

**Follow-up:** Continue improving the presentation and verify changes against the deployed application. Treat example or recreated visuals as previews, not as proof of a live execution.

## Day 02 — NetRecon

**Focus:** Network security and reconnaissance.

**Built so far:** A Python command-line tool with TCP connect scanning, concurrent port checks, basic service labels, optional banner collection, target resolution, and JSON reporting.

**Learning themes:**
- Socket programming and connection timeouts
- Concurrency with a thread pool
- Parsing user-provided port ranges
- Structuring scan results and writing JSON reports
- Responsible-use boundaries for network tools

**Evidence:** [Repository](https://github.com/devanshshukla-3004/NetRecon)

**Verification still to record:** Run the tool locally against an owned system or lab, execute the tests, capture genuine output, and document any issues found. Until then, do not describe the implementation as fully tested.

## Weekly reflection template

Copy this section at the end of each week:

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

*Write down real observations. It is fine to record a failed attempt or an unresolved issue; honest technical reflection is part of the challenge.*
