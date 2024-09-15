from art import logo, espresso, latte, cappuccino

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

money = 0  # created a variable that will store the money


def get_report():
    print("Water:\t", resources["water"], "mL")
    print("Milk:\t", resources["milk"], "mL")
    print("Coffee:\t", resources["coffee"], "mL")
    print("Money:\t $", money)


def ask_money():
    print('Please insert coins.')
    quarters = int(input("How many quarters?:\t"))
    dimes = int(input("How many dimes?:\t"))
    nickels = int(input("How many nickels?:\t"))
    pennies = int(input("How many pennies?:\t"))
    total_money = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
    return total_money


def check_amount(paid_amount, cost_of_beverage, beverage_type):
    if paid_amount > cost_of_beverage:
        change = paid_amount - cost_of_beverage
        return f"Here is your {beverage_type} ☕. Enjoy!", change

    elif amount_paid < cost_of_beverage:
        change = paid_amount - cost_of_beverage  # this has to be -ve
        return "Sorry that's not enough money. Money refunded.", change
        # figure a way to refund the money

    else:
        # amount_paid == cost_of_beverage
        change = paid_amount - cost_of_beverage
        return f"Here is your {beverage_type} ☕. Enjoy!", change


def check_ingredients(beverage):
    enough = True
    ingredients = ["water", "milk", "coffee"]
    for item in ingredients:
        if resources[item] < MENU[beverage]['ingredients'][item]:
            print(f"Sorry, not enough {item} :( ")
            enough = False
            return enough


def display_menu():
    print("1. espresso --> $ 1.5")
    print("2. latte --> $ 2.5")
    print("3. cappuccino --> $ 3.0")


def deduct_ingredients(beverage_type):
    resources["water"] -= MENU[beverage_type]["ingredients"]["water"]
    resources["milk"] -= MENU[beverage_type]["ingredients"]["milk"]
    resources["coffee"] -= MENU[beverage_type]["ingredients"]["coffee"]


# quarters = $0.25
# dimes = $0.10
# nickels =$0.05
# pennies = $0.01

print(logo)
machine_on = True
while machine_on:

    user_input = int(
        input("What would you like? (1 --> espresso/2 --> latte/3 --> cappuccino):\n4 - menu\nEnter choice :__"))
    match user_input:
        case 1:
            espresso_cost = MENU["espresso"]["cost"]
            print("Cost of beverage : $", espresso_cost)
            status = check_ingredients("espresso")
            if status is False:
                continue

            amount_paid = ask_money()
            message, change_left = check_amount(amount_paid, espresso_cost, "espresso")
            if change_left < 0:  # money should be added after the payment has processed
                print(message)
            else:  # (payment done)
                money += espresso_cost
                deduct_ingredients("espresso")
                print("Here is $", "%.2f" % change_left, "in change ")
                print(message)
                print(espresso)
            continue

        case 2:
            latte_cost = MENU["latte"]["cost"]
            print(" Cost of beverage : $", latte_cost)
            status = check_ingredients("latte")
            if status is False:
                continue

            amount_paid = ask_money()
            message, change_left = check_amount(amount_paid, latte_cost, "latte")
            if change_left < 0:  # money should be added after the payment has processed
                print(message)
            else:  # (payment done)
                money += latte_cost
                deduct_ingredients("latte")
                print("Here is $", "%.2f" % change_left, "in change ")
                print(message)
                print(latte)
            continue

        case 3:
            cappuccino_cost = MENU["cappuccino"]["cost"]
            print(" Cost of beverage : $", cappuccino_cost)
            status = check_ingredients("cappuccino")
            if status is False:
                continue
            amount_paid = ask_money()

            message, change_left = check_amount(amount_paid, cappuccino_cost, "cappuccino")
            if change_left < 0:  # money should be added after the payment has processed
                print(message)
            else:  # (payment done)
                money += cappuccino_cost
                deduct_ingredients("cappuccino")
                print("Here is $", "%.2f" % change_left, "in change ")
                print(message)
                print(cappuccino)
            continue

        case 4:
            print("\nHere's the menu:")
            display_menu()
            print("\n")

        case "report":
            get_report()
            continue
        case "off":
            machine_on = False
