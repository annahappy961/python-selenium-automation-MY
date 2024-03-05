from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class HelpPage(Page):
    TARGET_HELP_TEXT = (By.XPATH, "//*[contains(text(), 'Target Help')]")
    SEARCH_FIELD = (By.CSS_SELECTOR, ".search-input")
    SEARCH_BTN = (By.CSS_SELECTOR, ".search-btn")
    WHAT_WOULD_YOU_LIKE_TEXT = (By.CSS_SELECTOR, "h2.header")
    BROWSE_ALL_HELP_PAGES_TEXT = (By.CSS_SELECTOR, ".grid_18 h2")
    WHAT_WOULD_YOU_LIKE_ELEMENTS = (By.CSS_SELECTOR, "[class*='col'] [class*='grid_6']")
    CONTACT_US_PRODUCT_RECALLS_ELEMENTS = (By.CSS_SELECTOR, ".grid_4")
    BROWSE_ALL_HELP_PAGES_ELEMENTS = (By.CSS_SELECTOR, ".grid_6 li.expandable")
    HEADER_RETURNS = (By.XPATH, "//h1[text()=' Returns']")
    HEADER_PROMOTIONS = (By.XPATH, "//h1[text()=' Current promotions']")
    HEADER = (By.XPATH, "//h1[text()=' {HEADER_TEXT}']")
    TOPIC_SELECTION = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")

    # Dynamic locator
    def _get_header_locator(self, expected_header_text):
        # [By.XPATH, "//h1[text()=' Returns']"]
        return [self.HEADER[0], self.HEADER[1].replace('{HEADER_TEXT}', expected_header_text)]

    def open_target_help(self):
        self.open("https://help.target.com/help")

    def verify_target_help_text_shown(self, expected_text, *locator):
        self.verify_text(expected_text, *self.TARGET_HELP_TEXT)

    def verify_search_field_shown(self):
        self.find_element(*self.SEARCH_FIELD)

    def verify_search_btn_shown(self):
        self.find_element(*self.SEARCH_BTN)

    def verify_what_would_you_text_shown(self, expected_text, *locator):
        self.verify_text(expected_text, *self.WHAT_WOULD_YOU_LIKE_TEXT)

    def verify_browse_all_help_pages_text_shown(self, expected_text, *locator):
        self.verify_text(expected_text, *self.BROWSE_ALL_HELP_PAGES_TEXT)

    def verify_what_would_you_elements_shown(self, expected_amount, *locator):
        self.verify_amount_of_elements(expected_amount, *self.WHAT_WOULD_YOU_LIKE_ELEMENTS)

    def verify_contact_us_product_recalls_elements_shown(self, expected_amount, *locator):
        self.verify_amount_of_elements(expected_amount, *self.CONTACT_US_PRODUCT_RECALLS_ELEMENTS)

    def verify_browse_all_help_elements_shown(self, expected_amount, *locator):
        self.verify_amount_of_elements(expected_amount, *self.BROWSE_ALL_HELP_PAGES_ELEMENTS)

    def open_help_returns(self):
        self.open('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def select_topic(self, help_topic):
        print(f"Trying to find element: {self.TOPIC_SELECTION}")
        self.wait_element_visible(*self.TOPIC_SELECTION)
        topics_dd = self.find_element(*self.TOPIC_SELECTION)
        select = Select(topics_dd)
        select.select_by_value(help_topic)

    def verify_returns_opened(self):
        self.wait_element_visible(*self.HEADER_RETURNS)

    def verify_promotions_opened(self):
        self.wait_element_visible(*self.HEADER_PROMOTIONS)

    def verify_header(self, expected_header_text):
        locator = self._get_header_locator(expected_header_text)
        print(locator)
        self.wait_element_visible(*locator)
