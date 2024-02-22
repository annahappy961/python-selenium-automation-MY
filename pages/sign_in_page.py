from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_TEXT = (By.CSS_SELECTOR, "[class*='StyledHeading'] span")

    def verify_sign_in_form_open(self, expected_text, *locator):
        self.verify_text(expected_text, *self.SIGN_IN_TEXT)
