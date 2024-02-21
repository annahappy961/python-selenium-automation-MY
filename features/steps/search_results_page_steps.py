from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")

SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")

PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test*='product-title']")
PRODUCT_PRICE = (By.CSS_SELECTOR, "[class*='h-text-bold h-display']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")


@then('Search results for {expected_result} are shown')
def verify_search_results_correct(context, expected_result):
    context.app.search_results_page.verify_search_results_correct(expected_result)


@then('Page URL has search term {expected_part_url}')
def verify_search_results_page_url(context, expected_part_url):
    context.app.search_results_page.verify_search_results_page_url(expected_part_url)


@when("Click on Add to Cart button")
def click_add_to_cart(context):
    context.app.search_results_page.click_add_to_cart()


@when("Confirm Add to Cart button from side navigation")
def click_add_to_cart(context):
    context.app.side_navigation_menu.click_add_to_cart()


@when("Store product name")
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text


@when("Store product price")
def store_product_price(context):
    context.product_price = context.driver.find_element(*PRODUCT_PRICE).text


@when('Close side navigation')
def side_nav_back_click(context):
    context.app.side_navigation_menu.side_nav_back_click()


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
    # Why is it here?

    # TARGET_HELP_H2 = (By.XPATH, '')
    # context.wait.until(
    #     EC.text_to_be_present_in_element(TARGET_HELP_H2, 'Target Help'),
    #     message="'Target Help' text did not appear")
    current_product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    try:  # try to add a product to context.product_names:
        context.product_names.append(current_product_name)
    except AttributeError:  # if context.product_names not set, set it and put the current_product_name itno it:
        context.product_names = [current_product_name]


@then("Verify that every product has a title and an image")
def verify_products_name_img(context):
    context.app.search_results_page.verify_products_name_img()
