from turtle import Turtle
STARTING_POSITIONS = [(-600, 0), (600, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Pong:

    def __init__(self):
        self.pongs = []
        self.create_pongs()
        self.head = self.pongs[0]

    def create_pongs(self):
        for position in STARTING_POSITIONS:
            pong = Turtle()
            pong.shape("square")
            pong.color("black")
            pong.penup()
            pong.shapesize(4, 1)
            pong._tracer(0)
            pong.goto(position)
            pong._tracer(1)
            self.pongs.append(pong)

    def go_up(self):
        new_y = self.pongs[0].ycor() + 20
        self.pongs[0].goto(self.pongs[0].xcor(), new_y)

    def go_down(self):
        new_y = self.pongs[0].ycor() - 20
        self.pongs[0].goto(self.pongs[0].xcor(), new_y)
