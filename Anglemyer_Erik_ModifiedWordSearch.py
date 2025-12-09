import random # Imports the random module
import string # Imports the string module

wordsList = [] # Empty list that the user can add to
letters = string.ascii_lowercase
subject = input("Please enter a subject: ")
while True:
    gridSize = input("Please enter the size of your wordsearch (integer): ")
    try:
        gridSize = int(gridSize)
        break
    except:
        print("Please enter a valid size.") # Detects if the input is an integer and tells the user to reinput if not

for i in range(gridSize): # Loops the inputted number of times
    while True:
        valid = True
        wordsList.append(input("Please enter a word related to your subject: ").lower()) # Adds the users word to the list
        for char in wordsList[i]:
            if char not in string.ascii_letters: # Detects if the user inputted only letters
                print("Please enter only letters in your words.")
                valid = False
                break
        if len(wordsList[i]) - 1 >= gridSize:
            print("One or more of your words have too many characters.") # Detects if the word will not fit in the grid
            valid = False
        if valid == True:
            break
        else:
            wordsList.pop()


print("Here are your words: ", wordsList)

while True:
    grid = []
    failed = False
    for i in range(gridSize): # Create inputted number of rows
        row = [" "] * gridSize # Each row has the given number of spaces
        grid.append(row) # Add the row to the grid

    # Iterates through each word in the list
    # If the word doesnt work in the randomly generated position, it retries
    for i in range(gridSize):
        attempts = 0
        success = False
        while True:
            attempts += 1
            wordLength = len(wordsList[i]) # Rolls the first letter
            row = random.randint(0, gridSize - 1) # Random row between 0 and inputted size - 1
            col = random.randint(0, gridSize - 1) # Random column between 0 and inputted size - 1
            direction = random.choice(["H", "V"]) # Randomly choose horizontal (H) or vertical (V)
            while col + wordLength > gridSize and direction == ("H"):
                row = random.randint(0, gridSize - 1) # Pick a new number
                col = random.randint(0, gridSize - 1) # Pick a new number
            while row + wordLength > gridSize and direction == ("V"):
                row = random.randint(0, gridSize - 1) # Pick a new number
                col = random.randint(0, gridSize - 1) # Pick a new number
            x = 0
            taken = False
            for char in wordsList[i]:    # Places every letter in the word allowing for overlap between same letters
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
                if attempts < 100: # Program can retry up to 100 times, then it restarts the whole grid
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
    if i == gridSize - 1 and success: # Fills in the empty spaces with random letters
        for row_index in range(gridSize):
            for col_index in range(gridSize): 
                if grid[row_index][col_index] == " ":
                    grid[row_index][col_index] = random.choice(letters)
        break
    


for i in range(gridSize): # Prints the grid
    print(grid[i], "\n")
        