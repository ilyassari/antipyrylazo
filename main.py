from turtle import Turtle, colormode, Screen
from random import choice

from get_colors import get_color_list

GAP = 50
ROW = 10
COLUMN = 10
SIZE = 26

colors = get_color_list("image.jpg")
# colors = [(199, 13, 32), (250, 237, 17), (39, 76, 189), (39, 217, 69), (237, 226, 5), (229, 159, 46), (27, 39, 156), (215, 75, 13), (198, 14, 11), (15, 154, 15), (243, 34, 166), (229, 17, 122), (70, 10, 31)]
colormode(255)

leo = Turtle()
leo.penup()
leo.hideturtle()

leo.setheading(270)
leo.forward(((ROW - 1) * GAP) / 2)
leo.setheading(180)
leo.forward(((COLUMN - 1) * GAP) / 2)
leo.setheading(0)

for _ in range(ROW):
    for _ in range(COLUMN):
        leo.dot(SIZE, choice(colors))
        leo.forward(GAP)
    leo.setheading(90)
    leo.forward(GAP)
    leo.setheading(180)
    leo.forward(COLUMN * GAP)
    leo.setheading(0)

screen = Screen()
screen.exitonclick()