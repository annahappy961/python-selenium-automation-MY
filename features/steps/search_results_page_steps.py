from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[aria-label*='Add to cart']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
SIDE_NAV_PREV_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Previous']")
PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test*='product-title']")
PRODUCT_PRICE = (By.CSS_SELECTOR, "[class*='h-text-bold h-display']")
PRODUCT_IMG = (By.CSS_SELECTOR, "[class*='StyledCol'] [class*='ProductCardImageWrapper']")


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
    sleep(10)
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@when("Confirm Add to Cart button from side navigation")
def click_add_to_cart(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()


@when("Store product name")
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text


@when("Store product price")
def store_product_price(context):
    context.product_price = context.driver.find_element(*PRODUCT_PRICE).text


@when('Close side navigation')
def side_nav_click_add_to_cart(context):
    sleep(10)
    context.driver.find_element(*SIDE_NAV_PREV_BUTTON).click()


@when('Click on Add to Cart button for product {i}')
def click_add_to_cart_by_index(context, i):
    # Find all Add to cart buttons, click on a button by index:
    # product 1 -> index 0
    # product 2 -> index 1, etc.
    sleep(10)
    context.driver.find_elements(*ADD_TO_CART_BTN)[int(i) - 1].click()


@when('Store product name to a list')
def store_product_names(context):
    context.wait.until(EC.presence_of_element_located(SIDE_NAV_PRODUCT_NAME), message='Side nav did not open')
    current_product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    try:  # try to add a product to context.product_names:
        context.product_names.append(current_product_name)
    except AttributeError:  # if context.product_names not set, set it and put the current_product_name itno it:
        context.product_names = [current_product_name]


def scroll_and_verify_elements(context, element_locator, expected_amount):
    # Initial scroll down
    context.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)

    # Wait for the initial set of elements to load
    context.wait.until(EC.visibility_of_all_elements_located(element_locator))

    # Check the number of elements after the initial scroll
    actual_amount = len(context.driver.find_elements(*element_locator))

    # Perform additional scrolls until the expected amount is reached
    while actual_amount < expected_amount:
        context.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        context.wait.until(EC.visibility_of_all_elements_located(element_locator))
        actual_amount = len(context.driver.find_elements(*element_locator))

    assert actual_amount == expected_amount, f"Expected {expected_amount} but got {actual_amount}"


@then("Verify {amount} names in shown")
def verify_product_name_shown(context, amount):
    expected_names = int(amount)
    scroll_and_verify_elements(context, PRODUCT_NAME, expected_names)


@then("Verify {amount} images in shown")
def verify_product_name_shown(context, amount):
    expected_amount = int(amount)
    scroll_and_verify_elements(context, PRODUCT_IMG, expected_amount)
