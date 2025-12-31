from playwright.sync_api import sync_playwright, expect

def verify_buttons():
    with sync_playwright() as p:
        # Launch browser with fake media stream to simulate camera
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--use-fake-ui-for-media-stream",
                "--use-fake-device-for-media-stream",
            ]
        )
        page = browser.new_page()

        # Navigate to detection page
        # Note: In a real scenario with authentication, we might need to login first.
        # But 'detection_page' url in base.html seems accessible or redirected to login.
        # Let's check if we need login. The detection_page template has {% if user.is_authenticated %}.
        # If not authenticated, the navbar shows Login/Signup.
        # But the content?
        # base.html doesn't restrict content block.
        # detection_page.html content is visible.
        # However, checking views.py would be better to know if @login_required is used.
        # Assuming it might be protected, let's try to access it directly.

        try:
            page.goto("http://localhost:8000/detection/")

            # Check if we are redirected to login
            if "login" in page.url:
                print("Redirected to login. Logging in...")
                # We need a user. I'll create one via Django shell if needed, but let's see if we can access without login first or if I can just register.
                # Actually, I can create a superuser in python script before running this.
                # Or just use the 'guest_login' if available? Login html showed "Continue as Guest".
                # Let's try to click "Continue as Guest" if we are on login page.

                # Wait for potential redirect
                page.wait_for_load_state("networkidle")

                if "login" in page.url:
                     guest_link = page.get_by_role("link", name="Continue as Guest")
                     if guest_link.count() > 0:
                         guest_link.click()
                         print("Clicked Continue as Guest")
                     else:
                         print("No guest login found.")

            # Now we should be on detection page or home.
            # If we are on home, navigate to detection.
            page.wait_for_load_state("networkidle")

            if "detection" not in page.url:
                print(f"Current URL: {page.url}. Navigating to detection page...")
                page.goto("http://localhost:8000/detection/")

            page.wait_for_load_state("networkidle")
            print(f"On page: {page.title()}")

            # 1. Verify initial state
            start_btn = page.locator("#start")
            stop_btn = page.locator("#stop")

            print("Verifying initial state...")
            expect(start_btn).to_be_enabled()
            expect(start_btn).to_have_text("Start Detection")
            expect(stop_btn).to_be_disabled()

            # 2. Click Start
            print("Clicking Start...")
            start_btn.click()

            # 3. Verify loading state
            # The transition might be fast, but we added a spinner.
            # We check if it contains the spinner icon class or text changes.
            # InnerHTML changes to include fa-spinner and text "Initializing..."

            # Wait for the button to become disabled (immediate action in JS)
            expect(start_btn).to_be_disabled()

            # Check for Loading text/icon
            # We can check if text contains "Initializing..."
            # Note: innerText might just be "Initializing..."
            # expect(start_btn).to_have_text("Initializing...")

            # It might quickly change to "Running..." if camera starts fast with fake device.
            # So we check if it is either Initializing or Running.

            page.wait_for_timeout(500) # Give it a moment

            text = start_btn.inner_text()
            print(f"Start button text: {text}")

            if "Initializing" in text or "Running" in text:
                print("PASS: Button shows loading/running state.")
            else:
                print(f"FAIL: Button text unexpected: {text}")

            # 4. Take screenshot
            page.screenshot(path="verification_screenshot.png")
            print("Screenshot taken.")

        except Exception as e:
            print(f"Error: {e}")
            page.screenshot(path="error_screenshot.png")
        finally:
            browser.close()

if __name__ == "__main__":
    verify_buttons()
