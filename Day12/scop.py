enemies=1       #global varible and it accesble within a function or outside the function also

def incriese_enemies():
    enemies=2           # local variable an it only acceseble inside the function 
    print(f"inside the enemies {enemies}")

                                    #same rule applied on function also
incriese_enemies()
print(f"outside the enemies {enemies}")