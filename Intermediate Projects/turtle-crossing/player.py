from turtle import Turtle
START_POSITION = [(0, -300)]
MOVE_DISTANCE = 10
FINISH_LINE_Y = 400


class Terrance():

    def __init__(self):
        self.turtles = []
        self.generate_terrance()
        self.head = self.turtles[0]

    def generate_terrance(self):
        for position in START_POSITION:
            t = Turtle()
            t.left(90)
            t.shape("turtle")
            t.color("black")
            t.penup()
            t._tracer(0)
            t.goto(position)
            t._tracer(1)
            self.turtles.append(t)

    def go_up(self):
        new_y = self.turtles[0].ycor() + MOVE_DISTANCE
        self.turtles[0].goto(self.turtles[0].xcor(), new_y)
