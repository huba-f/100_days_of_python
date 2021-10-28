weight = float(input('enter your weight: '))
height = float(input('enter your height: '))

bmi = height / (weight ** 2)

if bmi <= 18.5:
    print('your bmi is ' + str(bmi) + ' and you are underweight')
elif bmi > 18.5 and bmi <= 25:
    print('your bmi is ' + str(bmi) + ' and you are normal weight')
elif bmi > 25 and bmi <= 30:
    print('your bmi is ' + str(bmi) + ' and you are normal overweight')
elif bmi > 30 and bmi <= 35:
    print('your bmi is ' + str(bmi) + ' and you are normal obese')
else:
    print('just die')
