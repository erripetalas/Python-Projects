# Function to perform the calculation
def calculate(num1, num2, operator): 
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        # Check for division by zero
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operator"
        # print("Error: Invalid operator")

# Function to get valid number input from the user
def get_number_input(prompt):
    while True:
        try:
            # Try to convert the input to a float. If successful, return the number.
            return float(input(prompt))
        except ValueError:
            # If conversion fails (e.g., user enters non-numeric input):
            # 1. Catch the ValueError to prevent the program from crashing
            # 2. Print an error message
            # 3. Continue the loop to ask for input again
            print("Invalid input. Please enter a number.")

# Main function to run the calculator
def main():
    print("Python Calculator")
    print("Operations: + (add), - (subtract), * (multiply), / (divide)")
    
    # Main loop of the calculator
    while True:
        # Get the operator from the user
        operator = input("Enter an operator (+ - * /) or 'q' to quit: ")
        
        # Check if the user wants to quit
        if operator.lower() == 'q':
            print("Thank you for using the calculator. Goodbye!")
            break
        
        # Validate the operator
        if operator not in ["+", "-", "*", "/"]:
            print("Invalid operator. Please try again.")
            continue
        
        # Get the two numbers from the user
        num1 = get_number_input("Enter the 1st number: ")
        num2 = get_number_input("Enter the 2nd number: ")
        
        # Perform the calculation
        result = calculate(num1, num2, operator)
        
        # Display the result
        print(f"\nResult: {num1} {operator} {num2} = {result}\n")
main()