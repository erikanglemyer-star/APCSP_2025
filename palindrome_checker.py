# Sends a greeting to the user
print("Welcome to the palindrome checker!")
print("A palindrome is a word that is spelled the same way forwards and backwards.")

# Gets user input
inputWord = input("What word would you like to check to see if it is a palindrome? ")
word = inputWord.lower()
word = word.replace(" ","")

# The function reversed() reverses the word and the function join() makes it a string
# Reverses user input
reversedWord = ''.join(reversed(word))

# Tests to see if it is a palindrome and communicates result
if reversedWord == word:
    print(inputWord.capitalize() + " is a palindrome. The word reads the same forwards and backwards.")
else:
    print(inputWord.capitalize() + " is not a palindrome. The word does not read the same forwards and backwards.")
