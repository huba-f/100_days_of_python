# higher lower game
from game_data import *
from random import randint


def chose_account():
    global accounts
    random_number = randint(0, len(accounts) - 1)
    random_account = accounts[random_number]
    accounts.remove(accounts[random_number])
    return random_account


name1 = chose_account()
print(
    f"\n{name1['name']} is a {name1['description']} from the {name1['country']} with {name1['follower_count']}M followers on Instagram.")
print('\nVS\n')
name2 = chose_account()
print(f"{name2['name']} is a {name2['description']} from the {name2['country']}.\n")


def game():
    if len(accounts) == 1:
        print('congratulations, you beat the game!')
        return
    # choosing and deleting a random 'account' from the 'accounts'

    user_guess = input('which one got more followers?: ')

    # checking if the user is right

    def higher_or_not(n1, n2):
        global name1
        global name2
        if n1['follower_count'] > n2['follower_count']:
            print('\ntrue\n')
            name1 = n1
            name2 = chose_account()
            print(
                f"\n{name1['name']} is a {name1['description']} from the {name1['country']} with {name1['follower_count']}M followers on Instagram.")
            print('\nVS\n')
            print(f"{name2['name']} is a {name2['description']} from the {name2['country']}.\n")
            game()
        elif n1['follower_count'] < n2['follower_count']:
            print(f"\nyou lost, {name2['name']} got {name2['follower_count']}M followers.")
            return

    if user_guess == name1['name']:
        higher_or_not(name1, name2)
    elif user_guess == name2['name']:
        higher_or_not(name2, name1)
    else:
        print('\n!! learn to type you fucking donkey !!')
        return


game()
