#handling multiple operations in a simple calculator

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = num1 + num2
        print(f"The result of is {result}")
    case "-":
        result = num1 - num2
        print(f"The result of is {result}")
    case "*":
        result = num1 * num2
        print(f"The result of is {result}")
    case "/":
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else :
            result = num1 / num2
        print(f"The result of is {result}")
    case _:
        print("Invalid operation. Please choose from +, -, *, /")


        
        



        