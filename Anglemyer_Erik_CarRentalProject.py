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