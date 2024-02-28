from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_TEXT = (By.CSS_SELECTOR, "[class*='StyledHeading'] span")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#password")
    SIGN_IN_BTN = (By.CSS_SELECTOR, "#login")
    NEXT_BTN = (By.CSS_SELECTOR, "#capturePhone")
    TERMS_CONDITIONS_LINK = (By.CSS_SELECTOR, "[aria-label*='terms & conditions']")

    # def open_sign_in_page(self):
    #     self.open(
    #         "https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin")

    def click_sign_in(self):
        self.click(*self.SIGN_IN_BTN)

    def click_terms_conditions_link(self):
        self.wait_element_clickable_click(*self.TERMS_CONDITIONS_LINK)

    def input_user_email_password(self):
        self.input_text("nykeila@gudri.com", *self.INPUT_EMAIL)
        self.input_text("Test1Test12024", *self.INPUT_PASSWORD)

    def verify_user_logged_in(self):
        self.wait_element_clickable(self.NEXT_BTN)

    def verify_sign_in_form_open(self, expected_text, *locator):
        self.verify_text(expected_text, *self.SIGN_IN_TEXT)

    def verify_terms_conditions_page_open(self):
        self.verify_partial_url("https://www.target.com/c/terms-conditions/")
