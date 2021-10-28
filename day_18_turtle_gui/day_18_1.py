import turtle as t
from turtle import Turtle, Screen
from random import randint

bot = Turtle()
bot.hideturtle()
bot.pensize(5)
t.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    bot_color = (r, g, b)
    return bot_color


def move_bot():
    bot.pencolor(random_color())
    direction = randint(0, 3)
    if direction == 0:
        bot.right(90)
        bot.forward(15)
    elif direction == 1:
        bot.left(90)
        bot.forward(15)
    elif direction == 2:
        bot.forward(15)
    else:
        bot.left(180)
        bot.forward(15)


for _ in range(330):
    move_bot()

screen = Screen()
screen.exitonclick()
