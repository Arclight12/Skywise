## 2026-11-28 - Risk of Unbounded Input Strings
**Vulnerability:** Application parsing CSV files without enforcing input string length limits.
**Learning:** Destructive character stripping can corrupt valid strings (like spaces or hyphens). Instead, enforcing length limits provides robust protection against memory exhaustion and Denial of Service (DoS) attacks from unbounded strings.
**Prevention:** Implement strict length validations on inputs (e.g., maximum 255 characters for identifiers/names) during initialization of internal data models.
