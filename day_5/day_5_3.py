scores = input('enter scores: ').split()
lowest_score = 100
for score in scores:
    if int(lowest_score) >= int(score):
        lowest_score = score


print(f'the lowest score was {lowest_score}.')
