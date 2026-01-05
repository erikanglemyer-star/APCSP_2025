print("Welcome to the Car Rental Charge Calculator!")

def checkPosInt(check, command):
    while True:
        check = input("Please enter " + command + ": ")
        try:
            check = int(check)
            if check > 0:
                break
            else:
                print("Please enter a valid number of days.")
        except:
            print("Please enter a valid number of days.")
    return check

while True:
    code = ""
    check = ""
    while code != "g" and code != "b" and code != "w" and code != "q":
        code = input("Please enter your car classification code (Q to quit): ").lower()
        if code == "g" or code == "b" or code == "w" or code == "q":
            break
        else:
            print("Please enter a valid code.")
    if code == "q":
        break
    code = code.upper()

    daysRented = checkPosInt(check, "the number of days rented")
    
    startMile = checkPosInt(check, "the odometer reading at start")

    while True:
        endMile = checkPosInt(check, "the odometer reading at end")
        if endMile < startMile:
            print("Please enter a higher ending mileage reading than starting.")
        else:
            break



    


