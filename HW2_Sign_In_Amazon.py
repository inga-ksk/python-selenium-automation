from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# click on Orders
driver.find_element(By.XPATH, '//a[@id="nav-orders"]//span[@class="nav-line-2"]').click()

# verify Sign In Header is visible
#expected_header = "Sign-In"
driver.find_element(By.XPATH, '//*[@id="authportal-main-section"]//h1')

#verify field e-mail is present
driver.find_element(By.ID, 'ap_email').send_keys('inga.alyakskina@gmail.com')

driver.quit()