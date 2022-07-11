from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Click on the cart icon')
def click_on_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, ".nav-cart-icon.nav-sprite").click()
    sleep(4)

@then('Verify product count equals to 0')
def check_item_count(context):
    expected_text = 'Your Amazon Cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty").text
    assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'

