# snake game
import turtle as t
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

t.colormode(255)
# creating screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor((186, 199, 1))
screen.title('Snake')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.13)
    snake.move()

    # detect collision with food

    if snake.head_of_snake.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall

    if snake.head_of_snake.xcor() > 280 or snake.head_of_snake.xcor() < -280 or snake.head_of_snake.ycor() > 280 or snake.head_of_snake.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        game_is_on = False
        # scoreboard.wall_hit()

    # detect collision with tail

    for segment in snake.segments[1:]:
        if snake.head_of_snake.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            game_is_on = False
            # scoreboard.tail_hit()


screen.exitonclick()
