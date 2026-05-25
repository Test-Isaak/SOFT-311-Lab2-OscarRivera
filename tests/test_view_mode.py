import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.products_page import ProductsPage
import time


def run():

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(headless=False)

        page = browser.new_page()

        products = ProductsPage(page)

        products.open_shop()
        time.sleep(2)

        products.click_list_view()
        time.sleep(2)

        page.screenshot(path="screenshots/listviewsuccess.png")

        assert "all-products-view-switcher-list" in page.content()

        browser.close()


if __name__ == "__main__":
    run()