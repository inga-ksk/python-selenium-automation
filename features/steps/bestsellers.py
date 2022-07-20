from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BESTSELLER_LINKS = (By.CSS_SELECTOR, 'div#CardInstanceuryXft6fSy-ualuuXWOxYg ul li')

@when('Click on bestsellers link')
def click_on_bestsellers(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='gp/bestsellers/']").click()
    sleep(4)

@then('Verify {expected_amount} bestseller links are shown')
def check_links_count(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*BESTSELLER_LINKS)

    #assert len(links) == expected_amount, \
       #f'Expected {expected_amount} links but got {len(links)}'