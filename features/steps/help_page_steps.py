from selenium.webdriver.common.by import By
from behave import given, when, then
# from time import sleep

TARGET_HELP_TEXT = (By.XPATH, "//*[contains(text(), 'Target Help')]")
SEARCH_FIELD = (By.CSS_SELECTOR, ".search-input")
SEARCH_BTN = (By.CSS_SELECTOR, ".search-btn")
WHAT_WOULD_YOU_LIKE_TEXT = (By.CSS_SELECTOR, "h2.header")
WHAT_WOULD_YOU_LIKE_ELEMENTS = (By.CSS_SELECTOR, "[class*='col'] [class*='grid_6']")
CONTACT_US_PRODUCT_RECALLS_ELEMENTS = (By.CSS_SELECTOR, ".grid_4")
BROWSE_ALL_HELP_PAGES_TEXT = (By.CSS_SELECTOR, ".grid_18 h2")
BROWSE_ALL_HELP_PAGES_ELEMENTS = (By.CSS_SELECTOR, ".grid_6 li.expandable")


@given("Open Target Help page")
def open_target_help(context):
    context.driver.get("https://help.target.com/help")


@then("Verify Target Help text is shown")
def verify_target_help_text_shown(context):
    context.driver.find_element(*TARGET_HELP_TEXT)


@then("Verify Search Help field is shown")
def verify_field_shown(context):
    context.driver.find_element(*SEARCH_FIELD)


@then("Verify Search btn is shown")
def verify_btn_shown(context):
    context.driver.find_element(*SEARCH_BTN)


@then("Verify {expected_text} text is shown")
def verify_what_would_you_text_shown(context, expected_text):
    actual_text = context.driver.find_element(*WHAT_WOULD_YOU_LIKE_TEXT).text
    assert expected_text in actual_text, f"Expected {expected_text} but got {actual_text}"


@then("Verify {expected_text} is shown")
def verify_browse_all_help_pages_text_shown(context, expected_text):
    actual_str = context.driver.find_element(*BROWSE_ALL_HELP_PAGES_TEXT).text
    assert actual_str in expected_text, f"Expected {expected_text} but got {actual_str}"


@then("Verify 'What would you...' {expected_amount} elements are shown")
def verify_what_would_you_elements_shown(context, expected_amount):
    expected_amount = int(expected_amount)
    actual_number = len(context.driver.find_elements(*WHAT_WOULD_YOU_LIKE_ELEMENTS))
    assert actual_number == expected_amount, f"Expected {expected_amount} but got {actual_number}"


@then("Verify Contact Us and Product Recalls {expected_amount} elements are shown")
def verify_contact_us_product_recalls_elements_shown(context, expected_amount):
    expected_amount = int(expected_amount)
    actual_amount = len(context.driver.find_elements(*CONTACT_US_PRODUCT_RECALLS_ELEMENTS))
    assert actual_amount == expected_amount, f"Expected {expected_amount} but got {actual_amount}"


@then("Verify 'Browse all Help pages' {expected_amount} elements are shown")
def verify_browse_all_help_elements_shown(context, expected_amount):
    expected_amount = int(expected_amount)
    actual_amount = len(context.driver.find_elements(*BROWSE_ALL_HELP_PAGES_ELEMENTS))
    assert actual_amount == expected_amount, f"Expected {expected_amount} but got {actual_amount}"
