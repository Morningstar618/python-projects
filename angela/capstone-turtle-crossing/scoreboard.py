from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('black')
        self.penup()
        self.goto(-340, 260)
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.write(f"LEVEL: {self.level}", align='center', font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align='center', font=("Arial", 15, "bold"))