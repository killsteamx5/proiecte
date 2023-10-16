from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

latte = MenuItem("latte", 200, 150, 24, 2.5)
aparat = CoffeeMaker()
meniu = Menu()
bani = MoneyMachine()
aparat.report()
comanda = meniu.find_drink(input("ce doresti? "))
if aparat.is_resource_sufficient(comanda):
    bani.process_coins()
if bani.make_payment(latte.cost):
    aparat.make_coffee(latte)
