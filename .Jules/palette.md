## 2025-01-22 - Loading States on Django Forms
**Learning:** Standard Django forms in this project lack client-side feedback on submission. Adding a simple inline script to disable the button and show a spinner improves perceived performance.
**Action:** Use the `pageshow` event to reset the button state to handle browser back/forward cache navigation issues.
