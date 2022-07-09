# import colorgram
#
# colors = colorgram.extract('download.jpg', 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# printed color list
import random
import turtle
from turtle import Screen

color_list = [(233, 222, 92), (211, 158, 105), (116, 177, 210), (226, 57, 131), (181, 78, 33), (210, 135, 174), (41, 103, 161), (12, 21, 62), (184, 46, 111), (186, 164, 23), (43, 182, 112), (122, 187, 155), (25, 32, 158), (173, 16, 67), (234, 164, 199), (229, 75, 43), (22, 179, 205), (11, 41, 23), (49, 126, 73), (146, 218, 196), (51, 21, 11), (227, 220, 10), (106, 95, 206), (133, 215, 229), (175, 177, 227), (59, 16, 31)]

from turtle import Turtle
turtle.colormode(255)
tim = Turtle()
tim.speed('fastest')
tim.penup()

tim.hideturtle()
number_of_dots = 100

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()