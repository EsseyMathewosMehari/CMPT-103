#---------------------------------
# Name:Essey Mehari
# Program: Lab_6_EM.py
#----------------------------------
#I certify that this work is mine
#----------------------------------
#This code makes sure that the application only runs when valid input is given by checking for user input mistakes. It asks the user for the item's name and checks to make sure the field is not blank. The next step is to see if the item with that name already exists in the inventory. If so, it asks the user how many things they want to add to the inventory and checks to make sure they provide an integer. If the item's name is not present in the inventory, the user is prompted for the price and the quantity of products to add, and both inputs are verified as being correct.
def add_item(inventory):
    name = input("Enter the name of the item: ").upper()
    while not name:
        print("Invalid name. Please try again.")
        name = input("Enter the name of the item: ").upper()
    
    if name in inventory:
        
        count_str = input("Enter the number of {}(s) to add to inventory: ".format(name))
        try:
            count = int(count_str)
        except ValueError:
            print("Invalid count. Please enter an integer.")
        inventory[name]['count'] += count
        print("{} {}(s) have been added to inventory".format(count, name))
    else:
        price_str = input("Enter the price of {} (format: 21.67): ".format(name))
        try:
            price = float(price_str)
        except ValueError:
            print("Invalid price. Please enter a float.")
        count_str = input("Enter the number of {}(s) to add to inventory: ".format(name))
        try:
            count = int(count_str)
        except ValueError:
            print("Invalid count. Please enter an integer.")
    inventory[name] = {"price": price, "count": count}
    print("{} {}(s) have been added to inventory".format(count, name))
        
#It asks the user to input the name of the item they wish to remove from inventory, determines whether the item is already in the inventory, and then requests the user's desired removal quantity. The process next determines if there are sufficient items in the inventory to remove them, and if so, subtracts those items' total from the inventory count.        
def remove_item(inventory):
    name = input("Enter the name of the item: ").capitalize()
    if name not in inventory:
        print("There are no {}(s) in inventory".format(name))
        return
    
    count_str = input("How many {}(s) would you like to remove?: ".format(name))
    try:
        count = int(count_str)
    except ValueError:
        print("Invalid count. Please enter an integer.")
    
    if inventory[name]['count'] < count:
        print("There are not enough {}(s) in inventory".format(name))
        return
    
    inventory[name]['count'] -= count
    print("{} {}(s) have been removed from inventory".format(count, name))
    
#uses an inventory dictionary as input and iterates through the inventory items to determine the value of each one based on its price and count before adding it to a running total to determine the total value of the inventory. The function then outputs a formatted string with the value of each item and a final formatted string with the value of the entire inventory. The items are iterated over using the sorted function to arrange them alphabetically by item name.    
def calc_worth(inventory):
    total_worth = 0
    for name, item in sorted(inventory.items()):
        worth = item['price'] * item['count']
        print("There are {} {}(s) worth ${:,.2f}".format(item['count'], name, worth))
        total_worth += worth
    print("The total worth of the inventory is ${:,.2f}".format(total_worth))

def main():
    inventory = {}
    print("(1) Add an item to the inventory")
    print("(2) Remove an item from the inventory")
    print("(3) Calculate the worth of the inventory")
    print("(4) Quit")
    try:
        choice = int(input("Select option (1 to 4): "))
    except ValueError:
            print("Invalid option. Please enter a number between 1 and 4.")
        
    if choice == 1:
        add_item(inventory)
    elif choice == 2:
        remove_item(inventory)
    elif choice == 3:
        calc_worth(inventory)
    elif choice == 4:
        done = True
    else:
        print("Invalid option. Please enter a number between 1 and 4.")