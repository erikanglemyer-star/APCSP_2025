print("Welcome to the Car Rental Charge Calculator!")

while True:
    code = ""
    while code != "g" and code != "b" and code != "w" and code != "q":
        code = input("Please enter your car classification code (Q to quit): ").lower()
        if code == "g" or code == "b" or code == "w" or code == "q":
            break
        else:
            print("Please enter a valid code.")
    if code == "q":
        break
    code = code.upper()

    while True:
        daysRented = input("Please enter how many days the car was rented: ")
        try:
            daysRented = int(daysRented)
            break
        except:
            print("Please enter a valid number of days.")

    


