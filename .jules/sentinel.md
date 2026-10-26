## 2025-02-14 - Preserving Original Types While Enforcing String Length Limits
**Vulnerability:** Potential Denial of Service (DoS) attack surface via exceptionally long input strings in uncontrolled data model instantiation, risking high memory usage.
**Learning:** Destructive operations like direct character stripping might corrupt valid inputs. Therefore, string length constraints (e.g. max 255 chars) should be enforced by strictly casting the variable to a string temporarily using `len(str(var))` without altering its underlying type (useful for integers or UUIDs passed).
**Prevention:** Always validate and constrain input sizes immediately upon ingestion using non-destructive means to cast temporarily to check size without modifying the underlying raw data.
