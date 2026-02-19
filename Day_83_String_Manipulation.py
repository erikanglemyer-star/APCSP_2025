def decode_message(message, keyword):
    words = message.split(" ") # Splitting message into words
    keyword_index = message.find(keyword) # Finding the keyword in the message

    if keyword_index == -1:
        return "Keyword not found in message."

    first_word = words[0] # Accessing the first word using index
    last_word = words[-1] # Accessing the last word using index

    keyword_slice = message[keyword_index:keyword_index + len(keyword)] # Extracting keyword using slice

    print("\nDecoding Results:")
    print(f"First word in the message: {first_word}")
    print(f"Last word in the message: {last_word}")
    print(f"Extracted keyword: {keyword_slice}")

    words.remove(keyword) # Removing the keyword from the list
    new_message = " ".join(words) # Reconstructing the new message

    print("\nNew Message (After Extraction):")
    print(new_message)

    scrambled_words = words[::-1] # Reversing the list of words
    print("\nScrambled Message (Words Reversed):")
    print(" ".join(scrambled_words)) # Joining the words back into a string

# Get user input for coded message
message = input("Enter a coded message: ")
keyword = input("Enter a keyword to extract: ")

decode_message(message, keyword)