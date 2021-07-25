from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350 , 0))
l_paddle = Paddle((-350 , 0))

ball = Ball()

score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collission with wall
    if ball.ycor()  >280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # Detect collission with r_paddle
    if ball.distance(r_paddle) < 50  and ball.xcor() >320 or ball.distance(l_paddle) <50 and ball.xcor() < -320:
        ball.bounce_x()
    
    # Detect R_paddle misses
    if ball.xcor() >380:
        ball.resetposition()
        score.l_point()
    
    #  Detect L_paddle misses
    if ball.xcor() < -380:
        ball.resetposition()
        score.r_point()
        





screen.exitonclick()