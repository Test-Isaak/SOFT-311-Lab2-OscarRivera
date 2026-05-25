import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.faq_page import FAQPage
import time

def run():

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(headless=False)

        page = browser.new_page()

        faq = FAQPage(page)

        faq.open_homepage()

        faq.scroll()
        time.sleep(2)

        faq.click_faq()
        time.sleep(2)

        page.screenshot(path="screenshots/faq.png")

        assert faq.faq_is_expanded(), "FAQ did not expand correctly"

        browser.close()


if __name__ == "__main__":
    run()