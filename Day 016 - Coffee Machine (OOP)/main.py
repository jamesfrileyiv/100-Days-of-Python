from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def transaction(choice, coffee_maker, menu, money_machine):
    order = menu.find_drink(choice)
    if coffee_maker.is_resource_sufficient(order):
        if money_machine.make_payment(order.cost):
            coffee_maker.make_coffee(order)


machine = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while machine.get_power_state():
    choice = input(f'What would you like? ({menu.get_items()[:-1] + ")"}\n> ').lower()
    if choice in menu.get_items():
        transaction(choice, machine, menu, money_machine)
    elif choice == "report":
        machine.report()
        money_machine.report()
    elif choice == "off":
        machine.power_off()
    else:
        print("Please enter a valid input.")