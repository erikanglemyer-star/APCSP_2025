print("Welcome to the School Lunch Tracker!\nYou are managing the availablity of lunch items.")

menu = "pizza: available, salad: low, sandwich: available, juice: unavailable"
print("\nInitial Lunch Menu: ", menu)
print("\nThe word 'salad' starts at index: ", menu.find("salad"))
print("\nFirst two items on menu: ", menu[:menu.find("salad")-2])