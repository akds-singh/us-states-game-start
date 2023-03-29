import time
from turtle import Turtle, Screen


class Text(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.toward_angle = 0

    def set_heading(self, x, y):
        self.goto(0,0)
        self.setheading(0)
        self.toward_angle = self.towards(x, y)
        self.setheading(self.toward_angle)

    def move_text(self, text, x, y):
        # self.distance((x, y)) < 10
        # print(self.position())
        # print(self.heading())
        # print('distance: ', self.distance((x, y)))
        Screen().tracer(0)
        while self.distance((x, y)) > 10:
            Screen().update()
            time.sleep(0.1)
            # print('text is moving')
            self.clear()
            self.write(f'{text}', move=False, font=('Arial', 10, 'normal'))

            # text.setheading(toward)
            self.forward(10)

