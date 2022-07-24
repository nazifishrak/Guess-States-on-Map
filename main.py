import turtle
import pandas
image = "blank_states_img.gif"

screen = turtle.Screen()
screen.addshape(image)
turtle.shape(image)

csv_data_frame = pandas.read_csv('./50_states.csv')
score = 0
guessed_states = []
total_questions = len(csv_data_frame.state)
print(total_questions)
state_list = csv_data_frame.state.to_list()
while score < total_questions:
    user_input = screen.textinput(title=f"US states game {score}/{total_questions}", prompt="Guess a state").capitalize()

    if  user_input in state_list and user_input not in guessed_states:
        guessed_states.append(user_input)
        temp_turtle = turtle.Turtle()
        temp_turtle.hideturtle()
        temp_turtle.pu()
        ROW = csv_data_frame[csv_data_frame.state == user_input]
        # print(ROW)
        temp_turtle.goto(int(ROW.x), int(ROW.y))
        temp_turtle.write(ROW.state.item())
        score =  score + 1
        # print(score)
    elif user_input == 'Quit':
        break

states_not_guessed = []
for state in state_list:
    if state not in guessed_states:
        states_not_guessed.append(state)

data_frame = pandas.DataFrame(states_not_guessed)
data_frame.to_csv('./not_guessed_names.csv')

