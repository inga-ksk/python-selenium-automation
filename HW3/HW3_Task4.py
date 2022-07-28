from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='/Users/Inga/Documents/Careerist/Automation/python-selenium-automation/chromedriver')
driver.maximize_window()

# open the url
driver.get("https://www.amazon.com/")

# send product name to search field
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys("washing machine")
#click on search button
driver.find_element(By.ID, 'nav-search-submit-button').click()

#click on result on search results page
driver.find_element(By.CSS_SELECTOR, "span.a-price-whole").click()

#locate and click add to cart
driver.find_element(By.CSS_SELECTOR, "input#add-to-cart-button").click()

#decline insurance - in edge cases insurance pop-up window is showed
#driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby='attachSiNoCoverage-announce']").click()

#verify item is in cart
expected_text = 'Added to Cart'
actual_text = driver.find_element(By.CSS_SELECTOR, "span.a-size-medium-plus").text
assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'

driver.quit()
