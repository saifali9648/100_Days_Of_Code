print("Welcome to the python pizza delevry:")
size=input("what size of pizza do you want? S, M or L: ")
bill=0
pepperoni=input("do you want pepperoni on your pizza? y or n ")
extra_cheese=input("do you want extra cheese on your pizza? y or n ")

if size=="S":
    bill+=15
elif size=="M":
    bill+=20
elif size=="L":
    bill+=25
else:
    print("you entered worng size")

if pepperoni=="y":
    if size=="S":
        bill+=2
    else:
        bill+=3
if extra_cheese=="y":
    bill+=1
print(f"your final bill is ${bill}")


