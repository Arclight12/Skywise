## 2025-11-29 - [Information Leakage via Compiled Python Files]
**Vulnerability:** Compiled Python files (`.pyc` in `__pycache__` directories) were being tracked in version control. These files can leak absolute file paths from the machine where they were compiled, exposing sensitive developer environment details, usernames, and local directory structures.
**Learning:** Even generated binary artifacts can pose a minor security risk (Information Disclosure) if committed to version control.
**Prevention:** Ensure a `.gitignore` file explicitly ignores `__pycache__/` and `*.pyc` files to prevent tracking compiled bytecode files.
