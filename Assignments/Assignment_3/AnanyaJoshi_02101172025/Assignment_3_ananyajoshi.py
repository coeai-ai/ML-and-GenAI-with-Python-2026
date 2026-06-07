# ==========================================
# ASSIGNMENT 3
# ==========================================
import os

print("--- 1. Function to Print First 10 Natural Numbers ---")
def print_natural_numbers():
    """Prints the first 10 natural numbers using a for loop."""
    print("First 10 natural numbers: ", end="")
    for i in range(1, 11):
        print(i, end=" ")
    print() # For a new line

# Calling the function
print_natural_numbers()

# EXPECTED OUTPUT:
# --- 1. Function to Print First 10 Natural Numbers ---
# First 10 natural numbers: 1 2 3 4 5 6 7 8 9 10 
print("\n" + "="*40 + "\n")


print("--- 2. Function to Calculate Sum of First N Natural Numbers ---")
def sum_of_n_numbers(n):
    """Calculates the sum of first N natural numbers."""
    total = sum(range(1, n + 1))
    print(f"The sum of first {n} natural numbers is: {total}")

# Calling the function with N=10
sum_of_n_numbers(10)

# EXPECTED OUTPUT:
# --- 2. Function to Calculate Sum of First N Natural Numbers ---
# The sum of first 10 natural numbers is: 55
print("\n" + "="*40 + "\n")


print("--- 3. Function to Reverse a Number ---")
def reverse_number(num):
    """Reverses an integer using string slicing."""
    # Convert to string, reverse using [::-1], and convert back to int
    reversed_num = int(str(num)[::-1])
    print(f"Original: {num} | Reversed: {reversed_num}")

# Calling the function
reverse_number(12345)

# EXPECTED OUTPUT:
# --- 3. Function to Reverse a Number ---
# Original: 12345 | Reversed: 54321
print("\n" + "="*40 + "\n")


print("--- 4. Function to Count Digits in a Number ---")
def count_digits(num):
    """Counts the number of digits in a number."""
    # Convert number to string to easily find its length
    digit_count = len(str(abs(num))) # abs() ensures negative signs aren't counted
    print(f"The number {num} has {digit_count} digits.")

# Calling the function
count_digits(987654)

# EXPECTED OUTPUT:
# --- 4. Function to Count Digits in a Number ---
# The number 987654 has 6 digits.
print("\n" + "="*40 + "\n")


print("--- 5. Function to Check Palindrome Number ---")
def check_palindrome(num):
    """Checks if a number reads the same forwards and backwards."""
    num_str = str(num)
    if num_str == num_str[::-1]:
        print(f"{num} is a Palindrome number.")
    else:
        print(f"{num} is NOT a Palindrome number.")

# Calling the function with two examples
check_palindrome(121)
check_palindrome(123)

# EXPECTED OUTPUT:
# --- 5. Function to Check Palindrome Number ---
# 121 is a Palindrome number.
# 123 is NOT a Palindrome number.
print("\n" + "="*40 + "\n")


print("--- 6. Function to Generate Fibonacci Series ---")
def generate_fibonacci(terms):
    """Generates a Fibonacci series up to 'terms' length."""
    fib_sequence = []
    a, b = 0, 1
    for _ in range(terms):
        fib_sequence.append(a)
        a, b = b, a + b
    
    print(f"Fibonacci series ({terms} terms): {fib_sequence}")

# Calling the function
generate_fibonacci(7)

# EXPECTED OUTPUT:
# --- 6. Function to Generate Fibonacci Series ---
# Fibonacci series (7 terms): [0, 1, 1, 2, 3, 5, 8]
print("\n" + "="*40 + "\n")


print("--- 7. Calculator Using Functions ---")
# Defining calculation functions
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Cannot divide by zero"

def calculator(choice, num1, num2):
    """Simulates a calculator where user selects operation and views result."""
    print(f"User Selected Operation: {choice} | Numbers: {num1}, {num2}")
    
    if choice == '1':   result = add(num1, num2)
    elif choice == '2': result = subtract(num1, num2)
    elif choice == '3': result = multiply(num1, num2)
    elif choice == '4': result = divide(num1, num2)
    else: result = "Invalid Selection"
    
    print(f"Result: {result}")

# Calling the calculator function (Simulating User choosing "3" for Multiply)
print("1. Add | 2. Subtract | 3. Multiply | 4. Divide")
calculator('3', 15, 4)

# EXPECTED OUTPUT:
# --- 7. Calculator Using Functions ---
# 1. Add | 2. Subtract | 3. Multiply | 4. Divide
# User Selected Operation: 3 | Numbers: 15, 4
# Result: 60
print("\n" + "="*40 + "\n")


print("--- 8 & 9. Create Text File, Store Details, and Read Data ---")
file_name = "student_details.txt"

# 8. Create text file and store student details (Write Mode)
with open(file_name, "w") as file:
    file.write("Student Name: Ananya Joshi\n")
    file.write("Enrollment: 02101172025\n")
    file.write("College: IGDTUW\n")
print("Data successfully written to file.")

# 9. Read data from a file (Read Mode)
print("\nReading data from file:")
with open(file_name, "r") as file:
    file_content = file.read()
    print(file_content)

# Clean up (Optional: Removes the file after reading so it doesn't clutter your folder)
if os.path.exists(file_name):
    os.remove(file_name)

# EXPECTED OUTPUT:
# --- 8 & 9. Create Text File, Store Details, and Read Data ---
# Data successfully written to file.
# 
# Reading data from file:
# Student Name: Ananya Joshi
# Enrollment: 02101172025
# College: IGDTUW
print("="*40 + "\n")


print("--- 10. Handle Division by Zero Using Exception Handling ---")
def safe_division(numerator, denominator):
    """Demonstrates handling the ZeroDivisionError."""
    try:
        result = numerator / denominator
        print(f"{numerator} divided by {denominator} is: {result}")
    except ZeroDivisionError:
        print("Exception Caught: You cannot divide a number by zero!")

# Calling the function with valid and invalid denominators
safe_division(10, 2)
safe_division(10, 0)

# EXPECTED OUTPUT:
# --- 10. Handle Division by Zero Using Exception Handling ---
# 10 divided by 2 is: 5.0
# Exception Caught: You cannot divide a number by zero!
print("\n" + "="*40 + "\n")


print("--- 11. Create a Student Class with Name and Marks ---")
# Defining the Class
class Student:
    # The __init__ method initializes the object's attributes
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    # A method to display the student's details
    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Marks Scored: {self.marks}")

# Creating objects (instances) of the Student class
student1 = Student("Ananya Joshi", 95)
student2 = Student("Riya", 88)

# Accessing the methods inside the class
student1.display_info()
print("-" * 15)
student2.display_info()

# EXPECTED OUTPUT:
# --- 11. Create a Student Class with Name and Marks ---
# Student Name: Ananya Joshi
# Marks Scored: 95
# ---------------
# Student Name: Riya
# Marks Scored: 88
