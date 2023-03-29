from turtle import Turtle, Screen


class Prompt:
    def __init__(self):
        self.screen = Screen()
        # self.display_prompt()

    def display_prompt(self, remain_state, total_state):
        state_name = self.screen.textinput(f'{remain_state}/{total_state}Enter US state',
                                           prompt="What's US State name?").title()
        return state_name
