import turtle
import random as celebrations # Renaming random library for thematc purposes

# Set up the Turtle screen
screen = turtle.Screen()
screen.title("Fall Celebrations")
screen.bgcolor("black")

# Create a turtle for text
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.color("white")

# Draw "Let's Celebrate!" in large letters
text_turtle.penup()
text_turtle.goto(0, 150)
text_turtle.write("Let's Celebrate!", align="center", font=("Arial", 40, "bold"))

# Create a turtle for fireworks
fireworks = turtle.Turtle()
fireworks.speed(0)
fireworks.hideturtle()

# Draw fireworks effect
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]
for _ in range(30): # Draw 30 fireworks
    fireworks.penup()
    x = celebrations.randint(-200, 200)
    y = celebrations.randint(-200, 200)
    fireworks.goto(x, y)
    fireworks.pendown()
    # Choose a random color
    fireworks.color(celebrations.choice(colors))
    # Draw lines radiating from the point to create a firework effect
    for _ in range(12): # 12 lines per firework
        fireworks.forward(50)
        fireworks.backward(50)
        fireworks.right(30) # 360 degrees divided by 12 lines

screen.exitonclick()
