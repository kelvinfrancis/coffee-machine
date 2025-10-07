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

def check_resources(choice):
    ingredients = choice["ingredients"]
    for key, value in ingredients.items():
        if resources[key] < value:
            print(f"Sorry there is not enough {key}!")
        else:
            return True
    return None

def process_coins():
    """Return the total amount of coins."""
    print("Please insert coins.")
    total = int(input("How much quarters? ")) * 0.25
    total += int(input("How much dimes? ")) * 0.10
    total += int(input("How much nickels? ")) * 0.05
    total += int(input("How much pennies? ")) * 0.01
    return total

def is_transaction_successful(money_receive, drink_cost):
    """Check if a transaction is successful."""
    if money_receive >= drink_cost:
        change = round(money_receive - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(coffee_name, ingredients):
    """Make a coffee."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {coffee_name} ☕️, enjoy!")

profit = 0
is_on = True

while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {profit}")
    else:
        if user_choice not in MENU:
            print("Please enter a valid choice.")
        else:
            drink = MENU[user_choice]
            if check_resources(drink):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(user_choice, drink["ingredients"])

    #TODO: 4. Check resources sufficient?
    #TODO: 5. Process coins.
    #TODO: 6. Check transaction successful?
    #TODO: 7. Make Coffee.
