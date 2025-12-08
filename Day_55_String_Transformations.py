print("Welcome to the Text Reverser and Mirrorer!")
print("You will enter a word or sentence, and we'll show you some fun transformations.\n")

# Step 1: Get user input
text = input("Enter a word or sentence: ")

# Step 2: Reverse the text using a for loop and accumulator pattern
reversed_text = "" # Initialize the accumulator variable
for char in text: # Step through each character in the text
    reversed_text = char + reversed_text # Add each character to the beginning of the accumulator

# Display the reversed text
print("\nReversed Text: " + reversed_text)

# Step 3 Create a mirrored version of the text
mirrored_text = text + reversed_text # Combine the original text and the reversed text

# Display the mirrored text
print("Mirrored Text: " + mirrored_text)

# Step 4: Modify the reversed text using a while loop to capitalize alternating characters
modified_text = "" # Initialize another accumulator variable
index = 0 # Counter to track the position of each character
while index < len(reversed_text): # Loop while the index is within the range of the text
    if index % 2 == 0: # Check if the index is even
        modified_text += reversed_text[index].upper() # Capitalize the character if the index is even
    else:
        modified_text += reversed_text[index].lower() # Make the character lowercase if the index is odd
    index += 1 # Increment the counter

# Display the modified reversed text
print("Modified Reversed Text: " + modified_text)
print("\nThank you for exploring text transformations with Python!")