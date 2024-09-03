#   if   condition:
#       do this...
#   else:
#       do this

# =====================================


print("wellcome to the rollercoster")
height=int(input("enter your height in cm?"))
if height >=120:
    print("you can ride the rollercoster")
    age=int(input("enter your age:"))
    if age>18:
        print("you have to pay 12$")
    else:
        print("you have to pay 7$")
else:
    print("sorry: you can not ride the rollercoster")