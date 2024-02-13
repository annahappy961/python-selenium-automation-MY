from selenium.webdriver.common.by import By
from behave import given, when, then
# from time import sleep
from selenium.webdriver.support import expected_conditions as EC

CART_HEADER = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")
CART_SUMMARY_TOTAL = (By.CSS_SELECTOR, "[data-test*='cart-summary-total']")
TOTAL_PRICE = (By.CSS_SELECTOR, "[data-test*='cart-summary-total'] p")
SIGNIN_BTN_EMPTY_CART = (By.CSS_SELECTOR, "[class*='ButtonPrimary']")
BULLSEYE_IMG_EMPY_CART = (By.CSS_SELECTOR, "[data-test='empty-cart-bullseye-img']")
PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
CART_SUMMARY = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')


@then("Verify {expected_text} message is shown")
def verify_cart_empty_message(context, expected_text):
    actual_text = context.wait.until(EC.element_to_be_clickable(*CART_HEADER)).text
    assert expected_text in actual_text, f"Expected {expected_text} but got {actual_text}"


@then("Verify SignIn btn is clickable on empty cart page")
def click_signin_btn_empty_cart(context):
    context.driver.find_element(*SIGNIN_BTN_EMPTY_CART).click()


@then("Verify Bullseye empty cart is seen")
def verify_bullseye_empy_cart_seen(context):
    context.driver.find_element(*BULLSEYE_IMG_EMPY_CART)


@then("Verify the Total Price is shown")
def total_price_shown(context):
    context.driver.find_element(*CART_SUMMARY_TOTAL)


@then("Verify cart has {amount} item(s)")
def verify_cart_items(context, amount):
    cart_summery = context.driver.find_element(*CART_SUMMARY).text
    assert amount in cart_summery, f"Expected items {amount} but got {cart_summery}"


@then("Verify cart has correct product name")
def verify_product_name(context):
    actual_name = context.driver.find_element(*PRODUCT_NAME).text
    assert context.product_name in actual_name, f"Expected {context.product_name} but got {actual_name}"


@then('Verify cart has correct multiple products')
def verify_product_names(context):
    # Grab title text of every product in the cart and store in actual_names:
    actual_names = [product.text for product in context.driver.find_elements(*CART_ITEM_TITLE)]
    # Sort lists before verification:
    context.product_names.sort()
    actual_names.sort()
    assert context.product_names == actual_names, f'Expected {context.product_names} did not match {actual_names}'
