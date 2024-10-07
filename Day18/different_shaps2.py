import random
from turtle import Turtle,Screen
from random import Random
tim=Turtle()
rand=Random()
screen=Screen()
clr=["red","green","blue","black","gray"]

def draw_shape(number_of_side,rand_color):
    angle=360/number_of_side
    for i in range(number_of_side):
        tim.color(rand_color)
        tim.forward(30)
        tim.right(angle)
for number in range(3,10):
    random_color=random.choice(clr)
    draw_shape(number,random_color)
screen.exitonclick()