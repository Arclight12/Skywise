## 2025-03-09 - Add missing input length limits (DoS risk)
**Vulnerability:** Core data models like `DataNode` allowed unbound string lengths for fields such as `id`, `region`, and `event_type`. This is a classic DoS / resource exhaustion vulnerability since loading massive strings could crash the system.
**Learning:** Data classes should strictly enforce input bounds upon instantiation to prevent memory spikes, especially when parsing untrusted input or large datasets.
**Prevention:** Always implement length constraints on string parameters in core entities using `len(str(field)) > MAX_LENGTH` checking logic at the constructor level.
