from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.color("black")
        self.goto(0, -250)
        self.display()

    def display(self):
        self.clear()
        self.write(f"Level {self.level}", align="center", font=FONT)

    def display_level(self):
        self.level += 1
        self.display()

    def display_game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER.", align="center", font=FONT)

