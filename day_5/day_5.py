import random
# import string_utils

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(len(letters))
print(len(symbols))
print(len(numbers))

print("Welcome to the PyPassword Generator!")
number_of_letters = int(input("How many letters would you like in your password?\n"))
number_of_symbols = int(input(f"How many symbols would you like?\n"))
number_of_numbers = int(input(f"How many numbers would you like?\n"))

password = ''

for letter in range(1, number_of_letters + 1):
    random_letters = random.randint(0, 52)
    password += letters[random_letters - 1]

for symbol in range(1, number_of_symbols + 1):
    random_symbols = random.randint(0, 9)
    password += symbols[random_symbols - 1]

for number in range(1, number_of_numbers + 1):
    random_numbers = random.randint(0, 10)
    password += numbers[random_numbers - 1]

''.join(random.sample(password,len(password)))

print(f'your password is: {password}')
