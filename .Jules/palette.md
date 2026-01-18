## 2026-01-18 - Standalone Auth Templates
**Learning:** Login and Signup pages are standalone and do not extend `base.html`. They rely on direct CDN links and inline styles. UX improvements like loading states must be injected directly into these files.
**Action:** Always check if a template extends `base.html` before assuming global assets (like jQuery or custom scripts) are available.
