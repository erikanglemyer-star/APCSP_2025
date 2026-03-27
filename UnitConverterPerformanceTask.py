print("Welcome to the Customary Unit Converter")
units = ["feet", "yards", "miles", "inches"]
unitConverter = 1
finalUnit = 1

def checkUnit(unit):
    while True:
        if unit in units:
            return unit
        else:
            print("Invalid unit entered.")
            unit = input("Please input the customary distance unit you are converting (inches, feet, yards, miles): ").lower()

originalUnit = checkUnit(input("Please input the customary distance unit you are converting from (inches, feet, yards, miles): ").lower())

while True:
    unitAmount = input("Please enter the amount of the unit you would like to convert: ")
    try:
        unitAmount = float(unitAmount)
        if unitAmount < 0:
            print("Please enter a valid non-negative number.")
        else:
            break
    except:
        print("Please enter a valid non-negative number.")

newUnit = checkUnit(input("Please input the customary distance unit you are converting to (inches, feet, yards, miles): ").lower())

if originalUnit == "yards":
    unitConverter = unitAmount * 3
elif originalUnit == "inches":
    unitConverter = unitAmount / 12
elif originalUnit == "miles":
    unitConverter = unitAmount * 5280

if newUnit == "yards":
    finalUnit = unitConverter / 3
elif newUnit == "inches":
    finalUnit = unitAmount * 12
elif newUnit == "miles":
    finalUnit = unitAmount / 5280

print(str(unitAmount) + " " + originalUnit + " converts to " + str(finalUnit) + " " + newUnit + ".")