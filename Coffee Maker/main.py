from coffee_maker import CoffeeMaker
from menu import MenuItem, Menu
from money_machine import MoneyMachine


maker = CoffeeMaker()
menu_list = Menu()
money = MoneyMachine()

def main():
    make_coffee = True
    while make_coffee:
        order = input(f"What would you like? {menu_list.get_items()}: ").lower()
        if order == "report":
            maker.report()
            money.report()
        elif order in menu_list.get_items():
            drink = menu_list.find_drink(order)
            if maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
                maker.make_coffee(drink)
        else:
            make_coffee = False


if __name__ == "__main__":
    main()
