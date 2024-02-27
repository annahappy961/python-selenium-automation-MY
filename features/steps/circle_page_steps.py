from behave import given, when, then
from time import sleep


@given("Open Target Circle page")
def open_target_circle(context):
    context.app.circle_page.open_target_circle()


@given("Store original window")
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    # print("Current window", context.original_window)
    # print("All windows:", context.driver.window_handles)


@when("Click Google Play button")
def click_googlex_play_btn(context):
    context.app.circle_page.click_google_play_btn()
    # sleep(2)
    # print("All windows after GPlay click:", context.driver.window_handles)


@when("Switch to new window")
def switch_to_new_window(context):
    context.app.circle_page.switch_to_new_window()


@then("Verify {expected_amount} benefit cards are shown")
def verify_benefit_boxes(context, expected_amount):
    context.app.circle_page.verify_benefit_boxes(expected_amount)


@then("Verify that clicking through Circle tabs works")
def verify_can_click_through_tabs(context):
    context.app.circle_page.verify_can_click_through_tabs()


@then("Return to original window")
def return_to_circle_page_tab(context):
    context.app.circle_page.switch_to_window_by_id(context.original_window)
