from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.score_update()

    def score_update(self):
        self.write(f'Score: {self.score}',
                   align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.score_update()
