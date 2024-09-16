import random
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card


def calculate_score(cards2):
    if sum(cards2)==21 and len(cards2)==2:
        return 0
    if 11 in cards2 and sum(cards2)>21:
        cards2.remove(11)
        cards2.append(1)
    return sum(cards2)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score==0:
        return "lose, opponent has blackjack"
    elif user_score==0:
        return "win with blackjack"
    elif user_score>21:
        return "you went over: you lose"
    elif computer_score>21:
        return " opponent went over : you win"
    elif user_score>computer_score:
        return "you win"
    else:
        return "you lose"

def play_game():
    user_cards=[]
    computer_cards=[]
    computer_socre=-1
    user_score=-1
    is_game_over=False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_socre=calculate_score(computer_cards)
        print(f"your hand {user_cards} and current socre{user_score}")
        print(f"computer hand {computer_cards[0]}")

        if user_score ==0 or computer_socre==0 and user_score>21:
            is_game_over=True
        else:
            user_should_deal=input("type 'y' for take another card or type 'n' for pass:")
            if user_should_deal=="y":
                user_cards.append(deal_card())
            else:
                is_game_over=True

    while computer_socre !=0 and computer_socre < 17:
        computer_cards.append(deal_card())
        computer_socre = calculate_score(computer_cards)

    print(f"your final hand: {user_cards}, final score: {user_score}")
    print(f"computer's final hand: {computer_cards}, final score: {computer_socre}")
    print(compare(user_score=user_score,computer_score=computer_socre))
while input("Do you want to play game type 'y' for yes or 'n' for No:- ")=="y":
    print("\n"*20)
    play_game()