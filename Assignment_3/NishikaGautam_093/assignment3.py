# ==========================================
# MENU DRIVEN PROGRAM USING FUNCTIONS
# ==========================================

# Q1: Function to print first 10 natural numbers
def print_first_10_natural_numbers():
    print("\nFirst 10 Natural Numbers:")
    for i in range(1, 11):
        print(i, end=" ")
    print()


# Q2: Function to calculate sum of first N natural numbers
def sum_of_n_natural_numbers():
    try:
        n = int(input("Enter value of N: "))

        if n < 0:
            print("Please enter a non-negative number.")
            return

        total = 0
        for i in range(1, n + 1):
            total += i

        print(f"Sum of first {n} natural numbers = {total}")

    except ValueError:
        print("Invalid input! Please enter an integer.")


# Q3: Function to reverse a number
def reverse_number():
    try:
        num = int(input("Enter a number: "))

        sign = -1 if num < 0 else 1
        num = abs(num)

        reverse = 0

        while num > 0:
            digit = num % 10
            reverse = reverse * 10 + digit
            num //= 10

        reverse *= sign

        print("Reversed Number =", reverse)

    except ValueError:
        print("Invalid input! Please enter an integer.")


# Q4: Function to count digits in a number
def count_digits():
    try:
        num = int(input("Enter a number: "))

        num = abs(num)

        if num == 0:
            count = 1
        else:
            count = 0
            while num > 0:
                count += 1
                num //= 10

        print("Number of digits =", count)

    except ValueError:
        print("Invalid input! Please enter an integer.")


# Q5: Function to check palindrome number
def palindrome_number():
    try:
        num = int(input("Enter a number: "))

        original = num
        num = abs(num)

        reverse = 0

        while num > 0:
            digit = num % 10
            reverse = reverse * 10 + digit
            num //= 10

        if abs(original) == reverse:
            print("Palindrome Number")
        else:
            print("Not a Palindrome Number")

    except ValueError:
        print("Invalid input! Please enter an integer.")


# Q6: Function to generate Fibonacci series
def fibonacci_series():
    try:
        n = int(input("Enter number of terms: "))

        if n <= 0:
            print("Please enter a positive number.")
            return

        a = 0
        b = 1

        print("Fibonacci Series:")

        if n == 1:
            print(a)
            return

        for i in range(n):
            print(a, end=" ")
            c = a + b
            a = b
            b = c

        print()

    except ValueError:
        print("Invalid input! Please enter an integer.")


# Q7: Calculator using functions

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Division by zero not allowed."
    return a / b


def calculator():
    try:
        print("\n----- CALCULATOR -----")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = int(input("Select operation (1-4): "))

        if choice not in [1, 2, 3, 4]:
            print("Invalid Choice!")
            return

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

    except ValueError:
        print("Invalid input! Please enter numeric values.")


# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n===================================")
    print("     MENU DRIVEN PROGRAM")
    print("===================================")
    print("1. Print First 10 Natural Numbers")
    print("2. Sum of First N Natural Numbers")
    print("3. Reverse a Number")
    print("4. Count Digits in a Number")
    print("5. Check Palindrome Number")
    print("6. Generate Fibonacci Series")
    print("7. Calculator")
    print("8. Exit")
    print("===================================")

    try:
        choice = int(input("Enter your choice (1-8): "))

        if choice == 1:
            print_first_10_natural_numbers()

        elif choice == 2:
            sum_of_n_natural_numbers()

        elif choice == 3:
            reverse_number()

        elif choice == 4:
            count_digits()

        elif choice == 5:
            palindrome_number()

        elif choice == 6:
            fibonacci_series()

        elif choice == 7:
            calculator()

        elif choice == 8:
            print("Thank You! Program Exited Successfully.")
            break

        else:
            print("Invalid Choice! Please select between 1 and 8.")

    except ValueError:
        print("Invalid input! Please enter an integer.")

# Q8: Create a Text File and Store Student Details

#Taking student details as input
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
course = input("Enter Course: ")
marks = input("Enter Marks: ")

# Creating and opening a text file in write mode
with open("student_details.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Roll Number: {roll_no}\n")
    file.write(f"Course: {course}\n")
    file.write(f"Marks: {marks}\n")

print("Data saved successfully.")

# Q9: Read Data from File

try:
    with open("student_details.txt", "r") as file:
        data = file.read()

    print("Contents of the file:")
    print(data)

except FileNotFoundError:
    print("Error: File does not exist.")

#Q10: Handle Division by Zero Using Exception Handling

try:
    num1 = float(input("Enter numerator: "))
    num2 = float(input("Enter denominator: "))

    result = num1 / num2

    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid numeric values.")

#Q11: Student Class with Name and Marks
# Creating Student class

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)


# Creating object
s1 = Student("Sneha", 85)

# Displaying details
s1.display()