import art
print(art.logo)

final_aucation_list={}
def secret_aucation(key,value):
    final_aucation_list[key]=value


def higher_bid(bidder_list):
    winner=""
    highest_bid=0
    for bidder in bidder_list:
        bid_amount=bidder_list[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"winner is {winner} with a bid of {highest_bid}") 


should_continue=True
while should_continue:
    name=input("What is your name: ")
    amount=int(input("What's your big amount: "))
    secret_aucation(key=name,value=amount)
    flag=input("Are any other bidders? Type 'yes' or 'no' ")
    if flag=="no":
        should_continue=False
        higher_bid(final_aucation_list)
    elif flag=="yes":
        print("\n"*100)
        
