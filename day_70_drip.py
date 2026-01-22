# Movie Night Cost Planner
# Inputs
group_size = int(input("Enter the number of attendees: "))
ticket_type = input("Enter ticket type (standard or premium): ").lower()
snacks = input("Will snacks be included? (yes or no): ").lower()
reserved_seating = input("Will reserved seating be included? (yes or no):").lower()
# Constants
STANDARD_TICKET_COST = 12.00
PREMIUM_TICKET_COST = 18.00
SNACK_COST = 5.00
RESERVED_SEATING_COST = 3.00
GROUP_DISCOUNT_THRESHOLD = 10 # Minimum group size for a discount
GROUP_DISCOUNT_RATE = 0.15 # 15% discount for groups of 10 or more
# TODO: Assign base cost based on ticket type
# Calculate the base cost based on ticket type.
if ticket_type == "standard":
    cost = STANDARD_TICKET_COST
else:
    cost = PREMIUM_TICKET_COST
# TODO: Add cost for snacks
# Calculate and add the snack cost if snacks == "yes".
if snacks == "yes":
    cost += SNACK_COST
    print("Snack cost added.")

# TODO: Add cost for reserved seating
# Calculate and add the reserved seating cost if reserved_seating == "yes".
if reserved_seating == "yes":
    cost += RESERVED_SEATING_COST
    print("Reserved seating cost added.")

# TODO: Apply group discount if applicable
# Calculate the discount for groups of 10 or more and apply it to the total cost.
if group_size >= 10:
    cost -= cost * 0.15
    print("Group discount applied.")

cost = cost * group_size

# Output the total cost
print("Total movie night cost: ${:,.2f}".format(cost))