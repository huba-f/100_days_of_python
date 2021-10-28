


import smtplib
import datetime as dt
import random

my_email = 'nyelrugosibakugan@gmail.com'
my_password = 'macskafasza'



now = dt.datetime.now()

if now.weekday() == 6:
	with open('quotes.txt') as file:
		quote_list = file.readlines()
		random_quote = random.choice(quote_list)



	with smtplib.SMTP('smtp.gmail.com') as connection:
	    connection.starttls()
	    connection.login(user=my_email, password=my_password)
	    connection.sendmail(
	    	from_addr=my_email,
			to_addrs='huba0ferencz@gmail.com',
            msg=f"Subject:sunday motivation\n\n{random_quote}")
	print(random_quote)