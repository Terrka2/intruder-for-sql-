# Blind SQL Injection Exploitation Scripts

A collection of lightweight Python automation scripts designed to extract database data via Blind SQL Injection vulnerabilities. Originally developed to solve PortSwigger Web Security Academy lab challenges.

> **Disclaimer:** This repository is created for educational purposes and authorized penetration testing only. Do not run these scripts against targets without explicit permission.

---

## Supported Attack Techniques

The project demonstrates three distinct data-exfiltration approaches:

1. **Conditional Errors (Error-Based Blind SQLi)**  
   Forces a runtime database error (e.g., division by zero `1/0`) when a character guess is true, triggering an HTTP 500 status code.
2. **Conditional Responses (Boolean-Based Blind SQLi)**  
   Infers characters by observing changes in application UI content (e.g., presence of the `"Welcome back"` string).
3. **Time Delays (Time-Based Blind SQLi)**  
   Induces an asynchronous sleep function (`pg_sleep`) on true conditions and measures response latency via `response.elapsed`.

---

## Features

- Character-by-character brute-force logic using `string.ascii_lowercase` and `string.digits`.
- Session management using `requests.Session()` to reduce TCP handshake overhead.
- Configurable payload injection into HTTP headers and Cookie parameters (`TrackingId`).

---

## Getting Started

### Prerequisites

- Python 3.8+

```bash
pip install requests
