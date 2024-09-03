print("wellcome to the rollercoster")
height=int(input("enter your height in cm?"))
bill=0
if height>=120:
    print("you can ride")
    age=int(input("enter your age:"))
    if age<=5:
        print(" child ticket are 5$")
        bill=5
    elif age<=12:
        print("youth ticket are 7$")
        bill=7
    elif age<=18:
        print("youth+ ticket are 10$")
        bill=10
    else:
        print("adult ticket are 15$")
        bill=15
    want_photo=input("do you wnat photo type y for yes or n for no:- ")
    if want_photo=="y":
        bill+=3
    print(f"your final bill is ${bill}")
else:
    print("sorry you can not ride")