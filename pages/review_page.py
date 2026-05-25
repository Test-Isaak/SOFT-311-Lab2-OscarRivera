from playwright.sync_api import Page
from playwright.sync_api import expect


class ReviewPage:

    def __init__(self, page: Page):
        self.page = page

    def open_products_page(self):
        self.page.goto("https://storedemo.testdino.com/products")

    def open_product(self):
        self.page.get_by_text("Rode NT1-A Condenser Mic").click()

    def click_reviews_tab(self):
        self.page.locator("[data-testid='reviews-tab']").click()

    def click_write_review_button(self):
        self.page.locator("[data-testid='write-review-button']").click()

    def fill_name(self, name):
        self.page.locator("[data-testid='review-form-name-input']").fill(name)

    def fill_email(self, email):
        self.page.locator("[data-testid='review-form-email-input']").fill(email)

    def fill_title(self, title):
        self.page.locator("[data-testid='review-form-title-input']").fill(title)

    def fill_review(self, review):
        self.page.locator("[data-testid='review-form-review-input']").fill(review)     

    def click_rating(self):
        fifth_star = self.page.locator('[data-testid="review-form-rating-5"]')

        fifth_star.wait_for(state="visible")
        fifth_star.click(force=True)

        expect(fifth_star).to_be_visible()

    def submit_review(self):
        self.page.locator("[data-testid='review-form-submit-button']").click()
