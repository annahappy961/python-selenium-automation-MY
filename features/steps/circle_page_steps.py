from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("Open Target Circle page")
def open_target_circle(context):
    context.app.circle_page.open_target_circle()


@then("Verify {expected_amount} benefit cards are shown")
def verify_benefit_boxes(context, expected_amount):
    context.app.circle_page.verify_benefit_boxes(expected_amount)


@then("Verify that clicking through Circle tabs works")
def verify_can_click_through_tabs(context):
    context.app.circle_page.verify_can_click_through_tabs()
