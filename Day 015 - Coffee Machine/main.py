import data

while data.get_power_state():
    choice = input("What would you like? (espresso/latte/cappuccino)\n> ").lower()
    if choice in data.MENU:
        data.make_coffee(choice)
    elif choice == "off":
        data.power_off()
    elif choice == "report":
        data.print_report()
    elif choice == "help":
        data.print_help()
    else:
        print("Please enter a valid input.")
