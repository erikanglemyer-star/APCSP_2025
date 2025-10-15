print("Welcome to the Simple Calculator Program!")

#Assigns initial values
num1 = 10
num2 = 5
operation = "addition"


#Prints initial values
print("Initial values:")
print("Number 1:", num1)
print("Number 2:", num2)
print("Operation:", operation)


#Prompts the user to enter new values
num1 = int(input("Enter a new value for Number 1: "))
num2 = int(input("Enter a new value for Number 2: "))
operation = (input("Enter an operation (addition, subtraction, multiplication, division): "))


#Checks the value of the operation value
if operation == "addition":
    result = num1 + num2
elif operation == "subtration":
    result = num1 - num2
elif operation == "multiplication":
    result = num1 * num2
elif operation == "division":
    result = num1 / num2
else:
    result = None
    print("Invalid operation entered.")


#Prints the result of the operation
if result is not None:
    print("The result of the operation is:", result)


#Reassigns values and prints the updated values
num1 = result
num2 = num2 * 2
print("Updated values after reassignment")
print("Number 1 (result of previous operation):", num1)
print("Number 2 (doubled):", num2)