import random
word_list=["saif","rashid","moni","tomato"]
choosen_word=random.choice(word_list)
print(choosen_word)
# choosen_word_list=list(choosen_word)
# print(choosen_word_list)
placeholder=""
for j in choosen_word:
    placeholder+="_"
print(f"{placeholder} ")

game_over=False
correct_letter=[]
lives=6
while not game_over:
    guess=input("guess a letter: ").lower()
    blank_fill_word=""
    for i in choosen_word:
        if i==guess:
            blank_fill_word+=i
            correct_letter.append(guess)
        elif i in correct_letter:
            blank_fill_word+=i
        else:
            blank_fill_word+="_"

    if guess not in choosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("you lose")
    print(blank_fill_word)
    if "_" not in blank_fill_word:
        game_over=True
        print("you win")