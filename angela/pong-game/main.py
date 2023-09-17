from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
turtle = Turtle()

screen.setup(800, 600)
screen.title('Pong')
screen.bgcolor('black')
screen.listen()
screen.tracer(0)

paddle = Paddle(350, 0)
paddle2 = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(fun=paddle.up, key='Up')
screen.onkey(fun=paddle.down, key='Down')

screen.onkey(fun=paddle2.up, key='w')
screen.onkey(fun=paddle2.down, key='s')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # Detect collision with right wall
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()
    #Detect collision with left wall
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()
  
screen.exitonclick()