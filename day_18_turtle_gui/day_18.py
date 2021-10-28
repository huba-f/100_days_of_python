from turtle import Turtle, Screen
import heroes

print(heroes.gen())
timmy = Turtle()
timmy.hideturtle()
timmy.pensize(2)


# def dashed_line_maker():
#     timmy.forward(20)
#     timmy.up()
#     timmy.forward(20)
#     timmy.down()
#     timmy.forward(20)

def triangle():
    for _ in range(3):
        timmy.pencolor('rosybrown')
        timmy.right(120)
        timmy.forward(100)


def square():
    for _ in range(4):
        timmy.pencolor('lightcoral')
        timmy.right(90)
        timmy.forward(100)


def pentagon():
    for _ in range(5):
        timmy.pencolor('indianred')
        timmy.right(72)
        timmy.forward(100)


def hexagon():
    for _ in range(6):
        timmy.pencolor('brown')
        timmy.right(60)
        timmy.forward(100)


def heptagon():
    for _ in range(7):
        timmy.pencolor('firebrick')
        timmy.right(51.428571429)
        timmy.forward(100)


def octagon():
    for _ in range(8):
        timmy.pencolor('maroon')
        timmy.right(45)
        timmy.forward(100)


def nonagon():
    for _ in range(9):
        timmy.pencolor('darkred')
        timmy.right(40)
        timmy.forward(100)


def decagon():
    for _ in range(10):
        timmy.pencolor('red')
        timmy.right(36)
        timmy.forward(100)


def circle():
    for _ in range(100):
        timmy.pencolor('purple')
        timmy.right(3.6)
        timmy.forward(100)


triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
nonagon()
decagon()
circle()

screen = Screen()
screen.exitonclick()
