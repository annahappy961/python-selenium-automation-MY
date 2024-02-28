from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("Open Target Help page")
def open_target_help(context):
    context.app.help_page.open_target_help()


@given('Open Help page for Returns')
def open_target_help_returns(context):
    context.app.help_page.open_help_returns()


@when('Select Help topic {help_topic}')
def select_promotions(context, help_topic):
    context.app.help_page.select_topic(help_topic)

# @then('Verify Returns page opened')
# def verify_returns_opened(context):
#    context.app.help_page.verify_returns_opened()
#
#
# @then('Verify Current promotions page opened')
# def verify_promotions_opened(context):
#     context.app.help_page.verify_promotions_opened()


@then('Verify {expected_header} page opened')
def verify_promotions_opened(context, expected_header):
    context.app.help_page.verify_header(expected_header)


@then("Verify {expected_text} text in shown")
def verify_target_help_text_shown(context, expected_text):
    context.app.help_page.verify_target_help_text_shown(expected_text)


@then("Verify Search Help field is shown")
def verify_search_field_shown(context):
    context.app.help_page.verify_search_field_shown()


@then("Verify Search btn is shown")
def verify_search_btn_shown(context):
    context.app.help_page.verify_search_btn_shown()


@then("Verify {expected_text} text is shown")
def verify_what_would_you_text_shown(context, expected_text):
    context.app.help_page.verify_what_would_you_text_shown(expected_text)


@then("Verify {expected_text} is shown")
def verify_browse_all_help_pages_text_shown(context, expected_text):
    context.app.help_page.verify_browse_all_help_pages_text_shown(expected_text)


@then("Verify 'What would you...' {expected_amount} elements are shown")
def verify_what_would_you_elements_shown(context, expected_amount):
    context.app.help_page.verify_what_would_you_elements_shown(expected_amount)


@then("Verify Contact Us and Product Recalls {expected_amount} elements are shown")
def verify_contact_us_product_recalls_elements_shown(context, expected_amount):
    context.app.help_page.verify_contact_us_product_recalls_elements_shown(expected_amount)


@then("Verify 'Browse all Help pages' {expected_amount} elements are shown")
def verify_browse_all_help_elements_shown(context, expected_amount):
    context.app.help_page.verify_browse_all_help_elements_shown(expected_amount)
