from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SideNavigationMenu(Page):
    VIEW_CART_BTN = (By.XPATH, "//*[contains(text(), 'View cart & check out')]")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[aria-label*='Add to cart']")
    BACK_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Previous']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
    ACCOUNT_SIGN_IN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "[class*='h-text-bold h-display']")

    def open_cart_from_side_navigation(self):
        self.wait_element_clickable_click(*self.VIEW_CART_BTN)

    def click_add_to_cart(self):
        self.wait_element_clickable_click(*self.ADD_TO_CART_BTN)

    def side_nav_back_click(self):
        self.wait_element_clickable_click(*self.BACK_BUTTON)

    def account_sign_in_click(self):
        self.wait_element_clickable_click(*self.ACCOUNT_SIGN_IN)

    def store_product_name(self, context):
        product_name = self.get_text(*self.PRODUCT_NAME)
        context.product_name = product_name

    def store_product_price(self, context):
        product_price = self.get_text(*self.PRODUCT_PRICE)
        context.product_price = product_price

    def store_product_names(self, context):
        # context.wait.until(EC.presence_of_element_located(SIDE_NAV_PRODUCT_NAME), message='Side nav did not open')
        # # Why is it here?

        # TARGET_HELP_H2 = (By.XPATH, '')
        # context.wait.until(
        #     EC.text_to_be_present_in_element(TARGET_HELP_H2, 'Target Help'),
        #     message="'Target Help' text did not appear")
        current_product_name = self.get_text(*self.PRODUCT_NAME)
        try:  # try to add a product to context.product_names:
            context.product_names.append(current_product_name)
        except AttributeError:  # if context.product_names not set, set it and put the current_product_name itno it:
            context.product_names = [current_product_name]
