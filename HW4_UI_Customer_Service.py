from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='/Users/Inga/Documents/Careerist/Automation/python-selenium-automation/chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')

# find UI elements
#1 - text "What would you like help with today?"
driver.find_element(By.CSS_SELECTOR, 'p.header-subtext')

#2 - container with actions' tiles
driver.find_element(By.CSS_SELECTOR, 'div.issue-card-container')

#3 - search help library field
driver.find_element(By.ID, 'hubHelpSearchInput')

#4 - text "all help topics"
driver.find_element(By.XPATH, '//h2[text()="All help topics"]')

#5 - container with help topics
driver.find_element(By.CSS_SELECTOR, 'ul.help-topics')

driver.quit()