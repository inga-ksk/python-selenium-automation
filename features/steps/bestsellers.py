from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

BESTSELLER_LINKS = (By.CSS_SELECTOR, 'div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq > ul > li:nth-child(n)')

@when('Click on bestsellers link')
def click_on_bestsellers(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='gp/bestsellers/']").click()

@then('Verify {expected_amount} bestseller links are shown')
def check_links_count(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*BESTSELLER_LINKS)

    assert len(links) == expected_amount, \
       f'Expected {expected_amount} links but got {len(links)}'

@then('Click on each top link and verify that correct page opens')
def loop_through_bestsellers_links(context):
    expected_links = ['Best Sellers', 'New Releases', 'Movers & Shakers', 'Most Wished For', 'Gift Ideas']
    actual_links = []
    links = context.driver.find_elements(*BESTSELLER_LINKS)
#Lana - it doesn't work properly but this is what I tried to do - to locate elements every loop again
    for n in range(0, len(links)):
        context.driver.wait.until(
            EC.element_to_be_clickable(links[n]), message='Link is not clickable'
        )
        actual_links += [
            context.driver.find_element(links[n]).text]
        context.driver.find_element(links[n]).click()
        context.driver.back()
        sleep(5)

    assert expected_links == actual_links, f'Expected {expected_links} but got {actual_links}'



