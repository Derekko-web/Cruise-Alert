## 2026-02-06 - Missing Loading States on Authentication Forms
**Learning:** Users lack feedback during authentication requests, potentially leading to confusion or double-submissions. Since the app uses Bootstrap 5 but relies on standard HTML form submissions (not AJAX), we can use the `submit` event to inject a loading spinner.
**Action:** Standardize form submission feedback by injecting a script that disables the submit button and shows a Bootstrap spinner upon valid submission. Ensure `pageshow` event restores the button state to handle browser back/forward navigation correctly.
