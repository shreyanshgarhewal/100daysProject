import pandas
import csv

import turtle
screen = turtle.Screen()

game_score = 0

screen.title(" U.S States Game")
image = "blank_states_img.gif"

us_map = turtle.Turtle()
screen.addshape(image)
us_map.shape(image)

file = open("50_states.csv")
data = pandas.read_csv(file)

guessed_state = []


def state_pop_up(name, x, y):
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(int(x), int(y))
    turtle.write(f"{name}", font=("Ariel", 8, "normal"))


while len(guessed_state) <= 50:

    state_input = screen.textinput(f"your score {game_score}/ 50", "Enter the states name inside USA: ").title()

    for row in data.state:
        if state_input == "Exit":
            break

        if state_input not in guessed_state:
            if state_input == row:
                s = data[data.state == state_input]
                state_pop_up(row, int(s['x']), int(s['y']))
                guessed_state.append(state_input)
                game_score = len(guessed_state)
