from menu import MENU

# TODO - change is_sufficient logic so that it shows what type of ingredient is missing.
# TODO - create a functionality that it keep asking if user still want to dispense coffee.
# TODO - create an OFF function that turn off the coffee machine


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: {money}")


def deduct_resources(type_of_coffee):
    global resources
    if type_of_coffee == 'espresso':
        resources['water'] = resources['water'] - MENU[type_of_coffee]['ingredients']['water']
        resources['coffee'] = resources['coffee'] - MENU[type_of_coffee]['ingredients']['coffee']
    else:
        resources['water'] = resources['water'] - MENU[type_of_coffee]['ingredients']['water']
        resources['coffee'] = resources['coffee'] - MENU[type_of_coffee]['ingredients']['coffee']
        resources['milk'] = resources['milk'] - MENU[type_of_coffee]['ingredients']['milk']


def is_sufficient(type_of_coffee):
    water = MENU[type_of_coffee]['ingredients']['water']
    milk = MENU[type_of_coffee]['ingredients']['milk']
    coffee = MENU[type_of_coffee]['ingredients']['coffee']
    water_resources = resources['water']
    coffee_resources = resources['coffee']
    milk_resources = resources['milk']

    if coffee == 'espresso':
        if water_resources > water and coffee_resources > coffee:
            return True
        else:
            return False
    else:
        if water_resources > water and coffee_resources > coffee and milk_resources > milk:
            return True
        else:
            return False

def print_resources():
    print(resources)
def calculate_change(total, coffee):
    total_change = format(total - MENU[coffee]['cost'], ".2f")
    return total_change


def dispense_coffee(coffee):
    if is_sufficient(coffee):
        deduct_resources(coffee)
        print(f"Here is {calculate_change(total, coffee)} in change.")
        print(f"Here is your {coffee}☕. Enjoy!")


user_input = input("What would you like? (espresso/latte/cappuccino)")
print("Please insert coins")
quarters = int(input("How many quarters?: ")) * 0.250
dimes = int(input("How many dimes?: ")) * 0.10
nickels = int(input("How many nickels?: ")) * 0.05
pennies = int(input("How many pennies?: ")) * 0.01
total = float(format(quarters + dimes + nickels + pennies, ".2f"))
dispense_coffee(user_input)
print_resources()