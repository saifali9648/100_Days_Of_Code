h_amount=0
l_amount=0
def show_result(higher,lower):
    if higher>lower:
        print(higher)
        print("Result is : Lower")
    elif higher<lower:
        print(lower)
        print("Result is : Higher")


bet_again=True
while bet_again:
    print("Welcome to the Higher/Lower Guessing Game !")
    print("You can choose Higher or Lower for your bet.")
    choose_difficulty_level=input("Choose your bet. The 'Higher' or 'Lower':")
    bet_amount=int(input("Enter your bet amount: "))
    yes_no=input("do you want to more bet yes for y or no for n:")
    if choose_difficulty_level=="higher":
        h_amount+=bet_amount
    elif choose_difficulty_level=="lower":
        l_amount+=bet_amount
    if yes_no=="n":
        bet_again=False
        show_result(h_amount,l_amount)
        
