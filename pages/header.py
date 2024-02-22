from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    HEADER = (By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")
    HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader']")
    SIGN_IN = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")

    def search_product(self, search_product):
        self.input_text(search_product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON)
        sleep(6)

    def click_cart(self):
        self.click(*self.CART_ICON)

    def verify_header(self):
        # header = context.driver.find_element(*HEADER)
        # print(header)
        self.find_element(*self.HEADER)

    def verify_header_links(self, expected_amount):
        expected_amount = int(expected_amount)
        header_links = self.find_elements(*self.HEADER_LINKS)
        assert len(header_links) == expected_amount, f'Expected {expected_amount} links, but got {len(header_links)}'

    def sign_in_click(self):
        self.wait_element_clickable_click(*self.SIGN_IN)