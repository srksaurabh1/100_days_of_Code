# from turtle import Turtle,Screen
#
# tim = Turtle()
# screen = Screen()
#
#
# def move_forward():
#     tim.forward(10)
# def move_backward():
#     tim.backward(10)
# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
# def clear_draw():
#     tim.home()
#     tim.clear()
#
# screen.listen()
# screen.onkey(key= 'w', fun= move_forward)
# screen.onkey(key= 's', fun= move_backward)
# screen.onkey(key= 'a', fun= turn_left)
# screen.onkey(key= 'd', fun= turn_right)
# screen.onkey(key= 'c', fun= clear_draw)
#
# screen.exitonclick()
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make Your Bet',
                 prompt='Which turtle will win the race? Enter a color: ')

# rim = Turtle(shape='turtle')
# rim.color('red')
# rim.penup()
# rim.goto(x = - 230, y = -100)
# rim.pendown()
#
# oim = Turtle(shape='turtle')
# oim.color('orange')
# oim.penup()
# oim.goto(x = - 230, y = -60)
# oim.pendown()
#
# yim = Turtle(shape='turtle')
# yim.color('yellow')
# yim.penup()
# yim.goto(x = - 230, y = -20)
# yim.pendown()
#
# gim = Turtle(shape='turtle')
# gim.color('green')
# gim.penup()
# gim.goto(x = - 230, y = 20)
# gim.pendown()
#
# bim = Turtle(shape='turtle')
# bim.color('blue')
# bim.penup()
# bim.goto(x = - 230, y = 60)
# bim.pendown()
#
# blim = Turtle(shape='turtle')
# blim.color('black')
# blim.penup()
# blim.goto(x = - 230, y = 100)
# blim.pendown()

import random

is_race_on = False
colors = ['red', 'orange', 'yellow', 'green', 'blue',
          'purple']
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The "
                      f"{winning_color} turtle is "
                      f"the winner")
            else:
                print(f"You've Lost! The "
                      f"{winning_color} turtle is "
                      f"the winner")
            is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()