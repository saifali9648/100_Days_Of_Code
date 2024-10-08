import random
import turtle
from turtle import Turtle,Screen
from random import Random
import colorgram
rgb_list=[]
colors=colorgram.extract('herist.jpg',20)
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    rgb_tuple=(r,g,b)
    rgb_list.append(rgb_tuple)


turtle.colormode(255)
tim=Turtle()
rand=Random()
screen=Screen()
directions=[0,90,180,270]

def random_moves(dir,clr):
    tim.pensize(10)
    tim.speed("fastest")
    tim.color(clr)
    tim.forward(30)
    tim.setheading(dir)

for i in range(200):
    random_clor=random.choice(rgb_list)
    random_direction=rand.choice(directions)
    random_moves(random_direction,random_clor)