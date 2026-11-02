## 2024-11-02 - Preserve Object Types During Security Validation
**Vulnerability:** Missing input length limits could lead to Denial of Service (DoS) if large strings are provided to object constructors.
**Learning:** When validating attributes that may be integers, UUIDs, or strings, it is crucial to avoid inadvertently changing the type. For example, casting `id` to string for validation shouldn't alter the `self.id` attribute's original type (e.g. `self.id = str(id)`), as downstream logic may expect the original integer or UUID form.
**Prevention:** Perform validation checks by temporarily casting to string (e.g., `len(str(id)) > 255`) and keep the assignment to the original value (`self.id = id`). Also, avoid destructive character stripping which corrupts valid characters.
