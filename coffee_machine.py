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

# how much money are we making
money = 0


def remaining_resources():
    global money
    print(f"Remaining Resources:\nWater:\t{resources['water']}ml\nMilk:\t{resources['milk']}ml\n"
          f"Coffee:\t{resources['coffee']}g\nMoney:\t${money}")


def check_resources(coffee):
    a = MENU[str(coffee_type)]['ingredients']
    if selection == "espresso":
        a['milk'] = 0
    if resources['water'] < a['water']:
        print("Sorry there is not enough water.")
        return False
    elif resources['milk'] < a['milk']:
        print("Sorry there is not enough milk.")
        return False
    elif resources['coffee'] < a['coffee']:
            print("Sorry there is not enough coffee.")
            return False
    else:
        customer_payment()


def customer_payment():
    """Fucntion that calculates the payment and returns any over payment"""
    global money
    quarters = int(input("How many quarters have you inserted: ")) * 0.25
    dimes = int(input("How many dimes have you inserted: ")) * 0.10
    nickels = int(input("How many nickels have you inserted: ")) * 0.05
    pennies = int(input("How many pennies have you inserted: ")) * 0.01
    payment = quarters + dimes + nickels + pennies
    print(f"Total payment received: ${round(payment,2)}")

    coffee_cost = MENU[str(coffee_type)]['cost']
    if payment < coffee_cost:
        print("Sorry that's not enough money. Money refunded.")
    elif payment > coffee_cost:
        overpaid = payment - coffee_cost
        print(f"Here is ${round(overpaid,2)} dollars in change.")
        money += coffee_cost
        subtract_resources()
        print(f"“Here is your {coffee_type}. Enjoy!”")
    else:
        money += coffee_cost
        subtract_resources()
        print(f"“Here is your {coffee_type}. Enjoy!”")


def subtract_resources():
    "This function removes resources from the coffee machine"
    a = MENU[str(coffee_type)]['ingredients']
    resources["water"] -= a["water"]
    resources["milk"] -= a["milk"]
    resources["coffee"] -= a["coffee"]


while True:
    """ This is continue indefinitely, user most turn 'off'"""
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()

#TODO Turn off the Coffee Machine by entering “ off ” to the prompt

    if selection == "report":
        remaining_resources()
    elif selection == "off":
        print("Turning off...")
        break
    else:
        if selection in ("espresso", "latte", "cappuccino"):
            coffee_type = selection
        check_resources(coffee_type)
        # if check_resources(coffee_type):
