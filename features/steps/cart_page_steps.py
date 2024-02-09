from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_HEADER = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")
CART_SUMMERY_TOTAL = (By.CSS_SELECTOR, "[data-test*='cart-summary-total']")
TOTAL_PRICE = (By.CSS_SELECTOR, "[data-test*='cart-summary-total'] p")
SIGNIN_BTN_EMPTY_CART = (By.CSS_SELECTOR, "[class*='ButtonPrimary']")
BULLSEYE_IMG_EMPY_CART = (By.CSS_SELECTOR, "[data-test='empty-cart-bullseye-img']")


@then("Verify {expected_text} message is shown")
def verify_cart_empty_message(context, expected_text):
    sleep(10)
    actual_text = context.driver.find_element(*CART_HEADER).text
    assert expected_text in actual_text, f"Expected {expected_text} but got {actual_text}"


@then("Verify SignIn btn is clickable on empty cart page")
def click_signin_btn_empty_cart(context):
    context.driver.find_element(*SIGNIN_BTN_EMPTY_CART).click()


@then("Verify Bullseye empty cart is seen")
def verify_bullseye_empy_cart_seen(context):
    context.driver.find_element(*BULLSEYE_IMG_EMPY_CART)


@then("Verify the Total Price is shown")
def total_price_shown(context):
    context.driver.find_element(*CART_SUMMERY_TOTAL)
