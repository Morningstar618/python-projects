from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

screen.colormode(255)
sides = 3
while sides < 11:
    angle = 360 / sides
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy.color(r, g, b)
    for i in range(sides):
        timmy.forward(100)
        timmy.right(angle)
    sides += 1

screen.exitonclick()

