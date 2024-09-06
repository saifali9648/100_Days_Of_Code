def turn_right():
    turn_left()
    turn_left()
    turn_left()
def repeat_step():    # turn_left() and move() in predefine function in reebog world
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
for i in range(6):
    repeat_step()

# Website_link =  https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
