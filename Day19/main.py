from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()
def move_forward():
    tim.forward(10)

def  move_backward():
    tim.backward(10)
def counter_clockwise():
    cur_head=tim.heading()
    tim.setheading(cur_head+10)
    # tim.forward(10)
def clockwise():
    cur_head=tim.heading()
    tim.setheading(cur_head-10)
    # tim.forward(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(counter_clockwise,"a")
screen.onkey(clockwise,"d")
screen.onkey(clear,"c")

screen.exitonclick()