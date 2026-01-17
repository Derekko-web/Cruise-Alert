## 2024-05-22 - Standalone Auth Templates
**Learning:** `login.html` and `signup.html` are standalone and do not extend `base.html`, preventing global script application for things like form loading states.
**Action:** When applying global UX patterns, check for standalone templates and duplicate logic or refactor to a shared partial/base if possible.
