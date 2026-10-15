## 2025-02-05 - Secure Exception Handling in CLI
**Vulnerability:** Unhandled exceptions in the main script dump stack traces directly to stdout, potentially exposing internal implementation details, file paths, and dependency structure to the executing user.
**Learning:** Even in local data-science CLI scripts, failing securely is important to prevent accidental leakage in environments where standard output might be piped or logged to insecure locations.
**Prevention:** Always wrap main entry points (`if __name__ == "__main__":`) in top-level `try...except` blocks that catch generic exceptions, log the full traceback to a secure log file, emit a generic error message, and explicitly exit with a non-zero status code (`sys.exit(1)`).
