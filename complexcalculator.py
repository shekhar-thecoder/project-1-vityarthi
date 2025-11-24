import math

# Basic Arithmetic Operations
def addition(x, y):
    """Adds two numbers."""
    return x + y

def subtraction(x, y):
    """Subtracts the second number from the first."""
    return x - y

def multiplication(x, y):
    """Multiplies two numbers."""
    return x * y

def division(x, y):
    """Performs division, handles zero division."""
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def exponentiation(x, y):
    """Raises the first number to the power of the second."""
    return x ** y

# Scientific Functions
def square_root(x):
    """Calculates the square root."""
    if x < 0:
        return "Error: Cannot calculate the square root of a negative number"
    return math.sqrt(x)

def natural_logarithm(x):
    """Calculates the natural logarithm (ln X)."""
    if x <= 0:
        return "Error: Cannot calculate the logarithm of a non-positive number"
    return math.log(x)

def factorial(x):
    """Calculates the factorial (X!)."""
    if x < 0 or x != int(x):
        return "Error: Factorial requires a non-negative integer"
    return math.factorial(int(x))

def sine(x):
    """Calculates the sine (sin X, in radians)."""
    return math.sin(x)

def cosine(x):
    """Calculates the cosine (cos X, in radians)."""
    return math.cos(x)

# Advanced Math
def solve_quadratic_equation(a, b, c):
    """Solves quadratic equation ax^2 + bx + c = 0."""
    if a == 0:
        return "Error: This is a linear equation (a=0)"
    
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return "The equation has no real roots"
    elif discriminant == 0:
        x = -b / (2*a)
        return f"The only real root is x = {x}"
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"The real roots are x1 = {x1} and x2 = {x2}"

# --- Main Program Loop ---
while True:
    print("\n--- Scientific Calculator ---")
    print("Select Operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponent")
    print("6. Square Root (X)")
    print("7. Natural Log (ln X)")
    print("8. Factorial (X!)")
    print("9. Sine (sin X)")
    print("10. Cosine (cos X)")
    print("11. Solve Quadratic Equation")
    print("12. Exit")

    choice = input("Enter the number of the desired operation (1-12): ").strip()

    if choice == '12':
        print("Thank you for using the application.")
        break

    if choice not in [str(i) for i in range(1, 12)]:
        print("Invalid option. Please choose a valid option (1-12).")
        continue

    result = None
    
    try:
        if choice in ('1', '2', '3', '4', '5'):
            num1 = float(input("Enter the first number (X): "))
            num2 = float(input("Enter the second number (Y): "))
        elif choice in ('6', '7', '8', '9', '10'):
            num1 = float(input("Enter the number (X): "))
            num2 = None # Unary operations don't need a second number
        elif choice == '11':
            a = float(input("Enter coefficient a: "))
            b = float(input("Enter coefficient b: "))
            c = float(input("Enter coefficient c: "))
            
        # --- Perform Calculation ---
        if choice == '1':
            result = addition(num1, num2)
        elif choice == '2':
            result = subtraction(num1, num2)
        elif choice == '3':
            result = multiplication(num1, num2)
        elif choice == '4':
            result = division(num1, num2)
        elif choice == '5':
            result = exponentiation(num1, num2)
        elif choice == '6':
            result = square_root(num1)
        elif choice == '7':
            result = natural_logarithm(num1)
        elif choice == '8':
            result = factorial(num1)
        elif choice == '9':
            result = sine(num1)
        elif choice == '10':
            result = cosine(num1)
        elif choice == '11':
            result = solve_quadratic_equation(a, b, c)

    except ValueError:
        print("Error: Invalid input. Please ensure you enter valid numbers.")
        continue

    # Print the final result
    if result is not None:
        print("--- Result ---")
        print("Result:", result)