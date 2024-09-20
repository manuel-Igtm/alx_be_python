#Create a simplified Python script that uses conditional statements, Match Case, and loops to remind the user about a single, priority task for the day based on time sensitivity.

#prompt for a single task
task = input("Enter a task description: ")
priority = input("Enter the task's priority (high/ medium/ low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        priority_message = (f"Reminder: {task} is a high-priority task.")
        if time_bound.lower() == "yes":
            reminder = f"Today, you have a {priority_message} task '{task}' that requires immediate attention today!"
        else:
            reminder = f"Today, you have a {priority_message} task '{task}'."
    case "medium":
        priority_message = (f"Reminder: {task} is a medium-priority task.")
        if time_bound.lower() == "yes":
            reminder = f"Today, you have a {priority_message} task '{task}' that requires attention today!"
        else:
            reminder = f"Today, you have a {priority_message} task '{task}'."
    case "low":
        priority_message = (f"Reminder: {task} is a low-priority task.")
        if time_bound.lower() == "yes":
            reminder = f"Today, you have a {priority_message} task '{task}' that needs to be done today!"
        else:
            reminder = f"Today, you have a {priority_message} task '{task}'."
# Provide a Customized Reminder
print(reminder)
        
