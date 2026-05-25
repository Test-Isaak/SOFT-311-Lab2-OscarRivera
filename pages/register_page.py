from playwright.sync_api import Page


class RegisterPage:

    def __init__(self, page: Page):
        self.page = page

    def open_register(self):
        self.page.goto("https://storedemo.testdino.com/signup")

    def fill_firstname(self, firstname):
        self.page.locator("[data-testid='signup-firstname-input']").fill(firstname)

    def fill_lastname(self, lastname):
        self.page.locator("[data-testid='signup-lastname-input']").fill(lastname)

    def fill_email(self, email):
        self.page.locator("[data-testid='signup-email-input']").fill(email)

    def fill_password(self, password):
        self.page.locator("[data-testid='signup-password-input']").fill(password)

    def click_createaccount(self):
        self.page.locator("[data-testid='signup-submit-button']").click()