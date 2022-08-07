from selenium.webdriver.common.by import By
from pages.base_page import Page

TOP_LINKS = (By.CSS_SELECTOR, '#zg_header a')

class BestsellersPage(Page):

    def open_bestsellers(self):
        self.open_url(end_url='gp/bestsellers')

    def verify_links_present(self):
        actual_links = self.driver.find_elements(*TOP_LINKS)
        assert len(actual_links) == int(expected_links), f' Expected {expected_links} links, but got {len(actual_links)}'