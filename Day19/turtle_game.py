from  turtle import Turtle,Screen
tim1=Turtle()
tim2=Turtle()
tim3=Turtle()
tim4=Turtle()
tim5=Turtle()
tim6=Turtle()
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
tim2.goto(-235,15)
tim3.penup()
tim3.goto(-235,30)
tim4.penup()
tim4.goto(-235,-15)
tim5.penup()
tim5.goto(-235,-30)
tim6.penup()
tim6.goto(-235,-45)
Screen.exitonclick()
