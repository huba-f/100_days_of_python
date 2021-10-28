age = int(input('how old are you: '))
all_ages = 200
agest_left = all_ages - age
months_left = round(agest_left * 12, 2)
days_left = round(agest_left * 365, 2)

print(f'you have left {agest_left} ages, {months_left} months and {days_left} days')
