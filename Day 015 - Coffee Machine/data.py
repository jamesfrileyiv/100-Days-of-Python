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
    "money": 0
}

power_state = True


def make_coffee(coffee):
    if check_resources(coffee):
        message = f"{coffee.title()} costs ${MENU[coffee]['cost']:.2f}."
        print(message)
        process_coins(coffee, MENU[coffee]['cost'])
    else:
        print("Sorry, we are currently unable to make this.")


def check_resources(coffee):
    flag = True
    for ingredient in MENU[coffee]["ingredients"]:
        if resources[ingredient] >= MENU[coffee]["ingredients"][ingredient]:
            flag = flag and True
        else:
            flag = flag and False
    return flag


def process_coins(coffee, cost):
    print("Please insert coins.")
    quarter_amount = round(int(input("Number of Quarters: ")) * .25, 2)
    dime_amount = round(int(input("Number of Dimes: ")) * .1, 2)
    nickel_amount = round(int(input("Number of Nickels: ")) * .05, 2)
    penny_amount = round(int(input("Number of Pennies: ")) * .01, 2)
    total = quarter_amount + dime_amount + nickel_amount + penny_amount
    if total < cost:
        print("Sorry, you did not pay enough. Returning coins entered.")
    else:
        print(f"You paid ${total:.2f}. Change is ${total - cost:.2f}.\nEnjoy your {coffee}!")
        global resources
        process_resources(coffee, cost)


def process_resources(coffee, cost):
    global resources
    for ingredient in MENU[coffee]["ingredients"]:
        resources[ingredient] -= MENU[coffee]["ingredients"][ingredient]
    resources["money"] += cost



def get_power_state():
    return power_state


def power_off():
    global power_state
    power_state = False


def print_report():
    for resource in resources:
        if resource == "money":
            print(f"{resource.title()}: ${resources[resource]:.2f}")
        else:
            print(f"{resource.title()}: {resources[resource]}")


HELP_MENU = {
    "espresso": "makes an espresso",
    "latte": "makes a latte",
    "cappuccino": "makes a cappuccino",
    "off": "turns the coffee machine off",
    "report": "prints a report of resources",
    "help": "prints list of commands",
}


def print_help():
    for item in HELP_MENU:
        print(f"{item.title()}: {HELP_MENU[item].title()}")