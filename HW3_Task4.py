from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# send product name to search field
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys("pen")

#click on search button
driver.find_element(By.ID, 'nav-search-submit-button').click()

#click on second result on search results page

