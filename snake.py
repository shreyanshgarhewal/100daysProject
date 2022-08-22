from turtle import Turtle, Screen
import time
import random
from scoreboard import Score


class Snake:

    def __init__(self, sw, sh):
        self.w = sw
        self.h = sh
        self.body = []
        self.make_body()
        self.fd = Turtle("circle")
        self.screen = Screen()
        self.screen.title("Snake in your ass")
        self.screen.setup(sw, sh)
        self.screen.bgcolor("black")
        self.move()
        self.screen.exitonclick()

    def make_body(self):
        pos = [100-(self.w / 2), 80-(self.w / 2), 60-(self.w / 2)]

        for i in range(0, 3):
            pixel = Turtle("square")
            pixel.color("white")
            pixel.penup()
            pixel.goto(pos[i], 0)
            self.body.append(pixel)

    def f1(self):
        if self.body[0].heading() != 180:
            self.body[0].setheading(0)

    def f2(self):
        if self.body[0].heading() != 270:
            self.body[0].setheading(90)

    def f3(self):
        if self.body[0].heading() != 0:
            self.body[0].setheading(180)

    def f4(self):
        if self.body[0].heading() != 90:
            self.body[0].setheading(270)

    def food_generator(self):
        self.fd.shape("circle")
        self.fd.color("green")
        self.fd.penup()
        xx = random.randint(-self.w/2 + 40, self.w/2 - 40)
        yy = random.randint(-self.h/2 + 40, self.h/2 - 40)
        self.fd.speed("fastest")
        self.fd.goto(xx, yy)

    def move(self):
        game_is_on = True
        self.screen.tracer(0)
        self.food_generator()

        while game_is_on:

            scr = Score()

            for i in range(1, len(self.body)):

                x = self.body[0].xcor()
                y = self.body[0].ycor()
                self.body[0].forward(20)
                self.body[i].goto(x, y)

                self.screen.listen()
                self.screen.update()
                self.screen.onkey(fun=self.f1, key="d")
                self.screen.onkey(fun=self.f2, key="w")
                self.screen.onkey(fun=self.f3, key="a")
                self.screen.onkey(fun=self.f4, key="s")

                if x > (self.w/2) - 60 or x < 60 - (self.w/2):

                    x = -x
                    self.body[0].goto(x, y)
                    self.body[0].forward(20)

                if y > (self.h/2) - 60 or y < 60 - (self.h/2):

                    y = -y
                    self.body[0].goto(x, y)
                    self.body[0].forward(20)

                self.body[0].forward(20)
                time.sleep(1)

                if self.body[0].distance(self.fd) < 15:

                    self.food_generator()
                    increment = Turtle("square")
                    increment.penup()
                    increment.color("white")
                    self.body.append(increment)

                    scr.update()

                for i in range(2, len(self.body)):
                    if self.body[0].distance(self.body[i]) < 5:
                        scr.game_over_prompt()
                        game_is_on = False

            self.screen.update()



