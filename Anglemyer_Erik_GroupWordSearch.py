import random # Imports the random module

wordsList = [] # Empty list that the user can add to

subject = input("Please enter a subject: ")

for i in range(10): # Loops 10 times
    wordsList.append(input("Please enter a word related to your subject: ")) # Adds the users word to the list

print("Here are your words: ", wordsList)

grid = []
for i in range(10): # Create 10 rows
    row = [" "] * 10 # Each row has 10 spaces
    grid.append(row) # Add the row to the grid
for i in range(10):
    print(grid[i], "\n") # Prints a grid as a list of lists with each entry on its own line

# Do a loop iterating through each word in the list
# if it doesnt fit, redo with the same i. 
for i in range(10):
    while True:
        character = 0
        wordLength = len(wordsList[i]) # Rolls the first letter
        print(wordLength)
        row = random.randint(0, 9) # Random row between 0 and 9
        col = random.randint(0, 9) # Random column between 0 and 9
        direction = random.choice(["H", "V"]) # Randomly choose horizontal (H) or vertical (V)
        print("Rolled coords: ", row, col, direction)
        while row + wordLength >= 10 and direction == ("H"):
            row = random.randint(0, 9) # Pick a new number
            col = random.randint(0, 9) # Pick a new number
            print("Rerolled coords: ", row, col, direction)
        while col + wordLength >= 10 and direction == ("V"):
            row = random.randint(0, 9) # Pick a new number
            col = random.randint(0, 9) # Pick a new number
            print("Rerolled coords: ", row, col, direction)
        x = 0
        taken = False
        for char in wordsList[i]:    # Places every letter in the word
            if direction == ("V"):
                if grid[row][col + x] != " ":
                    taken = True
            else:
                if grid[row + x][col] != " ":
                    taken = True
        if taken:
            break

        x = 0
        for char in wordsList[i]:    # Places every letter in the word
            if direction == ("V"):
                grid[row][col + x] = char
            else:
                grid[row + x][col] = char
            x += 1

for i in range(10):
    print(grid[i], "\n")
        


