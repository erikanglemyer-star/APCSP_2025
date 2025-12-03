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

direction = random.choice(["H", "V"]) # Randomly choose horizontal (H) or vertical (V)
print(direction) # Prints either 'H' or 'V'

row = random.randint(0, 9) # Random row between 0 and 9
col = random.randint(0, 9) # Random column between 0 and 9
print(row, col) # Prints a random position, e.g. 3, 7
print(grid[row][col] == " ")