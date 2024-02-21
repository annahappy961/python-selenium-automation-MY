from pages.base_page import Page
from pages.cart_page import CartPage
from pages.circle_page import CirclePage
from pages.header import Header
from pages.help_page import HelpPage
from pages.main_page import MainPage
from pages.product_details_page import ProductDetailsPage
from pages.search_results_page import SearchResultsPage
from pages.side_navigation_menu import SideNavigationMenu


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.cart_page = CartPage(driver)
        self.circle_page = CirclePage(driver)
        self.header = Header(driver)
        self.help_page = HelpPage(driver)
        self.main_page = MainPage(driver)
        self.product_details_page = ProductDetailsPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.side_navigation_menu = SideNavigationMenu(driver)

