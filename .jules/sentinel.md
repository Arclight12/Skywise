## 2025-02-27 - Implement Input Length Limits over Destructive Stripping
**Vulnerability:** Input data string variables like id, region, and event_type had no bounds checking. Excessive length could lead to potential DoS or buffer overflow.
**Learning:** Destructive character stripping should be avoided because it can corrupt valid characters (like spaces and hyphens). Enforcing length constraints is a safer and less destructive approach.
**Prevention:** Always validate and restrict the length of incoming string parameters at the boundary (e.g., inside constructors like `DataNode`) instead of stripping out arbitrary characters. Fail securely by catching exceptions without exposing internal stack traces.
