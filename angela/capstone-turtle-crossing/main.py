from turtle import Screen
from turtles import Turtles
from scoreboard import Scoreboard
from cars import Car
import time

screen = Screen()
screen.setup(800, 600)
screen.tracer(0)
screen.listen()

timmy = Turtles()
scoreboard = Scoreboard()
car = Car()

screen.onkey(fun=timmy.move, key='Up')

car_list = []
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    car.create_car()
    car.move_car()

    # Check collision with cars
    for car_object in car.car_list:
        if timmy.distance(car_object) < 18:
            scoreboard.game_over()
            game_is_on = False

    # Detect collision with top wall
    if timmy.ycor() > 280:
        timmy.reset()
        car.increase_speed()
        scoreboard.update_scoreboard()

screen.exitonclick()


