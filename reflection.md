# Reflection – Lab 5: Static Code Analysis

### 1. What is the purpose of static code analysis?

Static code analysis examines source code without executing the program. It helps identify programming mistakes, coding-style violations, code-quality problems, and potential security vulnerabilities before deployment.

### 2. What did you learn from Pylint, Flake8, and Bandit?

I learned that each tool serves a different purpose:

- **Pylint:** Identifies code-quality issues, naming problems, unused variables, and missing documentation.
- **Flake8:** Detects coding-style violations, formatting problems, and unused imports.
- **Bandit:** Identifies potential security vulnerabilities such as unsafe `eval()`, weak hashing algorithms, and insecure shell commands.

### 3. What were the major issues identified, and how did you fix them?

The analysis identified several issues in the original ticket booking program, including unsafe use of `eval()`, weak MD5 hashing, shell command execution using `os.system()`, insecure random PIN generation, bare exception handling, unused variables, and mutable default arguments.

I fixed these by using safe calculation logic, SHA-256 hashing, Python's `secrets` module, proper input validation, and improved exception and file handling.

### 4. Why is static code analysis important in software development?

Static code analysis improves software reliability, readability, maintainability, and security. It helps developers detect problems early, reduce debugging effort, and produce cleaner and safer applications. Using multiple analysis tools provides better coverage of different types of programming issues.