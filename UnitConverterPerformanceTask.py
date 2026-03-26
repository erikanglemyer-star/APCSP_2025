units = ["feet", "yards", "miles", "meters", "kilometers", "centimeters", "inches"]
unitConverter = 1
finalUnit = 1

def checkUnit(unit):
    while True:
        if unit in units:
            return unit
        else:
            print("Invalid unit entered.")
            unit = input("Please input the distance unit you are converting (feet, yards, miles, meters, kilometers, centimeters):")

originalUnit = checkUnit(input("Please input the distance unit you are converting from (feet, yards, miles, meters, kilometers, centimeters): "))

while True:
    unitAmount = input("Please enter the amount of the unit you would like to convert: ")
    if unitAmount < 0:
        print("Please enter a valid non-negative number.")
    else:
        try:
            unitAmount = float(unitAmount)
            break
        except:
            print("Please enter a valid non-negative number.")

newUnit = checkUnit(input("Please input the distance unit you are converting to (feet, yards, miles, meters, kilometers, centimeters): "))

if originalUnit == "yards":
    unitConverter = unitAmount / 3
elif originalUnit == "inches":
    unitConverter = unitAmount * 12
elif originalUnit == "meters":
    unitConverter = unitAmount * 0.3048
elif originalUnit == "centimeters":
    unitConverter = unitAmount * 30.48
elif originalUnit == "miles":
    unitConverter = unitAmount * 5280

if newUnit == "yards":
    finalUnit = unitConverter * 3
elif newUnit == "inches":
    finalUnit = unitAmount / 12
elif newUnit == "meters":
    finalUnit = unitAmount / 0.3048
elif newUnit == "centimeters":
    finalUnit = unitAmount / 30.48
elif newUnit == "miles":
    finalUnit = unitAmount / 5280