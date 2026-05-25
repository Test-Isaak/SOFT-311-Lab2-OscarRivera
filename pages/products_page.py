from playwright.sync_api import Page


class ProductsPage:

    def __init__(self, page: Page):
        self.page = page

    def open_shop(self):
        self.page.goto("https://storedemo.testdino.com/products")

    def click_list_view(self):
        self.page.locator("[data-testid='all-products-view-switcher-list']").click()