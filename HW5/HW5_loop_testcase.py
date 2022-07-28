from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='/Users/Inga/Documents/Careerist/Automation/python-selenium-automation/chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/Backpack-Lightweight-Kindergarten-Preschool-Elementary/dp/B0B1CD3881')

#get the item's list of available colors
expected_colors = ['Dinosaur', 'Galaxy', 'Space']
colors = driver.find_elements(By.CSS_SELECTOR, 'div#variation_color_name li')
print(colors)

actual_colors = []

for color in colors:
    color.click()
    actual_colors +=  [driver.find_element(By.CSS_SELECTOR, 'div#variation_color_name span.selection').text]
    print('Actual_colors:', actual_colors)

assert expected_colors == actual_colors, f'Expected {expected_colors} but got {actual_colors}'

driver.quit()
