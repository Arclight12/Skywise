## 2025-02-28 - Input Validation: Length Limits vs Character Stripping
**Vulnerability:** String inputs lacking length bounds present a Denial of Service (DoS) / memory exhaustion risk. If length limits are absent or if they are "fixed" by indiscriminately stripping characters, it can corrupt valid data (e.g., stripping spaces or hyphens).
**Learning:** Enforcing hard length limits is a more secure and robust approach for string inputs than relying on destructive character stripping, which can alter intended safe characters and corrupt the input.
**Prevention:** Always implement explicit maximum length checks on all external string inputs before further processing or assignment.
