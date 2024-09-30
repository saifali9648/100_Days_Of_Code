MENU={
    "esperesso":{
        "ingredients":{
            "water":50,
            "coffee":18,
            "milk":0
        },
        "cost":125
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":210
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24
        },
        "cost":250
    }
}

resource={
    "water":300,
    "milk":200,
    "coffee":100
}

profit=0

def resource_formate(report):
    resource_water=report["water"]
    resource_milk=report["milk"]
    resource_coffee=report["coffee"]
    return f"🚰 water: {resource_water}ml\n🍼milk: {resource_milk}ml\n☕coffee: {resource_coffee}g\n{profit}$"

def process_coin():
    print("please insert coin")
    total=int(input("How many 1 rupee coin 💰 :"))*1
    total+=int(input("How many 2 rupee coin 💰 :"))*2
    total+=int(input("How many 5 rupee coin 💰 :"))*5
    total+=int(input("How many 10 rupee coin 💰 :"))*10
    total+=int(input("How many 20 rupee coin 💰 :"))*20
    return total

def is_payment_successfull(money_recieved,drink_cost):
    if money_recieved>=drink_cost:
        global profit
        change=round(money_recieved-drink_cost,2)
        print(f"Here is your change {change}")
        profit+=drink_cost
        return True
    else:
        print("Sorry that's not enough money! Money refunded!")
        return False
    
def make_coffe(user_order,left_resource):
    for item in left_resource:
        resource[item]=(left_resource[item]-user_order[item])
    return resource



def is_resource_sufficent(order_ingredients):
    is_enough=True
    for item in order_ingredients:
        if order_ingredients[item]>=resource[item]:
            print(f"insufficent {item}")
            is_enough=False
    return is_enough

# def check_resource(type,resource):
#     if type=="espresso":
#         if resource["water"]>=50 and resource["coffee"]>=18:
#             print("sufficient resource for espresso")
#         else:
#             print("sorry insuffincient resource")
#     elif type=="latte":
#         if resource["water"]>=200 and resource["milk"]>=150 and resource["coffee"]>=24:
#             print("resource is sufficent for latte")
#         else:
#             print("sorry insufficent resource")
#     elif type=="cappuccino":
#         if resource["water"]>=250 and resource["milk"]>=100 and resource["coffee"]>=24:
#             print("resource is sufficent for capppuccino")
#         else:
#             print("sorry insufficent resource")

order_agian=True
while order_agian:
    user=input("What would you like? (esperesso/ latte/ cappuccino):").lower()
    if user=="report":
        print(resource_formate(report=resource))
    elif user=="off":
        order_agian=False
    else:
        #check_resource(type=user,resource=resource)
        drink=MENU[user]
        if is_resource_sufficent(drink["ingredients"]):
            payment=process_coin()
            if is_payment_successfull(payment,drink["cost"]):
                reamin_resource=make_coffe(drink["ingredients"],resource)
                print(f"Available 🚰 water:{reamin_resource["water"]}ml")
                print(f"Available 🍼 milk:{reamin_resource["milk"]}ml")
                print(f"Available ☕ coffee:{reamin_resource["coffee"]}g")
                print(f"profit:{profit}Rs")
                print(f"Here is ☕ {user}! and enjoy 😊 your ☕ {user} Have a Good day! 😎")
            else:
                print(f"Available 🚰 water:{reamin_resource["water"]}ml")
                print(f"Available 🍼 milk:{reamin_resource["milk"]}ml")
                print(f"Available ☕ coffee:{reamin_resource["coffee"]}g")
                print(f"profit:💸{profit}Rs")
        
       
       







