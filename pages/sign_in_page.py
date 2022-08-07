from selenium.webdriver.common.by import By
from pages.base_page import Page

SIGN_IN_HEADER = (By.CSS_SELECTOR, 'h1.a-spacing-small')

class SignIn(Page):

    def sign_in_page_verification(self):
        self.verify_element_text('Sign-In', *SIGN_IN_HEADER)