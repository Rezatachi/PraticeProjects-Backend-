from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
bet = screen.textinput("Betting", "Which turtle is going to win?")
colors = ["red", "orange", "blue", "green", "yellow", "purple"]
y_pos = [-70, -40, 110, -90, 20, -50]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-410, y_pos[turtle_index])
    all_turtles.append(new_turtle)


if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You won!, The {turtle.pencolor} won! ")
            else:
                print("You lost lmao")


screen.exitonclick()
