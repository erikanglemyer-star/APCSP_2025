import time

time_left = 5

print("Welcome to the Escape Room Timer!")
print("You have 5 minutes to complete the challenge.")
print("Type 'exit' anytime to stop the timer.\n")

while time_left > 0:
    print("Time left:", time_left, "minutes")
    user_input = input("Press Enter to continue or type 'exit' to stop: ").lower
    if user_input == "exit":
        print("You chose to exit the timer.")
        break
    time_left -= 1
if time_left == 0:
    print("\nTime's up!")

print("\nNow, let's look at the clues to solve the escape room!")

clues = [
    "The first key is hidden under the table.",
    "Look for a red book on the bookshelf.",
    "The combination for the lock is the year the school was founded.",
    "Check the drawer for a flashlight.",
    "Use the flashlight to reveal the hidden message on the wall."
]

print("\nHere are your clues:\n")

clue_number = 1
for clue in clues:
    print("Clue " + str(clue_number) + ": " + clue)
    clue_number += 1