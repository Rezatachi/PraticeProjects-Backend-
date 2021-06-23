import turtle
from turtle import Screen
# Reached into the Turtle package and grabbed a class then saved it into a variablle called timmy'
timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.shapesize(stretch_len=10, stretch_wid=10)
timmy.color("red")


def mt():
    turtle.distance(30, 40)


def mr():
    timmy.right(20)


def ml():
    timmy.left(20)


def mb():
    timmy.down(20)


# # Showing the object, the Turtle as the attribute
# my_screen = Screen()
# my_screen.title("Welcome to the turtle zoo!")
# my_screen.onkey(mr, "Up")
# my_screen.onkey(mr, "Right")
# my_screen.onkey(ml, "Left")
# my_screen.onkey(mb, "Down")
# my_screen.listen()
# my_screen.exitonclick()

# from prettytable import PrettyTable

# table = PrettyTable()
# table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
# table.add_column("Type", ["Electric", "Water", "Fire"])

# print(table)
