from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu =Menu()

turn_on = True
while turn_on:
    order = input(f"What would you like? ({menu.get_items()}): ")
    if order == "report":
        coffee_maker.report()
        money_machine.report()

    elif order == "off":
        turn_off = False

    else:
        drink = menu.find_drink(order)     
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):

            coffee_maker.make_coffee(drink)
