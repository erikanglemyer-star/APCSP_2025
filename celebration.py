from PIL import Image #Uses pillow to import an image

def convert_to_gif(image_path): #defines a function to convert an image to a gif
    img = Image.open(image_path)
    gif_path = "converted_image.gif"
    img.save(gif_path, format="GIF")
    return gif_path

image_path = input("Enter the path to an image (JPG, PJEP, PNG, or GIF) for the background: ").strip() #prompts user to provide their image
if image_path.lower().endswith(('.jpg', '.jpeg', '.png')): 
    gif_path = convert_to_gif(image_path) #If it is a JPG, JPEG, or PNG, converts it to a GIF
else:
    gif_path = image_path # Assume it's already a GIF if not a JPG, JPEG, or PNG

import turtle
import random as celebrations # Renaming random library for thematc purposes

screen = turtle.Screen()
screen.title("Fall Celebrations")
screen.bgcolor('black') #Sets up screen

# Set background GIF if a path is provided
if gif_path:
    try:
        screen.addshape(gif_path) # Register the GIF shape
        background_turtle = turtle.Turtle()
        background_turtle.shape(gif_path)
        background_turtle.penup()
        background_turtle.goto(0, 0)
    except turtle.TurtleGraphicsError:
        print("Error: The file could not be loaded. Please ensure it's a valid .gif file.")
 # Create a turtle for text

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

def diwali():
    return ["Light diyas", "Prepare sweets", "Fireworks", "Family gathering"]
def thanksgiving():
    return ["Cook a turkey", "Family dinner", "Express gratitude", "Watch a parade", "Watch football"]
def day_of_the_dead():
    return ["Visit graves", "Make sugar skulls", "Create altars", "Share family stories"]
def guy_fawkes_day():
    return ["Bonfires", "Fireworks", "Burning effigies", "Sing traditional songs"]
def st_andrews_day():
    return ["Ceilidh dancing", "Traditional Scomsh meal", "ADend events", "CelebrateScomsh culture"]
def remembrance_day():
    return ["Attend ceremonies", "Moment of silence", "Wear poppies", "Thank veterans"]
def mid_autumn_festival():
    return ["Family reunion", "Eat mooncakes", "Moon worship", "Lantern lighting"]
def yom_kippur():
    return ["Day of fasting", "Attend synagogue services", "Reflect on past actions", "Seek forgiveness"]
def rosh_hashanah():
    return ["Attend synagogue services", "Blow the shofar", "Eat symbolic foods like apples and honey", "Pray for a good year ahead"]
def halloween():
    return ["Dress up in costumes, Trick or treat, Attend Halloween parties, Watch scary movies"] #Bonus Task: Adding a Fall Holiday Function

# Dictionary linking each holiday's name to its function
holiday_functions = {
    "Diwali": diwali,
    "Thanksgiving": thanksgiving,
    "Day of the Dead": day_of_the_dead,
    "Guy Fawkes Day": guy_fawkes_day,
    "St. Andrew's Day": st_andrews_day,
    "Remembrance Day": remembrance_day,
    "Mid-Autumn Festival": mid_autumn_festival,
    "Yom Kippur": yom_kippur,
    "Rosh Hashanah": rosh_hashanah,
    "Halloween": halloween #Bonus Task: Adding a Fall Holiday Function
}

def display_activities(holiday_name):
    if holiday_name in holiday_functions:
        print("\nActivities for " + holiday_name + ":")
        activities = holiday_functions[holiday_name]() # Call the function to get activities
        for activity in activities:
            print("- " + activity)
    else:
        print(holiday_name + " is not in the list of holidays.") #If the holiday is not in the list, tell the user that nothing could be found

print("Do you celebrate any of the following holidays?") #Allows user to enter a holiday they celebrate
for holiday in holiday_functions.keys():
    print("- " + holiday)
user_holiday = input("\nIf you celebrate one of these holidays, please enter its name, or press Enter to skip: ").strip()
if user_holiday in holiday_functions:
    display_activities(user_holiday) # Display activities for the chosen holiday
else:
    print(user_holiday + " is not recognized as one of the holidays in our list.")
