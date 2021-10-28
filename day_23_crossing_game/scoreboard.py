from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('Black')
        self.penup()
        self.score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-230, y=265)
        self.write(f'Level: {self.score}', align='center', font=('Courier', 20, 'normal'))

    def score_increase(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.update_scoreboard()
        message = Turtle()
        message.hideturtle()
        message.penup()
        message.goto(x=0, y=0)
        message.color('black')
        message.write('Game Over', align='center', font=('Courier', 50, 'bold'))
