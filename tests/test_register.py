import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.register_page import RegisterPage
import time


def test_register():

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(headless=False)

        page = browser.new_page()

        register = RegisterPage(page)

        register.open_register()

        register.fill_firstname("test")

        register.fill_lastname("python")

        register.fill_email("test@python3.com")

        register.fill_password("Qwerty123@")
        time.sleep(5)

        register.click_createaccount()
        time.sleep(3)

        page.screenshot(path="screenshots/registersuccess.png")

        assert page.get_by_role("status").text_content() == "Account created successfully! Please login to continue."

        browser.close()


if __name__ == "__main__":
    test_register()