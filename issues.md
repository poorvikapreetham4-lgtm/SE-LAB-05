# Issues Identified – Lab 5: Static Code Analysis

**Project:** Movie Theater Ticket Booking System  
**File Analyzed:** `ticket_booking_system.py`  
**Tools Used:** Pylint, Flake8, Bandit

## 1. Issues Identified

The following issues were identified during static code analysis of the original program. They are arranged by severity.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Weak MD5 Hashing | Security – High | 47 | MD5 is a weak hashing algorithm and is not suitable for security-sensitive applications. | Replaced MD5 with SHA-256 using the hashlib module. |
| Unsafe Shell Command Execution | Security – High | 58 | `os.system()` executes shell commands and may expose the application to command injection. | Removed `os.system()` and used a normal print statement. |
| Unsafe eval() Usage | Security – Medium | 42 | `eval()` executes dynamically supplied expressions and may allow arbitrary code execution. | Replaced `eval()` with a safe discount calculation using numeric input. |
| Bare Exception Handling | Code Quality – Low | 26 | A bare `except` silently catches all exceptions and hides unexpected errors. | Removed the exception block and checked whether the seat exists before cancellation. |
| Insecure Random PIN Generation | Security – Low | 51 | `random.randint()` is not designed for generating security-sensitive values. | Replaced it with `secrets.randbelow()` to generate a secure four-digit PIN. |
| Mutable Default Argument | Code Quality | 15 | Using an empty list as a default argument can cause data to be shared between function calls. | Replaced the default list with `None` and initialized the list inside the function. |
| Unused Import | Code Quality | 6 | The `math` module was imported but never used. | Removed the unused import. |
| Unused Variables | Code Quality | 31, 41 | Variables such as `booking_fee` and `base_price` were assigned but not properly used in the original code. | Removed unnecessary variables and used required values in calculations. |
| Incorrect None Comparison | Code Quality | 32 | Used `== None` instead of Python's recommended `is None`. | Used `is None` for checking missing seat information. |
| Missing Function Docstrings | Code Quality | Multiple | Functions did not contain descriptions explaining their purpose. | Added descriptive docstrings to all functions. |
| Incorrect Function Naming | Code Style | 15 | `reserveSeat()` did not follow Python's snake_case naming convention. | Renamed it to `reserve_seat()`. |
| Missing Final Newline | Formatting | 82 | The original source file did not end with a newline character. | Added a newline at the end of the file. |
| Unsafe File Handling | Code Quality | 55 | The file was opened without a context manager or explicit encoding. | Used `with open()` and specified UTF-8 encoding. |
| Hardcoded Secret | Security | 70 | A secret token was hardcoded in the program and printed to the console. | Removed the hardcoded secret from the demonstration program. |

## 2. Summary of Fixes

The following improvements were made to the original program:

1. Replaced unsafe `eval()` with safe numerical discount calculations.
2. Replaced MD5 hashing with SHA-256.
3. Removed unsafe shell command execution.
4. Used the `secrets` module for secure PIN generation.
5. Improved exception handling and seat validation.
6. Removed unused imports and variables.
7. Corrected function naming and mutable default arguments.
8. Added function docstrings and improved file handling.
9. Removed the hardcoded secret.

## 3. Final Analysis

After applying the corrections, the program was analyzed again using Pylint, Flake8, and Bandit.

| Tool | Purpose | Final Result |
|---|---|---|
| Pylint | Code quality analysis | No reported issues |
| Flake8 | Coding style and formatting | No reported issues |
| Bandit | Security vulnerability analysis | No reported issues |

## 4. Conclusion

Static code analysis helped identify security vulnerabilities, coding-style violations, and maintainability problems in the original ticket booking system. By fixing these issues, the program became cleaner, safer, and easier to maintain while preserving its main functionality.