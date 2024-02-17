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

    # def compare_two_variables(self, expected, actual):
    #     assert {expected} in {actual}, f"Expected {expected} but got {actual}"
