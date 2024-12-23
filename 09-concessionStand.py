def display_menu(menu):
    print("------ Concession Stand Menu ------")
    for item, price in menu.items():
        print(f"{item:<15}: ${price:.2f}")
    print("-----------------------------------")

def take_order(menu):
    order = {}
    total_cost = 0

    while True:
        item = input("Enter the item you want to order (or type 'done' to finish): ").strip().title()
        if item.lower() == 'done':
            break
        if item in menu:
            try:
                quantity = int(input(f"How many {item} do you want? "))
                if quantity > 0:
                    if item in order:
                        order[item] += quantity
                    else:
                        order[item] = quantity
                    total_cost += menu[item] * quantity
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("Sorry, we don't have that item. Please choose from the menu.")

    return order, total_cost

def print_receipt(order, total_cost):
    print("\n------ Your Receipt ------")
    print(f"{'Item':<15} {'Quantity':<10} {'Price Each':<12} {'Total Price':<12}")
    print("-" * 49)
    
    for item, quantity in order.items():
        price_each = menu[item]
        total_price = price_each * quantity
        print(f"{item:<15} {quantity:<10} ${price_each:>10.2f} ${total_price:>10.2f}")
    
    print("-" * 49)
    print(f"{'Total Cost:':<37} ${total_cost:>10.2f}")
    print("--------------------------")

# Concession Stand Menu
menu = {
    "Hot Dog": 3.50,
    "Hamburger": 5.00,
    "Popcorn": 2.25,
    "Soda": 1.75,
    "Nachos": 4.00,
    "Candy": 1.50
}

def concession_stand():
    print("Welcome to the Concession Stand!")
    display_menu(menu)

    order, total_cost = take_order(menu)
    if order:
        print_receipt(order, total_cost)
    else:
        print("No items ordered.")

# Start the program
concession_stand()
