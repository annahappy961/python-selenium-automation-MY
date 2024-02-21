from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    PRODUCT_TILE = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
    PRODUCT_IMG = (By.CSS_SELECTOR, "[class*='ProductCardImage']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")

    def verify_search_results_correct(self, expected_result):
        actual_text = self.driver.find_element(*self.SEARCH_RESULTS_HEADER).text
        assert expected_result in actual_text, f'Expected word {expected_result} not in {actual_text}'

    def verify_search_results_page_url(self, expected_part_url):
        self.verify_partial_url(expected_part_url)

    def verify_products_name_img(self):
        self.window_scroll_down()
        all_products = self.find_elements(*self.PRODUCT_TILE)

        for product in all_products:
            title = product.find_element(*self.PRODUCT_TITLE).text
            # print(title)
            assert title, "Product title not shown"
            product.find_element(*self.PRODUCT_IMG)

    def click_add_to_cart(self):
        self.wait_element_clickable_click(*self.ADD_TO_CART_BTN)
