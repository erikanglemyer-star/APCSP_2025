print("Welcome to the Customary Unit Converter")

units = ["inches", "feet", "yards", "miles"]
feetConversion = [1/12, 1, 3, 5280]

def checkUnit(unit):
    while True:
        if unit in units:
            return unit
        else:
            print("Invalid unit entered.")
            unit = input("Please input the customary distance unit you are converting (inches, feet, yards, miles): ").lower()

def convertUnit(quantity, originalUnit, newUnit):
    for i in range(len(units)):
        if units[i] == originalUnit:
            amountInFeet = quantity * feetConversion[i]

    for i in range(len(units)):
        if units[i] == newUnit:
            finalQuantity = amountInFeet / feetConversion[i]

    return finalQuantity

originalUnit = checkUnit(input("Please input the customary distance unit you are converting from (inches, feet, yards, miles): ").lower())

while True: 
    originalQuantity = input("Please enter the quantity of the unit you would like to convert: ")
    try:
        originalQuantity = float(originalQuantity)
        if originalQuantity < 0:
            print("Please enter a valid non-negative number.")
        else:
            break
    except:
        print("Please enter a valid non-negative number.")

newUnit = checkUnit(input("Please input the customary distance unit you are converting to (inches, feet, yards, miles): ").lower())

convertedQuantity = convertUnit(originalQuantity, originalUnit, newUnit)

print(str(originalQuantity) + " " + originalUnit + " converts to " + str(convertedQuantity) + " " + newUnit + ".")