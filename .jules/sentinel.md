## 2023-10-23 - Prevent Resource Exhaustion (DoS) in DataNode
**Vulnerability:** Missing input length validation in `DataNode` could allow maliciously crafted large string inputs to cause resource exhaustion or Denial of Service (DoS) during data processing.
**Learning:** Data models parsing untrusted or large datasets must implement length limits on key fields. We learned that `id` fields might be integers or UUIDs, so length checks must convert them to strings dynamically (`len(str(id)) > 255`) without changing the underlying type.
**Prevention:** Always enforce strict length limits on string fields or fields representation within constructors, especially when processing batch data or CSVs.
