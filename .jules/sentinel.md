## 2025-02-18 - Non-Destructive Length Validation
**Vulnerability:** Application missing input length limits, posing a DoS risk through resource exhaustion, but directly modifying or stripping inputs can corrupt valid string parameters (like IDs formatted as UUIDs or complex strings).
**Learning:** Checking length via `str()` cast before assignment safely enforces a maximum constraint without destructively stripping valid characters, and respects the type of input (e.g. integer or UUID passed instead of string).
**Prevention:** Always enforce reasonable length constraints on string input in constructors/validation layers by utilizing non-destructive validation (e.g. `len(str(val)) < max_len`) rather than blindly replacing or stripping data.
