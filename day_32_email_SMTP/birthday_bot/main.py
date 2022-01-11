import datetime as dt
import random
import smtplib
import pandas


# constants
my_email = 'nyelrugosibakugan@gmail.com'
my_password = 'xxxx'



# extracting data
birthday_data = pandas.read_csv('employees.csv')
print(type(birthday_data.Name[2]))

celebrants = []

# converting it to managable format
for n in range(len(birthday_data)):
	celebrants.append({
	'name': birthday_data.Name[n],
	'email': birthday_data.Email[n],
	'month': birthday_data.Month[n],
	'day': birthday_data.Day[n], 
	})

# getting the date
now = dt.datetime.now()
current_day = now.day 
current_month = now.month

# creating letters
random_letter = f'wishes/wish{random.randint(1, 3)}.txt'

with open(random_letter,'r') as letter:
	data = letter.read()

# brain
for l in celebrants:
	current = l
	# formatting letter
	if current['month'] == current_month and current['day'] == current_day:
		pre_letter = data.replace('[my_name]', 'Huba')
		letter = pre_letter.replace('[Name]', current['name'])
		
		# sending email
		with smtplib.SMTP('smtp.gmail.com') as connection:
		    connection.starttls()
		    connection.login(user=my_email, password=my_password)
		    connection.sendmail(
		    	from_addr=my_email,
				to_addrs=current['email'],
	            msg=f"Subject:Happy Birthday\n\n{letter}")
