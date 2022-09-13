import time
from turtle import Screen
import car_manager
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True

pl = Player()
car_m = CarManager()
scrb = Scoreboard()

screen.listen()
screen.onkeypress(pl.go_up, "Up")

j = 5

while game_is_on:

    time.sleep(0.1)
    screen.update()

    i = random.randint(0, j)

    if i == 0:
        car_m.create_cars()

    for cars in car_m.all_cars:
        if pl.distance(cars) < 20:
            scrb.display_game_over()
            game_is_on = False

    if pl.ycor() >= 250:
        pl.goto(0, -300)
        j -= 1
        car_m.level_up()
        scrb.display_level()

    car_m.move()


screen.exitonclick()




