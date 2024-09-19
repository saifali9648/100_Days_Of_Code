try:
    age=int(input("enter your age:-"))
except ValueError:
    print("you are enterd a invalid number. please try with numerical value like 25")
    age=int(input("enter your age:-"))
if age>18:
    print(f"you can drive at age of {age}")
else:
    print(f"you can't drive at age of {age}")