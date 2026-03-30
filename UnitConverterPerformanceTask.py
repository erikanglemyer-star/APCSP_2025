print("Welcome to the Customary Unit Converter") # Welcome the user
# List of available units to convert
units = ["inches", "feet", "yards", "miles"]
feetConversion = [1/12, 1, 3, 5280]

# Initialize the variables
unitConverter = 1
finalAmount = 1

# Function that checks to ensure the unit entered is a customary distance unit
def checkUnit(unit):
    while True: # Loops until a valid unit is entered
        if unit in units: # Iterate through the list "units" and check if the input is in the list
            return unit
        else:
            print("Invalid unit entered.")
            unit = input("Please input the customary distance unit you are converting (inches, feet, yards, miles): ").lower() # Prompts the user to enter a new input

# User inputs which unit they are converting from
originalUnit = checkUnit(input("Please input the customary distance unit you are converting from (inches, feet, yards, miles): ").lower())

# Collect the amount of the unit the user is converting
while True: 
    originalAmount = input("Please enter the amount of the unit you would like to convert: ") # Collects user input
    try: # Checks to make sure it is a non-negative number
        originalAmount = float(originalAmount)
        if originalAmount < 0:
            print("Please enter a valid non-negative number.")
        else:
            break
    except:
        print("Please enter a valid non-negative number.")

# User inputs which unit they are converting to
newUnit = checkUnit(input("Please input the customary distance unit you are converting to (inches, feet, yards, miles): ").lower())

# Convert the original unit to feet and store in variable unitConverter
def convertUnit(amount, originalUnit, newUnit):
    for i in range(4):
        if units[i] == originalUnit:
            finalAmount = originalUnit * feetConversion[i]


# Print final calculation
print(str(originalAmount) + " " + originalUnit + " converts to " + str(finalAmount) + " " + newUnit + ".")