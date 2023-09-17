from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.shapesize(5, 1)
        self.color('white')
        self.penup()
        self.goto(x, y)

    def up(self):
        self.newy = self.ycor() + 20
        self.goto(self.xcor(), self.newy)

    def down(self):
        self.newy = self.ycor() - 20
        self.goto(self.xcor(), self.newy)


