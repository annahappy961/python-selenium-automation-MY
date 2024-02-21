from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SideNavigationMenu(Page):
    VIEW_CART_BTN = (By.XPATH, "//*[contains(text(), 'View cart & check out')]")
    SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[aria-label*='Add to cart']")
    SIDE_NAV_BACK_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Previous']")

    def open_cart_from_side_navigation(self):
        self.wait_element_clickable_click(*self.VIEW_CART_BTN)

    def click_add_to_cart(self):
        self.wait_element_clickable_click(*self.SIDE_NAV_ADD_TO_CART_BTN)

    def side_nav_back_click(self):
        self.wait_element_clickable_click(*self.SIDE_NAV_BACK_BUTTON)
