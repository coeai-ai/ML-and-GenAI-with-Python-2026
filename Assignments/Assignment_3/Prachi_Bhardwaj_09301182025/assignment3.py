# Student Name: Prachi Bhardwaj
# Enrollment Number: 09301182025
# College Name: IGDTUW

# ASSIGNMNET 3

#1)  Print First 10 Natural Numbers

def print_natural_numbers():
    for i in range(1, 11):
        print(i)

print_natural_numbers()


#2) Calculate Sum of First N Natural Numbers

def sum_natural_numbers(n):
    return n * (n + 1) // 2

n = int(input("Enter N: "))
print("Sum =", sum_natural_numbers(n))


#3) Reverse a Number

def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev

num = int(input("Enter a number: "))
print("Reversed number:", reverse_number(num))


#4) Count Digits in a Number

def count_digits(num):
    count = 0

    if num == 0:
        return 1

    while num > 0:
        count += 1
        num //= 10

    return count

num = int(input("Enter a number: "))
print("Number of digits:", count_digits(num))


#5) Check Palindrome Number

def is_palindrome(num):
    original = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10

    return original == rev

num = int(input("Enter a number: "))

if is_palindrome(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")


#6) Generate Fibonacci Series

def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter number of terms: "))
fibonacci(n)


#7) Calculator Using Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero not allowed"
    return a / b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\n1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Choose operation: "))

if choice == 1:
    print("Result =", add(a, b))
elif choice == 2:
    print("Result =", subtract(a, b))
elif choice == 3:
    print("Result =", multiply(a, b))
elif choice == 4:
    print("Result =", divide(a, b))
else:
    print("Invalid Choice")


#8) Create a Text File and Store Student Details

name = input("Enter student name: ")
marks = input("Enter marks: ")

with open("student.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Marks: {marks}\n")

print("Student details saved successfully.")


#9)  Read Data from a File

with open("student.txt", "r") as file:
    data = file.read()

print("File Content:")
print(data)


#10) Handle Division by Zero Using Exception Handling

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))

    result = a / b
    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


#11) Create a Student Class with Name and Marks

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

name = input("Enter student name: ")
marks = float(input("Enter marks: "))

student = Student(name, marks)
student.display()
