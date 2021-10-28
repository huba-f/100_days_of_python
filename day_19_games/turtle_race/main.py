from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='make your bet!', prompt='choose your turtle: ')
colors = ['red', 'blue', 'brown', 'green', 'purple', 'orange']
all_turtles = []

y = -100
for _ in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-50)
    y += 30
    new_turtle.color(colors[_])
    new_turtle.goto(x=-230, y=y)
    all_turtles.append(new_turtle)


if user_bet != '':
    is_race_on = True

while is_race_on:

    for t in all_turtles:
        if t.xcor() > 230:
            winner = t.pencolor()
            if user_bet == winner:
                print(f"you bet right! {winner} is the winner")
            else:
                print(f"you bet for the {user_bet} turtle, and {winner} is the winner, more luck next time!")
            is_race_on = False

        rand_distance = randint(1, 10)
        t.forward(rand_distance)

screen.exitonclick()
