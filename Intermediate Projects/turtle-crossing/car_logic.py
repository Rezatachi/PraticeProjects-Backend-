from turtle import Turtle
import random

COLORS = ["red", "blue", "green", "yellow", "orange", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 0.5


class CarManager:
    def __init__(self):
        self.cars = []
        self.generate_cars()
        self.move()

    def generate_cars(self):
        for num in range(1, 20):
            car = Turtle()
            car._tracer(0)
            randomcolor = random.choice(COLORS)
            car.color(randomcolor)
            car.shape("square")
            car.shapesize(1, 2)
            car.penup()
            car.goto(400, random.choice(range(-300, 300)) + 10)
            car._tracer(1)
            self.cars.append(car)

    def move(self):
        for car_move in range(len(self.cars)):
            new_x = (self.cars[car_move - 1].xcor()) - MOVE_INCREMENT
            self.cars[car_move].goto(new_x, self.cars[car_move].ycor())
            self.head = self.cars[car_move]
        self.head.forward(STARTING_MOVE_DISTANCE)
