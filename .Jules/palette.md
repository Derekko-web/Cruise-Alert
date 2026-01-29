## 2026-01-29 - Form Loading State Patterns
**Learning:** Standard form submissions in Django templates require explicit JS handling for loading states. Crucially, `pageshow` is needed to handle BFCache resets, and `checkValidity()` prevents UI freeze on validation errors.
**Action:** Use the standard snippet: `submit` listener with `checkValidity()`, followed by `pageshow` reset, for all future form buttons in this project.
