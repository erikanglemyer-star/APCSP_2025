intro_message = "Dogs are loyal and friendly animals!"

print("Original message:", intro_message)

has_dog = input("Do you have a dog? (yes or no): ").lower()

if has_dog == "yes":
    dog_name = input("What is your dog's name? ")
    dog_info = intro_message + " Your dog's name is " + dog_name + "."
    print(dog_info)

    dog_age = input("How old is your dog? ")
    dog_age_message = "Your dog is " + dog_age + " years old."
    print(dog_age_message)

    lowercase_message = intro_message.lower()
    print("Lowercase message:", lowercase_message)

    capitalized_message = intro_message.capitalize()
    print("Capitalized message:", capitalized_message)

    message_length = len(intro_message)
    print("The length of the message is:", message_length)

    find_dogs = intro_message.find("Dogs")
    print("The word 'Dogs' starts at index:", find_dogs)

    try:
        intro_message[0] = "C"
    except TypeError as e:
        print("Error! Strings are immutable:", e)

    sliced_message = intro_message [0:4]
    print("Sliced message (first 4 characters):", sliced_message)

    slice_from_middle = intro_message[13:]
    print("Sliced from index 13 to the end:", slice_from_middle)

else:
    print("That's okay! Dogs are still wonderful animals to learn about!")

print("The original message remains unchanged:", intro_message)