## 2025-05-18 - [DoS Risk] Lack of Input Length Limits in DataNode
**Vulnerability:** Core data structure `DataNode` allowed unbounded string lengths for `id`, `region`, and `event_type`.
**Learning:** Python does not automatically limit string size, meaning malicious payloads or improperly formatted CSV files could overwhelm memory via massive strings, creating a potential DoS vector.
**Prevention:** Implement stringent `len()` checks during object instantiation, ensuring fields do not exceed reasonable boundaries (e.g., 255 characters). For non-string inputs (like integers or UUIDs), safely cast to string solely for the length check.
