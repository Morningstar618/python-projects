def transaction(drink):
    for key in MENU[drink]['ingredients']:
        if resources[key] >= MENU[drink]['ingredients'][key]:
            continue
        else:
            print(f"Sorry there is not enough {key}")
            return
        
    cost = MENU[drink]['cost']

    print(f"The cost of the coffee is ${cost}")
    print("Please insert coins.")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    global money

    if total >= cost:
        change = total - cost
        money += cost
    else:
        print("Sorry that's not enough money. Money refunded.")
        return
    
    if change != 0.0:
       print(f"Here is ${change:.2f} in change.")
    print(f"Here is your {drink}. Enjoy!")
    
    for key in MENU[drink]['ingredients']:
        resources[key] = resources[key] - MENU[drink]['ingredients'][key]


def coffeMachine():
    while True:
        user_input = input("What would you like? (espresso/latte/cappuccino): ")
        while user_input not in MENU:
            user_input = input("Please enter from one of the following (espresso/latte/cappuccino): ")

        if user_input == 'report':
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money}")
        elif user_input == 'off':
            print("Turning off coffee machine")
            exit()
        else:
            transaction(user_input)


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

money = 0


###################################################################################################################
coffeMachine()


