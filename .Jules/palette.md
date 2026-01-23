## 2025-01-28 - Async Feedback for Synchronous Forms
**Learning:** In Django templates without a JS framework, synchronous form submissions lack immediate feedback, causing user uncertainty.
**Action:** Use inline JS to listen for `submit` events, check `form.checkValidity()`, and replace the submit button content with a Bootstrap spinner. Ensure `pageshow` event restores the button state for BFCache support.
