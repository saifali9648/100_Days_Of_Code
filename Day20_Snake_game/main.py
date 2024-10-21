# from turtle import Turtle,Screen
# screen=Screen()
# screen.setup(width=600,height=600)
# screen.bgcolor("black")
# screen.title("My Snake Game!")
# x=0
# y=0
# for i in range(0,2):
#     snake=Turtle(shape="square")
#     snake.color("red")
#     snake.goto(x=x,y=y)
#     snake.penup()
#     x-=20
# screen.exitonclick()\


def factorial(n):
    # Base case
    if n == 0:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)


print(factorial(5))