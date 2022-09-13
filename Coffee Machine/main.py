from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

mmenu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
items = mmenu.get_items()

is_on = True

while is_on:

    order = input(f"Hello! What would you like to have?: {items} _____")

    att = mmenu.find_drink(order)

    if coffee_maker.is_resource_sufficient(att) is True:

        if money_machine.make_payment(att.cost) is True:
            coffee_maker.make_coffee(att)

        coffee_maker.report()
        money_machine.report()

        q = input("Do you want to a coffee?: Type 'y' for yes 'n' for no: ")

        if q == "n":
            is_on = False

        else:
            is_on = True

    else:
        print("Insufficient Resources!!\n")
        q = input("Do you want to a coffee?: Type 'y' for yes 'n' for no")

        if q == "n":
            is_on = False

        else:
            is_on = True
