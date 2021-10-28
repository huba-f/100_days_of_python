from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
# screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()

screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 's')
screen.onkey(l_paddle.go_down, 'x')

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce_y()

    # detect collision with r_paddle
    if ball.xcor() > 340 and ball.distance(r_paddle) < 55:
        ball.bounce_x()
    # if it misses
    elif ball.xcor() > 350:
        scoreboard.point_to_l()
        ball.reset()

    # detect collision with l_paddle
    if ball.xcor() < -340 and ball.distance(l_paddle) < 55:
        ball.bounce_x()
    # if it misses
    elif ball.xcor() < -350:
        scoreboard.point_to_r()
        ball.reset()

    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        scoreboard.game_over()
        game_is_on = False
screen.exitonclick()
