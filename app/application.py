from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage
from pages.bestsellers_page import BestsellersPage
from pages.sign_in_page import SignIn
from pages.cart_page import CartPage
from pages.product_page import ProductPage


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.bestsellers_page = BestsellersPage(self.driver)
        self.sign_in_page = SignIn(self.driver)
        self.cart_page = CartPage(self.driver)
        self.product_page = ProductPage(self.driver)