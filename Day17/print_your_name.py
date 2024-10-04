#printing your name using class and constructor
class User():
    def __init__(self,user_id,user_name):
        self.id=user_id
        self.user_name=user_name
userid=input("enter your user id: ")
username=input("enter your uername: ")
user1=User(userid,username)
print(user1.id)
print(user1.user_name)