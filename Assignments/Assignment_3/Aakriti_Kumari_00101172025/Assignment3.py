# Assignment 3

# 1. Function to print first 10 natural numbers
def print_natural_numbers():
    print("First 10 natural numbers are:")
    for i in range(1, 11):
        print(i, end=" ")
    print()


# 2. Function to calculate sum of first N natural numbers
def sum_natural_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print("Sum of first", n, "natural numbers is:", total)


# 3. Function to reverse a number
def reverse_number(num):
    rev = 0
    temp = num

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10

    print("Reverse of", temp, "is:", rev)
    return rev


# 4. Function to count digits in a number
def count_digits(num):
    count = 0
    temp = num

    while num > 0:
        count += 1
        num //= 10

    print("Number of digits in", temp, "is:", count)


# 5. Function to check palindrome number
def palindrome_number(num):
    temp = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10

    if temp == rev:
        print(temp, "is a palindrome number")
    else:
        print(temp, "is not a palindrome number")


# 6. Function to generate Fibonacci series
def fibonacci(n):
    a = 0
    b = 1

    print("Fibonacci series:")
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
    print()


# 7. Calculator using functions
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed"


print("\nCalculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

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


# 8. Create a text file and store student details
file = open("student.txt", "w")
file.write("Name: Aakriti\n")
file.write("Roll No: 101\n")
file.write("Marks: 95\n")
file.close()

print("\nStudent details stored in file.")


# 9. Read data from file
file = open("student.txt", "r")
data = file.read()
print("\nStudent Details:")
print(data)
file.close()


# 10. Handle division by zero using exception handling
try:
    x = int(input("Enter numerator: "))
    y = int(input("Enter denominator: "))
    result = x / y
    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


# 11. Student class with name and marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("\nStudent Information")
        print("Name:", self.name)
        print("Marks:", self.marks)


s1 = Student("Aakriti", 95)
s1.display()


