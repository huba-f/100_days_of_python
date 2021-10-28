year = int(input('year: '))
month = int(input('month (..th): '))
days_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def days_in_month():
    return days_months[month - 1]

if year % 4 == 0 and year % 100 != 0:
    days_months[1] = 29
    print(f'{days_in_month()} days in this month')
elif year % 4 == 0 and year % 100 == 0:
    if year % 400 == 0:
        days_months[1] = 29
        print(f'{days_in_month()} days in this month')
    else:
        print(f'{days_in_month()} days in this month')
else:
    print(f'{days_in_month()} days in this month')
