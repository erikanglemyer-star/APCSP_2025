# Welcome message, ctrl + cmd + space for emoji
print("🎟️ Welcome to the Concert Ticket & Merchandise Selector! 🎶")

# List of available tickets
tickets = ["VIP Pass", "Front Row", "General Admission", "Balcony"]
print("\nAvailable ticket types:", tickets)

# User selects a ticket type
selected_ticket = input("Which ticket would you like to purchase? ").strip()
if selected_ticket in tickets:
    print(f"✅ {selected_ticket} added to your order!")
else:
    print(f"{selected_ticket} is not a valid option. Defaulting to 'General Admission'.")
    selected_ticket = "General Admission"

# User decides how many T-shirts they want
num_shirts = int(input("\nHow many T-Shirts would you like to buy? (Enter a number): "))
shirts = ["T-Shirt"] * num_shirts # Using * to create multiples

# Creating the order list
order = [selected_ticket] + shirts

# Displaying the full order
print("\n Your order summary:")
for item in order:
    print("-",item)

# Showing total number of items using len()
print("\nTotal items in your order:", len(order))

# User can view items in reverse order
reverse_choice = input("\nWould you like to see your order in reverse? (yes/no)").strip().lower()
if reverse_choice == "yes":
    order.reverse()
    print("\n🔄 Reversed order list:", order)

# Generating a unique ticket number using range()
ticket_number = list(range(1000, 1010)) # Ticket numbers from 1000 to 1009
print(f"\nYour ticket number: {ticket_number[0]}") # Assigning the first available number

# Countdown to the concert
print("\n🎵 Countdown to the concert:")
countdown = list(range(10, 0, -1)) # Using range() to create a decreasing list
for num in countdown:
    print(num, end="...")
print("\n🚀 Enjoy the concert!")