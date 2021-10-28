import random

name_input = input('enter names: ')
names = name_input.split(', ')

number_of_names = len(names)
random_int = random.randint(0, number_of_names)
bill_payer = names[random_int]
print(f'{bill_payer} have to pay for the bill.')
