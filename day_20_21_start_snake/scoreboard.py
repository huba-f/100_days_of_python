from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highest_score.txt", mode="r") as file:
            self.high_score = file.read()
        self.high_score = int(self.high_score)
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | Highest Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("highest_score.txt", mode="w") as file:
                file.write(str(self.score))
            with open("highest_score.txt", mode="r") as file:
                self.high_score = file.read()
        self.score = 0
        self.update_scoreboard()

    # def wall_hit(self):
    #     # self.goto(0, 0)
    #     # self.write(f"Game Over\nYou hit a wall\nFinal score: {self.score}", align=ALIGNMENT, font=FONT)
    #     pass

    # def tail_hit(self):
    #     # self.goto(0, 0)
    #     # self.write(f"Game Over\nYou hit your tail\nFinal score: {self.score}", align=ALIGNMENT, font=FONT)
    #     pass

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
