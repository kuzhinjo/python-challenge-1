# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.992,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

menu_dashes = "-" * 42
cust_order = []
order = {}
# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to view different sections of the menu, so let's create a 
# continuous loop
while True:
    # Ask the customer which menu category they want to view
    print("Which menu would you like to view? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval 
    menu_items = {}


    # Print the options to choose from menu headings (all the first level 
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number to view or q to quit: ")

    # Exit the loop if user typed 'q'
    if menu_category == 'q':
        break
    # Check if the customer's input is a number
    elif menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Display the heading for the sub-menu
            print(menu_dashes)
            print(f"This is the {menu_category_name} menu.")
            print(menu_dashes)
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")

            # Initialize a menu item counter
            item_counter = 1
            # Print out the menu options from the menu_category_name
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    # Iterate through the dictionary items
                    for key2, value2 in value.items():
                        # Print the menu item
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{item_counter}      | "
                              + f"{key} - {key2}{item_spaces} | "
                              + f"${value2}")
                        # Add 1 to the item_counter
                        item_counter += 1
                else:
                    # Print the menu item
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{item_counter}      | "
                          + f"{key}{item_spaces} | ${value}")
                    # Add 1 to the item_counter
                    item_counter += 1
            
            menu_selection = input("Select An Item Or Press Enter To Return To The Main Menu.")
            menu_item = ""
            price = ""
            # check menu delection is s digit
            if menu_selection.isdigit():
                # if not a valid selection
                if int(menu_selection) >= item_counter:
                    print(menu_selection+" IS NOT a valid menu selection Returning to main menu")
                else:
                    item_counter = 1
                    for key, value in menu[menu_category_name].items():
                        if type(value) is dict:
                            # Iterate through the dictionary items
                            # for selected  menu_item and price
                            for key2, value2 in value.items():
                                if int(menu_selection) == item_counter:
                                    menu_item = key+" "+key2
                                    price = value2

                                item_counter += 1
                        else:
                            # for selected  menu_item and price
                            if int(menu_selection) == item_counter:
                                menu_item = key
                                price = value                           
                            item_counter += 1
                quantity = input("Select number of quantity(es): ")
                if not quantity.isdigit():
                    quantity = 1
                # Create a dictonary for the user item selection
                order = {"Item Name": menu_item, "Price": price, "Quantity":quantity}
                # append the single order to the whole
                cust_order.append(order)

                # Provide exit option
                while True:
                    # Ask the customer if they would like to order anything else
                    keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

                    # Check the customer's input
                    match keep_ordering.lower():
                        # Customer chose yes
                        case 'y':
                            # Keep ordering
                            place_order = True
                            # Exit the keep ordering question loop
                            break
                        # Customer chose no
                        case 'n':
                            # Complete the order
                            place_order = False
                            # Since the customer decided to stop ordering, thank them for their order
                            print("-----------------------------|-----------------|-------------")
                            print("                Thank you for your order                     ")
                            # Display the heading for the sub-menu
                            print("-----------------------------|-----------------|-------------")
                            print("                       Final Order                           ")
                            print("-----------------------------|-----------------|-------------")
                            print("Item name #                  | Price           | Quantity")
                            print("-----------------------------|-----------------|-------------")                            
                            orders_list = []        
                            totalPrice = 0.0                                               
                            # Since the order to be displayed horizondally
                            # Create a list of order to iterate and display horizondallly
                            for order in cust_order:
                                order_list =[]                         
                                for key, value in order.items():
                                    order_list.append(value)
                                orders_list.append(order_list)
                            for order in orders_list:
                                # Print the order
                                item_name_spaces = 29 - len(order[0])
                                item_name_spaces = " " * item_name_spaces
                                price_spaces = 15 - len(str(order[1]))
                                price_spaces = " " * price_spaces                                
                                print(f"{order[0]}{item_name_spaces}| "
                                        + f"${order[1]}{price_spaces}| {order[2]}")
                                # Multiply quantity and price to add to total for the order
                                totalPrice += order[1]*float(order[2])
                            print("-----------------------------|-----------------|-------------")
                            print(f'Total Price: ${totalPrice:,.2f}')
                            print("-----------------------------|-----------------|-------------")
                            # Get the customer's input
                            quit_ordering = input("Type q To Start A New Order : ")

                            # Exit the loop if user typed 'q'
                            if quit_ordering == 'q':
                                # Due to somereason cust_order.clear or cust_order.remove is not working
                                # Empting the list
                                cust_order = []
                                break

                        # Customer typed an invalid input
                        case _:
                            # Tell the customer to try again
                            print("I didn't understand your response. Please try again.")          
            else:       
                print(menu_selection+" IS NOT a valid menu selection Returning to main menu")
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")