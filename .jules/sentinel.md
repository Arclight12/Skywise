## 2026-10-20 - Exception handling leaking stack traces
**Vulnerability:** The application was not wrapping execution in try-except blocks, causing detailed unhandled internal errors and stack traces to be exposed to standard output.
**Learning:** Python scripts executed directly expose full stack traces for unhandled exceptions to the console by default. These stack traces leak internal implementation details and paths, and must be intercepted.
**Prevention:** Always implement a top-level try-except block that securely catches all `Exception` types, logs the detailed traceback securely to a private log file, and prints a generic, safe error message to the user.
