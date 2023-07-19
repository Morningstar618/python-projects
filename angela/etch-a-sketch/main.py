from turtle import Turtle, Screen

t = Turtle()
s = Screen()


def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def clear_screen():
    s.resetscreen()

def counter_clockwise():
    t.left(10)

def clockwise():
    t.right(10)


s.listen()
s.onkey(key="w", fun=move_forward)
s.onkey(key="s", fun=move_backward)
s.onkey(key="a", fun=counter_clockwise)
s.onkey(key="d", fun=clockwise)
s.onkey(key="c", fun=clear_screen)


s.exitonclick()