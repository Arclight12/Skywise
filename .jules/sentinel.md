## 2025-10-16 - Prevent Resource Exhaustion via Length Limits
**Vulnerability:** Unbounded string inputs in DataNode instantiation could lead to resource exhaustion (DoS) or memory corruption if arbitrarily large strings are provided.
**Learning:** When validating input data strings (e.g. in DataNode), enforce length limits instead of destructive character stripping, which corrupts valid characters like spaces or hyphens.
**Prevention:** Validate the length of all external string inputs before instantiation to ensure they fall within acceptable boundaries.
