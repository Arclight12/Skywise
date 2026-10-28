## 2026-10-28 - Missing Input Validation Length Limits
**Vulnerability:** Input fields (`id`, `region`, `event_type`) in `DataNode` lacked length restrictions, which could lead to DoS by memory consumption or processing overhead if maliciously large strings were provided.
**Learning:** Even internal data models that process pre-existing data (like CSVs) should enforce length limits to defend against corrupted or maliciously modified datasets.
**Prevention:** Always validate the length of string or string-castable inputs at the point of instantiation.
