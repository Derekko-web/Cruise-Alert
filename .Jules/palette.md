## 2024-05-22 - Handling BFCache with Loading States
**Learning:** When adding loading states to form submissions (disabling buttons/showing spinners), relying solely on the `submit` event isn't enough to handle browser history navigation. If a user navigates back to the page, the button may remain in its disabled "Loading..." state due to the Back/Forward Cache (bfcache).
**Action:** Always include a `window.addEventListener('pageshow', ...)` handler to explicitly reset the button state when the page is restored from history.
