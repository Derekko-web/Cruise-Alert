# Palette's Journal

## 2026-01-09 - Loading States & BFCache
**Learning:** When disabling submit buttons and showing loading states, the browser's Back/Forward Cache (BFCache) can restore the page with the button still disabled. This is critical in Django forms where submission is synchronous.
**Action:** Always add a `pageshow` event listener to check `event.persisted` and reset the button state.

## 2026-01-09 - Inline Script robustness
**Learning:** Hardcoding restoration text (e.g., `btn.innerText = "Login"`) is brittle.
**Action:** Capture the original text into a variable (`const originalText = btn.innerText`) at the start of the script to ensure the correct text is restored regardless of future template changes.
