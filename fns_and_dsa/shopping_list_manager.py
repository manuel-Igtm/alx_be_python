# # Function to display the menu options to the user
# def display_menu():
#     """
#     Displays the menu for the shopping list manager.
#     """
#     print("\nShopping List Manager")
#     print("1. Add Item")
#     print("2. Remove Item")
#     print("3. View List")
#     print("4. Exit")

# # Main function to handle the shopping list operations
# def main():
#     # Initialize an empty shopping list
#     shopping_list = []
    
#     # Infinite loop to keep the program running until the user exits
#     while True:
#         # Display the menu options
#         display_menu()

#         # Get the user's choice
#         choice = input("Enter your choice: ").strip()

#         # Handle the 'Add Item' option
#         if choice == '1':
#             item = input("Enter the item to add: ").strip()
#             # Add the item to the shopping list
#             shopping_list.append(item)
#             print(f"'{item}' has been added to your shopping list.")

#         # Handle the 'Remove Item' option
#         elif choice == '2':
#             item = input("Enter the item to remove: ").strip()
#             # Check if the item exists in the shopping list
#             if item in shopping_list:
#                 shopping_list.remove(item)
#                 print(f"'{item}' has been removed from your shopping list.")
#             else:
#                 print(f"'{item}' not found in the shopping list.")

#         # Handle the 'View List' option
#         elif choice == '3':
#             if shopping_list:
#                 print("\nYour Shopping List:")
#                 # Display each item in the shopping list
#                 for i, item in enumerate(shopping_list, 1):
#                     print(f"{i}. {item}")
#             else:
#                 print("\nYour shopping list is empty.")

#         # Handle the 'Exit' option
#         elif choice == '4':
#             print("Goodbye! and thanks for shopping")
#             break

#         # Handle invalid input for menu options
#         else:
#             print("Invalid choice. Please try again.")

# # Entry point of the script
# if __name__ == "__main__":
#     main()



# # Function to display the menu options to the user
# def display_menu():
#     """
#     Displays the menu for the shopping list manager.
#     """
#     # Display the title of the menu
#     print("\nShopping List Manager")
#     print("1. Add Item")
#     print("2. Remove Item")
#     print("3. View List")
#     print("4. Exit")

# # Main function to handle the shopping list operations
# def main():
#     # Initialize an empty shopping list
#     shopping_list = []
    
#     # Infinite loop to keep the program running until the user exits
#     while True:
#         # Display the menu options
#         display_menu()

#         # Get the user's choice
#         choice = input("Enter your choice: ").strip()

#         # Handle the 'Add Item' option
#         if choice == '1':
#             item = input("Enter the item to add: ").strip()
#             # Add the item to the shopping list
#             shopping_list.append(item)
#             print(f"'{item}' has been added to your shopping list.")

#         # Handle the 'Remove Item' option
#         elif choice == '2':
#             item = input("Enter the item to remove: ").strip()
#             # Check if the item exists in the shopping list
#             if item in shopping_list:
#                 shopping_list.remove(item)
#                 print(f"'{item}' has been removed from your shopping list.")
#             else:
#                 print(f"'{item}' not found in the shopping list.")

#         # Handle the 'View List' option
#         elif choice == '3':
#             if shopping_list:
#                 print("\nYour Shopping List:")
#                 # Display each item in the shopping list
#                 for i, item in enumerate(shopping_list, 1):
#                     print(f"{i}. {item}")
#             else:
#                 print("\nYour shopping list is empty.")

#         # Handle the 'Exit' option
#         elif choice == '4':
#             print("Goodbye!")
#             break

#         # Handle invalid input for menu options
#         else:
#             print("Invalid choice. Please try again.")

# # Entry point of the script
# if __name__ == "__main__":
#     main()


def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"Added '{item}' to the list.")
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Removed '{item}' from the list.")
            else:
                print(f"'{item}' not found in the list.")
        elif choice == '3':
            # Display the shopping list
            if not shopping_list:
                print("The list is empty.")
            else:
                print("Current Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()