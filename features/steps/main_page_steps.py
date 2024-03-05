from behave import given, when, then
from selenium.webdriver.common.action_chains import ActionChains


@given('Open Target main page')
def open_target_main(context):
    context.app.main_page.open_main()


@when('Hover over signin')
def hover_signin_btn(context):
    context.app.header.hover_signin_btn()


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product(product)


@when('Click on cart icon')
def click_cart(context):
    context.app.header.click_cart()


@then('Verify header in shown')
def verify_header(context):
    context.app.header.verify_header_shown()


@then('Verify header has {expected_amount} links')
def verify_header_links(context, expected_amount):
    context.app.header.verify_header_links(expected_amount)


@then('Verify signin arrow shown')
def verify_signin_arrow(context):
    context.app.header.verify_signin_arrow()
