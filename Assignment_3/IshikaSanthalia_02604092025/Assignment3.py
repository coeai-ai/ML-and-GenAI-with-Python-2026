# Print first 10 natural numbers

def print_natural_numbers():
    print("First 10 Natural Numbers:")
    for i in range(1, 11):
        print(i, end=" ")
    print()

print_natural_numbers()

# Sum of first N natural numbers

def sum_of_n_numbers():
    n = int(input("Enter value of N: "))
    total = 0
    for i in range(1, n + 1):
        total += i
    print("Sum of first", n, "natural numbers =", total)

sum_of_n_numbers()

# Reverse a number

def reverse_number():
    num = int(input("Enter a number to reverse: "))
    original = num
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10
    print("Reverse of", original, "=", reverse)

reverse_number()

# Count digits in a number

def count_digits():
    num = int(input("Enter a number to count digits: "))
    count = 0
    temp = num
    while temp > 0:
        count += 1
        temp //= 10
    print("Number of digits in", num, "=", count)

count_digits()

# Check palindrome number

def check_palindrome():
    num = int(input("Enter a number to check palindrome: "))
    original = num
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10
    if original == reverse:
        print(original, "is a Palindrome")
    else:
        print(original, "is not a Palindrome")

check_palindrome()

# Generate Fibonacci Series

def fibonacci_series():
    n = int(input("Enter number of terms for Fibonacci series: "))
    a = 0
    b = 1
    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
    print()

fibonacci_series()

# Calculator Using Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero"
    return a / b

print("\n CALCULATOR ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Select operation (1/2/3/4): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    result = add(num1, num2)
    print("Result =", result)
elif choice == 2:
    result = subtract(num1, num2)
    print("Result =", result)
elif choice == 3:
    result = multiply(num1, num2)
    print("Result =", result)
elif choice == 4:
    result = divide(num1, num2)
    print("Result =", result)
else:
    print("Invalid choice")

# Create a text file and store student details

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
marks = float(input("Enter Marks: "))

file = open("student_details.txt", "w")
file.write("Student Name : " + name + "\n")
file.write("Roll Number  : " + roll_no + "\n")
file.write("Marks        : " + str(marks) + "\n")
file.close()

print("Student details saved to file.")

# Read data from a file

file = open("student_details.txt", "r")
print("\n Student Details from File ")
print(file.read())
file.close()

# Handle division by zero using exception handling

try:
    a = float(input("Enter numerator: "))
    b = float(input("Enter denominator: "))
    result = a / b
    print("Result =", result)
except ZeroDivisionError:
    print("Error! Cannot divide by zero.")

# Create a Student class with name and marks

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("\n Student Information ")
        print("Name  :", self.name)
        print("Marks :", self.marks)

student_name = input("Enter Student Name: ")
student_marks = float(input("Enter Student Marks: "))

s1 = Student(student_name, student_marks)
s1.display()
