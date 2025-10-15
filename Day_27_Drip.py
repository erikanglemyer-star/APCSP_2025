print("Welcome to the Space Mission Inventory Manager")
print("You will check and manage the inventory for your space mission.")

inventory = "oxygen: full, water: full, food: low, fuel: medium, tools: available, medkits: low, spare parts: available"

print("\nCurrent Inventory: ")
print(inventory)

oxygen_status_index = inventory.find("oxygen")
oxygen_status = inventory[oxygen_status_index:oxygen_status_index + 11]
print("\nOxygen status:", oxygen_status)

food_status_index = inventory.find("food")
food_status = inventory[food_status_index:food_status_index + 9]
print("Food status:", food_status)

medkits_status_index = inventory.find("oxygen")
medkits_status = inventory[medkits_status_index:medkits_status_index + 11]
print("\nMedkit status:", medkits_status)

if "low" in inventory:
    print("\nWarning: One or more resources are low!")
    if "oxygen: low" in inventory:
        print("Warning: oxygen is low!")
    if "water: low" in inventory:
        print("Warning: water is low!")
    if "food: low" in inventory:
        print("Warning: food is low!")
    if "fuel: low" in inventory:
        print("Warning: fuel is low!")
    if "tools: low" in inventory:
        print("Warning: tools are low!")
    if "medkits: low" in inventory:
        print("Warning: medkits are low!")
    if "spare parts: low" in inventory:
        print("Warning: spare parts are low!")

inventory_length = len(inventory)
print("\nThe total number of characters in the inventory description is:", inventory_length)

updated_inventory = inventory.replace("food: low", "food: full")
print("\nUpdated Inventory: ")
print(updated_inventory)

uppercase_inventory = updated_inventory.upper()
print("\nUppercase Inventory: ")
print(uppercase_inventory)

inventory_summary = updated_inventory[:30]
print("\nInventory Summary (First 2 Resources): ")
print(inventory_summary)