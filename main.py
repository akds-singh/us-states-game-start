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

prompt = Prompt()
data = pd.read_csv('50_states.csv')
total_states = data['state'].count()
remain_states = 0
screen.title(f'{remain_states}/{total_states}US states Game')


count_state = 0
at_des = False
while not at_des:

    state_name = prompt.display_prompt(count_state, total_states)

    row_df = data[data.state == state_name]
    state_col = data['state']
    if not state_col[state_col.isin([state_name])].empty:
        print('under is statement')
        count_state += 1
        text = Text()
        text.set_heading(int(row_df.x), int(row_df.y))
        text.move_text(state_name, int(row_df.x), int(row_df.y))

screen.mainloop()

