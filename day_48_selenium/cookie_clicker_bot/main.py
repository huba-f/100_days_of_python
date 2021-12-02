from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_file_path = "/home/huba/chromedriver_linux64/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_file_path)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")
# cursor_item = driver.find_element_by_id("buyCursor")

# money = driver.find_element_by_id("money").text
#
# # finding items
# items = driver.find_elements_by_css_selector("#store div")
# item_ids = [item.get_attribute("id") for item in items]
# item_ids = item_ids[::-1]
# # finding prices
# all_prices = driver.find_elements_by_css_selector("#store b")
# item_prices = []
#
# # slicing up prices
# for price in all_prices:
#     element_text = price.text
#     if element_text != "":
#         cost = int(element_text.split("-")[1].strip().replace(",", ""))
#         item_prices.append(cost)
#

while True:
    # for item in item_ids:
    #     print(item)
    #     current_item = driver.find_element_by_id(item)
    #
    #     current_item.click()
    cookie.click()

