def basic_calculator():
    """
    A simple calculator program that performs addition, subtraction,
    multiplication, or division based on user input.
    """
    print("Welcome to the Basic Calculator!")

    # --- Get the first number from the user ---
    while True:
        try:
            num1_str = input("Enter the first number: ")
            num1 = float(num1_str) # Convert input to a float to handle decimals
            break # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # --- Get the second number from the user ---
    while True:
        try:
            num2_str = input("Enter the second number: ")
            num2 = float(num2_str) # Convert input to a float
            break # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # --- Get the desired operation from the user ---
    while True:
        operation = input("Enter the operation (+, -, *, /): ").strip() # .strip() removes leading/trailing whitespace
        if operation in ['+', '-', '*', '/']:
            break # Exit loop if operation is valid
        else:
            print("Invalid operation. Please choose from +, -, *, /.")

    # --- Perform the calculation and display the result ---
    result = None # Initialize result variable

    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 != 0: # Check for division by zero
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        # This case should ideally not be reached due to the input validation loop
        print("An unexpected error occurred with the operation.")

# --- Call the function to run the calculator ---
if __name__ == "__main__":
    basic_calculator()