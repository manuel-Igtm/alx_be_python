#Use a for loop to generate and print the multiplication table for a given number.
X = int(input("Enter a number to see its multiplication table: "))

for Y in range(1,11):
    Z = X * Y
    print(f"{X} x {Y} = {Z}")
