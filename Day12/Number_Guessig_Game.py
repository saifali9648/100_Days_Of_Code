import random
import art
print(art.logo)
random_number=random.randint(1,100)

def number_guessing(level):
    if level=="easy":
        attempt=10
        for i in range(attempt):
            print(f"you have {attempt} attempt remaining to guess the number.")
            user_guessed_number=int(input("Make a guess: "))
            if user_guessed_number==random_number:
                print(f"you got it. The answer is {random_number}")
                break
            elif user_guessed_number>random_number:
                print("To high")
                print("guess again")
            else:
                print("To low")
                print("guess again")
            attempt-=1
    elif level=="hard":
        attempt=5
        for i in range(attempt):
            print(f"you have {attempt} attempt remaining to guess the number.")
            user_guessed_number=int(input("Make a guess: "))
            if user_guessed_number==random_number:
                print(f"you got it. The answer is {random_number}")
                break
            elif user_guessed_number>random_number:
                print("To high")
                print("guess again")
            else:
                print("To low")
                print("guess again")
            attempt-=1
print("Welcome to the Number Guessing Game !")
print("I'm thinking of a Number between 1 to 100.")
choose_difficulty_level=input("Choose a difficulty. The 'easy' or 'hard':")
number_guessing(choose_difficulty_level)