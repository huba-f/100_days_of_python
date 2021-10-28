import random
from ascii_art import *
from random_words import *
# hangman

print(hangman_text)
end_of_game = False
# chosing the random word from the list
chosen_word = list(random.choice(random_words_list))

# creating the blank list
blank = ['_']
word_lenght = len(chosen_word)
while not len(blank) == word_lenght:
    blank += '_'

lives = 6
hangman = 6

while not end_of_game:
    # getting the user to guess a letter
    guess = input('guess a letter: ').lower()

    # checking and inserting the 'guess' letter into the 'blank' list
    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            blank[position] = letter
    # losing lifes
    if not guess in chosen_word:
        hangman -= 1
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"you lose, your word was {' '.join(chosen_word)}")
        print(f'you have left {lives}')
    # win
    if not '_' in blank:
        end_of_game = True
        print('\nyou won')
    print(f"{stages[hangman]}\n\n{' '.join(blank)}")
