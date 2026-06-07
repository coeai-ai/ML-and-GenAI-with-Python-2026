# Function to print first 10 natural numbers
def print_numbers():
    for i in range(1, 11):
        print(i)

print_numbers()


# Function to calculate sum of first N natural numbers
def sum_n(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total

n = int(input("Enter N: "))
print("Sum =", sum_n(n))


# Function to reverse a number
def reverse_number(num):
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    return rev

num = int(input("Enter a number: "))
print("Reversed Number =", reverse_number(num))


# Function to count digits
def count_digits(num):
    count = 0

    while num > 0:
        count += 1
        num = num // 10

    return count

num = int(input("Enter a number: "))
print("Number of digits =", count_digits(num))



# Function to check palindrome number
def is_palindrome(num):
    original = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    return original == rev

num = int(input("Enter a number: "))

if is_palindrome(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")



# Function to generate Fibonacci series
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("How many terms? "))
fibonacci(n)


# Addition
def add(a, b):
    return a + b

# Subtraction
def subtract(a, b):
    return a - b

# Multiplication
def multiply(a, b):
    return a * b

# Division
def divide(a, b):
    return a / b

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice (1-4): "))

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

name = input("Enter student name: ")
marks = input("Enter marks: ")

file = open("student.txt", "w")

file.write("Name: " + name + "\n")
file.write("Marks: " + marks)

file.close()

print("Student details saved successfully.")


# Read data from a file

file = open("student.txt", "r")
data = file.read()
print(data)
file.close()


# Handle division by zero

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result =", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")

# Student class

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name :", self.name)
        print("Marks:", self.marks)

# Creating object
s1 = Student("Prachi", 95)

s1.display()