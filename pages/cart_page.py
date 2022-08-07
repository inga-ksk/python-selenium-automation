from selenium.webdriver.common.by import By
from pages.base_page import Page

CART_STATE = (By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty')
ADDED_TO_CART_TEXT = (By.CSS_SELECTOR, "span.a-size-medium-plus")

class CartPage(Page):

    def cart_page_empty_state(self):
        self.verify_element_text('Your Amazon Cart is empty', *CART_STATE)

    def verify_product_added_to_cart(self):
        actual_text = self.find_element(*ADDED_TO_CART_TEXT).text
        expected_text = 'Added to Cart'
        assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'