print("Welcome to the Car Rental Charge Calculator!")

def checkPosInt(check, command):
    while True:
        check = input("Please enter " + command + ": ")
        try:
            check = int(check)
            if check > 0:
                break
            else:
                print("Please enter a valid number.")
        except:
            print("Please enter a valid number.")
    return check

while True:
    code = ""
    check = ""
    while code != "d" and code != "b" and code != "w" and code != "q":
        code = input("Please enter your car classification code (Q to quit): ").lower()
        if code == "d" or code == "b" or code == "w" or code == "q":
            break
        else:
            print("Please enter a valid code.")
    if code == "q":
        print("Thank you for using the Car Rental Charge Calculator.")
        break
    code = code.upper()

    if code == "W":
        weeksRented = checkPosInt(check, "the number of weeks rented")
    else:
        daysRented = checkPosInt(check, "the number of days rented")
    
    startMile = checkPosInt(check, "the odometer reading at start")

    while True:
        endMile = checkPosInt(check, "the odometer reading at end")
        if endMile < startMile:
            print("Please enter a higher ending mileage reading than starting.")
        else:
            break
    
    miles = endMile - startMile
    
    print("Customer Classification code: ", code)

    if code == "B":
        baseCharge = 40 # per day
        mileageCharge = 0.25 # per mile
        total = daysRented * baseCharge + miles * mileageCharge
        print("Rental period (days):", daysRented)
        print("Odometer reading at start:", startMile)
        print("Odometer reading at end:", endMile)
        print("Number of Miles Driven:", miles)
        print("Base Charge: $" + str(baseCharge) + "/day x " + str(daysRented) + " days = $" + str(baseCharge * daysRented))
        print("Mileage Charge: $" + str(mileageCharge) + "/mile x " + str(miles) + " miles = $" + str(mileageCharge * miles))
        print("Total Amount Due: $" + str(total))

    
    if code == "D":
        baseCharge = 60 # per day
        mileageCharge = 0.25 # Free for up to 100 miles per day, then per mile
        freeMiles = 100 # per day
        paidMiles = miles - daysRented * freeMiles
        total = paidMiles * mileageCharge + baseCharge * daysRented
        print("Rental period (days):", daysRented)
        print("Odometer reading at start:", startMile)
        print("Odometer reading at end:", endMile)
        print("Number of Miles Driven:", miles)
        print("Base Charge: $" + str(baseCharge) + "/day x " + str(daysRented) + " days = $" + str(baseCharge * daysRented))
        print("Mileage Charge: First " + str(daysRented * freeMiles) + " miles free (100 miles/day), Extra " + str(paidMiles) + " miles x $" + str(mileageCharge) + " = $" + str(paidMiles * mileageCharge))
        print("Total Amount Due: $" + str(total))

    if code == "W":
        baseCharge = 190 # per week
        if miles >= 900 and miles <= 1500:
            mileageCharge = 0 
            flatMileCharge = 100
        elif miles > 1500:
            flatMileCharge = 200
            mileageCharge = 0.25 # For every mile past 1500
        print("Rental period (weeks): ", weeksRented)
        print("Odometer reading at start: ", startMile)
        print("Odometer reading at end: ", endMile)
        print("Number of Miles Driven: ", miles)
