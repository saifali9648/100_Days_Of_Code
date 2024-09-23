from art import logo,logo2
from game_data import data
import random
print(logo)
score=0
def format_data(account):
    account_name=account["name"]
    account_desc=account["description"]
    account_follower=account["follower"]
    account_country=account["country"]
    return f"{account_name},a {account_desc} from {account_country}"

def check_answer(guess,a_followr,b_follower):
    if a_followr>b_follower:
        return guess=='a'
    else:
        return guess=='b'
should_continue=True
account_b=random.choice(data)
while should_continue:
    account_a=account_b
    account_b=random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(logo2)
    print(f"against B: {format_data(account_b)}")

    user_input=input("Who has more follower: Type 'A' OR 'B' ").lower()
    print("\n"*20)
    print(logo)

    a_follower_count=account_a["follower"]
    b_follower_count=account_b["follower"]

    is_correct=check_answer(user_input,a_followr=a_follower_count,b_follower=b_follower_count)
    if is_correct:
        score+=1
        print(f"you are right current score {score}")
    else:
        print(f"sorry you are wrong: your final score {score}")
        should_continue=False








 




