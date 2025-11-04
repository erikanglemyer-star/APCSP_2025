import turtle
screen = turtle.Screen()
screen.bgcolor("lightgreen")
turtle.setup(width=800, height=800)
t = turtle.Turtle()
xPos = [250, 250, -125, -125]
yPos = [-250, 110, -250, 110]
color = ["blue", "green", "pink", "red"]
spotColor = ["orange", "white", "purple", "black"]

for i in range(4):
    t.setheading(0)
    t.pensize(2)
    t.penup()
    t.goto(xPos[i]-100, yPos[i]-50)
    t.pendown()
    t.fillcolor(color[i])
    t.begin_fill()
    t.circle(110) # Draw a larger body as a circle
    t.end_fill()
    t.penup()
    t.goto(xPos[i]-100, yPos[i]+150) # PosiIon for the head
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(40) # Draw the head
    t.end_fill()
    t.penup()
    t.goto(xPos[i]-100, yPos[i]+150)
    t.setheading(-90)
    t.pendown()
    t.pensize(3)
    t.forward(200) # Line separaIng the body

    spots_posiIons = [(xPos[i]-50, yPos[i]+50), (xPos[i]+50, yPos[i]+50), (xPos[i]-75, yPos[i]), (xPos[i]+75, yPos[i]), (xPos[i]-50, yPos[i]-50), (xPos[i]+50, yPos[i]-50)]
    for spot_x, spot_y in spots_posiIons:
        t.penup()
        t.goto(-115 + spot_x, 60 + spot_y)
        t.pendown()
        t.pencolor(spotColor[i])
        t.fillcolor(spotColor[i])
        t.begin_fill()
        t.circle(15) # Draw the spots
        t.end_fill()

    legs_posiIons = [(xPos[i]-90, 50), (xPos[i]-110, 0), (xPos[i]-102, -50)]
    for leg_x, leg_y in legs_posiIons:
        t.pencolor("black")
        t.penup()
        t.goto(-100 + leg_x, 75 + leg_y + yPos[i])
        t.pendown()
        t.setheading(-150) # Adjust leg direcIon
        t.forward(50) # Draw the legs
        t.penup()

    right_legs = [(xPos[i]+90, 50), (xPos[i]+110, 0), (xPos[i]+102, -50)]
    for leg_x, leg_y in right_legs:
        t.penup()
        t.goto(-100 + leg_x, 75 + leg_y + yPos[i])
        t.pendown()
        t.setheading(-40) # Adjust leg direcIon
        t.forward(50) # Draw the legs
        t.penup()

    t.goto(xPos[i]-100, yPos[i]+230) # LeY antenna posiIon
    t.setheading(60)
    t.pendown()
    t.forward(60)
    t.penup()
    t.goto(xPos[i]-100, yPos[i]+230)
    t.setheading(120)
    t.pendown()
    t.forward(60)

t.hideturtle()
screen.exitonclick()