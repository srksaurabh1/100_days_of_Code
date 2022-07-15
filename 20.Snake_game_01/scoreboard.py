from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.write(f'Score: {self.score}',
                   align='center',font=
                   ('Arial', 24, 'normal'))

    def score_update(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}',
                   align='center', font=
                   ('Arial', 24, 'normal'))

