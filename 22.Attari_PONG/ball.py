from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.goto((0, 0))
        self.color('white')

    def move(self):
        self.penup()
        self.goto((360, 260))