from behave import given, when, then


@when('Open cart page')
def open_cart(context):
    context.app.cart_page.open_cart()


@then("Verify {empty_cart_message} message seen")
def verify_cart_empty_message(context, empty_cart_message):
    context.app.cart_page.verify_cart_empty_message(empty_cart_message)


@then("Verify SignIn btn is clickable on empty cart page")
def empty_cart_signin_btn_click(context):
    context.app.cart_page.empty_cart_signin_btn_click()


@then("Verify cart has {expected_amount} item(s)")
def verify_cart_items(context, expected_amount):
    context.app.cart_page.verify_cart_items(expected_amount)


@then("Verify cart has correct product name")
def verify_product_name(context):
    expected_product_name = context.product_name
    context.app.cart_page.verify_product_name(expected_product_name)


@then("Verify cart has correct product price")
def verify_product_price(context):
    expected_product_price = context.product_price
    expected_product_price = expected_product_price.split()[0]
    context.app.cart_page.verify_product_price(expected_product_price)
    # actual_price = context.driver.find_element(*CART_SUMMARY).text
    # actual_price = actual_price.split()[0]
    # # print(actual_price)
    # assert actual_price == context.product_price, \
    #     f"Expected {context.product_price} but got {actual_price}"


@then('Verify cart has correct multiple products')
def verify_product_names(context):
    context.app.cart_page.verify_product_names(context)
    # # Grab title text of every product in the cart and store in actual_names:
    # actual_names = [product.text for product in context.driver.find_elements(*CART_ITEM_TITLE)]
    # # Sort lists before verification:
    # context.product_names.sort()
    # actual_names.sort()
    # assert context.product_names == actual_names, f'Expected {context.product_names} did not match {actual_names}'
