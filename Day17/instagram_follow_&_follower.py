class User():
    def __init__(self,user_id,username):
        self.id=user_id
        self.username=username
        self.follower=0
        self.following=0

    def follow(self,user):            #self ko samajhne ke liye is program ko dekhe
        user.follower+=1
        self.following+=1

    def follow_back(self,user):
        user.follower+=1
        self.following+=1

# userid=input("enter your user_id: ")
# username=input("enter your username: ")
user1=User("1","saif")
user2=User("2","ali")
user1.follow(user2)
follow_back=input("do you want to follow back type yes for y and no for n: ")
if follow_back=="y":
    user2.follow_back(user1)
    print(user1.follower)
    print(user1.following)
    print(user2.follower)
    print(user2.following)
else:
    print(user1.follower)
    print(user1.following)
    print(user2.follower)
    print(user2.following)
