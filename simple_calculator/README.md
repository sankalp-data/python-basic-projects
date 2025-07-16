This is a basic command-line calculator built using Python. It supports four arithmetic operations: Addition, Subtraction, Multiplication, and Division.

# Features

✅ Addition

➖ Subtraction

✖️ Multiplication

➗ Division (with division-by-zero protection)

👨‍💻 User input interface via terminal


# How the Program Works

1. The program defines four functions:

 - add(a, b) – returns sum

 - sub(a, b) – returns difference

 - multi(a, b) – returns product

 - division(a, b) – returns quotient or a warning if b == 0

2. Displays a menu of operations for the user.

3. Prompts the user to:

 - Choose an operation (1, 2, 3, or 4)

 - Enter two numbers

4. Performs the operation and displays the result.

5. If an invalid operation is chosen, it prints "Invalid input".


# How to Run

1. Save the code in a file named simple_calculator.py.

2. Run the script from the terminal:

 - python simple_calculator.py

# Concepts Used

 - Function definitions with def

 - Conditional statements (if, elif, else)

 - User input handling with input() and float()

 - Defensive programming (division by zero check)