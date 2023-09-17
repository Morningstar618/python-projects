from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

screen.colormode(255)
timmy.pensize(10)
timmy.speed(0)
movement = [0, 90, 180, 270]

for _ in range(100):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy.color(r, g, b)

    timmy.setheading(random.choice(movement))
    timmy.forward(30)
   

screen.exitonclick()

