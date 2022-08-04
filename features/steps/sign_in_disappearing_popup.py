from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

SIGN_IN_POPUP_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip span.nav-action-inner')

@when('Wait for {sec} sec') # '8'
def sleep_sec(context, sec):
    sleep(int(sec))


@then('Verify Sign In is clickable')
def verify_sign_in_btn_clickable(context):
    context.wait = WebDriverWait(context.driver, 10)
    context.driver.wait.until(
        EC.element_to_be_clickable(SIGN_IN_POPUP_BTN), message='SignIn not clickable'
    )


@then('Verify Sign In disappears')
def verify_sign_in_btn_disappear(context):
    context.driver.wait.until(
        EC.invisibility_of_element_located(SIGN_IN_POPUP_BTN), message='SignIn btn is visible'
    )


@then('Verify hamburger menu is present')
def verify_hamburger_menu_present(context):
    context.driver.find_element(*HAM_MENU)
    ham_menu = context.driver.find_element(*HAM_MENU)
    ham_menu.click()