# number guessing game
from design import *
from random import randint

print(logo)
print('\nfind out what random number the computer choose between 1 - 100')
level = input("choose your difficulty level ('hard' or 'easy'): ")
random_number = randint(1, 101)
# print(random_number)
if level == 'hard':
    lives = 5
elif level == 'easy':
    lives = 10
def game():
    global lives
    guess = int(input(f'you got {lives} live(s), enter your guess: '))
    if guess == random_number:
        print(f'you won. {random_number} was the number.')
    elif guess >= 1 and guess < random_number:
        lives -= 1
        print("too low'")
        if lives == 0:
            print(f"the number was {random_number} and you couldn't find it")
            return
        game()
    elif guess <= 100 and guess > random_number:
        lives -= 1
        print("too high")
        if lives == 0:
            print(f"the number was {random_number} and you couldn't find it")
            return
        game()
    else:
        print('your number is out of range')
        game()

game()