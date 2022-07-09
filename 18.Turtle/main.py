import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255) # turtle default 0
tim = Turtle()

tim.shape("turtle")
# tim.color('black')


# Different Shapes
# for i in range(3,10):
#     for _ in range(i):
#         tim.forward(50)
#         tim.right(360 / i)

# Random Walk
# directions = [0, 90, 180, 270]    # E, S, W , N
# colours = ['CornflowerBlue', 'DarkOrchid', 'black',
#            'IndianRed', 'DeepSkyBlue', 'yellow',
#            'LightSeaGreen', 'wheat', 'SeaGreen']
# tim.pensize(10)
# tim.speed('fastest')
#
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color1 = (r, g, b)
    return random_color1
#
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#


# Spirograph - circle + change angle
#
# tim.speed('fastest')
#
# def draw_spirograph(size):
#     n = int(360/size)
#     for i in range(n):
#         tim.color(random_color())
#         tim.circle(100)
#
#         tim.setheading(tim.heading() + size)
#
# draw_spirograph(5)


# Random of dotted painting, spot painting
import colorbar



screen = Screen()
screen.exitonclick()

