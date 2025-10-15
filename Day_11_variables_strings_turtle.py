import turtle

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
favorite_color = input("Enter your favorite color: ")
favorite_food = input("Enter your favorite food: ")


full_name = first_name + " " + last_name

personal_message = ("Hello, " + full_name + "!" + 
                    " Its great to know that your favorite color is " +
                    favorite_color + " and you love eating " +
                    favorite_food + ".")

print(personal_message)

screen = turtle.Screen()
screen.title("Personalized Message")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("black")

pen.penup()
pen.goto(0, 0)
pen.write(personal_message, align="center", font=("Arial", 16, "normal"))

screen.mainloop()