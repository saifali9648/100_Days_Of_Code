import art
def add(n1,n2):
    return n1+n2
def substract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2

operation={
    "+": add,
    "-": substract,
    "*": multiply,
    "/": division
}




# def calculator(number1,number2,operator):
#     result=0
#     if operator=="+":
#         return number1 + number2
#     elif operator=="-":
#         return number1-number2
#     elif operator=="*":
#         return number1*number2
#     elif operator=="/":
#         return number1/number2
#     else:
#         print("select valid opearator and try again:")
print(art.calculator_logo)
number1=float(input("enter a number that you want to calculate:-\n"))

# for symbol in operation:
#     print(symbol)
print("+\n-\n*\n/")
operator=input("choose a operation that you want:-\n")
number2=float(input("enter your second number that you want to calclulate:-"))

result=(operation[operator](number1,number2))
should_continiou=True
while should_continiou:
    re_calculation=input("Do you want to continiue with perivious calculation Type 'y' for  yes or 'n' for no:-")
    if re_calculation=="y":
        print("+\n-\n*\n/")
        operator=input("choose a operation that you want:-\n")
        number2=float(input("enter your second number that you want to calclulate:-"))
        result=(operation[operator](result,number2))
    elif re_calculation=="n":
        # should_continiou=False
        print(f"{result}")
        result=0
        number1=float(input("enter a number that you want to calculate:-\n"))
        print("+\n-\n*\n/")
        operator=input("choose a operation that you want:-\n")
        number2=float(input("enter your second number that you want to calclulate:-"))

        result=(operation[operator](number1,number2))
    else:
        should_continiou=False
        print(f"{result}")
        print("Thank you")

    


