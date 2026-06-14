# ============================================
# Assignment 3 - Python Functions
# ============================================


# 1. Print First 10 Natural Numbers
def print_natural_numbers():
    """Prints the first 10 natural numbers."""
    print("First 10 Natural Numbers:")
    for i in range(1, 11):
        print(i, end=" ")
    print()  # New line after printing


# 2. Calculate Sum of First N Natural Numbers
def sum_of_n_numbers(n):
    """Returns the sum of first N natural numbers."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


# 3. Reverse a Number
def reverse_number(num):
    """Returns the reverse of a given number."""
    reversed_num = 0
    original = num
    while num > 0:
        digit = num % 10          # Extract last digit
        reversed_num = reversed_num * 10 + digit  # Build reversed number
        num = num // 10           # Remove last digit
    return reversed_num


# 4. Count Digits in a Number
def count_digits(num):
    """Returns the count of digits in a number."""
    count = 0
    num = abs(num)  # Handle negative numbers
    if num == 0:
        return 1    # 0 has 1 digit
    while num > 0:
        count += 1
        num = num // 10
    return count


# 5. Check Palindrome Number
def is_palindrome(num):
    """Returns True if the number is a palindrome, else False."""
    original = num
    reversed_num = reverse_number(num)  # Reuse reverse function
    if original == reversed_num:
        return True
    else:
        return False


# 6. Generate Fibonacci Series
def fibonacci_series(n):
    """Prints Fibonacci series up to N terms."""
    print(f"Fibonacci Series ({n} terms):")
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b  # Move to next two terms
    print()  # New line after series


# ============================================
# 7. Calculator Using Functions
# ============================================

def add(a, b):
    """Returns sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns difference of two numbers."""
    return a - b

def multiply(a, b):
    """Returns product of two numbers."""
    return a * b

def divide(a, b):
    """Returns division of two numbers. Handles divide by zero."""
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b

def modulus(a, b):
    """Returns remainder of two numbers."""
    if b == 0:
        return "Error! Cannot divide by zero."
    return a % b

def power(a, b):
    """Returns a raised to the power b."""
    return a ** b

def calculator():
    """Calculator that lets user select operation and displays result."""
    print("\n========== CALCULATOR ==========")
    print("Select an operation:")
    print("  1. Addition       (+)")
    print("  2. Subtraction    (-)")
    print("  3. Multiplication (*)")
    print("  4. Division       (/)")
    print("  5. Modulus        (%)")
    print("  6. Power          (^)")
    print("=================================")

    choice = input("Enter your choice (1-6): ")

    # Validate choice
    if choice not in ['1', '2', '3', '4', '5', '6']:
        print("Invalid choice! Please select between 1 and 6.")
        return

    # Get numbers from user
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number: "))

    # Perform operation based on user selection
    if choice == '1':
        result = add(num1, num2)
        operator = "+"
    elif choice == '2':
        result = subtract(num1, num2)
        operator = "-"
    elif choice == '3':
        result = multiply(num1, num2)
        operator = "*"
    elif choice == '4':
        result = divide(num1, num2)
        operator = "/"
    elif choice == '5':
        result = modulus(num1, num2)
        operator = "%"
    elif choice == '6':
        result = power(num1, num2)
        operator = "^"

    # Display result
    print(f"\nResult: {num1} {operator} {num2} = {result}")
    print("=================================")


# ============================================
# MAIN PROGRAM - Calling All Functions
# ============================================

print("=" * 45)
print("        FUNCTION DEMONSTRATIONS")
print("=" * 45)

# 1. Print first 10 natural numbers
print("\n--- 1. First 10 Natural Numbers ---")
print_natural_numbers()

# 2. Sum of first N natural numbers
print("\n--- 2. Sum of First N Natural Numbers ---")
n = int(input("Enter N: "))
result = sum_of_n_numbers(n)
print(f"Sum of first {n} natural numbers = {result}")

# 3. Reverse a number
print("\n--- 3. Reverse a Number ---")
num = int(input("Enter a number to reverse: "))
print(f"Reverse of {num} = {reverse_number(num)}")

# 4. Count digits
print("\n--- 4. Count Digits in a Number ---")
num = int(input("Enter a number: "))
print(f"Number of digits in {num} = {count_digits(num)}")

# 5. Check palindrome
print("\n--- 5. Check Palindrome Number ---")
num = int(input("Enter a number to check palindrome: "))
if is_palindrome(num):
    print(f"{num} is a Palindrome number!")
else:
    print(f"{num} is NOT a Palindrome number.")

# 6. Fibonacci series
print("\n--- 6. Fibonacci Series ---")
terms = int(input("Enter number of terms: "))
fibonacci_series(terms)

# 7. Calculator
print("\n--- 7. Calculator ---")
calculator()
