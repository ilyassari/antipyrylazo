from turtle import Turtle, colormode, Screen
from random import choice

from get_colors import get_color_list

colors = get_color_list("image.jpg")
# colors = [(199, 13, 32), (250, 237, 17), (39, 76, 189), (39, 217, 69), (237, 226, 5), (229, 159, 46), (27, 39, 156), (215, 75, 13), (198, 14, 11), (15, 154, 15), (243, 34, 166), (229, 17, 122), (70, 10, 31)]
colormode(255)

leo = Turtle()
leo.penup()
leo.hideturtle()

gap = 50
leo.setheading(225)
leo.forward(6.5 * gap)
leo.setheading(0)

for _ in range(10):
    for _ in range(10):
        leo.dot(20, choice(colors))
        leo.forward(gap)
    leo.setheading(90)
    leo.forward(gap)
    leo.setheading(180)
    leo.forward(10 * gap)
    leo.setheading(0)


screen = Screen()
screen.exitonclick()