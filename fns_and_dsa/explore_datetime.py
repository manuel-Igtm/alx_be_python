# Importing the necessary components from the datetime module
from datetime import datetime, timedelta

# Part 1: Display the current date and time
def display_current_datetime():
    """
    Displays the current date and time in the format YYYY-MM-DD HH:MM:SS.
    """
    # Get the current date and time
    current_date = datetime.now()
    
    # Format the current date and time as 'YYYY-MM-DD HH:MM:SS'
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the formatted current date and time
    print(f"Current date and time: {formatted_date}")
    
# Part 2: Calculate a future date based on user input
def calculate_future_date():
    """
    Calculates and prints the future date after adding a specified number of days to the current date.
    """
    # Get the current date
    current_date = datetime.now()
    
    # Prompt the user to enter the number of days to add
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=days_to_add)
    
    # Format the future date as 'YYYY-MM-DD'
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    
    # Print the future date
    print(f"Future date: {formatted_future_date}")

# Main function to run both parts
def main():
    # Display the current date and time
    display_current_datetime()
    
    # Calculate and display the future date
    calculate_future_date()

# Entry point of the script
if __name__ == "__main__":
    main()
