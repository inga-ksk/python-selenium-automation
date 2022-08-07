from behave import given, then
from selenium.webdriver.common.by import By
from time import sleep

@when('Click Amazon Orders link')
def click_orders(context):
    context.app.header.order_click()

@when('Click on cart icon')
def click_cart(context):
    context.app.header.cart_icon_click()

@then('Verify Sign In page is opened')
def sign_in_open(context):
    context.app.sign_in_page.sign_in_page_verification()

@then('Verify \'Your Shopping Cart is empty.\' text present')
def cart_is_empty_check(context):
    context.app.cart_page.cart_page_empty_state()