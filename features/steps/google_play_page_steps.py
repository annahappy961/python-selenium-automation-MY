from behave import given, when, then
from time import sleep


@then("Verify Google Play Target page opened")
def verify_google_play_open(context):
    context.app.google_play_page.verify_google_play_open()


@then("Close current page")
def close_google_play_tab(context):
    context.driver.close()
