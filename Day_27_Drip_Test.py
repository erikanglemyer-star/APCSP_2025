# Space Mission Inventory Manager
print("Welcome to the Space Mission Inventory Manager")
print("You will check and manage the inventory for your space mission.")

# Step 1: Load fuel status from file or set to "medium" if not present
try:
    with open("fuel_status.txt", "r") as f:
        fuel_status_value = f.read().strip()
except FileNotFoundError:
    fuel_status_value = "medium"

# Step 2: Update fuel status for next run
if fuel_status_value == "medium":
    next_fuel_status = "low"
elif fuel_status_value == "low":
    next_fuel_status = "empty"
else:
    next_fuel_status = "empty"  # stays empty

# Save new fuel status for next run
with open("fuel_status.txt", "w") as f:
    f.write(next_fuel_status)

# Step 3: Define inventory with current fuel status
inventory = f"oxygen: full, water: full, food: low, fuel: {fuel_status_value}, tools: available, medkits: low, spare parts: low"

print("\nCurrent Inventory:")
print(inventory)

# Extract specific statuses
oxygen_status_index = inventory.find("oxygen")
oxygen_status = inventory[oxygen_status_index:oxygen_status_index + 11]
print("\nOxygen status:", oxygen_status)

food_status_index = inventory.find("food")
food_status = inventory[food_status_index:food_status_index + 9]
print("Food status:", food_status)

medkits_status_index = inventory.find("medkits")
medkits_status = inventory[medkits_status_index:medkits_status_index + 14]
print("\nMedkit status:", medkits_status)

# Warnings
if "low" in inventory or "empty" in inventory:
    print("\nWarning: One or more resources are low or empty!")
    if "oxygen: low" in inventory:
        print("Warning: oxygen is low!")
    if "water: low" in inventory:
        print("Warning: water is low!")
    if "food: low" in inventory:
        print("Warning: food is low!")
    if "fuel: low" in inventory:
        print("Warning: fuel is low!")
    if "fuel: empty" in inventory:
        print("Critical Warning: fuel is empty!")
    if "tools: low" in inventory:
        print("Warning: tools are low!")
    if "medkits: low" in inventory:
        print("Warning: medkits are low!")
    if "spare parts: low" in inventory:
        print("Warning: spare parts are low!")



inventory_length = len(inventory)
print("\nThe total number of characters in the inventory description is:", inventory_length)

updated_inventory = inventory.replace("food: low", "food: full")
print("\nUpdated Inventory:")
print(updated_inventory)

update_request = input("Enter the resource you want to update (e.g, food, water, fuel): ")
new_status = input("Enter the new status (e.g., full, medium, low): ")

if update_request == "oxygen":
    newInventory = updated_inventory.replace("oxygen: full", "oxygen: " + new_status)
elif update_request == "water":
    newInventory = updated_inventory.replace("water: full", "water: " + new_status)
elif update_request == "food":
    newInventory = updated_inventory.replace("food: full", "food: " + new_status)
elif update_request == "fuel":
    newInventory = updated_inventory.replace("fuel: {fuel_status_value}", "fuel: " + new_status)
elif update_request == "tools":
    newInventory = updated_inventory.replace("tools: available", "tools: " + new_status)
elif update_request == "medkits":
    newInventory = updated_inventory.replace("medkits: low", "medkits: " + new_status)
elif update_request == "spare parts":
    newInventory = updated_inventory.replace("spare parts: low", "spare parts: " + new_status)

print("Updated inventory after user input: ", newInventory)
print("Inventory Report: \nOxygen: ", newInventory[newInventory.find("oxygen"):newInventory.find("water")-2], "\nWater: ", newInventory[newInventory.find("water"):newInventory.find("food")-2], "\nFood: ", newInventory[newInventory.find("food"):newInventory.find("fuel")-2])
