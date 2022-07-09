from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color('black')

# Different Shapes
# for i in range(3,10):
#     for _ in range(i):
#         tim.forward(50)
#         tim.right(360 / i)

# Random Walk
directions = [0, 90, 180, 270]    # E, S, W , N
colours = ['CornflowerBlue', 'DarkOrchid', 'black',
           'IndianRed', 'DeepSkyBlue', 'yellow',
           'LightSeaGreen', 'wheat', 'SeaGreen']
tim.pensize(10)
tim.speed('fastest')

for _ in range(200):
    tim.forward(30)
    tim.setheading(random.choice(directions))
    tim.color(random.choice(colours))




screen = Screen()
screen.exitonclick()

