from selenium.webdriver.common.by import By

from pages.base_page import Page


class ProductPage(Page):

    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "input#add-to-cart-button")
    DECLINE_PLAN = (By.CSS_SELECTOR, '#attachSiNoCoverage input.a-button-input')

    def add_to_cart(self):
        self.find_element(*self.ADD_TO_CART_BUTTON).click()

    def decline_protection(self):
        self.find_element(*self.DECLINE_PLAN).click()