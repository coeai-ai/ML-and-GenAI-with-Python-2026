# Function to print first 10 natural numbers

def print_numbers():
    for i in range(1, 11):
        print(i)

print_numbers()

# Function to calculate sum of first N natural numbers

def calculate_sum(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total

num = int(input("Enter N: "))
print("Sum =", calculate_sum(num))

# Function to reverse a number

def reverse_number(num):
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return reverse

number = int(input("Enter a number: "))
print("Reversed Number =", reverse_number(number))

# Function to count digits

def count_digits(num):
    count = 0

    while num > 0:
        count += 1
        num = num // 10

    return count

number = int(input("Enter a number: "))
print("Number of Digits =", count_digits(number))

# Function to check palindrome number

def is_palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if original == reverse:
        return True
    else:
        return False

number = int(input("Enter a number: "))

if is_palindrome(number):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

# Function to generate Fibonacci Series

def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")

        next_term = a + b
        a = b
        b = next_term

terms = int(input("Enter number of terms: "))
fibonacci(terms)

# Calculator Using Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Choose operation (1-4): "))

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

# Store student details in a file

name = input("Enter Student Name: ")
marks = input("Enter Marks: ")

with open("student_details.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Marks: " + marks)

print("Student details saved successfully.")

# Read data from file

with open("student_details.txt", "r") as file:
    content = file.read()

print("File Content:")
print(content)

# Division by zero exception handling

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result =", result)

except ZeroDivisionError:
    print("Division by zero is not allowed.")

finally:
    print("Program Finished")

# Student class

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student Name :", self.name)
        print("Marks :", self.marks)

name = input("Enter Student Name: ")
marks = float(input("Enter Marks: "))

student1 = Student(name, marks)

student1.display()
