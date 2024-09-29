MENU={
    "esperesso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
    "cost":2.5
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24
        }
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
    return f"water: {resource_water}ml\nmilk: {resource_milk}ml\ncoffee: {resource_coffee}g\n{profit}$"



def is_resource_sufficent(order_ingredients):
    for item in order_ingredients:
        order_ingredients[item]>=resource[item]
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
        is_resource_sufficent(drink["ingredients"])
        
       
       







