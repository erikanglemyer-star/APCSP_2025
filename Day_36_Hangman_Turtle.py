import turtle

original_text = "Let's Draw a Hangman Game Board!"
print("Original text:", original_text)

lower_text = original_text.lower()
print("Lowercase text:", lower_text)

my_screen = turtle.Screen()
my_screen.bgcolor("lightyellow")

my_turtle = turtle.Turtle()

my_turtle.color("black")
my_turtle.pensize(5)

my_turtle.penup()
my_turtle.goto(-150, -100)
my_turtle.pendown()
my_turtle.forward(300)

my_turtle.penup()
my_turtle.goto(-100, -100)
my_turtle.pendown()
my_turtle.left(90)
my_turtle.forward(200)

my_turtle.right(90)
my_turtle.forward(100)

my_turtle.right(100)
my_turtle.forward(40)

my_turtle.circle(20)

my_screen.exitonclick()
