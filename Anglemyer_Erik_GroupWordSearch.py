import random # Imports the random module
import string # Imports the string module

wordsList = [] # Empty list that the user can add to
letters = string.ascii_lowercase
subject = input("Please enter a subject: ")

for i in range(10): # Loops 10 times
    while True:
        valid = True
        wordsList.append(input("Please enter a word related to your subject: ").lower()) # Adds the users word to the list
        for char in wordsList[i]:
            if char not in string.ascii_letters:
                print("Please enter only letters in your words.")
                valid = False
                break
        if len(wordsList[i]) >= 10:
            print("One or more of your words have too many characters.")
            valid = False
        if valid == True:
            break
        else:
            wordsList.pop()

print("Here are your words: ", wordsList)

while True:
    grid = []
    failed = False
    for i in range(10): # Create 10 rows
        row = [" "] * 10 # Each row has 10 spaces
        grid.append(row) # Add the row to the grid

    # Do a loop iterating through each word in the list
    # if it doesnt fit, redo with the same i. 
    for i in range(10):
        attempts = 0
        success = False
        while True:
            attempts += 1
            wordLength = len(wordsList[i]) # Rolls the first letter
            row = random.randint(0, 9) # Random row between 0 and 9
            col = random.randint(0, 9) # Random column between 0 and 9
            direction = random.choice(["H", "V"]) # Randomly choose horizontal (H) or vertical (V)
            while col + wordLength > 10 and direction == ("H"):
                row = random.randint(0, 9) # Pick a new number
                col = random.randint(0, 9) # Pick a new number
            while row + wordLength > 10 and direction == ("V"):
                row = random.randint(0, 9) # Pick a new number
                col = random.randint(0, 9) # Pick a new number
            x = 0
            taken = False
            for char in wordsList[i]:    # Places every letter in the word
                if direction == ("V"):
                    if grid[row + x][col] != " " and grid[row + x][col] != char:
                        taken = True
                        break
                else:
                    if grid[row][col + x] != " " and grid[row][col + x] != char:
                        taken = True
                        break
                x = x + 1
            if taken:
                if attempts < 100:
                    continue
                else:
                    success = False 
                    failed = True
                    break
            x = 0
            for char in wordsList[i]:    # Places every letter in the word
                if direction == ("V"):
                    grid[row + x][col] = char
                else:
                    grid[row][col + x] = char
                x += 1
            success = True
            break
        if failed:
            break
    if failed:
        continue
    if i == 9 and success:
        for row_index in range(10):
            for col_index in range(10):
                if grid[row_index][col_index] == " ":
                    grid[row_index][col_index] = random.choice(letters)
        break
    


for i in range(10):
    print(grid[i], "\n")
        