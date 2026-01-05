## 2024-01-05 - Login Button Feedback
**Learning:** Adding a loading spinner to the login button significantly improves perceived performance and prevents double-submission, but requires careful handling of form events (especially with Django's synchronous forms) to ensure the UI updates before the page reloads.
**Action:** When enhancing synchronous forms, verify the feedback state persists long enough or is verified by preventing default submission in tests. Always check if existing form validation (`checkValidity()`) is respected before showing loading states.
