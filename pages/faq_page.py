from playwright.sync_api import Page

class FAQPage:

    def __init__(self, page: Page):
        self.page = page

    def open_homepage(self):
        self.page.goto("https://storedemo.testdino.com/")

    def get_faq(self):
        return self.page.locator("details",has_text="What is TestDino Demo Store?")
    
    def scroll(self):
        faq = self.get_faq()
        faq.scroll_into_view_if_needed()

    def click_faq(self):
        faq = self.get_faq()
        faq.click()

    def faq_is_expanded(self):
        faq = self.get_faq()

        return faq.get_attribute("open") is not None