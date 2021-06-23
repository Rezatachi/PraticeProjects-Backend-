# Event listeners in python

# Using screen events
# turtle.listen(xdummy=None, ydummy=None)
# Set focus on TurtleScreen (in order to collect key-events). Dummy arguments are provided in order to be able to pass listen() to the onclick method.

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# Event listening


def move_forwards():

    tim.forward(10)


def move_backwards():
    tim.setheading(180)
    tim.backward(10)


def move_clockwise():
    tim.setheading(90)


def move_counterclockwise():
    tim.setheading(270)


def clear():
    tim.clear()
    tim.penup()
    tim.home()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_counterclockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()

# Higher order functions are functionst that work with other functions. It is taking functions as a parameter and working wtih it in side the body of the function. In python this is pretty commonly used.
