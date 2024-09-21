from art import logo
from game_data import data
import random
account_a=random.choice(data)
account_b=random.choice(data)
if account_a==account_b:
    account_b=random.choice(data)
print(random_account)