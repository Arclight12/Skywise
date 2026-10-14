## 2025-02-14 - Missing Input Length Validation
**Vulnerability:** String inputs (`id`, `region`, `event_type`) in `DataNode` had no length validation, exposing the system to potential Denial of Service (DoS) from arbitrarily large string inputs leading to high memory usage.
**Learning:** Destructive character stripping shouldn't be used for string sanitization because it can corrupt valid values containing spaces or hyphens. Input length enforcement provides a clean security boundary.
**Prevention:** Always enforce maximum length bounds (e.g., 255 for identifiers, 100 for categorical strings) on all unconstrained external text inputs.
