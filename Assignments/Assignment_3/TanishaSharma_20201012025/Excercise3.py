# Create a function to print first 10 natural numbers.
def print_first_10_natural():
    for i in range(1, 11):
        print(i)


# Create a function to calculate sum of first N natural numbers.
def sum_natural():
    n = int(input("Enter N: "))
    print("Sum =", n * (n + 1) // 2)


# Create a function to reverse a number.
def reverse_number():
    num = int(input("Enter a number: "))
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10

    print("Reversed Number =", rev)


# Create a function to count digits in a number.
def count_digits():
    num = int(input("Enter a number: "))
    print("Number of digits =", len(str(abs(num))))


# Create a function to check palindrome number.
def is_palindrome():
    num = int(input("Enter a number: "))
    temp = num
    rev = 0

    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10

    if num == rev:
        print("Palindrome Number")
    else:
        print("Not a Palindrome Number")


# Create a function to generate Fibonacci series.
def fibonacci():
    n = int(input("Enter number of terms: "))
    a, b = 0, 1

    print("Fibonacci Series:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


# Calculator Using Functions that contains the following features; - User selects operation - Program performs calculation - Display result
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


def calculator():
    print("\nCalculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter choice: "))
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
        except ZeroDivisionError:
            print("Cannot divide by zero")
    else:
        print("Invalid Choice")


# Create a text file and store student details.
def write_student_details():
    name = input("Enter student name: ")
    marks = input("Enter student marks: ")

    with open("students.txt", "w") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Marks: {marks}\n")

    print("Student details saved.")


# Read data from a file.
def read_file():
    with open("students.txt", "r") as file:
        print(file.read())


# Handle division by zero using exception handling.
def safe_division():
    try:
        a = float(input("Enter numerator: "))
        b = float(input("Enter denominator: "))
        print("Result =", a / b)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")


# Create a Student class with name and marks.
class Student:
    def __init__(self):
        self.name = input("Enter student name: ")
        self.marks = float(input("Enter student marks: "))

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)



print_first_10_natural()

sum_natural()

reverse_number()

count_digits()

is_palindrome()

fibonacci()

calculator()

write_student_details()

read_file()

safe_division()

s = Student()
s.display()