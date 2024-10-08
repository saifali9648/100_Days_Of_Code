import turtle
from random import randint
from turtle import Turtle,Screen
import random

turtle.colormode(255)
def random_clor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color_tuple=(r,g,b)
    return random_color_tuple

def draw_spirograph(size):
    for i in range(int(360/size)):
        turtle.color(random_clor())
        turtle.circle(90,360)
        turtle.speed(20)
        current_headding = turtle.heading()
        turtle.setheading(current_headding+size)



draw_spirograph(5)


screen=Screen()
screen.exitonclick()