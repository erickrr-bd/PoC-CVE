# 🛡️ PoC-CVE

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Security Focus](https://img.shields.io/badge/Focus-Cybersecurity%20%26%20Research-red.svg)](#)

A centralized repository containing functional Proofs of Concept (PoC) and lab environments for specific historical and contemporary vulnerabilities. 

This repository was created to facilitate security research, malware analysis, and vulnerability validation in isolated, controlled environments.

---

## 📌 Vulnerabilities & PoCs Index

| CVE | Vulnerability Name | Severity | Attack Vector | Target Environment |
| :--- | :--- | :---: | :---: | :--- |
| **CVE-2010-1899** | IIS Repeated Parameter DoS | 🟡 Medium | Remote | IIS 5.1, 6.0, 7.0, 7.5 |
| **CVE-2021-44228** | Log4Shell (Apache Log4j2) | 🔴 Critical | Remote (RCE) | Java Application Frameworks |
| **CVE-2023-46604** | Apache ActiveMQ RCE | 🔴 Critical | Remote (RCE) | OpenWire Protocol Services |
| **CVE-2026-41651** | Pack2TheRoot (PackageKit LPE) | 🔴 Critical | Local (LPE) | Linux (D-Bus / Polkit / PackageKit) |

---

## 🔍 Detailed Vulnerability Breakdown

### 🔹 CVE-2010-1899 — Microsoft IIS Stack Consumption DoS
* **Type:** Denial of Service (DoS)
* **Description:** A stack consumption vulnerability in the ASP implementation (`asp.dll`) in Microsoft Internet Information Services (IIS) 5.1 through 7.5. Remote attackers can trigger daemon outages via specially crafted HTTP request parameters.

### 🔹 CVE-2021-44228 — Log4Shell (Apache Log4j2 RCE)
* **Type:** Remote Code Execution (RCE)
* **Description:** A critical zero-day vulnerability in the Apache Log4j 2 Java logging library. Allows unauthenticated remote attackers to execute arbitrary code via JNDI lookup parameters.

### 🔹 CVE-2023-46604 — Apache ActiveMQ RCE
* **Type:** Remote Code Execution (RCE)
* **Description:** Unauthenticated RCE vulnerability in specific versions of Apache ActiveMQ allowing attackers to run arbitrary shell commands by manipulating serialized class types in the OpenWire protocol.

### 🔹 CVE-2026-41651 — Pack2TheRoot (PackageKit LPE)
* **Type:** Local Privilege Escalation (LPE)
* **Description:** A critical security flaw affecting PackageKit on Linux systems. Allows a local, unprivileged attacker to bypass authorization rules via D-Bus race conditions and escalate privileges to `root`.

---

## ⚡ Impact Assessment

The exploits and PoCs housed in this repository demonstrate severe security impacts when left unmitigated:

* **Remote Code Execution (RCE):** Complete system takeover from external network vectors without authentication.
* **Local Privilege Escalation (LPE):** Unprivileged local users obtaining permanent superuser (`root`) access.
* **Denial of Service (DoS):** Service disruption and crash of core enterprise services via minimal traffic volume.

---

## ⚠️ Disclaimer

> **IMPORTANT:** This project is intended strictly for educational purposes, security research, and authorized penetration testing in controlled laboratory environments. 

Do not run these exploits against systems you do not own or do not have explicit, written permission to test. The author assumes no responsibility for any misuse, damage, or legal consequences resulting from the execution of the code provided in this repository.
