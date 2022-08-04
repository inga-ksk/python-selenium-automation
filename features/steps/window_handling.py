from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

PRIVACY_NOTICE_LINK = (By.CSS_SELECTOR, 'a[href="https://www.amazon.com/privacy"]')
PRIVACY_NOTICE_HEADER = (By.CSS_SELECTOR, 'div.help-content h1')

@given('Open Amazon T&C page')
def open_amazon_tc(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_window(context):
    context.original_window = context.driver.current_window_handle
    print('Original window: ', context.original_window)


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(PRIVACY_NOTICE_LINK), message='Link is not clickable'
    ).click()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    print('Current windows', context.driver.window_handles)
    #['CDwindow-45A4AE2E4351064A97FAFA1C4C1DD9E2', 'CDwindow-2985D1CA77366E4CD68BE1617A4A69CE']
    new_window = context.driver.window_handles[1]
    context.driver.switch_to.window(new_window)


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_policy_open(context):
    text_header = context.driver.find_element(*PRIVACY_NOTICE_HEADER).get_attribute('innerHTML')
    expected_text = 'Amazon.com Privacy Notice'
    assert text_header.lower() in expected_text.lower(), f"The open page doesn't contain information on {expected_text}"


@then('User closes new window')
def close_privacy_notice(context):
    context.driver.close()


@then('User switches back to original window')
def return_to_original_window(context):
    context.driver.switch_to.window(context.original_window)