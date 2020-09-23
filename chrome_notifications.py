# Handle notifications in Python + Selenium Chrome WebDriver
# How can Selenium Chrome WebDriver notifications be handled in Python?

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.google.com/")
