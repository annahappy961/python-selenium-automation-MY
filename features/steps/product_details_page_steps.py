from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[aria-label*='Add to cart']")
VIEW_CART_BTN = (By.XPATH, "//*[contains(text(), 'View cart & check out')]")
COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")


@given("Open target product {product_id} page")
def open_target_product_page(context, product_id):
    context.driver.get(f"https://www.target.com/p/{product_id}")
    sleep(10)


@when("Add product to cart from PP")
def add_product_to_cart(context):
    context.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN)).click()


@when("Click View cart & check out from side navigation")
def open_cart_from_side_navigation(context):
    context.wait.until(EC.element_to_be_clickable(VIEW_CART_BTN)).click()


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ["Blue Tint", "Denim Blue", "Marine"]
    actual_colors = []

    context.wait.until(EC.element_to_be_clickable(COLOR_OPTIONS))
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors[:3]:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        selected_color = selected_color.split("\n")[1]
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f"Expected {expected_colors} but got {actual_colors}"
