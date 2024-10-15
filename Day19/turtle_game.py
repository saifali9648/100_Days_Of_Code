from  turtle import Turtle,Screen
import random
tim1=Turtle(shape="turtle")
tim2=Turtle(shape="turtle")
tim3=Turtle(shape="turtle")
tim4=Turtle(shape="turtle")
tim5=Turtle(shape="turtle")
tim6=Turtle(shape="turtle")
Screen=Screen()
Screen.setup(width=500,height=400)
user_input=Screen.textinput("make your bet","which turtle will win the race? Choose a color:")
tim1.color("red")
tim2.color("green")
tim3.color("blue")
tim4.color("yellow")
tim5.color("pink")
tim6.color("brown")
tim1.penup()
tim1.goto(-235,0)
tim2.penup()
tim2.goto(-235,30)
tim3.penup()
tim3.goto(-235,55)
tim4.penup()
tim4.goto(-235,-30)
tim5.penup()
tim5.goto(-235,-55)
tim6.penup()
tim6.goto(-235,-75)
tim_list=[tim1,tim2,tim3,tim4,tim5,tim6]


for i in range(500):
    # random_step=random.randint(1,5)
    random_tim=random.choice(tim_list)
    random_tim.forward(5)
    # print(random_step)
    

Screen.exitonclick()
