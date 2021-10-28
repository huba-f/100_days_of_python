from turtle import Turtle


class TextMover(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_state(self, name, x, y):
        self.goto(x, y)
        self.write(name, align='center', font=('Arial', 8, 'normal'))

    def end_of_game(self):
        self.goto(0, 0)
        self.write('The game ended', align='center', font=('Arial', 16, 'normal'))

    def won(self):
        self.goto(0, 0)
        self.write('You won!', align='center', font=('Arial', 16, 'normal'))
