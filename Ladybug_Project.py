import turtle
screen = turtle.Screen()
screen.bgcolor("lightgreen")
turtle.setup(width=600, height=600)
t = turtle.Turtle()
t.pensize(2)
t.penup()
t.goto(-100, -50)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(110) # Draw a larger body as a circle
t.end_fill()
t.penup()
t.goto(-100, 150) # PosiIon for the head
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(40) # Draw the head
t.end_fill()
t.penup()
t.goto(-100, 150)
t.setheading(-90)
t.pendown()
t.pensize(3)
t.forward(200) # Line separaIng the body
spots_posiIons = [(-50, 50), (50, 50), (-75, 0), (75, 0), (-50, -50), (50, -50)]
for spot_x, spot_y in spots_posiIons:
    t.penup()
    t.goto(-115 + spot_x, 60 + spot_y)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(15) # Draw the spots
    t.end_fill()
legs_posiIons = [(-100, 50), (-100, 0), (-100, -50)]
for leg_x, leg_y in legs_posiIons:
    t.penup()
    t.goto(-100 + leg_x, 75 + leg_y)
    t.pendown()
    t.setheading(leg_x-40) # Adjust leg direcIon
    t.forward(50) # Draw the legs
    t.penup()
right_legs = [(100, 50), (100, 0), (100, -50)]
for leg_x, leg_y in right_legs:
    t.penup()
    t.goto(-100 + leg_x, 75 + leg_y)
    t.pendown()
    t.setheading(-40) # Adjust leg direcIon
    t.forward(50) # Draw the legs
    t.penup()
t.goto(-100, 230) # LeY antenna posiIon
t.setheading(60)
t.pendown()
t.forward(60)
t.penup()
t.goto(-100, 230)
t.setheading(120)
t.pendown()
t.forward(60)
t.hideturtle()
screen.exitonclick()