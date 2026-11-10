## 2025-02-12 - Prevent DoS via excessive string length allocation

**Vulnerability:** String fields (`id`, `region`, `event_type`) in `DataNode` had no length validation, posing a potential DoS risk through excessive memory allocation when processing maliciously large inputs. Destructive character stripping to sanitize input could also corrupt valid characters.

**Learning:** It is crucial to enforce length limits for input data strings instead of aggressive character stripping, as stripping can corrupt valid characters (like spaces and hyphens) and cause logic errors down the line. When doing this check, cast to a string temporarily to measure length, but preserve the original data type.

**Prevention:** Add a maximum length check on raw string fields during object initialization (like `len(str(field)) <= max_len`) and raise a `ValueError` if the length is exceeded. This fails securely and prevents processing oversized data.
