from selenium import webdriver

chrome_driver_file_path = "/home/huba/chromedriver_linux64/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_file_path)

driver.get('https://www.python.org/')
# price = driver.find_element_by_id("price_inside_buybox")
# print(price.text)
# # driver.close()

events_times = driver.find_elements_by_css_selector('.event-widget time')
events_names = driver.find_elements_by_css_selector('.event-widget li a')

events = {}

for n in range(len(events_times)):
    events[n] = {
        "time": events_times[n].text,
        "name": events_names[n].text
    }

print(events)


driver.quit()


