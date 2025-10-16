print("Welcome to the Coding Competition Tracker!")
print("This program will track your progress as you complete tasks.")

tasks = "complete Python tutorial, submit project proposal, debug code"
print("\nInitial tasks to complete: ", tasks)
#Task 1
tasks = tasks + ", review final project"
print("\nUpdated tasks list after adding a new task: ", tasks)
#Task 2
print("\nTasks in uppercase: ", tasks.upper())
#Task 3
print("\nThe phrase 'debug code' starts at index: ", tasks.find("debug code"))
#Task 4
print("\nFirst two tasks: ", tasks[:49])
#Task 5
new_tasks = tasks.replace("debug code", "optimize code:")
print("\nTasks after replacing 'debug code': ")
#Task 6
print("\nFinal tasks list: ", new_tasks)
#Task 7
print("\nThe total number of characters in the final task list is : ", len(new_tasks))
#Task 8
print("\nAttempting to change the first task...")
tasks.capitalize()
# Strings are immutable and cannot be changed in place
#Task 9
print("Original first task: complete")
print("Updated first task in the task list: ", tasks)