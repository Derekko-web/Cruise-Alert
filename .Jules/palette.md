## 2026-01-30 - Loading Spinners on Auth Forms
**Learning:** Intercepting form submission with Playwright's `route.fulfill(status=204)` allows verifying transient UI states (like loading spinners) that would otherwise be lost on page reload.
**Action:** Use this pattern to test all future "click-and-wait" interactions.
