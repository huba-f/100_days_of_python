import requests
import telegram_send
import smtplib


my_email = 'nyelrugosibakugan@gmail.com'
my_password = 'xxxx'

is_on = True
# getting api
while is_on:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    # extracting data from api
    latitude = data['iss_position']['latitude']
    longitude = data['iss_position']['longitude']

    LAT = False
    LNG = False

    # brain
    if float(latitude) >= 46.590685 and float(latitude) <= 46.973424:
        LNG = True
    if float(longitude) >= 25.261515 and float(longitude) <= 25.633677:
        LAT = True

    link = f"https://www.latlong.net/c/?lat={latitude}&long={longitude}"

    if LAT and LNG:
        # sending telegram
        telegram_send.send(messages=[link])
        # sending email
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs='zltnfrncz@gmail.com',
                msg=f"Subject:ISS\n\n{link}")
            is_on = False
