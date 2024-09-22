from art import logo,logo2
from game_data import data
import random
print(logo)
account_a=random.choice(data)
account_b=random.choice(data)
if account_a==account_b:
    account_b=random.choice(data)
account_name=account_a["name"]
account_desc=account_a["description"]
account_follower=account_a["follower"]
account_country=account_a["country"]

against_account_name=account_b["name"]
against_account_desc=account_b["description"]
against_account_follower=account_b["follower"]
against_account_country=account_b["country"]

if account_follower>against_account_follower:
    result='a'
else:
    result='b'


should_continiue=True
while should_continiue:
    print(f"Compare_A : {account_name},{account_desc} from {account_country}")
    print(logo2)
    print(f"against_b: {against_account_name},{against_account_desc} from {against_account_country}")
    user_input=input("who have more followers. Type 'a' and 'b': ")
    count=1
    if user_input==result and user_input=='a':
        count+=1
        account_name=account_a["name"]
        account_desc=account_a["description"]
        account_follower=account_a["follower"]
        account_country=account_a["country"]
        should_continiue==True
    elif user_input==result and user_input=='b':
        against_account_name=account_b["name"]
        against_account_desc=account_b["description"]
        against_account_follower=account_b["follower"]
        against_account_country=account_b["country"]
        should_continiue==True
    else:
        print("invalid input")




