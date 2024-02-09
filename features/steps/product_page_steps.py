from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[aria-label*='Add to cart']")
VIEW_CART_BTN = (By.CSS_SELECTOR, "a[class*='ButtonSecondary']")


@given("Open Target Product page")
def open_target_product_page(context):
    context.driver.get("https://www.target.com/p/20-34-x20-34-oversize-york-faux-fur-square-throw-pillow-blush/-/A-52770446?preselect=52770446#lnk=sametab")


@when("Add product to cart from PP")
def add_product_to_cart(context):
    sleep(7)
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@when("Click View cart & check out from side navigation menu")
def open_cart_from_side_navigation(context):
    context.driver.find_element(*VIEW_CART_BTN).click()
