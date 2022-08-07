from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):
    INPUT_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    ORDERS = (By.CSS_SELECTOR, '#nav-orders span.nav-line-2')
    CART_ICON = (By.ID, 'nav-cart-count-container')

    def search_product(self, search_word):
        self.input_text(search_word, *self.INPUT_FIELD)
        self.click(*self.SEARCH_ICON)

    def order_click(self):
        self.click(*self.ORDERS)

    def cart_icon_click(self):
        self.click(*self.CART_ICON)