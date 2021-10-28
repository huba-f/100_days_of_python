from day_11_1 import *
from random import randint
print(blackjack_logo)
# black jack
list_of_cards = [
    # ACES:
    [1, 11], [1, 11], [1, 11], [1, 11],
    # COMMONS
    2, 2, 2, 2,
    3, 3, 3, 3,
    4, 4, 4, 4,
    5, 5, 5, 5,
    6, 6, 6, 6,
    7, 7, 7, 7,
    8, 8, 8, 8,
    9, 9, 9, 9,
    10, 10, 10, 10,
    # JACKS:
    10, 10, 10, 10,
    # QUEENS:
    10, 10, 10, 10,
    # KINGS:
    10, 10, 10, 10
]

comp_cards = []
user_cards = []
comp_total = sum(comp_cards)
user_total = sum(user_cards)




def game():
    global comp_cards
    global user_cards
    global comp_total
    global user_total

    should_continue = input('type \'y\' to get another card or \'n\' to pass: ')

    def choosen_card():
        global list_of_cards
        random_card = randint(0, len(list_of_cards) - 1)

        list_of_cards.remove(list_of_cards[random_card - 1])

        card = list_of_cards[random_card - 1]


        if card == [1, 11]:
            if comp_total + 11 > 21:
                card = 1
            else:
                card = 11
            if user_total + 11 > 21:
                card = 1
            else:
                card = 11
        return card

    if should_continue == 'y':
        comp_cards.append(choosen_card())
        user_cards.append(choosen_card())
        comp_total = sum(comp_cards)
        user_total = sum(user_cards)
        if comp_total == 21:
            print(f'\nBLACKJACK! computer won with the score of {comp_total}.\ncomputer\'s cards: {comp_cards}\nyour cards:{user_cards}')
            return
        if user_total == 21:
            print(f'\nBLACKJACK! you won with the score of {user_total}.\ncomputer\'s cards: {comp_cards}\nyour cards:{user_cards}')
            return
        if len(comp_cards) >= 5 and comp_total < 21:
            print(f'\nCHARLIE! computer has the score of {comp_total}, but got {len(comp_cards)}, The computer won\ncomputer\'s cards: {comp_cards}\nyour cards:{user_cards}')
            return
        if len(comp_cards) >= 5 and comp_total < 21:
            print(f'\nCHARLIE! computer has the score of {comp_total}, but got {len(comp_cards)}, The computer won\ncomputer\'s cards: {comp_cards}\nyour cards:{user_cards}')
            return
        if comp_total > 21 and user_total < 21:
            print(f'\nyou won with the score of {user_total}.\ncomputer\'s cards: {comp_cards}\nyour cards:{user_cards}')
            return
        if user_total > 21 and comp_total < 21:
            print(f'\ncomputer won with the score of {comp_total}.\ncomputer\'s cards: {comp_cards}\nyour cards:{user_cards}\ncomputer\'s cards: {comp_cards}\nyour cards:{user_cards}')
            return
        if comp_total >= 21 and comp_total == user_total:
            print(f'\ndraw\ncomputer\'s cards: {comp_cards}\nyour cards:{user_cards}')
            return
        print(f'computer\'s first card: {comp_cards[0]}\nyour card(s): {user_cards}, current score: {user_total}')
        game()

    if should_continue == 'n':
        comp_total = sum(comp_cards)
        user_total = sum(user_cards)
        if comp_total < 21 and comp_total > user_total:
            print(f'\ncomputer won with the score of {comp_total}.\ncomputer\'s cards: {comp_cards}\nyour cards:{user_cards}')
        if user_total < 21 and user_total > comp_total:
            print(f'\nyou won with the score of {user_total}.\ncomputer\'s cards: {comp_cards}\nyour cards:{user_cards}')
        if comp_total <= 21 and comp_total == user_total:
            print(f'\ndraw\ncomputer\'s cards: {comp_cards}\nyour cards:{user_cards}')



game()