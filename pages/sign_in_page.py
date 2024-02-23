from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_TEXT = (By.CSS_SELECTOR, "[class*='StyledHeading'] span")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#password")
    SIGN_IN_BTN = (By.CSS_SELECTOR, "#login")
    NEXT_BTN = (By.CSS_SELECTOR, "#capturePhone")

    def verify_sign_in_form_open(self, expected_text, *locator):
        self.verify_text(expected_text, *self.SIGN_IN_TEXT)

    def input_user_email_password(self):
        self.input_text("", *self.INPUT_EMAIL)
        self.input_text("", *self.INPUT_PASSWORD)

    def click_sign_in(self):
        self.click(*self.SIGN_IN_BTN)

    def verify_user_logged_in(self):
        self.wait_element_clickable(self.NEXT_BTN)
