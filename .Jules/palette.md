## 2024-10-12 - Inline Scripts and No JS Build System
**Learning:** This Django project uses inline JavaScript within templates and relies on CDNs for libraries (Bootstrap, FontAwesome). There is no `package.json` or frontend build system (no webpack/vite).
**Action:** When making frontend changes, I must edit the HTML templates directly. I cannot add npm dependencies. I must ensure inline scripts are robust and don't conflict with other scripts. Verification must rely on parsing HTML or manual checks (simulated via script parsing here) rather than running a test runner like Vitest.
