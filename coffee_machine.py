MENU = {
    "espresso": {
        "ingredient": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredient": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredient": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 3.0,
    },
}
resource = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}
profit = 0


def is_resource_sufficient(order_ingredient):
    """Returns True when order can be made ,false if ingredient are insufficient"""
    for item in order_ingredient:
        print(order_ingredient[item], "order_ingredient[item]")
        print(resource[item], "resource[item]")
        if int(order_ingredient[item]) >= int(resource[item]):
            print(f"sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("please insert the coins: ")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    print(total, "total")
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change. ")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients"""
    for item in order_ingredients:
        resource[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


is_on = True
while is_on:
    choice = input("What would you like?(cappuccino,latte,espresso): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water:{resource['water']}ml")
        print(f"milk:{resource['milk']}ml")
        print(f"coffee:{resource['coffee']}g")
        print(f"money:{profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredient"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredient"])
