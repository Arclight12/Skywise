## 2026-09-13 - [Data Validation & CSV Injection Prevention]
**Vulnerability:** Input fields from satellite data sources lacked both numerical bounding and sanitization for string fields, making downstream CSV reports vulnerable to Formula/CSV injection.
**Learning:** Even internal or backend scripts that aggregate data and dump to CSV must sanitize inputs, as analysts may open these reports in spreadsheet software that blindly executes formulas. Data model layers are critical chokepoints for enforcing these boundaries.
**Prevention:** Implement input range validation on object instantiation (e.g., `cloud_cover` bounded to [0.0, 1.0]) and prepend an apostrophe (`'`) to string fields that start with dangerous characters (`=`, `+`, `-`, `@`, `\t`, `\r`) before they are written to a CSV.
