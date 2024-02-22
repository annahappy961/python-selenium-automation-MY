from behave import given, when, then


@given("Open target product {product_id} page")
def open_product_details_page(context, product_id):
    context.app.product_details_page.open_product_details_page(product_id)


@when("Add product to cart from PP")
def add_product_to_cart(context):
    context.app.product_details_page.add_product_to_cart()


@when("Click View cart & check out from side navigation")
def open_cart_from_side_navigation(context):
    context.app.side_navigation_menu.open_cart_from_side_navigation()


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    context.app.product_details_page.click_and_verify_colors()
