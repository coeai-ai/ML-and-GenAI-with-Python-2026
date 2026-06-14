name: Yashica 
enrollment number: 22301172025
college: Igdtuw 

# 1. Function to Print First 10 Natural Numbers

def print_natural_numbers():
    print("First 10 Natural Numbers:")
    for i in range(1, 11):
        print(i, end=" ")
    print()

print_natural_numbers()


# 2. Function to Calculate Sum of First N Natural Numbers

def sum_natural_numbers(n):
    return sum(range(1, n + 1))

n = int(input("Enter N: "))
print("Sum =", sum_natural_numbers(n))


# 3. Function to Reverse a Number

def reverse_number(num):
    return int(str(num)[::-1])

num = int(input("Enter a number to reverse: "))
print("Reversed Number =", reverse_number(num))


# 4. Function to Count Digits in a Number

def count_digits(num):
    return len(str(num))

num = int(input("Enter a number: "))
print("Number of Digits =", count_digits(num))


# 5. Function to Check Palindrome Number

def is_palindrome(num):
    return str(num) == str(num)[::-1]

num = int(input("Enter a number: "))

if is_palindrome(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")


# 6. Function to Generate Fibonacci Series

def fibonacci(n):
    a, b = 0, 1

    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

terms = int(input("Enter number of terms: "))
fibonacci(terms)

# 7. Calculator Using Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("\nCalculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Select Operation (1-4): "))

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

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


# 8. Create a Text File and Store Student Details

file = open("student.txt", "w")

name = input("Enter Student Name: ")
marks = input("Enter Student Marks: ")

file.write("Name: " + name + "\n")
file.write("Marks: " + marks + "\n")

file.close()

print("Student details saved to student.txt")


# 9. Read Data from a File

file = open("student.txt", "r")

print("\nReading Student File:")
print(file.read())

file.close()


# 10. Handle Division by Zero Using Exception Handling

try:
    a = int(input("Enter Numerator: "))
    b = int(input("Enter Denominator: "))

    result = a / b

    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by Zero is Not Allowed")


# 11. Student Class with Name and Marks

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("\nStudent Details")
        print("Name :", self.name)
        print("Marks :", self.marks)

student_name = input("Enter Student Name: ")
student_marks = float(input("Enter Student Marks: "))

student = Student(student_name, student_marks)

student.display()
