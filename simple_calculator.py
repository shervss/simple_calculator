# Pseudocode

# Print the operations to choose from
print("\nSimple Calculator")
print("\nChoose the math operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

while True:
    try:
        # Get user's choice for the math operation
        choice = int(input("\nEnter choice (1-5): "))
        if choice == 5:
            print("Thank you!")
            break  # Exit the loop and program if the user chooses to exit
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
    except ValueError:
        print("Invalid input! Please enter a valid number (ValueError).")
    except ZeroDivisionError as e:
        print(e)  # Display the error message for division by zero
    else:
        # Ask the user if they want to try again
        try_again = input("Do you want to try again? (yes/no): ")
        if try_again.lower() != 'yes':
            print("Thank you!")
            break  # Exit the loop and program if the user doesn't want to try again

    finally:
        print("-" *100)