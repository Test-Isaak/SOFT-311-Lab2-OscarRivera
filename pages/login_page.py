from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

    def open_login(self):
        self.page.goto("https://storedemo.testdino.com/login")

    def fill_email(self, email):
        self.page.locator("#email").fill(email)

    def fill_password(self, password):
        self.page.locator("#password").fill(password)

    def click_login(self):
        self.page.locator("[data-testid='login-submit-button']").click()

