import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
import time


def test_login():

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(headless=False)

        page = browser.new_page()

        login = LoginPage(page)

        login.open_login()

        login.fill_email("test@python.com")

        login.fill_password("Qwerty123@")
        time.sleep(2)

        login.click_login()
        time.sleep(2)

        page.screenshot(path="screenshots/loginsuccess.png")

        assert page.get_by_role("status").text_content() == "Logged in successfully"


if __name__ == "__main__":
    test_login()