from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page


class CartPage(Page):
    CART_HEADER = (By.CSS_SELECTOR, "[data-test*='boxEmptyMsg'] h1")
    SIGNIN_BTN_EMPTY_CART = (By.CSS_SELECTOR, "[class*='ButtonPrimary']")

    def verify_cart_empty_message(self, empty_cart_message):
        # not sure how to implement wait until here
        sleep(8)
        actual_message = self.get_text(*self.CART_HEADER)
        assert empty_cart_message == actual_message, f"Expected {empty_cart_message} but got {actual_message}"

    def empty_cart_signin_btn_click(self):
        self.click(*self.SIGNIN_BTN_EMPTY_CART)

