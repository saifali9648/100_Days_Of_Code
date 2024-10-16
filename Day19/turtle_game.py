from  turtle import Turtle,Screen
import random

def move_turtle():
    tim.forward()


Screen=Screen()
Screen.setup(width=500,height=400)
user_input=Screen.textinput("make your bet","which turtle will win the race? Choose a color:")
colors=["red", "green", "blue", "yellow", "black", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
for i in range(0, 6):
    tim=Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230,y=y_positions[i])

Screen.exitonclick()
