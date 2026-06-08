# Write a function to:

# # Print first 10 natural numbers
def print_natural_numbers(n):
    for i in range(1, n + 1):
        print(i, end=' ')
    print()  # for new line after printing numbers
print("First 10 natural numbers:")
print_natural_numbers(10)

# Sum of first N natural numbers
def sum_natural_numbers(n):
    return sum(range(1, n + 1))
n = int(input("Enter a number to find the sum of first N natural numbers: "))
print(f"Sum of first {n} natural numbers is: {sum_natural_numbers(n)}")

#  Reverse a number
def reverse_number(num):
    return int(str(num)[::-1])
number = int(input("Enter a number to reverse: "))
print(f"Reversed number is: {reverse_number(number)}") 

# Count digits in a number
def count_digits(num):
    return len(str(num))
number = int(input("Enter a number to count its digits: "))
print(f"Number of digits in {number} is: {count_digits(number)}")

# Check palindrome number
def is_palindrome(num):
    return str(num) == str(num)[::-1]
number = int(input("Enter a number to check if it's a palindrome: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")

# Generate Fibonacci series
def fibonacci_series(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series
n_terms = int(input("Enter the number of terms for Fibonacci series: "))
print("Fibonacci series:")
print(fibonacci_series(n_terms))

# Calculator using functions
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"Addition: {num1} + {num2} = {add(num1, num2)}")
print(f"Subtraction: {num1} - {num2} = {subtract(num1, num2)}")
print(f"Multiplication: {num1} * {num2} = {multiply(num1, num2)}")
print(f"Division: {num1} / {num2} = {divide(num1, num2)}")


# Create a text file and store student details 
def save_student_details(name, age, grade):
    with open("student_details.txt", "a") as file:
        file.write(f"Name: {name}, Age: {age}, Grade: {grade}\n")
student_name = input("Enter student name: ")
student_age = int(input("Enter student age: "))
student_grade = input("Enter student grade: ")
save_student_details(student_name, student_age, student_grade)
print("Student details saved to student_details.txt")  

# Read data from a file
def read_student_details():
    try:
        with open("student_details.txt", "r") as file:
            details = file.read()
            print("\n--- Student Details ---")
            print(details)
    except FileNotFoundError:
        print("No student details found. Please save some details first.")
read_student_details()

# Handle division by zero using exception handling
def safe_divide(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
num1 = float(input("Enter numerator: "))
num2 = float(input("Enter denominator: "))
print(f"Result of {num1} / {num2} is: {safe_divide(num1, num2)}")   

# Create a student class with name and marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
student_name = input("Enter student name: ")
student_marks = float(input("Enter student marks: "))
student = Student(student_name, student_marks)
student.display_details()

