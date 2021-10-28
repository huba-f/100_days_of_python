import turtle as t
from turtle import Turtle, Screen
from random import randint

spiro = Turtle()
spiro.hideturtle()
spiro.speed(30)
t.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    bot_color = (r, g, b)
    return bot_color


def bot(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        spiro.color(random_color())
        spiro.circle(150)
        spiro.setheading(spiro.heading() + size_of_gap)


bot(1)
screen = Screen()
screen.exitonclick()
