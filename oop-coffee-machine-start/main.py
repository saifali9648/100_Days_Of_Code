from coffee_maker import CoffeeMaker
from menu import Menu,MenuItem
from money_machine import MoneyMachine

coffee_maker=CoffeeMaker()
menu=Menu()
money_machine=MoneyMachine()
is_on=True

while is_on:
    chooise=input(f"what would you like {menu.get_items()}")
    if chooise=="report":
        coffee_maker.report()
        money_machine.report()
    elif chooise=="off":
        is_on=False
    else:
        drink=menu.find_drink(chooise)
        print(drink)
        if coffee_maker.is_resource_sufficient(drink):
           money_machine.make_payment(drink.cost)
           coffee_maker.make_coffee(drink)




