from turtle import Turtle
import random

colors = ['red', 'blue', 'orange', 'pink', 'yellow', 'purple', 'green']

class Car:

    def __init__(self):
        self.car_list = []
        self.car_speed = 5

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.shapesize(1, 2)
            random_y = random.randint(-220, 220)
            new_car.goto(300, random_y)
            new_car.color(random.choice(colors))
            new_car.shapesize(1, 2)
            new_car.setheading(180)
            self.car_list.append(new_car)

    def move_car(self):
        for car in self.car_list:
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += 10


