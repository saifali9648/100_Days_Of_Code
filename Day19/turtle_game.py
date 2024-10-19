from  turtle import Turtle,Screen
import random
all_turtle=[]
is_game_on=False
Screen=Screen()
Screen.setup(width=500,height=400)
user_input=Screen.textinput("make your bet","which turtle will win the race? Choose a color:")
colors=["red", "green", "blue", "yellow", "black", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
for i in range(0, 6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[i])
    all_turtle.append(new_turtle)

if user_input:
    is_game_on=True
while is_game_on:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_game_on=False
            wining_color=turtle.pencolor()
            if wining_color==user_input:
                print(f"you've won! The {wining_color} turtle is winner of the race")
            else:
                print(f"you've lost! The {wining_color} turtle is winner of the race")
        random_step=random.randint(0,10)
        turtle.forward(random_step)

Screen.exitonclick()
