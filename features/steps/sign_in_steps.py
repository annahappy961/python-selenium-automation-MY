from behave import given, when, then


@given("Open sign in page")
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in_page()


@when("Click Sign In")
def sign_in_click(context):
    context.app.header.sign_in_click()


@when("From side navigation menu, click Sign In")
def account_sign_in_click(context):
    context.app.side_navigation_menu.account_sign_in_click()


@when("Input email and password on SighIn page")
def input_user_email_password(context):
    context.app.sign_in_page.input_user_email_password()


@when("Store original windows")
def store_window(context):
    context.original_window = context.driver.current_window_handle


@when("Click on Target terms and conditions link")
def click_terms_conditions_link(context):
    context.app.sign_in_page.click_terms_conditions_link()


@when("Switch to the newly opened window")
def switch_to_new_window(context):
    context.app.sign_in_page.switch_to_new_window()


@when("Click Sign In on Sign In page")
def click_sign_in(context):
    context.app.sign_in_page.click_sign_in()


@then("Verify {expected_text} seen")
def verify_sign_in_form(context, expected_text):
    context.app.sign_in_page.verify_sign_in_form_open(expected_text)


@then("Verify user is logged in")
def verify_user_logged_in(context):
    context.app.sign_in_page.verify_user_logged_in()


@then("Verify Terms and Conditions page is opened")
def verify_terms_conditions_page_open(context):
    context.app.sign_in_page.verify_terms_conditions_page_open()


@then("Close Terms and Conditions page page")
def close_terms_conditions_tab(context):
    context.driver.close()


@then("User can switch back to original")
def switch_to_original_window(context):
    context.app.sign_in_page.switch_to_window_by_id(context.original_window)
