## 2024-01-20 - [Loading States for Standalone Forms]
**Learning:** Standalone Django templates (like login/signup) often lack base template scripts, requiring inline JS solutions for UX improvements. BFCache (`pageshow` event) is critical for button state reset.
**Action:** When adding submit loaders, always use `form.checkValidity()` to respect HTML5 validation and add a `pageshow` listener to reset the button state.
