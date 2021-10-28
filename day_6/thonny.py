import random
# hangman
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
random_words = ['desktop', 'telephone', 'monday']
# chosing the random word from the list
chosen_word = list(random.choice(random_words))

# creating the blank list
blank = ['_']
word_lenght = len(chosen_word)
while not len(blank) == word_lenght:
    blank += '_'

lives = 6

while not end_of_game:
    # getting the user to guess a letter
    guess = input('guess a letter: ').lower()

    # checking and inserting the 'guess' letter into the 'blank' list
    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            blank[position] = letter
        if letter != guess:
            lives -= 1
            if lives == 0:
                end_of_game = True
                print('you lose')
    print(blank)
    print(lives)
    # lose
    if letter != guess:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('you lose')
    # win
    if not '_' in blank:
        end_of_game = True
        print('you win')
