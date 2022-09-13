from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.sp = MOVE_INCREMENT

    def create_cars(self):
        new_car = Turtle("square")
        self.hideturtle()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(300, random.randint(-250, 250))
        self.all_cars.append(new_car)

    def move(self):
        for one in self.all_cars:
            one.backward(STARTING_MOVE_DISTANCE + self.sp)
            if one.xcor() < -320:
                self.all_cars.remove(one)

    def level_up(self):
        self.sp += 5






