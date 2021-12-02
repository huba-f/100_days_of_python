from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chrome_driver_file_path = "/home/huba/chromedriver_linux64/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_file_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# num_of_articles = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')

# num_of_articles = driver.find_element_by_css_selector('#articlecount a')
# #
# print(num_of_articles.click())

search = driver.find_element_by_name("search")
search.send_keys("bitcoin")
search.send_keys(Keys.ENTER)

driver.quit()
