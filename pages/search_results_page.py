from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    FIRST_RESULT_PRICE = (By.CSS_SELECTOR, "span.a-price-whole")

    def verify_search_results(self, expected_result):
        self.verify_element_text(expected_result, *self.RESULT)

    def add_first_search_result_to_cart(self):
        self.find_element(*self.FIRST_RESULT_PRICE).click()