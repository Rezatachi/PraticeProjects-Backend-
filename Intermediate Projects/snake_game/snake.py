# Snake game

from turtle import Turtle, Screen

# Step 0: create screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


# Step 1: Create a snake body and display GUI
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in STARTING_POSITIONS:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    for seg in segments:
        seg.forward(20)


# Step 2: Move snake automatically and let us to change direction


# Step 3: Hit Food and create a new food on a new coordinate

# Step 4: Keep track of score and create a scoreboard


# Step 5: Detect wall collision and show Game Over


# Step 6: Detect snake collision with itself and show Game Over


screen.exitonclick()
