from behave import given, when, then


@when("Click Sign In")
def sign_in_click(context):
    context.app.header.sign_in_click()


@when("From side navigation menu, click Sign In")
def account_sign_in_click(context):
    context.app.side_navigation_menu.account_sign_in_click()


@then("Verify {expected_text} seen")
def verify_sign_in_form(context, expected_text):
    context.app.sign_in_page.verify_sign_in_form_open(expected_text)
