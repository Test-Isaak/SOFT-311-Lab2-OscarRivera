import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.review_page import ReviewPage

import time

def test_review():

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(headless=False)

        page = browser.new_page()

        review = ReviewPage(page)

        review.open_products_page()
        time.sleep(2)

        review.open_product()
        time.sleep(2)

        review.click_reviews_tab()
        time.sleep(2)

        review.click_write_review_button()
        time.sleep(2)

        review.fill_name("test")

        review.fill_email("test@python.com")
        time.sleep(1)

        review.click_rating()
        time.sleep(1)

        review.fill_title("Titulo de Pruebas")

        review.fill_review("Esto es una Review de Pruebas")
        time.sleep(2)

        review.submit_review()
        time.sleep(2)

        page.screenshot(path="screenshots/reviewsuccess.png")
        
        assert page.locator("[data-testid='review-title']").text_content() == "Titulo de Pruebas"

        browser.close()


if __name__ == "__main__":
    test_review()