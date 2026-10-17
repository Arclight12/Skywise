## 2023-10-17 - Safe Input Length Validation
**Vulnerability:** Input fields (`id`, `region`, `event_type`) in `DataNode` lacked length validation, allowing arbitrarily large strings which can lead to memory exhaustion (DoS).
**Learning:** When validating fields that might be UUIDs, integers, or strings in Python, blindly checking `.length` can throw exceptions. Stripping characters is also dangerous as it mutates data.
**Prevention:** Explicitly cast to string `len(str(val))` before applying length limits to ensure safe, non-destructive validation that gracefully handles different input types.
