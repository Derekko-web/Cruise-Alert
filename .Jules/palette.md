## 2026-01-25 - Loading State & BFCache
**Learning:** Standard form submission navigations can leave buttons in a disabled state when users navigate back via browser history (BFCache).
**Action:** Always attach a `pageshow` event listener to reset loading states (enable button, restore text) when modifying form submit buttons.
