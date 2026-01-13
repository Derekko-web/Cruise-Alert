## 2024-05-24 - [Handling BFCache for Form Submission Loading States]
**Learning:** When adding loading states (disabling buttons/changing text) on synchronous form submission, the browser's Back/Forward Cache (BFCache) can leave the page in that "loading" state if the user navigates back. This confuses users who think the form is still submitting or the page is broken.
**Action:** Always attach a `pageshow` event listener to `window` that checks if the button is disabled and resets it (re-enabling and restoring original text). This ensures the page is interactive even when loaded from the cache.

## 2024-05-24 - [Layout Shifts on Button State Changes]
**Learning:** Replacing button text (e.g., "Login") with a spinner and "Loading..." often changes the button's width, causing a jarring layout shift for centered elements.
**Action:** Before changing the `innerHTML`, explicitly set the element's `style.width` to its current computed `offsetWidth` or `getComputedStyle().width`. This "locks" the dimensions and provides a smoother transition.
