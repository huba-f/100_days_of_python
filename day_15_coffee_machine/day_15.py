from machine import *


def game():
    # check order
    def check_order():
        # check the type of coin the user wants and quantity of it and process them
        def coin_identifier():
            type_of_coin = input(
                f"we process 'pennies', 'nickels', 'dimes', 'quarters'. Please choose one: ").lower()
            quantity = int(input(f"how many of them?: "))
            if type_of_coin == 'penny' or type_of_coin == 'pennies':
                machine_resources['money'] = compatible_coins[0]['value'] * quantity
            elif type_of_coin == 'nickel' or type_of_coin == 'nickels':
                machine_resources['money'] = compatible_coins[1]['value'] * quantity
            elif type_of_coin == 'dime' or type_of_coin == 'dimes':
                machine_resources['money'] = compatible_coins[2]['value'] * quantity
            elif type_of_coin == 'quarter' or type_of_coin == 'quarters':
                machine_resources['money'] = compatible_coins[3]['value'] * quantity
            else:
                print("we don't support this type of coin")
                coin_identifier()
            while not machine_resources['money'] >= coffee['price']:
                print(f"not enough money (${machine_resources['money']}) please insert some more coin")
                coin_identifier()

        # check if the machine got the resources for the chosen type of coffee
        def check_modify_availability():
            if machine_resources['water'] <= coffee['water_needed']:
                print('not enough water')
                print(
                    f"here is the refund {machine_resources['money']}, we are sorry we couldn't serve you the {coffee['type']}")
                return
            elif machine_resources['money'] >= coffee['price']:
                machine_resources['water'] -= coffee['water_needed']
            if machine_resources['milk'] <= coffee['milk_needed']:
                print('not enough milk')
                print(
                    f"here is the refund {machine_resources['money']}, we are sorry we couldn't serve you the {coffee['type']}")
                return
            elif machine_resources['money'] >= coffee['price']:
                machine_resources['milk'] -= coffee['milk_needed']
            if machine_resources['coffee_powder'] <= coffee['coffee_powder_needed']:
                print('not enough coffee')
                print(
                    f"here is the refund {machine_resources['money']}, we are sorry we couldn't serve you the {coffee['type']}")
                return
            elif machine_resources['money'] >= coffee['price']:
                machine_resources['coffee_powder'] -= coffee['coffee_powder_needed']
            if machine_resources['money'] >= coffee['price']:
                machine_resources['money'] -= coffee['price']
                print(f"enjoy your {coffee['type']} ☕.")
                print(f"here is the change: {machine_resources['money']}, thanks for choosing us!")
                machine_resources['money'] = 0
                game()

        which_coffee = input('what would you like? (Espresso($1.50)/Latte($2.50)/Cappuccino($3.00)/nothing?: ').lower()
        if which_coffee == 'espresso':
            coffee = coffees[0]
            coin_identifier()
            check_modify_availability()
        elif which_coffee == 'latte':
            coffee = coffees[1]
            coin_identifier()
            check_modify_availability()
        elif which_coffee == 'cappuccino':
            coffee = coffees[2]
            coin_identifier()
            check_modify_availability()
        elif which_coffee == 'nothing':
            print('thanks for your time')
            return
        elif which_coffee == 'report':
            print(
                f"water: {machine_resources['water']} ml\nmilk: {machine_resources['milk']} ml\ncoffee powder: {machine_resources['coffee_powder']} g\ncash: ${machine_resources['money']}")
        else:
            print("we don't have this type of coffee, please choose one out of the available ones!")
            game()
        check_modify_availability()

    check_order()


game()
