# 1) Function to Print First 10 Natural Numbers

def print_natural_numbers():
    for i in range(1, 11):
        print(i)

print_natural_numbers()


# 2) Function to Calculate Sum of First N Natural Numbers

def sum_natural(n):
    return sum(range(1, n + 1))

n = int(input("Enter N: "))
print("Sum =", sum_natural(n))


# 3) Function to Reverse a Number

def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev

num = int(input("Enter Number: "))
print("Reversed Number =", reverse_number(num))


# 4) Function to Count Digits in a Number

def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count

num = int(input("Enter Number: "))
print("Number of Digits =", count_digits(num))


# 5) Function to Check Palindrome Number

def palindrome(num):
    original = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10

    if original == rev:
        print("Palindrome Number")
    else:
        print("Not a Palindrome Number")

num = int(input("Enter Number: "))
palindrome(num)


# 6) Function to Generate Fibonacci Series

def fibonacci(n):
    a, b = 0, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("\nEnter Number of Terms: "))
fibonacci(n)


# 7) Calculator Using Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("\n1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter Choice: "))

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


# 8) Create a Text File and Store Student Details

file = open("student.txt", "w")

name = input("Enter Student Name: ")
marks = input("Enter Marks: ")

file.write("Name: " + name + "\n")
file.write("Marks: " + marks)

file.close()

print("Student Details Saved")


# 9) Read Data from a File

file = open("student.txt", "r")

data = file.read()
print(data)

file.close()


# 10) Handle Division by Zero Using Exception Handling

try:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))

    result = a / b
    print("Result =", result)

except ZeroDivisionError:
    print("Cannot Divide by Zero")


# 11) Create a Student Class with Name and Marks

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

name = input("Enter Student Name: ")
marks = float(input("Enter Marks: "))

s1 = Student(name, marks)
s1.display()