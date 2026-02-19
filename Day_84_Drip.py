story = input("Please input a story (minimum two sentences and 30 words): ")
keywords = []
newWords = []

while len(keywords) < 5:
    keyword = input("Please enter a word in the story: ")
    if story.find(keyword) == -1:
        print("Word not found in the story. Please try again.")
    else:
        keywords.append(keyword)

for i in range(5):
    newWord = input("Please enter a replacement word: ")
