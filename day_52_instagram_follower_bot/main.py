from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import time


CHROME_DRIVER_PATH = "/home/huba/chromedriver_linux64/chromedriver"
INSTAGRAM_EMAIL = 'sdfgsdgsd'
INSTAGRAM_PASSWORD = 'sdfgsdfgsd'


chrome_driver_file_path = "/home/huba/chromedriver_linux64/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_file_path)

driver.get("https://www.instagram.com/accounts/login/")


cookie_accept_button = driver.find_element_by_class_name("aOOlW.bIiDR")
cookie_accept_button.click()
time.sleep(3)

email_input_field = driver.find_element_by_name('username')
email_input_field.send_keys(INSTAGRAM_EMAIL)
time.sleep(3)

password_input_field = driver.find_element_by_name('password')
password_input_field.send_keys(INSTAGRAM_PASSWORD)
password_input_field.send_keys(Keys.ENTER)
time.sleep(3)

driver.get('https://www.instagram.com/hubaferencz/')

time.sleep(3)
follower_count = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
follower_count.click()

all_buttons = driver.find_elements_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child(5) > div > div.Pkbci > button")
for button in all_buttons:
    try:
        button.click()
        time.sleep(1)
    except ElementClickInterceptedException:
        cancel_button = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
        cancel_button.click()

