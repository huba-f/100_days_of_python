from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()


def move_forwards():
    pen.forward(10)


def move_backwards():
    pen.backward(10)


def turn_left():
    pen.left(3)


def turn_right():
    pen.right(3)


def clear_drawings():
    pen.clear()
    pen.penup()
    pen.home()
    pen.pendown()


screen.listen()

screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear_drawings)

screen.exitonclick()
