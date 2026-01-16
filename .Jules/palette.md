# Palette's Journal

## 2025-01-29 - Adding Loading Feedback to Synchronous Forms
**Learning:** Users on slower connections often rage-click submit buttons on synchronous Django forms because there's no immediate feedback. Adding a simple JS interceptor that disables the button and shows a spinner immediately improves perceived performance and prevents duplicate submissions.
**Action:** Apply a standard `onsubmit` script to all synchronous forms that adds a spinner and disables the button, while handling `pageshow` for bfcache restoration.
