import os
os.system('cls' if os.name == 'nt' else 'clear')

user_number = input("Enter a whole number: ")

if not user_number.isdigit():
    print("Please enter a valid whole number.")


remainder = int(user_number) % 2

if remainder == 0:
    print("Your number is even.")
else: 
    print("Your number is odd.")