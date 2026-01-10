## 2024-05-24 - Loading States and BFCache
**Learning:** When implementing loading states on form submission by disabling buttons and changing text, the browser's Back/Forward Cache (BFCache) can cause the page to be restored in that disabled/loading state when the user navigates back.
**Action:** Always listen for the `pageshow` event and check if `event.persisted` (or just unconditionally reset) to restore the button to its original interactive state.
