# 🔐 100 Days • 100 Cybersecurity Projects

<p align="center">
  <strong>Build • Test • Document • Learn</strong><br/>
  A practical cybersecurity engineering challenge by <a href="https://github.com/devanshshukla-3004">Devansh Shukla</a>
</p>

<p align="center">
  <a href="PROJECT_TRACKER.md">Project Tracker</a> ·
  <a href="LEARNING_LOG.md">Learning Log</a> ·
  <a href="https://github.com/devanshshukla-3004">GitHub Profile</a>
</p>

---

## 🎯 About the challenge

I'm building **100 cybersecurity projects in 100 days** to strengthen practical security engineering skills through implementation, testing, documentation, and responsible experimentation.

The challenge deliberately increases in difficulty and changes the type of work over time:

**utilities → analyzers → security auditing → threat intelligence → detection engineering → SOC tooling → advanced security platforms**

This repository is the **central index**. Each substantial project lives in its own repository so its code, tests, evidence, limitations, and usage instructions can be documented independently.

## 🧭 Challenge principles

- **Build for understanding:** explain the problem, architecture, detection logic, and trade-offs.
- **Increase difficulty:** each phase should introduce new security concepts instead of repeating the same scanner pattern.
- **Be honest about status:** distinguish planned, built, tested, and published work.
- **Document reproducibly:** provide setup, usage, tests, and genuine evidence whenever practical.
- **Prioritize responsible security:** assess only systems, networks, accounts, and data I own or have explicit permission to test.
- **Prefer explainability:** security findings should include evidence and reasoning where possible.
- **Improve iteratively:** bugs, failed CI runs, limitations, and follow-up work are part of the engineering record.

## 📊 Current progress

**Days completed:** 09 / 100  
**Current phase:** Security analysis & defensive tooling  
**Next phase:** Detection engineering & SOC workflows  
**Central index:** This repository

### Progress

```text
Days 01–09   █████████░░░░░░░░░░░  09%
Days 10–25   ░░░░░░░░░░░░░░░░░░░░  Planned
Days 26–50   ░░░░░░░░░░░░░░░░░░░░  Planned
Days 51–75   ░░░░░░░░░░░░░░░░░░░░  Planned
Days 76–100  ░░░░░░░░░░░░░░░░░░░░  Planned
```

## 🧪 Project index

| Day | Project | Focus | Repository | Current status |
|---:|---|---|---|---|
| 01 | **LogSentinel** | Authentication log analysis & rule-based threat detection | [Repository](https://github.com/devanshshukla-3004/LogSentinel) · [Live dashboard](https://logsentinel-xon2pv6gnpi2cs7rtnj7ur.streamlit.app/) | ✅ Built & published |
| 02 | **NetRecon** | TCP reconnaissance, service discovery & JSON reporting | [Repository](https://github.com/devanshshukla-3004/NetRecon) | 🟡 Built & published; local verification to be recorded |
| 03 | **FileSentry** | SHA-256 file integrity monitoring | [Repository](https://github.com/devanshshukla-3004/FileSentry) | ✅ Tested & manually verified |
| 04 | **PhishLens** | Explainable phishing URL & email analysis | [Repository](https://github.com/devanshshukla-3004/PhishLens-Explainable-Phishing-URL-Email-Analyzer) | ✅ Tested & manually verified |
| 05 | **AuthShield** | Authentication security & brute-force detection | [Repository](https://github.com/devanshshukla-3004/AuthShield) | ✅ 9 tests passed; sample analysis verified |
| 06 | **IOC Inspector** | IOC extraction, normalization & heuristic triage | [Repository](https://github.com/devanshshukla-3004/IOC-Inspector) | ✅ CI green; published |
| 07 | **SecureConfig** | Windows/Linux security configuration auditing | [Repository](https://github.com/devanshshukla-3004/SecureConfig) | ✅ CI green; published |
| 08 | **HTTPShield** | HTTP security headers, redirects & cookie analysis | [Repository](https://github.com/devanshshukla-3004/HTTPShield-HTTP-Security-Header-Analyzer) | ✅ CI green; published |
| 09 | **DNSGuard** | DNS security, DNSSEC signals & mail-security configuration analysis | [Repository](https://github.com/devanshshukla-3004/DNSGuard) | ✅ CI green; published |
| 10 | **ProcHunt** | Endpoint process threat hunting & detection engineering | Repository to be created | 📋 Planned |

## 🧱 Difficulty progression

The challenge is intentionally structured as an engineering progression:

| Phase | Days | Direction |
|---|---:|---|
| Foundation utilities | 01–03 | Logs, network reconnaissance, host integrity |
| Defensive analyzers | 04–06 | Phishing, authentication analytics, IOC triage |
| Security posture | 07–09 | Host configuration, HTTP security, DNS security |
| Detection engineering | 10–20 | Process telemetry, behavioral detections, correlation, MITRE ATT&CK |
| SOC engineering | 21–40 | Pipelines, alert enrichment, investigation workflows, mini-SIEM capabilities |
| Advanced security systems | 41–70 | Threat hunting, malware analysis, forensics, cloud/container security, detection platforms |
| Capstone phase | 71–100 | Larger integrated security systems and progressively harder portfolio projects |

The exact future project list may evolve, but the **difficulty progression and domain coverage** are deliberate.

## 🧰 What each project should aim to include

Where relevant:

- Clear problem statement and learning objective
- Security-focused architecture
- Reproducible installation and usage
- Tests and/or manual verification
- Evidence-backed findings
- Structured output such as JSON/CSV
- Known limitations
- Responsible-use guidance
- CI where practical
- Genuine screenshots, terminal output, or demos
- A clear distinction between an MVP and production/enterprise claims

Not every project needs a web deployment. A strong CLI security tool can be demonstrated through reproducible local execution.

## 📚 Supporting documentation

- **[Project Tracker](PROJECT_TRACKER.md)** — source of truth for scope and status.
- **[Learning Log](LEARNING_LOG.md)** — technical lessons, verification notes, bugs, and follow-ups.

## 🤝 Follow the journey

I'll share selected project releases and reflections on LinkedIn, focusing on what I built, what I learned, what broke, and how I improved it.

- **GitHub:** [@devanshshukla-3004](https://github.com/devanshshukla-3004)
- **Project tracker:** [PROJECT_TRACKER.md](PROJECT_TRACKER.md)
- **Learning log:** [LEARNING_LOG.md](LEARNING_LOG.md)

## ⚠️ Responsible use

Cybersecurity tools can affect real systems. Projects in this challenge are for education, defensive security, and authorized testing.

**Do not use these tools against systems, networks, accounts, or data without explicit permission.** Follow applicable laws, organizational policies, and engagement scope.

---

<p align="center"><em>09 days completed. 91 to go. Build it. Test it. Understand it. Document it.</em></p>
