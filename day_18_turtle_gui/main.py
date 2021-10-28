import colorgram
import turtle as t
from random import randint
from turtle import Turtle, Screen
t.colormode(255)
colors = [(249, 218, 239), (229, 236, 244), (245, 233, 221), (200, 76, 9), (215, 246, 234), (227, 74, 153),
          (229, 103, 58), (222, 165, 129), (15, 73, 148), (189, 98, 39), (251, 62, 234), (96, 223, 174),
          (120, 151, 189), (3, 236, 168), (35, 139, 37), (241, 189, 159), (44, 15, 26), (4, 48, 97), (40, 102, 171),
          (248, 1, 239)]

j = Turtle()

j.hideturtle()
j.penup()
j.speed(300)
j.setx(-260)
j.sety(-250)


def line():
    for _ in range(9):
        j.color(colors[randint(0, 19)])
        j.dot(20)
        j.forward(50)
        j.color(colors[randint(0, 19)])
        j.dot(20)


def left():
    j.left(90)
    j.forward(50)
    j.left(90)


def right():
    j.right(90)
    j.forward(50)
    j.right(90)


for _ in range(5):
    line()
    left()
    line()
    right()


screen = Screen()
screen.exitonclick()
