## 2024-05-22 - Async Loading in Django Templates
**Learning:** For Django templates without a JS framework, hijacking the form `submit` event to inject Bootstrap spinners is a robust pattern, provided `pageshow` event is handled to support BFCache.
**Action:** Use the standard snippet (submit listener + pageshow reset) for all synchronous form submissions to improve perceived performance.
