def userProfile(name, color):
    lenName = len(name)
    lenColor = len(color)
    print("Hello, " + str(name) + "! Your favorite color is " + str(color) + ".")
    print("Your name has " + str(lenName) + " letters, and your color has " + str(lenColor) + " letters as well.")

name = input("Please enter your name: ")
color = input("Please enter your favorite color: ")
userProfile(name, color)
