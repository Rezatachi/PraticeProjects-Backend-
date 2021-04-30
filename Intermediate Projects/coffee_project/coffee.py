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

ordering = True
# Commands admins can use


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")


def is_enough(order_ingredients):
    # Maps over JSON and checks if there is more resources in the drink than there are in the actual resources
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"sorry there isn't enough {item}.")
            return False
    return True


profit = 0


def profit_finder():
    print(profit)


def make_da_coffee(drink_name, ordering_ingrdients):
    # Deduct the required ingredients from the resources.
    for item in ordering_ingrdients:
        resources[item] -= ordering_ingrdients[item]
    print("Mmm Here's your coffee :D ☕☕")


def transac_system():
    print("Please insert coins")
    total = int(input("how many quarters?:")) * 25
    total += int(input("how many nickels?:")) * 5
    total += int(input("how many dimes?:")) * 10
    total += int(input("how many pennies?:")) * 1
    return total


def is_process(money_recieved, drink_cost):
    # Return True when the payment is accepted, or False if money is insufficient.
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Your change is {change}")
        global profit
        return True
    else:
        print("Sorry you need more money to pay")
        return False

# TODO 1. ask what they want


while ordering == True:
    coffee_q = input(
        "What would you like? : (espresso/latte/cappucino). If you're an admin, please type report to check the status of your machine\n")
    if coffee_q == "report":
        report()
    elif coffee_q == "off":
        ordering = False
    else:
        drink = MENU[coffee_q]
        if is_enough(drink['ingredients']):
            ordering = False
            payment = transac_system()
            if is_process(payment, drink["cost"]):
                make_da_coffee(coffee_q, drink['ingredients'])
                print("Next customer!")
                ordering = True
