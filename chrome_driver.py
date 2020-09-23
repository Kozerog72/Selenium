# Web browser launch command:

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()  # start the browser - Google Chrome
# or specify the path: driver = webdriver.Chrome('/path/to/chromedriver')
driver.get("https://google.com")
print("Opened the browser and google website")
time.sleep(3)

search_text_box = driver.find_element_by_name("q")
print("Identified Google search box")
time.sleep(3)

search_text_box.clear()
search_text_box.send_keys("python selenium")
print("Cleared the search box then typed 'python selenium' words in it")
time.sleep(3)

search_text_box.send_keys(Keys.RETURN)
print("Hit the enter button")
time.sleep(3)

print("Now closing the browser...")

driver.close()
