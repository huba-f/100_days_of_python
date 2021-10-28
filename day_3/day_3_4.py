print('love calculator')
name_1 = input('first name: \n')
name_2 = input('second name: \n')

all_names = name_1.lower() + name_2.lower()

t = all_names.count('t')
r = all_names.count('r')
u = all_names.count('u')
e = all_names.count('e')
true = t + r + u + e

l = all_names.count('l')
o = all_names.count('o')
v = all_names.count('v')
e = all_names.count('e')

love = l + o + v + e

score =  str(true) + str(love)

score_for_calc = int(score)
if score_for_calc < 10 or score_for_calc > 90:
    print(f'your score is {score} and you go together like coke and menthos')
elif score_for_calc <= 40 and score_for_calc >= 50:
    print(f'your score is {score} and you are alright together')
else:
    print(f'your score is {score}.')



# combine the two name in one variable and then var.lower() ... nex time
