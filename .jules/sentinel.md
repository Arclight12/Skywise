## 2025-09-26 - Input Validation and Secure Error Handling
**Vulnerability:** Input fields (quality, cloud_cover, size_mb) lacked validation before being used in critical math/logic, and unexpected application errors could expose internal stack traces to users.
**Learning:** External data should always be sanitized and validated at boundary loading. Broad exception handling is poor for debugging, so exceptions should be scoped to validation logic to return clear, actionable, non-leaking error messages without swallowing other runtime bugs.
**Prevention:** Always validate numeric constraints bounds. Scope `try-except` blocks properly to handle known failure modes securely without masking unrelated operational errors.
