## 2025-02-12 - Missing Input Length Limits
**Vulnerability:** The application was not enforcing length limits on string inputs (`id`, `region`, `event_type`) in `DataNode`.
**Learning:** This is a DoS risk because an attacker could pass excessively large strings to exhaust memory or processing time.
**Prevention:** Enforce length limits (e.g., 255) on string inputs when constructing data models to prevent excessively large strings from being processed.
