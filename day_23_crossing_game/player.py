from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.hideturtle()
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.showturtle()
        self.at_finish = False

    def move(self):
        self.forward(MOVE_DISTANCE)

    def at_finish_line(self):
        if self.ycor() == FINISH_LINE:
            return True

    def go_to_start(self):
        self.goto(STARTING_POSITION)
