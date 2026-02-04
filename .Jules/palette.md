## 2026-02-04 - Loading States on Standalone Forms
**Learning:** Standalone auth pages often lack the global script context found in base templates, requiring inline scripts or specific static imports for interactions like loading states.
**Action:** Always check if auth templates extend the base layout; if not, ensure required assets (like FontAwesome or scripts) are explicitly included or use inline vanilla JS for resilience.
