print('welcome to the tim calculator!')
bill = input('bill: ')
tip_percentage = input('percentage of the tip you want to give: ')
persons = input('number of people who eated: ')

tip = (float(bill) * float(tip_percentage)) / 100
total_bill = (float(bill) + float(tip))
bill_per_person = float(total_bill) / float(persons)
print('each person should pay ' + str(bill_per_person))
