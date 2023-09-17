import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')

image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)
turtle.penup()

data = pandas.read_csv('50_states.csv')
states = data['state'].to_list()

game_is_on = True
correct = 0
title = 'Guess the state'

while game_is_on:
    answer = screen.textinput(title=title, prompt="What's another state's name?").title()
    if answer in states:
        correct += 1
        title = f"{correct}/50 States Correct"

        state_data = data[data.state == answer].to_dict()
        state_index = data.index[data.state == answer][0]

        x = state_data['x'][state_index]
        y = state_data['y'][state_index]

        screen.tracer(0)
        turtle.goto(x, y)
        turtle.write(f"{answer}", align='center', font=("Arial", 10, "normal"))
        turtle.goto(0, 0)
        screen.update()

        states.remove(answer)
    
    if correct == 50:
        game_is_on = False
        turtle.goto(0, 0)
        turtle.write("Congratulation, You've completed the game", align='center', font=("Arial", 16, "normal"))

    if answer == "Exit":
        game_is_on = False

pandas.DataFrame(states).to_csv('states_to_learn.csv')

screen.exitonclick()