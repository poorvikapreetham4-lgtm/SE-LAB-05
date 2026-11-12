# Lab 5: Static Code Analysis – Ticket Booking System

## Aim
To perform static code analysis on a Movie Theater Ticket Booking System using Pylint, Flake8, and Bandit to identify and fix code quality, coding style, and security issues.

## Project Description
The Movie Theater Ticket Booking System is a Python-based application that manages theater seats and ticket reservations. It supports seat booking, cancellation, availability checking, promotional discounts, ticket hash generation, secure PIN generation, and seating chart export.

Static code analysis tools are used to improve the quality, security, readability, and maintainability of the application.

## Objectives
- Identify programming and code-quality issues.
- Detect coding-style and formatting violations.
- Identify potential security vulnerabilities.
- Fix the issues found during analysis.
- Improve code readability and maintainability.
- Verify the corrected program using all three tools.

## Technologies Used
- **Programming Language:** Python
- **Pylint:** Code quality analysis
- **Flake8:** Coding style and formatting analysis
- **Bandit:** Security vulnerability analysis

## Project Structure

```text
Lab-5/
│
├── ticket_booking_system.py
├── issues.md
├── reflection.md
├── pylint_report.txt
├── flake8_report.txt
└── bandit_report.txt
```

## Application Features
1. Reserve available theater seats.
2. Cancel existing seat reservations.
3. Check seat availability.
4. Calculate promotional ticket discounts.
5. Generate SHA-256 ticket hashes.
6. Generate secure four-digit booking PINs.
7. Export theater seating information.
8. Display the total number of sold seats.

## Installation

Install the required static analysis tools:

```bash
pip install pylint flake8 bandit
```

## Execution

Run the Python application:

```bash
python ticket_booking_system.py
```

## Static Code Analysis

### 1. Pylint – Code Quality Analysis

Pylint identifies programming errors, unused variables, naming convention violations, and missing documentation.

```bash
python -m pylint ticket_booking_system.py
```

### 2. Flake8 – Code Style Analysis

Flake8 checks coding conventions, formatting problems, unused imports, and other style violations.

```bash
python -m flake8 ticket_booking_system.py
```

### 3. Bandit – Security Analysis

Bandit identifies potential security vulnerabilities in Python applications.

```bash
python -m bandit ticket_booking_system.py
```

## Issues Identified and Fixed

The original program contained several issues, including:

- Unsafe use of `eval()`.
- Weak MD5 hashing algorithm.
- Unsafe shell command execution using `os.system()`.
- Insecure random PIN generation.
- Bare exception handling.
- Mutable default arguments.
- Unused imports and variables.
- Incorrect naming conventions.
- Missing function docstrings.
- Unsafe file handling.
- Hardcoded secret information.

These issues were corrected to improve application security, code quality, and maintainability.

Refer to **[issues.md](issues.md)** for the detailed issue analysis and fixes.

## Final Analysis Results

After fixing the identified issues, all three static analysis tools were executed again.

| Tool | Analysis | Final Result |
|---|---|---|
| Pylint | Code quality | No reported issues |
| Flake8 | Coding style | No reported issues |
| Bandit | Security analysis | No reported issues |

## Reflection

The lab helped demonstrate how static code analysis tools identify software quality and security problems without executing the source code.

Refer to **[reflection.md](reflection.md)** for the learning outcomes and reflection.

## Conclusion

Static code analysis improved the overall quality, security, readability, and maintainability of the Movie Theater Ticket Booking System. By using Pylint, Flake8, and Bandit, potential problems were identified and corrected while preserving the main functionality of the application.

---

**Software Engineering Lab – Lab 5**  
**Topic:** Static Code Analysis  
**Language:** Python
