print("Welcome to the School Lunch Tracker!\nYou are managing the availablity of lunch items.")

menu = "pizza: available, salad: low, sandwich: available, juice: unavailable"
print("\nInitial Lunch Menu: ", menu)
print("\nThe word 'salad' starts at index: ", menu.find("salad"))
print("\nFirst two items on menu: ", (menu.split(", ")[0]))

menu = menu.replace("salad: low", "salad: available")
print("\nUpdated Lunch Menu after replacing 'salad': ", menu)
print("\nLunch Menu in UPPERCASE: ", menu.upper)
print("\nThe total number of characters in the lunch menu: ", len(menu))
menu = menu + " fries: available"
print("\nFinal Lunch Menu after adding 'fries': ", menu)