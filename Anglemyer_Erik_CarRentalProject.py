print("Welcome to the Car Rental Charge Calculator!") # Prints a welcome message

def checkPosInt(check, command): # Function that checks if the number inputted is a positive integer
    while True:
        check = input("Please enter " + command + ": ")
        try:
            check = int(check) # Checks if its a integer
            if check > 0: # Checks if its positive
                break
            else:
                print("Please enter a valid number.")
        except:
            print("Please enter a valid number.")
    return check # If its a positive integer it returns the value

def checkPos(check, command): # Function that checks if the input is a positive number
    while True:
        check = input("Please enter " + command + ": ")
        try:
            check = float(check) # Makes sure its a number
            if check > 0: # Checks if its positive
                break
            else:
                print("Please enter a valid number.")
        except:
            print("Please enter a valid number.")
    return check

while True: # Loop for the Car Rental Calculator
    # Ask user for their car classification code and check to make sure its valid
    code = ""
    check = ""
    while code != "d" and code != "b" and code != "w" and code != "q":
        code = input("Please enter your car classification code (Q to quit): ").lower()
        if code == "d" or code == "b" or code == "w" or code == "q":
            break
        else:
            print("Please enter a valid code.")
    if code == "q":
        print("Thank you for using the Car Rental Charge Calculator.") # Gracefully quit if the user inputs q or Q
        break
    code = code.upper()

    # Asks how many days or weeks the car is rented depending on the classification
    if code == "W":
        weeksRented = checkPosInt(check, "the number of weeks rented")
    else:
        daysRented = checkPosInt(check, "the number of days rented")
        if daysRented == 1: # Makes sure grammar is correct
            dayDays = "day"
        else:
            dayDays = "days"
    
    startMile = checkPos(check, "the odometer reading at start") # Gets starting odometer reading

    while True: # Gets a valid ending odometer reading
        endMile = checkPos(check, "the odometer reading at end")
        if endMile < startMile:
            print("Please enter a higher ending mileage reading than starting.")
        else:
            break
    
    miles = endMile - startMile # Calculates how many miles the user drove
    
    # Print Receipt
    print("Customer Classification code: ", code)

    if code == "B": # Calculates and prints receipt for B classification
        baseCharge = 40 # per day
        mileageCharge = 0.25 # per mile
        total = daysRented * baseCharge + miles * mileageCharge
        print("Rental period (days):", daysRented)
        print("Odometer reading at start:", startMile)
        print("Odometer reading at end:", endMile)
        print("Number of Miles Driven:", miles)
        print("Base Charge: $" + str("{:.2f}".format(baseCharge)) + "/day x " + str(daysRented) + " " + dayDays + " = $" + str("{:.2f}".format(baseCharge * daysRented)))
        print("Mileage Charge: $" + str("{:.2f}".format(mileageCharge)) + "/mile x " + str(miles) + " miles = $" + str("{:.2f}".format(mileageCharge * miles)))
        print("Total Amount Due: $" + str("{:.2f}".format(total)))

    
    if code == "D": # Calculates and prints receipt for D classification
        baseCharge = 60 # per day
        mileageCharge = 0.25 # Free for up to 100 miles per day, then per mile
        freeMiles = 100 # per day
        paidMiles = miles - daysRented * freeMiles
        if paidMiles < 0:
            paidMiles = 0
        total = paidMiles * mileageCharge + baseCharge * daysRented
        print("Rental period (days):", daysRented)
        print("Odometer reading at start:", startMile)
        print("Odometer reading at end:", endMile)
        print("Number of Miles Driven:", miles)
        print("Base Charge: $" + str("{:.2f}".format(baseCharge)) + "/day x " + str("{:.2f}".format(daysRented)) + " " + dayDays + " = $" + str("{:.2f}".format(baseCharge * daysRented)))
        print("Mileage Charge: First " + str(daysRented * freeMiles) + " miles free (100 miles/day), Extra " + str(paidMiles) + " miles x $" + str("{:.2f}".format(mileageCharge)) + " = $" + str("{:.2f}".format(paidMiles * mileageCharge)))
        print("Total Amount Due: $" + str("{:.2f}".format(total)))

    if code == "W": # Calculates and prints receipt for W classification
        baseCharge = 190 # per week
        baseMilesFree = 900 * weeksRented
        maxMiles = 1500 * weeksRented
        flatMileCharge = 0
        mileageCharge = 0
        if miles >= baseMilesFree and miles <= maxMiles:
            mileageCharge = 0 
            flatMileCharge = 100 * weeksRented
        elif miles > maxMiles:
            flatMileCharge = 200 * weeksRented
            mileageCharge = 0.25 # For every mile past 1500
        if weeksRented == 1: # Ensures grammar is correct
            weekWeeks = "week"
        else:
            weekWeeks = "weeks"
        total = (miles - maxMiles) * mileageCharge + weeksRented * baseCharge + flatMileCharge
        print("Rental period (weeks):", weeksRented)
        print("Odometer reading at start:", startMile)
        print("Odometer reading at end:", endMile)
        print("Number of Miles Driven:", miles)
        print("Base Charge: $" + str("{:.2f}".format(baseCharge)) + "/week x " + str("{:.2f}".format(weeksRented)) + " " + weekWeeks + " = $" + str("{:.2f}".format(weeksRented * baseCharge)))
        print("Mileage Charge: First " + str(baseMilesFree) + " miles free, Next " + str(600 * weeksRented) + " miles: $100.00. Your charge = " + str("{:.2f}".format(flatMileCharge * weeksRented)))
        if miles > maxMiles:
            print("Extra " + str(miles-maxMiles) + " miles ($0.25 per mile): $" + str("{:.2f}".format((miles - maxMiles) * mileageCharge)))
        print("Total Amount Due: $" + str("{:.2f}".format(total)))