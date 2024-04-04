from turtle import Screen, Turtle
import pandas
screen = Screen()
screen.title('US states')
image = 'blank_states_img.gif'
timmy = Turtle()
timmy.hideturtle()
timmy.penup()
screen.bgpic(image)
data = pandas.read_csv('50_states.csv')
states = data['state'].tolist()
x_cor = data['x'].tolist()
y_cor = data['y'].tolist()
game_is_on = Turtle
counter = 0
sayed_states = []
while game_is_on:
    name = screen.textinput(f'{counter}/ 50 Guess State:', 'Input : ').title()
    if name in states:
        index = states.index(name)
        position = (x_cor[index], y_cor[index])
        timmy.goto(position)
        timmy.write(name, align='center', font=('Courier', 8, 'normal'))
        if name not in sayed_states:
            counter += 1
            sayed_states.append(name)
    else:
        timmy.goto(0, 0)
        timmy.write(f'Score : {counter} \n Game Over', align='center', font=('Courier', 24, 'normal'))
        game_is_on = False
# timmy.color('red')
# for state in states:
#     if state not in sayed_states:
#         index = states.index(state)
#         position = (x_cor[index], y_cor[index])
#         timmy.goto(position)
#         timmy.write(state, align='center', font=('Courier', 8, 'normal'))

# for state in sayed_states:
#     if state in states:
#         states.remove(state)
#
# not_guessed = {
#     'states': states
# }
# new_data = pandas.DataFrame(not_guessed)
# new_data.to_csv('not_guessed')
screen.exitonclick()

# data_dict = {
#     'students': ['abebe', 'leul', 'tigist'],
#     'score': [43, 23, 63]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv('new.csv')
