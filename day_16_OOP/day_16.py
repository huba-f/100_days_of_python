# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color('chartreuse4')
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ['Pokemon', 'Type']
table.add_rows(
    [
        ['Aerodactyl', 'Flying'],
        ['Aggron', 'Rock'],
        ['Aipom', 'Normal'],
        ['Alakazam', 'Psychic'],
    ]
)
table.align = 'l'

print(table)