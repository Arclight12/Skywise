## 2024-11-03 - Added Input Length Limits to DataNode
**Vulnerability:** The application was lacking length validation on string inputs like `id`, `region`, and `event_type` in the core `DataNode` model, making it susceptible to resource exhaustion or denial-of-service via massive payload strings during data parsing.
**Learning:** Adding validation at the instantiation boundary prevents unexpected downstream behavior. To preserve the original type constraints while ensuring security limits are enforced, input validation logic should cast to strings strictly for the length check.
**Prevention:** Incorporate maximum length limits alongside strict type parsing when deserializing input configurations or datasets into core domain objects.
