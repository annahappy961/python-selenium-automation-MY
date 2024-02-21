from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

SEARCH_FIELD = (By.ID, 'search')
SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")


@given('Open Target main page')
def open_target_main(context):
    context.app.main_page.open_main()


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product(product)


@when('Click on cart icon')
def click_cart(context):
    context.app.header.click_cart()


@then('Verify header in shown')
def verify_header(context):
    context.app.header.verify_header()


@then('Verify header has {expected_amount} links')
def verify_header_links(context, expected_amount):
    context.app.header.verify_header_links(expected_amount)