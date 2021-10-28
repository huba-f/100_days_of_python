from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('White')
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-100, y=180)
        self.write(self.l_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(x=100, y=180)
        self.write(self.r_score, align='center', font=('Courier', 80, 'normal'))

    def point_to_l(self):
        self.l_score += 1
        self.update_scoreboard()

    def point_to_r(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        if self.l_score == 10:
            self.clear()
            self.goto(x=0, y=180)
            self.write('Left Player won', align='center', font=('Courier', 40, 'normal'))

        elif self.r_score == 10:
            self.clear()
            self.goto(x=0, y=180)
            self.write('Right Player won', align='center', font=('Courier', 40, 'normal'))
