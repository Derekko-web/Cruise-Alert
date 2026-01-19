## 2025-02-18 - Adding Loading States to Auth Forms
**Learning:** Users lack feedback during form submission on slower connections, leading to potential double-submits or frustration.
**Action:** Implemented a reusable pattern for button loading states that respects HTML5 validation and BFCache. Future forms should use a shared `base.html` block or a dedicated JS utility to apply this automatically.
