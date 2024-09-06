import random

letter=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
number=["0","1","2","3","4","5","6","7","8","9"]
symbol=["!","@","#","$","%","&","*",]

ur_letter=int(input("how many letter you want in your password: "))
ur_number=int(input("how many number you want in your password: "))
ur_symbol=int(input("how many symbol you want in your password: "))

#eassy level
# password=""

# for i in range(1,ur_letter+1):
#     random_char=random.choice(letter)
#     password+=random_char
# for j in range(1,ur_letter+1):
#     random_number=random.choice(number)
#     password+=random_number
# for k in range(1,ur_symbol+1):
#     random_symbol=random.choice(symbol)
#     password+=random_symbol
# print(password)

#hard level

password_list=[]
for i in range(1,ur_letter+1):
    random_char=random.choice(letter)
    password_list+=random_char
for j in range(1,ur_number+1):
    random_number=random.choice(number)
    password_list+=random_number
for k in range(1,ur_symbol+1):
    random_symbol=random.choice(symbol)
    password_list+=random_symbol

print(password_list)
random.shuffle(password_list)
password=""
for i in password_list:
    password+=i
print(password)









