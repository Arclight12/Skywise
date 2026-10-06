## 2026-10-06 - Unhandled Data Serialization Errors in Date Parsing
**Vulnerability:** Information Leakage via Error Messages
**Learning:** Python's built-in `datetime.fromisoformat()` can leak user-supplied string payloads (potentially malicious or excessively long) into application stack traces if a `ValueError` is raised without suppression.
**Prevention:** Catch explicit string parsing exceptions and return generic error messages that do not reflect the raw payload. Ensure all string inputs expected by datamodels have early explicit length checks to prevent arbitrary payload evaluation or DoS via resource exhaustion.
