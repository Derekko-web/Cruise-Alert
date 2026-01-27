## 2024-05-23 - Authentication Loading States
**Learning:** Users often double-submit forms or feel uncertain when clicking "Login" or "Sign Up" on slow connections, leading to frustration.
**Action:** Implementing a loading spinner on the submit button provides immediate visual feedback, assuring the user that the request is processing. Using `pageshow` ensures the button state is reset if the user navigates back (BFCache).
