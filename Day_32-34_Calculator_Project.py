#Defines the wantStop variable
wantStop = "no"

#Prints a welcome message
print("Welcome to the 2 Number Four Function Calculator!")

#Main calculator loop
while wantStop.lower() != "yes": #If the user doesn't say they want the program to stop, it will loop
    #Prompts user to enter valid numbers
    while True:
        num1 = input("Please enter your first number (integer or decimal): ")
        num2 = input("Please enter your second number (integer or decimal): ")
        try:
            num1 = float(num1)
            num2 = float(num2)
            break
        except:
            print("Please enter valid numbers.")
            continue
    #Performs Calculations
    print("The sum of the first and second number is: ", num1 + num2)
    print("The difference of the first and second number is: ", num1 - num2)
    print("The product of the first and second number is: ", num1 * num2)
    if num2 == 0: #stops division by 0 error
        print("Error: division by 0")
    else:
        print("The quotient of the first and second number is: ", num1 / num2)
        print("The remainder of the first and second number is: ", num1 % num2)
    wantStop = input("Would you like to stop calculating? (type yes to end, anything else to continue): ") 
