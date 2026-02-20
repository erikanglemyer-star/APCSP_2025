# Initialize the Story
# Get the story and split it into a list of words
story = input("Please input a story (minimum two sentences and 30 words): ")
keywords = []
newWords = []

story = story.split(" ")

# Identify the keywords the user wishes to change
# We did not use find() because find() works and outputs the index with strings. story is a list, so instead we used booleans, not in, to detect if the keyword is present in the list and worked with the index() function instead.
while len(keywords) < 5:
    keyword = input("Please enter a word in the story: ")
    if keyword not in story:
        print("Word not found in the story. Please try again.")
    else:
        keywords.append(keyword)

# Replace the keywords with new words, modify the narrative
for i in range(5):
    newWord = input("Please enter a replacement word: ")
    while keywords[i] in story:
        story.insert(story.index(keywords[i]), newWord)
        story.remove(keywords[i])

# Reconstruct the story and display
story = " ".join(story)
print(story)
