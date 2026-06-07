# 1:Create a function to print first 10 natural numbers.

def print_numbers():
    for i in range(1, 11):
        print(i)

print_numbers()

# 2:Create a function to calculate sum of first N natural numbers.

def sum_natural(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Enter N: "))
print("Sum =", sum_natural(n))

# 3:Create a function to reverse a number.

def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return rev

num = int(input("Enter a number: "))
print("Reversed Number =", reverse_number(num))

# 4:Create a function to count digits in a number.

def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num = num // 10
    return count

num = int(input("Enter a number: "))
print("Number of digits =", count_digits(num))

# 5:Create a function to check palindrome number

def palindrome(num):
    original = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    if original == rev:
        print("Palindrome Number")
    else:
        print("Not a Palindrome Number")

num = int(input("Enter a number: "))
palindrome(num)

# 6:Create a function to generate Fibonacci series

def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

n = int(input("Enter number of terms: "))
fibonacci(n)

# 7: Calculator Using Functions.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice (1-4): "))
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

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


# 8: Create a text file and store student details

file = open("student.txt", "w")
name = input("Enter student name: ")
roll = input("Enter roll number: ")

file.write("Name: " + name + "\n")
file.write("Roll No: " + roll + "\n")
file.close()

print("Student details saved in file.")


# 9: Read data from a file

file = open("student.txt", "r")
data = file.read()
print("\nStudent Details:")
print(data)
file.close()


# 10: Handle division by zero using exception handling

try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2
    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


# 11: Create a Student class with name and marks

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Annu", 90)
s1.display()