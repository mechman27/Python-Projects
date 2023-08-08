from menu import Menu, MenuItem
from Coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

money_machine.report()
coffee_maker.report()

is_on = True

while is_on:
    menu = Menu()
    options = menu.get_items()
    choice = input(f"What would you like to? ({options}):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost()):
                coffee_maker.make_coffee(drink)

