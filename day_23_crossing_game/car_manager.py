from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.difficulty_level = 5
        self.move_dist = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(0, self.difficulty_level)
        if random_chance == 0:
            new_car = Turtle('square')
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            random_y = random.randint(-235, 255)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.move_dist)

    def level_up(self):
        self.move_dist += MOVE_INCREMENT
