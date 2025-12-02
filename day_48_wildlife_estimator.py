import math # Import the math library to use its functions for rounding

# Renaming Python's built-in functions for use in the program
absolute_difference = abs # Function to get the absolute value of a number
conservative_estimate = math.floor # Function to round down to nearest integer
liberal_estimate = math.ceil # Function to round up the the nearest integer

# Welcome message and introduction to the program
print("Welcome to the Wildlife Population Analyzer!")
print("Analyzing population estimates for bald eagles and snow leopards from January to July.")

# Function to get a valid floating-point number from user input
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt)) # Try to convert input to a floating-point number
        except ValueError:
            print("Invalid input! Please enter a number.") # Handle non-numberic input

# Collect January population estimates for both species
print("\n--- January Population Estimates ---")
bald_eagle_jan = get_float_input("Enter the estimated January population for bald eagle (e.g., 316000.7): ")
snow_leopard_jan = get_float_input("Enter the estimated January population for snow leopards (e.g., 4000.9): ")
amur_leopard_jan = get_float_input("Enter the estimated January population for Amur leopards (e.g., 6704.1): ")

# Collect July population estimates for both species
print("\n--- July Population Estimates ---")
bald_eagle_jul = get_float_input("Enter the estimated July population for bald eagle (e.g., 318000.5): ")
snow_leopard_jul = get_float_input("Enter the estimated July population for snow leopards (e.g., 4100.3): ")
amur_leopard_jul = get_float_input("Enter the estimated July population for Amur leopards (e.g., 7006.7): ")

# Display the collected estimates for easy reference
print("\nBald eagle estimated population in January:", bald_eagle_jan)
print("Bald eagle estimated population in July:", bald_eagle_jul)
print("Snow leopard estimated population in January:", snow_leopard_jan)
print("Snow leopard estimated population in July:", snow_leopard_jul)
print("Amur leopard estimated population in January:", amur_leopard_jan)
print("Amur leopard estimated population in July:", amur_leopard_jul)

# Calculate and display the change in Bald Eagle population from January to July
bald_eagle_change = bald_eagle_jul - bald_eagle_jan # Calculate the difference
if bald_eagle_change > 0:
    print("\nBald eagle population increased by:", bald_eagle_change)
elif bald_eagle_change < 0:
    print("\nBald Eagle population decreased by:", absolute_difference(bald_eagle_change)) # Negative change
else:
    print("\nBald Eagle population remained the same.") # No change

# Calculate and display the change in snow leopard population from January to July
snow_leopard_change = snow_leopard_jul - snow_leopard_jan # Calculate the difference
if snow_leopard_change > 0:
    print("\nSnow leopard population increased by:", snow_leopard_change)
elif snow_leopard_change < 0:
    print("\nSnow leopard population decreased by:", absolute_difference(snow_leopard_change)) # Negative change
else:
    print("\nSnow leopard population remained the same.") # No change

# Calculate and display the change in amur leopard population from January to July
amur_leopard_change = amur_leopard_jul - amur_leopard_jan # Calculate the difference
if amur_leopard_change > 0:
    print("\nAmur leopard population increased by:", amur_leopard_change)
elif amur_leopard_change < 0:
    print("\nAmur leopard population decreased by:", absolute_difference(amur_leopard_change)) # Negative change
else:
    print("\nAmur leopard population remained the same.") # No change

# Calculate and display the conservative estimate for both populations (rounded down)
bald_eagle_conservative_jul = conservative_estimate(bald_eagle_jul)
snow_leopard_conservative_jul = conservative_estimate(snow_leopard_jul)
amur_leopard_conservative_jul = conservative_estimate(amur_leopard_jul)
print("\nConservative July Population Estimate (using conservative_estimate):")
print("Bald eagle:", bald_eagle_conservative_jul)
print("Snow leopard:", snow_leopard_conservative_jul)
print("Amur leopard:", amur_leopard_conservative_jul)

# Calculate and display the liberal estimate for both populations (rounded up)
bald_eagle_liberal_jul = liberal_estimate(bald_eagle_jul)
snow_leopard_liberal_jul = liberal_estimate(snow_leopard_jul)
amur_leopard_liberal_jul = liberal_estimate(amur_leopard_jul)
print("\nLiberal July Population Estimate (using liberal_estimate):")
print("Bald eagle:", bald_eagle_liberal_jul)
print("Snow leopard:", snow_leopard_liberal_jul)
print("Amur leopard:", amur_leopard_liberal_jul)

# Simplify population estimates by rounding to the nearest integer (ignoring decimals)
simple_bald_eagle_population = int(bald_eagle_jul)
simple_snow_leopard_population = int(snow_leopard_jul)
simple_amur_leopard_population = int(amur_leopard_jul)
print("Simplified Bald Eagle Population for Reporting (using int):", simple_bald_eagle_population)
print("Simplified Snow Leopard Population for Reporting (using int):", simple_snow_leopard_population)
print("Simplified Snow Leopard Population for Reporting (using int):", simple_amur_leopard_population)