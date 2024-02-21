from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class ProductDetailsPage(Page):
    COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
    SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[aria-label*='Add to cart']")

    def open_product_details_page(self, product_id):
        self.open(f"https://www.target.com/p/{product_id}")
        sleep(10)

    def click_and_verify_colors(self):
        expected_colors = ["Blue Tint", "Denim Blue", "Marine"]
        actual_colors = []

        self.wait_element_clickable(self.COLOR_OPTIONS)
        colors = self.find_elements(*self.COLOR_OPTIONS)
        sleep(10)

        for color in colors[:3]:
            color.click()
            self.wait_element_clickable(self.SELECTED_COLOR)
            selected_color = self.find_elements(*self.SELECTED_COLOR).text
            selected_color = selected_color.split("\n")[1]
            actual_colors.append(selected_color)
            print(actual_colors)

        assert expected_colors == actual_colors, f"Expected {expected_colors} but got {actual_colors}"
        # self.driver.verify_text(expected_colors, actual_colors)

    def add_product_to_cart(self):
        self.wait_element_clickable_click(*self.ADD_TO_CART_BTN)
