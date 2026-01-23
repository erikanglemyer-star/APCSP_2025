# Welcome the user
print("Welcome to the 2026 Olympics Travel Planner!")
venues = ["milan", "valtellina", "cortina", "cortina d'ampezzo", "val di fiemme", "val"]
# Checks to see if the input is a valid venue
def checkLocation(venue):
    venue = str(venue)
    venue = venue.lower()
    while True:
        if venue.lower() in venues:
            return venue
        else:
            venue = input("Invalid venue entered, please try again. (Milan, Valtellina, Cortina d'Ampezzo, Val di Fiemme): ")
        
# Get user location and destination
start = checkLocation(input("Which venue are you at currently? (Milan, Valtellina, Cortina d'Ampezzo, Val di Fiemme): "))
destination = checkLocation(input("Which venue would you like to travel to? (Milan, Valtellina, Cortina d'Ampezzo, Val di Fiemme): "))