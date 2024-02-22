from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page


class CartPage(Page):
    CART_HEADER = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")
    SIGNIN_BTN_EMPTY_CART = (By.CSS_SELECTOR, "[class*='ButtonPrimary']")
    CART_SUMMARY = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

    def open_cart(self):
        self.open('https://www.target.com/cart')

    def verify_cart_empty_message(self, empty_cart_message):
        # not sure how to implement wait until here
        sleep(10)
        self.verify_text(empty_cart_message, *self.CART_HEADER)

    def empty_cart_signin_btn_click(self):
        self.wait_element_clickable_click(*self.SIGNIN_BTN_EMPTY_CART)

    def verify_cart_items(self, expected_amount):
        self.verify_partial_text(expected_amount, *self.CART_SUMMARY)

    def verify_product_name(self, product_name):
        self.verify_partial_text(product_name, *self.PRODUCT_NAME)

        # actual_name = context.driver.find_element(*PRODUCT_NAME).text
        # assert context.product_name in actual_name, \
        #     f"Expected {context.product_name} but got {actual_name}"
