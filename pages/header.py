from pages.base_page import Page
from selenium.webdriver.common.by import By

class HeaderPage(Page):
    HEADER = (By.ID, 'twotabsearchtextbox')

    def search_product(self):
        self.input_text('coffee', *self.HEADER)

