from selenium.webdriver.common.by import By
from behave import given, when, then

BESTSELLER_LINKS = (By.CSS_SELECTOR, 'a[data-csa-c-content-id="nav_cs_bestsellers"]')

@when('Click on bestsellers link')
def click_on_bestsellers(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='gp/bestsellers/']").click()

@then('Verify {expected_amount} bestseller links are shown')
def check_links_count(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*BESTSELLER_LINKS)

    #assert len(links) == expected_amount, \
       #f'Expected {expected_amount} links but got {len(links)}'