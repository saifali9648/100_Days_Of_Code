from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()

tim.setheading(125)
tim.forward(300)
tim.setheading(0)
tim.hideturtle()

def left_to_right():
    for i in range(3):
        for c in ("blue","red","green"):
            # tim.color(c)
            tim.dot(15,c)
            tim.penup()
            tim.forward(30)
            tim.pendown()
            tim.dot(15)
def band_in_right_side():
    tim.right(90)
    tim.penup()
    tim.forward(30)
    tim.pendown()
    tim.right(90)

def band_in_left_side():
    tim.left(90)
    tim.penup()
    tim.forward(30)
    tim.pendown()
    tim.left(90)

def right_to_left():
    for j in range(3):
        for c in ("red","green","blue"):
            # tim.color(c)
            tim.dot(15,c)
            tim.penup()
            tim.forward(30)
            tim.pendown()
            tim.dot(15)

for i in range(5):
    left_to_right()
    band_in_right_side()
    right_to_left()
    band_in_left_side()
screen.exitonclick()

