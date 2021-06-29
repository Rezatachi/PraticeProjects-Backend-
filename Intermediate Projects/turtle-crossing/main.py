from turtle import Screen
from player import Terrance
from car_logic import CarManager
import random
import time


# Screen Init
screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=900, height=700)

# Turtle Init
terrance = Terrance()

# Carmanager Iinit
car_log = CarManager()

# Screen key logic
screen.listen()
screen.onkey(terrance.go_up, "Up")

game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_log.move()

screen.exitonclick()
