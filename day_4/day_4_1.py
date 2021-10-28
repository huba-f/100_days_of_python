import random
random_seed = int(input('enter a number: '))
random.seed(random_seed)
random_int = random.randint(0, 1)

if random_int == 0:
    print('heads')
else:
    print('tails')
