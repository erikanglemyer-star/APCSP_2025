print("Welcome to the Customary Unit Converter") # Welcome the user

# These lists store units and their conversions, allowing for the user to easily add more conversions without breaking the algorithm.
units = ["inches", "feet", "yards", "miles"]
feetConversion = [1/12, 1, 3, 5280]
shouldQuit = "yes"

# Function that checks to ensure the unit entered is a customary distance unit
def checkUnit(unit):
    while True: # Loops until a valid unit is entered
        if unit in units: # Iterate through the list "units" and check if the input is in the list
            return unit
        else:
            # Communicates the issue and prompts the user to enter a new input
            print("Invalid unit entered.")
            unit = input("Please input the customary distance unit you are converting (inches, feet, yards, miles): ").lower() 

def convertUnit(quantity, originalUnit, newUnit):
    # The algorithm uses iteration to search the list and selection to test if the item tested matches the user input
    for i in range(len(units)):
        if units[i] == originalUnit:
            amountInFeet = quantity * feetConversion[i]

    for i in range(len(units)):
        if units[i] == newUnit:
            finalQuantity = amountInFeet / feetConversion[i]

    return finalQuantity

while shouldQuit != "no":
    # User inputs which unit they are converting from
    originalUnit = checkUnit(input("Please input the customary distance unit you are converting from (inches, feet, yards, miles): ").lower())

    # Collect the Quantity of the unit the user is converting
    while True: 
        originalQuantity = input("Please enter the quantity of the unit you would like to convert: ") # Collects user input
        try: # Checks to make sure it is a non-negative number
            originalQuantity = float(originalQuantity)
            if originalQuantity < 0:
                print("Please enter a valid non-negative number.")
            else:
                break
        except:
            print("Please enter a valid non-negative number.")

    # User inputs which unit they are converting to
    newUnit = checkUnit(input("Please input the customary distance unit you are converting to (inches, feet, yards, miles): ").lower())

    # Call the function to convert the unit
    convertedQuantity = convertUnit(originalQuantity, originalUnit, newUnit)

    # Print final calculation
    print(str(originalQuantity) + " " + originalUnit + " converts to " + str(convertedQuantity) + " " + newUnit + ".")
    shouldQuit = input("Would you like to calculate another unit conversion? (Type 'no' to quit): ").lower()







