# Shipping Cost Simulator

# Inputs
weight = float(input("Enter the weight of the package (in kg): "))
length = float(input("Enter the length of the package (in cm): "))
width = float(input("Enter the width of the package (in cm): "))
destination = input("Enter the destination (domestic or international): ").lower()

# Constants
BASE_COST_DOMESTIC = 5.00
BASE_COST_INTERNATIONAL = 10.00
EXTRA_COST_WEIGHT = 2.00
EXTRA_COST_SIZE = 3.00

# Determine if the package is oversized
oversized = (length > 100) or (width > 100)

# Calculate base cost based on destination
if destination == "domestic":
    cost = BASE_COST_DOMESTIC
else:
    cost = BASE_COST_INTERNATIONAL

# Add extra cost for weight
if weight > 5:
    cost += EXTRA_COST_WEIGHT
    print("Extra cost added for weight")

# Add extra cost for size
if oversized:
    cost += EXTRA_COST_SIZE
    print("Extra cost added for oversized dimensions.")

# Final cost calculation
if (weight > 10 and oversized) or destination == "international":
    cost += 5.00
    print("Additional surcharge applied.")

# Display the total cost
print("Total shipping cost: ${:,.2f}".format(cost))