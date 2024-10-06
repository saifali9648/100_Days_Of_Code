from turtle import Turtle,Screen
from random import Random
tim=Turtle()
rand=Random()
screen=Screen()
color=["red","green","blue","black","gray"]
random_color=rand.choice(color)
def triangle():
    random_color = rand.choice(color)
    for i in range(3):
        tim.color(random_color)
        tim.forward(30)
        tim.right(120)
def square():
    random_color = rand.choice(color)
    for i in range(4):
        tim.color(random_color)
        tim.forward(30)
        tim.right(90)
def pentagun():
    random_color = rand.choice(color)
    for i in range(5):
        tim.color(random_color)
        tim.forward(30)
        tim.right(72)


triangle()
square()
pentagun()
screen.exitonclick()