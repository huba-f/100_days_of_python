from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


chrome_driver_file_path = "/home/huba/chromedriver_linux64/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_file_path)

driver.get('https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E87490&maxPrice=500'
           '&radius=0.25&propertyTypes=&includeLetAgreed=false&mustHave=&dontShow=&furnishTypes=&keywords=')

html = driver.page_source

soup = BeautifulSoup(html)

all_house = []

for house in soup.find_all('div', class_='l-searchResult is-list'):
    all_house.append({
        'address': house.find('address', class_="propertyCard-address").text,
        'price': house.find("span", class_="propertyCard-priceValue").text,
        'link': f"https://www.rightmove.co.uk{house.find('a', class_='propertyCard-priceLink propertyCard-rentalPrice').get('href')}"
    })


for house in all_house:
    driver.get('https://forms.gle/LHmtTBrUX2AU3pA59')

    address_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(house["address"])

    price_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(house["price"])

    link_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(house["link"])

    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit_button.click()

