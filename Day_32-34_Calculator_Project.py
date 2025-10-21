wantStop = "no"
print("Welcome to the 2 Number Four Function Calculator!")

while wantStop.lower() != "yes":
    num1 = input("Please enter your first number (integer or decimal): ")
    num2 = input("Please enter your second number (integer or decimal): ")
    while True:
        try:
            num1 = float(num1)
            num2 = float(num2)
            break
        except:
            print("Please enter valid numbers.")
            continue
    print("The sum of the first and second number is: ", num1 + num2)
    print("The difference of the first and second number is: ", num1 - num2)
    print("The product of the first and second number is: ", num1 * num2)
    if num2 == 0:
        print("Error: division by 0")
    else:
        print("The quotient of the first and second number is: ", num1 / num2)
        print("The remainder of the first and second number is: ", num1 % num2)
    wantStop = input("Would you like to stop calculating? (type yes to end, anything else to continue): ")