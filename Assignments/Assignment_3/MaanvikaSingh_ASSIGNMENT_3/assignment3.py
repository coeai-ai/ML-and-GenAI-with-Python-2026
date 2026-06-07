# 1. Function to print first 10 natural numbers
def print_natural_numbers():
    for i in range(1, 11):
        print(i, end=" ")
    print()

# 2. Function to calculate sum of first N natural numbers
def sum_natural(n):
    return n * (n + 1) // 2

# 3. Function to reverse a number
def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev

# 4. Function to count digits in a number
def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count

# 5. Function to check palindrome number
def is_palindrome(num):
    return num == reverse_number(num)

# 6. Function to generate Fibonacci series
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

# 7. Calculator Using Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Calculator")
choice = input("Enter operation (+, -, *, /): ")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == "+":
    print("Result =", add(a, b))
elif choice == "-":
    print("Result =", subtract(a, b))
elif choice == "*":
    print("Result =", multiply(a, b))
elif choice == "/":
    print("Result =", divide(a, b))
else:
    print("Invalid Operation")

# 8. Create a text file and store student details
file = open("student.txt", "w")
name = input("Enter student name: ")
marks = input("Enter marks: ")
file.write("Name: " + name + "\n")
file.write("Marks: " + marks)
file.close()

# 9. Read data from a file
file = open("student.txt", "r")
print("\nStudent File Data:")
print(file.read())
file.close()

# 10. Handle division by zero using exception handling
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print("Result =", a / b)
except ZeroDivisionError:
    print("Division by zero is not allowed.")

# 11. Student class with name and marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("maanvika", 85)
s1.display()