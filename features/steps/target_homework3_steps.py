# from selenium.webdriver.common.by import By
# from behave import given, when, then
# from time import sleep
#
#
# @when("Click on cart icon")
# def click_cart_icon(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[href*='Cart']").click()
#     sleep(6)
#
#
# @then("Verify 'Your cart is empty' message is shown")
# def verify_message_correct(context):
#     actual_message = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='StyledHeading']").text
#     assert "Your cart is empty" in actual_message, f"Expected message not in {actual_message}"
#
#
# @then("Verify Sing In clickable")
# def verify_button_clickable(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[class*='ButtonPrimary']").click()
#
#
# @when("Click Sign In")
# def click_sign_in(context):
#     context.driver.find_element(By.XPATH, "//*[contains(text(), 'Sign in')]").click()
#
#
# @when("Click Sign In from right side navigation menu")
# def click_sigh_in_side_menu(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
#
#
# @then("Verify 'Sign into your Target account' text seen")
# def verify_right_form_open(context):
#     context.driver.find_element(By.XPATH, "//*[contains(text(), 'Sign into your Target account')]")
#
#
# @given("Open product page")
# def open_product_page(context):
#     context.driver.get("https://www.target.com/p/20-34-x20-34-oversize-york-faux-fur-square-throw-pillow-blush/-/A-52770446?preselect=52770446#lnk=sametab")
#
#
# @when("Add product to cart")
# def add_product_to_cart(context):
#     sleep(10)
#     context.driver.find_element(By.CSS_SELECTOR, "button[aria-label*='Add to cart for']").click()
#
#
# @when("Click View cart & check out from side navigation menu")
# def open_cart_from_side_navigation(context):
#     sleep(6)
#     context.driver.find_element(By.CSS_SELECTOR, "a[href*='cart'][class*='StyledBaseButtonInternal']").click()
#
#
# @then("Verify the total price is seen in cart")
# def verify_total_price_in_cart(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[data-test*='cart-summary-total']")
#

# SEARCH_INPUT = (By.NAME, 'q')
# SEARCH_SUBMIT = (By.NAME, 'btnK')
#
#
# @given('Open Google page')
# def open_google(context):
#     context.driver.get('https://www.google.com/')
#
#
# @when('Input {search_word} into search field')
# def input_search(context, search_word):
#     search = context.driver.find_element(*SEARCH_INPUT)
#     search.clear()
#     search.send_keys(search_word)
#     sleep(4)
#
#
# @when('Click on search icon')
# def click_search_icon(context):
#     context.driver.find_element(*SEARCH_SUBMIT).click()
#     sleep(1)
#
#
# @then('Product results for {search_word} are shown')
# def verify_found_results_text(context, search_word):
#     assert search_word.lower() in context.driver.current_url.lower(), \
#         f'Expected query not in {context.driver.current_url.lower()}'