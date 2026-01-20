## 2024-05-22 - Handling BFCache with Loading States
**Learning:** When adding loading states to form submission buttons (disabling them), the browser's Back/Forward Cache (bfcache) can restore the page with the button still disabled if the user navigates back. This is a common UX trap.
**Action:** Always listen for the `pageshow` event and check `event.persisted` (or `performance.navigation.type === 2` as a fallback) to re-enable buttons and restore their original text.
