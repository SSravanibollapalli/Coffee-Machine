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
ttl = 0


def calculate():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    quarters_ttl = round(quarters * 0.25, 2)
    dimes_ttl = round(dimes * 0.10, 2)
    nickles_ttl = round(nickles * 0.05, 2)
    pennies_ttl = round(pennies * 0.01, 2)
    global ttl
    ttl = quarters_ttl + dimes_ttl + nickles_ttl + pennies_ttl


def rsrc_list(pick_p):
    resources["water"] -= MENU[pick_p]["ingredients"]["water"]
    resources["milk"] -= MENU[pick_p]["ingredients"]["milk"]
    resources["coffee"] -= MENU[pick_p]["ingredients"]["coffee"]
    global ttl
    ttl -= round(MENU[pick_p]["cost"], 2)


pick_flag = True
while pick_flag:
    pick = input("What would you like? (espresso/latte/cappuccino): ")
    if pick == 'off':
        pick_flag = False
        break
    elif pick == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${round(ttl,2)} ")
    elif pick == 'espresso':
        calculate()
        if ttl >= 1.50:
            if resources['water'] >= 50:
                if resources['coffee'] >= 18:
                    change = round(ttl - 1.50, 2)
                    print(f"Here is ${round(change,2)} in change.")
                    print("Here is your espresso ☕️. Enjoy!")
                    resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                    resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                    ttl -= round(MENU["espresso"]["cost"], 2)
                    pick_flag = True
                else:
                    print("Sorry that's not enough coffee.")
                    pick_flag = True
            else:
                print("Sorry that's not enough water.")
                pick_flag = True
        else:
            print("Sorry that's not enough money. Money refunded.")
            pick_flag = True
    elif pick == 'latte':
        calculate()
        if ttl >= 2.5:
            if resources['water'] >= 200:
                if resources['milk'] >= 150:
                    if resources['coffee'] >= 24:
                        change = ttl - 2.5
                        print(f"Here is ${round(change,2)} in change.")
                        print("Here is your latte ☕️. Enjoy!")
                        rsrc_list("cappuccino")
                        pick_flag = True
                    else:
                        print("Sorry that's not enough coffee.")
                        pick_flag = True
                else:
                    print("Sorry that's not enough milk.")
                    pick_flag = True
            else:
                print("Sorry that's not enough water.")
                pick_flag = True
        else:
            print("Sorry that's not enough money. Money refunded.")
            pick_flag = True
    elif pick == 'latte':
        calculate()
        if ttl >= 3:
            if resources['water'] >= 250:
                if resources['milk'] >= 100:
                    if resources['coffee'] >= 24:
                        change = ttl - 3
                        print(f"Here is ${round(change,2)} in change.")
                        print("Here is your cappuccino ☕️. Enjoy!")
                        rsrc_list("latte")
                        pick_flag = True
                    else:
                        print("Sorry that's not enough coffee.")
                        pick_flag = True
                else:
                    print("Sorry that's not enough milk.")
                    pick_flag = True
            else:
                print("Sorry that's not enough water.")
                pick_flag = True
        else:
            print("Sorry that's not enough money. Money refunded.")
            pick_flag = True
