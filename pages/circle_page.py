from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class CirclePage(Page):
    CIRCLE_TABS = (By.CSS_SELECTOR, "[class*='PageSelectionText'] a")
    BONUS_TAB = (By.CSS_SELECTOR, "[data-test*='bonus-tab']")

    def open_target_circle(self):
        self.driver.get("https://www.target.com/circle")

    def verify_can_click_through_tabs(self):
        self.wait_element_clickable(*self.BONUS_TAB)
        tabs = self.find_elements(*self.CIRCLE_TABS)
        # print(tabs)
        current_url = ""

        # for tab in tabs:
        #     print("\nITERATIONS\n")
        #     print(tabs)
        #     tab.click()
        for i in range(len(tabs)):
            tabs = self.find_elements(*self.CIRCLE_TABS)
            tabs[i].click()

            self.wait_url_changes(current_url)
            current_url = self.driver.current_url
