from color_extract import extract_color
from turtle import Turtle, Screen
import random


def draw_dot(x, y, y_coordinate):
    for _ in range(x):
        t.setposition(0, y_coordinate)
        t.pendown()
        for _ in range(y):
            t.dot(20, random.choice(color_list))
            t.penup()
            t.forward(50)
            t.pendown()

        t.penup()
        y_coordinate += 50


color_list = extract_color('dot.jpg', 20)

t = Turtle()
s = Screen()

s.colormode(255)
t.speed(4)

x = 10
y = 10
y_coordinates = 0


draw_dot(x, y, y_coordinates)

s.exitonclick()
