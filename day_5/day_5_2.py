scores = input('enter the scores: ').split()
highest_score = 0
for score in scores:
    if int(highest_score) < int(score):
        highest_score = score
print(f'the highest score is {highest_score}.')
