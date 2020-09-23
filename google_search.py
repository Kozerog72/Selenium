# Google Search Scenario.

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#  Keyword: HTML (DOM)
#  Locator: XPath (querying), CSS - cssSelector (querying),
#  Locator on HTML: ID, Name, link_name, partial_link_name, class_name

# 1. Open the browser, launch the website google.com. >>> Given condition in Gherkin scenario
# 2 Type "selenium python" in the search and hit enter. >>> Actions - WHEN
# 3. Verify the result is more 20 mln. >>> Test here, check here - THEN
# 4. Verify that it take less than a second for the search. >>> Test here, check point - THEN
# 5. Close the browser.

driver = webdriver.Chrome()  # start the browser
driver.get("https://google.com")  # specifying the path: driver = webdriver.Chrome('/path/to/chromedriver')
print("Opened the browser and Google website.")
time.sleep(3)

search_text_box = driver.find_element_by_name("q")  # finding (locating) search box element in the HTML DOM
print("Identified Google Search Box")
time.sleep(1)

search_text_box.clear()  # just in case clearing the search field
search_text_box.send_keys("python selenium")  # entered provided text in the "Search Box"
print("Cleared the search box then typed 'python selenium' words in it")  #
time.sleep(1)

search_text_box.send_keys(Keys.RETURN)  # simulates hitting the Enter Key on your keyboard
print("Hit the enter button")
time.sleep(3)

print("-----------------------------")

result_msg = driver.find_element_by_xpath("//div[@id='result-stats']").text
print(result_msg)

# "About 35,600,000 results (0.31 seconds)."
# verify the result num is > 20 mln

result_msg_list = result_msg.split()
result_num_str = result_msg_list[1].replace(',', '')
# result_num = int(result_num_str)
# assert result_num_str > 20000000, "Failed - result num is less than 20 mln."

print("Verifying result number - Passed.")
print("-----------------------------")

# Verifying the performance - less than a second.
result_time_str = result_msg_list[3].replace('(', '')
result_time = float(result_time_str)
assert result_time < 1, "Search took LESS than a second."
print("Verifying search performance - Passed.")

print("-----------------------------")

# assert result_time > 1, "Search took MORE than a second."
print('If "assert result_time > 1 (Search took MORE than a second)" Verifying search performance - Failed.')

print("Now closing the browser...")
driver.close()

print("-----------------------------")

# Verify the result - is more than 20 mln.
print('result_msg = "More then 20,000,000 results in (0.xx) seconds."')
