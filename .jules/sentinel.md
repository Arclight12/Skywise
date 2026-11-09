## 2025-11-28 - Missing Input Length Limits
**Vulnerability:** Missing input length limits on user-provided fields (like `id`, `region`, `event_type`) inside data models, which can lead to memory exhaustion and Denial of Service (DoS) attacks.
**Learning:** Data models (like `DataNode`) lacked bounds checking, relying solely on Python's memory management. Additionally, when checking lengths for identifiers, destructive stripping of characters should be avoided, and typing should be preserved.
**Prevention:** Implement strict length bounds checking for string inputs in all data constructors to reject exceptionally large payloads early, using non-destructive type preservation (e.g. `len(str(id)) > max_len`).
