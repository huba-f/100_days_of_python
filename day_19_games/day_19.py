from turtle import Turtle, Screen

han = Turtle()
screen = Screen()


def move_forward():
    han.forward(30)


screen.listen()
screen.onkey(key='space', fun=move_forward)
screen.exitonclick()
