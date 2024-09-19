import random
fruit=["apple","banana","orange","guava","papaya","seb"]    #index value start from 0
fruit_number=random.randint(1,6)                            #it will generate number between 1 to 6 including start and end value
print(fruit[fruit_number])


#correct code is:-


import random
fruit=["apple","banana","orange","guava","papaya","seb"]    #index value start from 0
fruit_number=random.randint(0,5)                            #it will generate number between 0 to 5 including start and end value cover 0 index and 5th index that is number 6 item in the list
print(fruit[fruit_number])