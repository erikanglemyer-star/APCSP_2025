from PIL import Image
import requests
from io import BytesIO

import turtle

my_screen = turtle.Screen()
my_screen.bgcolor("black")
routeArrow = turtle.Turtle()
my_screen.addshape(ezgif-2e7d39cf577b9f66.gif) # Register the GIF shape
routeArrow = turtle.Turtle()
routeArrow.shape(gif_path)
routeArrow.penup()
routeArrow.goto(0, 0)

# Welcome the user
print("Welcome to the 2026 Olympics Travel Planner!")
venues = ["milan", "valtellina", "cortina d'ampezzo", "val di fiemme"]
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
        
# Get user location and destination
destinationCheck = False
start = checkLocation(input("Which venue are you at currently? (Milan, Valtellina, Cortina d'Ampezzo, Val di Fiemme): "))
destinationCheck = True
destination = checkLocation(input("Which venue would you like to travel to? (Milan, Valtellina, Cortina d'Ampezzo, Val di Fiemme): "))