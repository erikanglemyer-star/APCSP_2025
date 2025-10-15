import turtle

screen = turtle.Screen()
screen.title("The Nested Target")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("black")

pen.penup()
pen.goto(-100,-100)

pen.pendown()
pen.setheading(90)
pen.forward(200)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(200)

pen.penup()
pen.goto(0, 50)
pen.pendown()
pen.circle(50)

screen.mainloop()



