from bs4 import BeautifulSoup
import requests
import smtplib

my_email = 'nyelrugosibakugan@gmail.com'
my_password = 'macskafasza'


response = requests.get("https://www.emag.ro/laptop-apple-macbook-pro-14-2021-cu-procesor-apple-m1-pro-8-nuclee-cpu"
                        "-and-14-nuclee-gpu-16gb-512gb-ssd-space-grey-int-kb-mkgp3ze-a/pd/D50SVXMBM/?cmpid=86846")
soup = BeautifulSoup(response.text, "html.parser")
current_price = soup.find(name="p", class_="product-new-price").get_text()

current_price = float(current_price[:6])


with open("old_price.txt", "r") as file:
    old_price = float(file.read())


if old_price > current_price:

    with open("old_price.txt", "w") as file:
        file.write(str(current_price))
    message = f"{current_price} ron for the macbook"
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='huba0ferencz@gmail.com',
            msg=f"Subject:price drop\n\n{message}: https://www.emag.ro/laptop-apple-macbook-pro-14-2021-cu-procesor-apple-m1-pro-8-nuclee-cpu-and-14-nuclee-gpu-16gb-512gb-ssd-space-grey-int-kb-mkgp3ze-a/pd/D50SVXMBM/?cmpid=86846")
