# Program: Field Trip Planner with Constraints
# This program determines if a filed trip to the scienec museum is affordable and ferasible.

# Input: User-provided budget, group size, meal preference, available time, and bus capacity

budget = float(input("Enter your group's total budget for the field trip (in dollars): $"))
group_size = int(input("Enter the number of students in the group: "))
meal_preference = input("Will the group eat at the museum? (yes or no): ").lower()
available_time = float(input("Enter the total time available for the trip (in hours): "))
bus_capacity = int(input("Enter the bus capacity (number of students it can hold): "))

# Constants
TICKET_COST = 15.00 # Cost per student ticket
DISCOUNT_THRESHOLD = 10 # Minimum group size for a discount
DISCOUNT_RATE = 0.2 # 20% discount for large groups
MEAL_COST = 8.50 # Cost per meal per student
TRIP_TIME_REQUIRED = 4.0 # Minimum time required for the trip (hours)

# Calculate the total ticket cost
if group_size >= DISCOUNT_THRESHOLD: # a >= b (True if a is greater or equal to b)
    ticket_cost = group_size * TICKET_COST * (1 - DISCOUNT_RATE)
    print("Your group qualifies for a 20% discount on tickets!")
else: # a < b (True if a is less than b)
    ticket_cost = group_size * TICKET_COST

# Calculate meal cost id the group plans toi eat at the museum
if meal_preference == "yes": # a == b (True if a is equal to b)
    meal_cost = group_size * MEAL_COST
    print("Meal cost for the group: $" + str(round(meal_cost, 2)))
else: # a != b  (True if a is not equal to b)
    meal_cost = 0
    print("No meal cost since the group will not eat at the museum.")

# Calculate the total cost
total_cost = ticket_cost + meal_cost
print("Total trip cost: $" + str(round(total_cost, 2)))

# Check time constraint
if available_time < TRIP_TIME_REQUIRED: # a < b (True if a is less than b)
    print("You do not have enough time for the trip. At least 4 hours are required.")
else: # a >= b (True if a is greater than or equal to b)
    print("You have enough time for the trip.")

# Check bus capacity constraint
if group_size > bus_capacity: # a > b (True if a is greater than b)
    print("The group size exceeds the bus capacity! You need a bigger bus or fewer students.")
else: # a <= b (True if a is less than or equal to b)
    print("The bus capacity is sufficient for your group.")

# Final decision: Is the trip feasable and affordable?
if total_cost <= budget and available_time >= TRIP_TIME_REQUIRED and group_size <= bus_capacity:
    print("The trip is affordable and feasible! Have a great time!")
else:
    print("The trip is not feasible. Check your budget, time, or group size constraints.")