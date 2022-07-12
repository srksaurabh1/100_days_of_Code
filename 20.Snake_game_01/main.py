from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('Black')
screen.title('My Snake Game')
screen.tracer(0)


# snake1 = Turtle(shape='square')
# snake1.color('white')
# snake2 = Turtle(shape='square')
# snake2.color('white')
# snake3 = Turtle(shape='square')
# snake3.color('white')
#
# snake2.setposition(x=-20,y=0)
# snake3.setposition(x=-40,y=0)


starting_pos = [(0,0), (-20,0), (-40,0)]

segments = []

for position in starting_pos:
    new_seqment = Turtle(shape='square')
    new_seqment.color('white')
    new_seqment.penup()
    new_seqment.goto(position)
    segments.append(new_seqment)

screen.update()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) -1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x,new_y)

    segments[0].forward(20)
    segments[0].left(90)













screen.exitonclick()