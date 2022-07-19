from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

paddle1 = Turtle()
paddle1.speed('fastest')
paddle1.shape('square')
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()

paddle1.goto((350, 0))
paddle1.color('white')


def go_up():
    new_y = paddle1.ycor() + 20
    paddle1.goto(paddle1.xcor(), new_y)


def go_down():
    new_y = paddle1.ycor() - 20
    paddle1.goto(paddle1.xcor(), new_y)


screen.listen()
screen.onkey(go_up, 'Up')
screen.onkey(go_down, 'Down')

game_is_on = True

while game_is_on:
    screen.update()


screen.exitonclick()
