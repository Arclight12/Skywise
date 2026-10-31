## 2025-11-28 - Type-Preserving Length Validation
**Vulnerability:** Input data fields like `id` could cause memory exhaustion or DoS if unvalidated lengths were passed.
**Learning:** Checking lengths of attributes without changing their types is critical in fields like `id` which might be passed as an integer, UUID, or string. Destructive string casting (or reassignment) corrupts their intended type.
**Prevention:** Cast the variable to string strictly for the length check conditional statement (e.g. `if len(str(id)) > 255:`).
