from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chrome_driver_file_path = "/home/huba/chromedriver_linux64/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_file_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")


first_name = driver.find_element_by_name("fName")
first_name.send_keys("huba")
first_name.send_keys(Keys.ENTER)

last_name = driver.find_element_by_name("lName")
last_name.send_keys("ferencz")
last_name.send_keys(Keys.ENTER)

email = driver.find_element_by_name("email")
email.send_keys('szewasz.te@gmail.com')
email.send_keys(Keys.ENTER)
