from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# click on Orders
driver.find_element(By.CSS_SELECTOR, 'a.nav-a.nav-a-2#nav-orders span.nav-line-2').click()
# verify Sign In Header is visible
expected_text = 'Sign-In'
actual_text = driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small").text
assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'
#driver.find_element(By.XPATH, '//*[@id="authportal-main-section"]//h1')

#verify field e-mail is present
assert driver.find_element(By.CSS_SELECTOR, '#ap_email').is_displayed()


driver.quit()