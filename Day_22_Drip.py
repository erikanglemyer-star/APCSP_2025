print("Welcome to the Simple Volume Calculator!")

#Assigns initial values
length = 6
width = 7
height = 9

print("The initial value of length is:", length)
print("The initial value of width is:", width)
print("The initial value of height is:", height)

length = int(input("Please enter the length of the rectangular prisim: "))
width = int(input("Please enter the width of the rectangular prisim: "))
height = int(input("Please enter the height of the rectangular prisim: "))

volume = length * width * height

print("The volume of the rectangular prism is:", volume)

length = volume
width = width * 2
height = height - 5

print("The updated values of the operation are:")
print("Length (the result of the previous operation):", length)
print("Width (doubled):", width)
print("Height (5 less):", height)