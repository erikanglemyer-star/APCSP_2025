print("Welcome to the Palindrome Challenge!")

# Function to generate a palindrome
def generate_palindrome(word):
    #nReverse the text using a for loop and accumulator pattern
    reversed_text = "" # Initialize the accumulator variable
    for char in word: # Step through each character in the text
        reversed_text = char + reversed_text # Add each character to the beginning of the accumulator
    palindrome = word + reversed_text
    return palindrome

while True:
    if input("Would you like to generate a palindrome? (type yes to create one or anything else to quit) ").lower() == "yes":
        print(generate_palindrome(input("Please enter the word you would like to convert: ")))
    else:
        break


print("Think of as many palindromes as you can. If you can't think of any more, type 'quit' to stop.\n")

# Function to check if a string is a palindrome:
def is_palindrome(word):
    reversed_word = "" # Initialize accumulator for the reversed word
    for char in word:
        reversed_word = char + reversed_word # Add each character to the beginning
    return word.lower() == reversed_word.lower() # Compare original and reversed (ignoring case)

# Initialize variables
score = 0 # Tracks the score
attempts = [] # List to store all attempted palindromes
while True:
    user_input = input("Enter a word you think is a palindrome (or type 'quit if you can't think of any more palindromes): ").strip()

    if user_input.lower() == "quit": # Checks if the user wants to quit
        print("\n You chose to quit the game.")
        break

    if user_input in attempts:
        print("You already tried this word. Try a different one!")
        continue # Skip to the next iteration

    # Add the input to the list of attempts
    attempts.append(user_input)

    # Check if the word is a palindrome
    if is_palindrome(user_input):
        print("'" + user_input + "' is a palindrome! Great job!")
        score += 1
    else:
        print("'" + user_input + "' is not a palindrome. Keep trying!")

# Display the final score
print("\nGame over! Your final score is " + str(score))
print("Here are all the words you attempted:")
for attempt in attempts:
    print("- " + attempt)

print("\nThank you for playing the Palindrome Challenge!")