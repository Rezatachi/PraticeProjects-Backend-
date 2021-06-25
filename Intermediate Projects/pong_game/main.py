from turtle import Screen
from pong import Pong
from ball import Ball
from scoreboard import Scoreboard
import time
s = Screen()
s.setup(width=1280, height=800)
s.title("Pong")
pong = Pong()
ball = Ball()
score = Scoreboard()
s.listen()
s.onkey(pong.go_up, "Up")
s.onkey(pong.go_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    s.update()
    ball.move()

    if ball.ycor() > 360 or ball.ycor() < -360:
        ball.bounce()

    if ball.distance(pong.pongs[0]) < 50 and ball.xcor() > 550 or ball.distance(pong.pongs[1]) < 50 and ball.xcor() > -550:
        ball.pong_bounce()

    if ball.xcor() > 600:
        ball.miss()
        score.l_point()

    if ball.xcor() < -600:
        ball.miss()
        score.r_point()


s.exitonclick()
