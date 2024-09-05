import random





print("Welcome To The Rock_Paper_Scissor Game,")
computer=random.randint(0,2)
# if computer==0:
#     computer_chooise="ROCK"

you=int(input("Type 0 for ROCK, 1 for PAPER or 2 for SCISSOR"))

if you==0 and computer==2:
    print("you win")

elif computer>you:
    print("you lose")

