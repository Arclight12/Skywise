## 2025-02-18 - Input Validation Constraints
**Vulnerability:** Unbounded string inputs in `DataNode` could lead to resource exhaustion (DoS).
**Learning:** Destructive character stripping for sanitization corrupts valid characters like spaces and hyphens in this dataset.
**Prevention:** Enforce explicit string length limits during initialization instead of character stripping to maintain data integrity while mitigating DoS risks.
