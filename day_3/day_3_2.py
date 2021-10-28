year = int(input('year: '))

if year % 4 == 0 and year % 100 != 0:
    print('leap year')
elif year % 4 == 0 and year % 100 == 0:
    if year % 400 == 0:
        print('leap year')
    else:
        print('not leap')
else:
    print('not leap')
