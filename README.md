# Ethical Keystroke Logging Demonstration

## Overview
This project presents an **ethical and controlled demonstration of keystroke logging**
to understand how such attacks operate and why endpoint security mechanisms are critical.

The implementation is intentionally designed to be **non-malicious**:
- Execution is user-initiated
- A visible graphical interface is used
- No background persistence or remote data exfiltration is implemented

The objective is to **study attack techniques from a defensive cybersecurity perspective**
and promote awareness and prevention strategies.

---

## Problem Statement
Keystroke logging is a commonly used technique by attackers to capture sensitive
user inputs such as passwords, credentials, and confidential information.
Many users and organizations underestimate how easily such data can be intercepted
at the endpoint level.

Understanding how keystroke logging works is essential for:
- Improving endpoint security
- Enhancing user awareness
- Designing effective detection and prevention mechanisms

---

## Project Description
This project demonstrates keystroke logging using Python in a **controlled and ethical environment**.

A graphical user interface (GUI) allows users to:
- Explicitly start keystroke logging
- Stop logging at any time
- Visually confirm when logging is active

Captured keystrokes are stored locally in:
- A text file for human-readable logs
- A JSON file for structured data analysis

Special key mappings are implemented to improve readability by converting keys such as
space, enter, and backspace into meaningful representations.

This project does **not** attempt to hide execution, disguise files, or transmit data externally.

---

## Key Features
- GUI-based user consent
- Local-only keystroke logging
- Clean and readable log formatting
- Structured JSON output for analysis
- Defensive and educational focus

---

## Technologies Used
- **Programming Language:** Python 3
- **GUI Framework:** Tkinter
- **Keyboard Listener:** pynput
- **Data Storage:** Text & JSON files
- **Operating System:** Windows

---

## Ethical Disclaimer
This project is strictly intended for **educational and research purposes**.
It does not include any form of stealth execution, persistence, remote communication,
or malicious payload delivery.

The goal is to understand attacker methodologies in order to design
stronger defensive cybersecurity solutions.

---

## Learning Outcomes
- Understanding how keystroke logging attacks function
- Awareness of endpoint security risks
- Ethical considerations in cybersecurity research
- Importance of user consent and transparency

---

## Author
Rohit Patil  
Cybersecurity Intern – VOIS
