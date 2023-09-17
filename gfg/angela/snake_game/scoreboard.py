from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_score()
        self.hideturtle()
        self.clear()
        self.penup()
        self.pencolor('white')
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_score()   
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def read_score(self):
        with open('data.txt') as file:
            contents = file.read()
            return int(contents)
        
    def write_score(self):
        with open('data.txt', mode='w') as file:
            score = str(self.high_score)
            file.write(score)

    