MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

user_input = input("What would you like? (espresso/latte/cappuccino)")
print("Please insert coins")
quarters = int(input("How many quarters?: ")) * 0.250
dimes = int(input("How many dimes?: ")) * 0.10
nickels = int(input("How many nickels?: ")) * 0.05
pennies = int(input("How many pennies?: ")) * 0.01
total = format(quarters + dimes + nickels + pennies, ".2f")

print(total
      )

