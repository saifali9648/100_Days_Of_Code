import random
print("Welcome to the ROCK_PAPER_SCISSOR GAME")
user_choise=""
user=int(input("Type 0 for ROCK, 1 for PAPER or 2 for SCISSOR"))
if user==0:
    user_choise="rock"
elif user==1:
    user_choise=="paper"
else:
    user_choise=="scissor" 

computer=random.randint(0,2)
if computer==0:
    computer_choise="rock"
elif computer==1:
    computer_choise="paper"
else:
    computer_choise="scissor"

if user_choise==computer_choise:
    print(f"you chose {user_choise}\ncomputer chose {computer_choise}\n game tie")
elif user_choise=="rock" and computer_choise=="paper":
    print(f"you chose {user_choise}\ncomputer chose {computer_choise}\n you lose")
elif user_choise=="rock" and computer_choise=="scissor":
    print(f"you chose {user_choise}\ncomputer chose {computer_choise}\n you win")
elif user_choise=="paper" and computer_choise=="rock":
    print(f"you chose {user_choise}\ncomputer chose {computer_choise}\n you win")
elif user_choise=="paper" and computer_choise=="scissor":
    print(f"you chose {user_choise}\ncomputer chose {computer_choise}\n you lose")
elif user_choise=="scissor" and computer_choise=="rock":
    print(f"you chose {user_choise}\ncomputer chose {computer_choise}\n you lose")
else:
    print(f"you chose {user_choise}\ncomputer chose {computer_choise}\n you win")





