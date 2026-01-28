## 2026-01-28 - [Loading States on Form Submission]
**Learning:** When implementing loading states on form submission by disabling buttons and changing text, the browser's Back/Forward Cache (BFCache) can leave the button in a disabled/loading state if the user navigates back.
**Action:** Always add a `pageshow` event listener to window to reset the button state if `event.persisted` is true or navigation type is "back_forward".
