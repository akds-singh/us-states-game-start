import time

import pandas as pd
from turtle import Turtle, Screen
from prompt import Prompt
from text import Text


turtle = Turtle()
screen = Screen()
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
# screen.tracer(0)


prompt = Prompt()
# print(state_name)

# TODO: 1. 'state' name that you have just typed , try to match with 'state' colomn of .csv file
data = pd.read_csv('50_states.csv')
total_states = data['state'].count()
# print(data)
remain_states = 0
screen.title(f'{remain_states}/{total_states}US states Game')

# print(row_df)
# print(type(xc))
# print(xc)
# print(yc)

# TODO: 2. create turtle with state name and Go to the state's corresponding cordinate on the map
# text = Text()
# text.hideturtle()
# text.penup()
# # print(text.heading())
# toward = text.towards(xc, yc)
# # print(toward)
# text.setheading(toward)
# text.penup()
# text.hideturtle()
# state = 'akash'
# screen.addshape(state)
# text.shape(state)
count_state = 0
at_des = False
while not at_des:
    # screen.update()
    # time.sleep(0.1)

    state_name = prompt.display_prompt(count_state, total_states)
    # print(state_name)

    row_df = data[data.state == state_name]
    state_col = data['state']
    # print(row_df)
    if not state_col[state_col.isin([state_name])].empty:
        print('under is statement')
        count_state += 1
        xc = row_df.x.item()
        yc = row_df.y.item()
        print(xc)
        print(yc)
    # text.goto(0,0)
    # text.setheading(0)
        text = Text()
    # toward = text.towards(xc, yc)
    # text.setheading(toward)
    # time.sleep(5)
    # text.move_text(state_name, xc, yc)
        text.set_heading(xc, yc)
    # time.sleep(5)
        text.move_text(state_name, xc, yc)
    # text.clear()
    # text.write(f'{state_name}', move=False, font=('Arial', 10, 'normal') )
    #
    # # text.setheading(toward)
    # text.forward(10)

    # if text.distance((xc, yc)) < 10:
    #     at_des = True

# text.goto(xc, yc)
# text.write(f'{state_name}', move=True, font=('Arial', 10, 'normal') )

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# screen.onscreenclick(get_mouse_click_coor)
#
screen.mainloop()

# screen.exitonclick()
