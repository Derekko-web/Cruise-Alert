## 2026-01-04 - Loading State for Synchronous Forms
**Learning:** Adding a loading state to synchronous Django forms (that reload the page) is highly effective for perceived performance, but testing it with Playwright requires preventing the default submission to inspect the transient state.
**Action:** When adding loading indicators to standard forms, always include a test case that intercepts the submit event to verify the loading state appears before navigation.
