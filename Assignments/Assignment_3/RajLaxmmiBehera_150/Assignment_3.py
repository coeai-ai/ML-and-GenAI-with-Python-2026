"""ASSIGNMENT 3"""

# Create a function to print first 10 natural numbers
def print_natural_numbers():
    for i in range(1, 11):
        print(i)
print_natural_numbers()

# Create a function to calculate sum of first n natural numbers
def sum_natural_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
n = int(input("Enter a number: "))
print("Sum =", sum_natural_numbers(n))

# Create a function to reverse a number
def reverse_number(num):
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    return reverse
n = int(input("Enter a number: "))
print("Reversed number =", reverse_number(n))

# Create a function to count digits in a number
def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num = num // 10
    return count
n = int(input("Enter a number: "))
print("Number of digits =", count_digits(n))

# Create a function to check polindrome number
def is_palindrome(num):
    original = num
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    return original == reverse
n = int(input("Enter a number: "))
if is_palindrome(n):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

# Create a function to generate Fibonacci series up to n terms
def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
n = int(input("Enter the number of terms: "))
print("Fibonacci series:")
fibonacci_series(n)

# Calculator using functions that contains the following features:
"""User selects Operations"""
"""Program performs calculations"""
"""Display the result"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not possible"
    return a / b

print("Calculator Menu")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result =", add(num1, num2))
elif choice == 2:
    print("Result =", subtract(num1, num2))
elif choice == 3:
    print("Result =", multiply(num1, num2))
elif choice == 4:
    print("Result =", divide(num1, num2))
else:
    print("Invalid Choice")

# Create a text file and store student details
def write_student_file():
    with open("student.txt", "w") as file:
        file.write("Name:RajLaxmi\n")
        file.write("Roll No:150\n")
        file.write("Marks:85")
    print("Student details saved in student.txt")

write_student_file()

# Read Data from a file
def read_student_file():
    try:
        with open("student.txt", "r") as file:
            data = file.read()
            print("File Contents:\n")
            print(data)
    except FileNotFoundError:
        print("Error: File not found.")

read_student_file()

# Handle division by zero using exception handling
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

# Create a student class with name and marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
student1 = Student("RajLaxmi", 85)
student1.display_details()
