import random # Imports the random module

wordsList = [] # Empty list that the user can add to

subject = input("Please enter a subject: ")

for i in range(10): # Loops 10 times
    wordsList.append(input("Please enter a word related to your subject: ")) # Adds the users word to the list


print("Here are your words: ", wordsList)

while True:
    grid = []
    print("New grid!")
    attempts = 0
    for i in range(10): # Create 10 rows
        row = [" "] * 10 # Each row has 10 spaces
        grid.append(row) # Add the row to the grid

    # Do a loop iterating through each word in the list
    # if it doesnt fit, redo with the same i. 
    for i in range(10):
        success = False
        if attempts >= 1000: 
            success = False
            break
        success = False
        while True:
            attempts += 1
            character = 0
            wordLength = len(wordsList[i]) # Rolls the first letter
            row = random.randint(0, 9) # Random row between 0 and 9
            col = random.randint(0, 9) # Random column between 0 and 9
            direction = random.choice(["H", "V"]) # Randomly choose horizontal (H) or vertical (V)
            while row + wordLength >= 10 and direction == ("H"):
                row = random.randint(0, 9) # Pick a new number
                col = random.randint(0, 9) # Pick a new number
            while col + wordLength >= 10 and direction == ("V"):
                row = random.randint(0, 9) # Pick a new number
                col = random.randint(0, 9) # Pick a new number
            x = 0
            taken = False
            for char in wordsList[i]:    # Places every letter in the word
                if direction == ("V"):
                    if grid[row][col + x] != " " and grid[row][col + x] != char:
                        taken = True
                        break
                else:
                    if grid[row + x][col] != " " and grid[row + x][col] != char:
                        taken = True
                        break
                x = x + 1
            if taken:
                if attempts < 1000:
                    continue
                else:
                    success = False 
                    break

            x = 0
            for char in wordsList[i]:    # Places every letter in the word
                if direction == ("V"):
                    grid[row][col + x] = char
                else:
                    grid[row + x][col] = char
                x += 1
            success = True
            break
    if i == 9 and success:
        break
    


for i in range(10):
    print(grid[i], "\n")
        