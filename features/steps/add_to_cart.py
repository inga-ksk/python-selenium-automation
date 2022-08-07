from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

TOP_LINKS = (By.CSS_SELECTOR, '#zg_header a')
HEADER = (By.CSS_SELECTOR, '#zg_banner_text')


@when('Paste washing machine into search field and click search')
def search_for_product(context):
    context.app.header.search_product('washing machine')

@when('Click on first search result')
def click_first_result(context):
    context.app.search_results_page.add_first_search_result_to_cart()

@when('Add product to cart')
def add_to_cart(context):
    context.app.product_page.add_to_cart()

@when('Decline appliance protection plan')
def decline_protection(context):
    context.app.product_page.decline_protection()

@then('1 item is present in cart')
def veify_product_is_in_cart(context):
    context.app.cart_page.verify_product_added_to_cart()