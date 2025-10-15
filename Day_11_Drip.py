import turtle

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
favorite_animal = input("Enter your favorite animal: ")

full_name = first_name + " " + last_name

personal_message = ("Hello " + full_name + ". Your favorite animal is a " + favorite_animal + ".")

print(personal_message)

screen = turtle.Screen()
screen.title = ("Personal Message <3")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("black")

pen.penup()
pen.goto(0,0)
pen.write(personal_message, align="center", font=("Arial", 16, "normal"))

screen.mainloop()