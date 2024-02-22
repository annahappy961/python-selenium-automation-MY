from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class CartPage(Page):
    CART_HEADER = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")
    SIGNIN_BTN_EMPTY_CART = (By.CSS_SELECTOR, "[class*='ButtonPrimary']")
    CART_SUMMARY = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

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

    def verify_product_price(self, product_price):
        self.verify_partial_text(product_price, *self.CART_SUMMARY)
        # actual_name = context.driver.find_element(*PRODUCT_NAME).text
        # assert context.product_name in actual_name, \
        #     f"Expected {context.product_name} but got {actual_name}"

    def verify_product_names(self, context):
        # Grab title text of every product in the cart and store in actual_names:
        actual_names = [product.text for product in self.find_elements(*self.CART_ITEM_TITLE)]
        # Sort lists before verification:
        context.product_names.sort()
        actual_names.sort()
        assert context.product_names == actual_names, f'Expected {context.product_names} did not match {actual_names}'
