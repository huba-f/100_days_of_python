from selenium import webdriver
from selenium.webdriver.common.keys import Keys

EMAIL = "xxxxx"
PASSWORD = "xxxxx"

chrome_driver_file_path = "/home/huba/chromedriver_linux64/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_file_path)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location"
           "=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

cookie_accept_button = driver.find_element_by_xpath('//*[@id="artdeco-global-alert-container"]/div/section/div/div['
                                                    '2]/button[2]')
cookie_accept_button.click()

sign_in_button = driver.find_element_by_class_name('nav__button-secondary')
sign_in_button.click()

username_field = driver.find_element_by_id("username")
username_field.send_keys(EMAIL)
username_field.send_keys(Keys.ENTER)

password_field = driver.find_element_by_id("password")
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)

save_button = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div[3]/div[2]/div/section[2]/div/div/div["
                                           "1]/div/div[1]/div/div[2]/div[3]/div/button")

save_button.click()
for n in range(1, 20):
    current_offer_class_name = f"jobs-search-two-pane__job-card-container--viewport-tracking-{n}"

    current_offer = driver.find_element_by_class_name(current_offer_class_name)
    current_offer.click()
    save_button.click()

