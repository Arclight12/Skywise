## 2026-09-23 - Prevented Data Corruption via Input Validation
**Vulnerability:** Core data model (`DataNode`) lacked numeric bound validation, which could allow negative file sizes or out-of-bounds percentages to be instantiated, leading to invalid logic processing in downstream systems.
**Learning:** Initial attempt to add CSV string injection sanitization to the core domain model corrupted the data internally across the system (e.g. changing integer IDs to strings). Output formatting concerns must strictly reside in export/serialization layers, not the core domain classes.
**Prevention:** Always isolate input validation (bounds, types) from output sanitization (escaping, encoding). Validate bounds defensively in constructors but leave output formatting for the final serialization step.
