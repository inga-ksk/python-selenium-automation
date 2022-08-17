from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class Header(Page):

    INPUT_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    ORDERS = (By.CSS_SELECTOR, '#nav-orders span.nav-line-2')
    CART_ICON = (By.ID, 'nav-cart-count-container')
    FLAG = (By.CSS_SELECTOR, 'span.icp-nav-flag')
    SPANISH_LANG = (By.CSS_SELECTOR, 'a[href="#switch-lang=es_US"]')
    DEPARTMENT = (By.ID, 'searchDropdownBox')
    ACTUAL_DEPT = (By.ID, 'nav-subnav')
    SELECTED_DEPT = (By.CSS_SELECTOR, '#searchDropdownBox option[selected="selected"]')
    NEW_ARRIVALS = (By.CSS_SELECTOR, 'a[aria-label="New Arrivals"]')
    NEW_ARRIVALS_WOMEN = (By.CSS_SELECTOR, 'a[href*="s?i=fashion-womens"]')

    def search_product(self, search_word):
        self.input_text(search_word, *self.INPUT_FIELD)
        self.click(*self.SEARCH_ICON)

    def order_click(self):
        self.click(*self.ORDERS)

    def cart_icon_click(self):
        self.click(*self.CART_ICON)

    def hover_lang(self):
        flag = self.find_element(*self.FLAG)
        actions = ActionChains(self.driver)
        actions.move_to_element(flag)
        actions.perform()

    def hover_new_arrivals(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def select_dept(self):
        dept = self.find_element(*self.DEPARTMENT)
        select = Select(dept)
        select.select_by_value('search-alias=amazonfresh')

    def get_act_dept(self):
        actual_dept = self.find_element(*self.ACTUAL_DEPT)
        actual_dept_name = actual_dept.get_attribute('data-category')
        selected_dept = self.find_element(*self.SELECTED_DEPT)
        selected_dept_name = selected_dept.get_attribute('value')
        assert actual_dept_name in selected_dept_name, f"You are currently seeing {actual_dept_name} department items while {selected_dept} is selected"

    def new_arrivals_appear_on_hovering(self):
        self.wait_for_element_appear(*self.NEW_ARRIVALS_WOMEN)

    def verify_spanish_lang(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

