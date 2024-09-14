#Use user input, variables, and arithmetic operations to calculate and provide feedback on a user’s monthly savings and potential future savings without applying conditional statements.
#Prompt the user for their monthly income: “Enter your monthly income: ”
#Ask for their total monthly expenses: “Enter your total monthly expenses: ”
monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses: "))
#Calculate the monthly savings by subtracting monthly expenses from the monthly income.
monthly_savings = monthly_income - monthly_expenses
#Assume a simple annual interest rate of 5%.
annual_interest_rate = 0.05
Projected_savings = monthly_savings * 12 + monthly_savings * 12 * 0.05
#Results
print(f"Your monthly savings is: ${monthly_savings}")
print(f"Your projected savings after one year is: ${Projected_savings:.2f}")

