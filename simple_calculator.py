# Pseudocode

# Print the operations to choose from
print("\nSimple Calculator")
print("\nChoose the math operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
# Get user's choice for the math operation
choice = int(input("\nEnter choice (1-5): "))
if choice == 5:
    print("Thank you!")
# Get user's input for two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
# Perform the selected math operation and display the result
if choice == 1:
    result = num1 + num2
    print("Result:", result)
elif choice == 2:
    result = num1 - num2
    print("Result:", result)
elif choice == 3:
    result = num1 * num2
    print("Result:", result)
elif choice == 4:
    if num2 == 0:
        raise ZeroDivisionError("Division by zero is not allowed (ZeroDivisionError).")
    result = num1 / num2
    print("Result:", result)
else:
    print("Invalid input! Please enter a number between 1 and 5.")


# Ask the user if they want to try again