## 2025-02-14 - Enforce Length Limits on Input Strings Instead of Stripping
**Vulnerability:** Unbounded input string lengths (`id`, `region`, `event_type`) in `DataNode` could lead to memory exhaustion or DoS. Previous approaches used destructive character stripping which corrupted valid characters like spaces or hyphens.
**Learning:** For validating input data strings, especially fields that may contain a variety of valid formats (like regions with spaces or IDs with hyphens), enforce reasonable maximum length limits instead of destructively stripping specific characters.
**Prevention:** Add explicit `len()` checks against maximum thresholds for input string parameters during object initialization or input parsing.
