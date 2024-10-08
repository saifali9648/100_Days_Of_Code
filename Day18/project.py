from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()

def left_to_right():
    for i in range(3):
        for c in ("blue","red","green"):
            tim.color(c)
            tim.dot(15)
            tim.penup()
            tim.forward(30)
            tim.pendown()
            tim.color("green")
def band_in_right_side():
    tim.right(90)
    tim.penup()
    tim.forward(15)
    tim.pendown()
    tim.right(90)

def band_in_left_side():
    tim.left(90)
    tim.penup()
    tim.forward(15)
    tim.pendown()
    tim.left(90)

def right_to_left():
    for j in range(3):
        for c in ("red","green","blue"):
            tim.penup()
            tim.forward(270)
            tim.pendown()
            # tim.color(c)
            # tim.dot(15)
            # tim.penup()
            # tim.forward(30)
            # tim.pendown


for i in range(5):
    left_to_right()
    band_in_right_side()
    right_to_left()
    band_in_left_side()

screen.exitonclick()

