from PIL import Image

import turtle

gifPath = "/Users/27anglee/Downloads/ezgif-2e7d39cf577b9f66.gif"\

def createRoute():
    screen = turtle.Screen()
    screen.setup(width=400, height=300)
    screen.bgcolor("black")

    # Add the shape first
    screen.addshape(gifPath)

    # Then create the turtle and set its shape
    routeArrow = turtle.Turtle()
    routeArrow.shape(gifPath)
    routeArrow.penup()
    routeArrow.goto(0, 0)

    screen.exitonclick()

# All distances in km
DIST_MILAN_VALTELLINA = 203
DIST_MILAN_CORTINA = 411
DIST_MILAN_VAL = 293
DIST_VALTELLINA_CORTINA = 274
DIST_VALTELLINA_VAL = 223
DIST_CORTINA_VAL = 88

# Welcome the user
print("Welcome to the 2026 Olympics Travel Planner!")
venues = ["milan", "valtellina", "cortina d'ampezzo", "val di fiemme"]
conditions = ["snowy", "icy", "wet", "none"]
# Checks to see if the input is a valid venue
def checkLocation(venue):
    venue = str(venue)
    venue = venue.lower()
    while True:
        if venue.lower() in venues:
            if destinationCheck:
                if start.lower() != venue.lower():
                    return venue
                else:
                    venue = input("Invalid venue entered, please try again. (Milan, Valtellina, Cortina d'Ampezzo, Val di Fiemme): ")
            else:
                return venue
        else:
            venue = input("Invalid venue entered, please try again. (Milan, Valtellina, Cortina d'Ampezzo, Val di Fiemme): ")

def checkWeather(condition):
    condition = str(condition)
    condition = condition.lower()
    while True:
        if condition.lower() in conditions:
            return condition
        else:
            venue = input("Invalid conditions entered, please try again (snowy, icy, wet, none): ")
        
# Get user location and destination
destinationCheck = False
start = checkLocation(input("Which venue are you at currently? (Milan, Valtellina, Cortina d'Ampezzo, Val di Fiemme): "))
destinationCheck = True
destination = checkLocation(input("Which venue would you like to travel to? (Milan, Valtellina, Cortina d'Ampezzo, Val di Fiemme): "))

# Get distance based on user location and destination
if start.lower() == "milan":
    if destination.lower() == "valtellina":
        distance = DIST_MILAN_VALTELLINA
    elif destination.lower() == "cortina d'ampezzo":
        distance = DIST_MILAN_CORTINA
    else:
        distance = DIST_MILAN_VAL
elif start.lower() == "valtellina":
    if destination.lower() == "milan":
        distance = DIST_MILAN_VALTELLINA
    elif destination.lower() == "cortina d'ampezzo":
        distance = DIST_VALTELLINA_CORTINA
    else:
        distance = DIST_VALTELLINA_VAL
elif start.lower() == "cortina d'ampezzo":
    if destination.lower() == "milan":
        distance = DIST_MILAN_CORTINA
    elif destination.lower() == "valtellina":
        distance = DIST_VALTELLINA_CORTINA
    else:
        distance = DIST_CORTINA_VAL
else:
    if destination.lower() == "milan":
        distance = DIST_MILAN_VAL
    elif destination.lower() == "cortina d'ampezzo":
        distance = DIST_CORTINA_VAL
    else:
        distance = DIST_VALTELLINA_VAL

print("Your distance from your destination is " + str(distance) + " kilometers.")

# Get mountain road conditions
roadQuality = checkWeather(input("Please enter the mountain road conditions (snowy, icy, wet, none): "))

# Get mode of transport

# Calculate travel time based on distance, conditions, and transport

createRoute()