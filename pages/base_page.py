class Page:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        self.driver.find_element(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def get_text(self, *locator):
        return self.driver.find_element(*locator).text

    # def verify_partial_text(self, expected_text, *locater):
    #     actual_text = self.find_element(*locater)
    #     assert expected_text in actual_text, f"Expected {expected_text} but got {actual_text}"
