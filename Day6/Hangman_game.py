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

guess=input("guess a letter: ").lower()
blank_fill_word=""
for i in choosen_word:
    if i==guess:
        blank_fill_word+=i
    else:
        blank_fill_word+="_"
print(blank_fill_word)