import random
word_list=["saif","rashid","moni"]
choosen_word=random.choice(word_list)
print(choosen_word)
#choosen_word_list=list(choosen_word)
#print(choosen_word_list)

guess=input("guess a letter: ").lower()
for i in choosen_word:
    print(i)
    if i==guess:
        print("right")
    else:
        print("wrong")



       # ==================================

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
        print(i)
        blank_fill_word+=i
    else:
        print("_")
        blank_fill_word+="_"
print(blank_fill_word)