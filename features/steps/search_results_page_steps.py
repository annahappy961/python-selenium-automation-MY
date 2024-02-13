from selenium.webdriver.common.by import By
from behave import given, when, then
# from time import sleep
from selenium.webdriver.support import expected_conditions as EC

SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
STORE_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")


@then('Search results for {expected_result} are shown')
def verify_search_results_correct(context, expected_result):
    actual_text = context.driver.find_element(*SEARCH_RESULTS_HEADER).text
    assert expected_result in actual_text, f'Expected word {expected_result} not in {actual_text}'


@then('Page URL has search term {expected_part_url}')
def verify_search_results_page_url(context, expected_part_url):
    url = context.driver.current_url
    assert expected_part_url in url, f'Expected {expected_part_url} not in {url}'


@when("Click on Add to Cart button")
def click_add_to_cart(context):
    context.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN)).click()


@when("Confirm Add to Cart button from side navigation")
def click_add_to_cart(context):
    context.wait.until(EC.element_to_be_clickable(SIDE_NAV_ADD_TO_CART_BTN)).click()


@when("Store product name")
def store_product_name(context):
    context.product_name = context.driver.find_element(*STORE_PRODUCT_NAME).text
