## 2024-05-23 - [Loading States in Traditional Forms]
**Learning:** Traditional synchronous form submissions often lack feedback, leaving users uncertain if the request is processing.
**Action:** Always intercept `submit` events on forms to disable the button and show a spinner. Crucially, handle `pageshow` to reset the state if the user navigates back via BFCache.
