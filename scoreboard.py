from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.clear()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.printing()

    def printing(self):
        self.goto(0, 200)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update(self):
        self.clear()
        self.score += 1
        self.printing()

    def game_over_prompt(self):
        self.goto(-130, 0)
        self.write(f"Game over.", font=FONT)




