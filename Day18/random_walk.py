from turtle import Turtle,Screen
from random import Random
tim=Turtle()
rand=Random()
screen=Screen()
clor=["red","green","blue","black","gray","crimson","medium violet red","yellow"]
directions=[0,90,180,270]

def random_moves(dir,clr):
    tim.pensize(10)
    tim.speed("fastest")
    tim.color(clr)
    tim.forward(30)
    tim.setheading(dir)

for i in range(200):
    random_clor=rand.choice(clor)
    random_direction=rand.choice(directions)
    random_moves(random_direction,random_clor)