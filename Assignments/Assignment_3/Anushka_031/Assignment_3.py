# 1. Create a function to print first 10 natural numbers

def print_first_10_natural_numbers():
    print("\nFirst 10 Natural Numbers:")
    for i in range(1, 11):
        print(i, end=" ")
    print()

# 2. Create a function to calculate sum of first N natural numbers

def sum_n_natural_numbers(n):
    return n * (n + 1) // 2

# 3. Create a function to reverse a number

def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev

# 4. Create a function to count digits in a number

def count_digits(num):
    return len(str(abs(num)))

# 5. Create a function to check palindrome number

def is_palindrome(num):
    return num == reverse_number(num)

# 6. Create a function to generate Fibonacci series

def fibonacci(n):
    a, b = 0, 1
    print("\nFibonacci Series:")
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
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

def calculator():
    print("\nCalculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice (1-10): "))

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Result =", add(a, b))
    elif choice == 2:
        print("Result =", subtract(a, b))
    elif choice == 3:
        print("Result =", multiply(a, b))
    elif choice == 4:
        try:
            print("Result =", divide(a, b))
        except ZeroDivisionError as e:
            print("Error:", e)
    else:
        print("Invalid Choice")


# 8. Create a text file and store student details

def write_student_details():
    with open("students.txt", "w") as file:
        file.write("Name: Anushka\n")
        file.write("Roll No: 31\n")
        file.write("Course: B.Tech CSE\n")
    print("\nStudent details stored in students.txt")


# 9. Read data from a file

def read_file():
    try:
        with open("students.txt", "r") as file:
            print("\nContents of students.txt:")
            print(file.read())
    except FileNotFoundError:
        print("File not found.")


# 10. Handle division by zero using exception handling

def division_by_zero_demo():
    try:
        a = int(input("\nEnter numerator: "))
        b = int(input("Enter denominator: "))
        result = a / b
        print("Result =", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")


# 11. Create a Student class with name and marks

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("\nStudent Details")
        print("Name :", self.name)
        print("Marks:", self.marks)


# MAIN PROGRAM

print(" Assignment 3 ")

# 1
print_first_10_natural_numbers()

# 2
n = int(input("\nEnter N for sum of first N natural numbers: "))
print("Sum =", sum_n_natural_numbers(n))

# 3
num = int(input("\nEnter a number to reverse: "))
print("Reversed Number =", reverse_number(num))

# 4
num = int(input("\nEnter a number to count digits: "))
print("Number of Digits =", count_digits(num))

# 5
num = int(input("\nEnter a number to check palindrome: "))
if is_palindrome(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

# 6
terms = int(input("\nEnter number of Fibonacci terms: "))
fibonacci(terms)

# 7
calculator()

# 8
write_student_details()

# 9
read_file()

# 10
division_by_zero_demo()

# 11
name = input("\nEnter Student Name: ")
marks = float(input("Enter Student Marks: "))

student = Student(name, marks)
student.display()

print("\n Program Completed Successfully ")