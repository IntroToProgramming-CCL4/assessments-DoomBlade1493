import random

CMF1 = ['Librarian', 'Medusa', 'Roman Commander', 'Warrior Woman', 'Tomahawk Warrior', 'Skydiver', 
        'Bumblebee Girl', 'Grandpa', 'Paintball Player', 'Sea Captain', 'Sad Clown', 'Revolutionary Soldier', 
        'Baseball Finder', 'Trendsetter', 'Decorator', 'Motorcycle Mechanic', 'Mr. Gold']
CMF2 = ['Kate Bishop', 'Moon Knight', 'Hawkeye', 'Mr. Knight', 'Agatha Harkness', 'Wolverine', 
        'Echo', 'Beast', 'She-Hulk', 'Storm', 'Werewolf', 'Goliath']

R1 = random.choice(CMF1)
R2 = random.choice(CMF2)

data = [
    {"Id": 1, "Name": "Lego CMF Series 10", 'Price': 30, "Stock": 15},
    {"Id": 2, "Name": "Lego Marvel CMF Series 2", 'Price': 30, "Stock": 15},
    {"Id": 3, "Name": "Lego SC Pagani Utopia", 'Price': 100, "Stock": 10},
    {"Id": 4, "Name": "Lego SC Lamborghini V12 VGT", 'Price': 120, "Stock": 10},
    {"Id": 5, "Name": "Lego Minecraft TDDBS", 'Price': 280, "Stock": 5},
    {"Id": 6, "Name": "Lego Star Wars ISD", 'Price': 580, "Stock": 2}
]

item = []

def displayProducts(data):
    print("=" * 40)
    print(f"{'Lego Set Vending Machine':^40}")
    print("=" * 40)
    print(f"{'ID':<5}{'Name':<30}{'Price':<10}{'Stock':<10}")
    print("-" * 40)
    for i in data:
        print(f"{i['Id']:<5}{i['Name']:<30}AED{i['Price']:<8}{i['Stock']:<10}")
    print("=" * 40)

def cancelEntireCart(item, data):
    for i in item:
        for product in data:
            if product["Name"] == i["Name"]:
                product["Stock"] += 1
    item.clear()
    print("Your cart has been cleared. Ending the process...")

def cancelPurchase(item, data):
    if not item:
        print("Your cart is empty. Nothing to cancel.")
        return False  # Indicate that the cart is not empty

    while True:
        print("\nItems in your cart:")
        for idx, i in enumerate(item):
            print(f"{idx + 1}. {i['Name']} - AED {i['Price']}")

        try:
            cancelIndices = input("Enter the numbers of the items you want to cancel (comma-separated): ")
            cancelIndices = [int(x.strip()) - 1 for x in cancelIndices.split(',')]

            for cancelIndex in sorted(cancelIndices, reverse=True):
                if 0 <= cancelIndex < len(item):
                    canceledItem = item.pop(cancelIndex)
                    for product in data:
                        if product['Name'] == canceledItem['Name']:
                            product['Stock'] += 1
                            break
                    print(f"Removed {canceledItem['Name']} from your cart. Updated stock: {product['Stock']}.")
                else:
                    print(f"Invalid selection: {cancelIndex + 1}. Skipping...")

            # Check if the cart is empty after cancellation
            if not item:
                print("Your cart is empty. Ending the process...")
                return True  # Indicate that the cart is empty
            break
        except ValueError:
            print("Invalid input. Please enter valid numeric values separated by commas.")

def vendingMachine(data, run, item, balance):
    while run:
        while True:
            try:
                buyItem = int(input("\nEnter the item ID for the item you want to buy: "))
                if 1 <= buyItem <= len(data):
                    selectedItem = data[buyItem - 1]

                    if selectedItem["Stock"] > 0:   
                        print(f"Your current balance is: AED {balance - sumItem(item)}")
                        
                        while True:
                            try:
                                quantity = int(input(f"How many {selectedItem['Name']}s would you like to buy? "))
                                if quantity <= 0:
                                    print("Please enter a valid quantity greater than 0.")
                                elif quantity > selectedItem["Stock"]:
                                    print(f"Sorry, only {selectedItem['Stock']} units are available.")
                                elif sumItem(item) + (selectedItem["Price"] * quantity) > balance:
                                    print("Adding this quantity will exceed your budget. Please reduce the quantity or choose another item.")
                                else:
                                    for _ in range(quantity):
                                        item.append(selectedItem)
                                    selectedItem["Stock"] -= quantity
                                    print(f"{quantity} x {selectedItem['Name']} added to your cart. Remaining stock: {selectedItem['Stock']}")
                                    break
                            except ValueError:
                                print("Invalid input. Please enter a numeric value for the quantity.")
                    else:
                        print(f"Sorry, {selectedItem['Name']} is out of stock.")
                    break
                else:
                    print("Invalid product ID. Please choose a valid ID.")
            except ValueError:
                print("Invalid input. Please enter a valid numeric item ID.")

        action = input("Type 'a' to add more items, 'c' to cancel a purchase, 'r' to remove entire cart, or 's' to go to checkout: ").lower()
        if action == "c":
            if cancelPurchase(item, data):  # Check if cart is empty after cancellation
                return  # Ends the process
        elif action == "r":
            cancelEntireCart(item, data)
            return  # Ends the process
        elif action == "s":
            run = False

    if not item:
        print("Your cart is empty. Transaction canceled.")
        return

    receiptValue = int(input("\nPrinting bill: Press 1 to continue, or 2 to cancel. "))
    if receiptValue == 1:
        print(createReceipt(item, balance))
    else:
        print("Cancelling payment process...")

def sumItem(item):
    return sum(i["Price"] for i in item)

def createReceipt(item, balance):
    total = sumItem(item)
    receipt = "\nPRODUCT NAME -- COST\n"

    for i in item:
        if i['Name'] == "Lego CMF Series 10":
            receipt += f"{i['Name']} -- AED {i['Price']}\nMinifigure Received: {R1}\n"
        elif i['Name'] == "Lego Marvel CMF Series 2":
            receipt += f"{i['Name']} -- AED {i['Price']}\nMinifigure Received: {R2}\n"
        else:
            receipt += f"{i['Name']} -- AED {i['Price']}\n"

    receipt += f"\nTotal: AED {total}\n"
    if balance < total:
        receipt += "Insufficient balance. Please add more funds to complete the purchase.\n"
    else:
        change = balance - total
        receipt += f"Total Paid: AED {balance}\nChange Due: AED {change}\n"

    receipt += f"Total Items Purchased: {len(item)}\n"
    return receipt

# Display products first
displayProducts(data)

# Ask for balance after showing products
try:
    balance = int(input("\nPlease Enter Balance (Minimum is 30 & Maximum is 2000): "))
    if balance <= 29:
        print("You wont be able to buy anything with a budget below 30.")
    elif balance > 2000:
        print("Balance exceeds the limit of 2000.")
    else:
        vendingMachine(data, True, item, balance)
except ValueError:
    print("Invalid input. Please enter a numeric value for the balance.")