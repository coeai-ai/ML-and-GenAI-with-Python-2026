#1.Function to print frst 10 natural number 
def print_numbers():
    for i in range(1, 11):
        print(i)

# Function Call
print_numbers()

#2.Function to calculate sum 
def sum_natural(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total

# User Input
n = int(input("Enter N: "))

print("Sum =", sum_natural(n))

#3.Reverse a number 
def reverse_number(num):
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return reverse

# User Input
num = int(input("Enter a number: "))

print("Reverse =", reverse_number(num))

#4.Count digit of a number
def count_digits(num):
    count = 0

    while num > 0:
        count = count + 1
        num = num // 10

    return count

# User Input
num = int(input("Enter a number: "))

print("Total digits =", count_digits(num))

#5. Check palindrome number
def palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if original == reverse:
        return True
    else:
        return False

# User Input
num = int(input("Enter a number: "))

if palindrome(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

#6.Generate Fibonacci Series
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

# User Input
n = int(input("Enter number of terms: "))

fibonacci(n)

#7.Calculator using functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 1:
    print("Answer =", add(num1, num2))

elif choice == 2:
    print("Answer =", subtract(num1, num2))

elif choice == 3:
    print("Answer =", multiply(num1, num2))

elif choice == 4:
    print("Answer =", divide(num1, num2))

else:
    print("Invalid Choice")


# 8.Creating a text file and storing student details

file = open("student.txt", "w")

name = input("Enter student name: ")
roll = input("Enter roll number: ")
marks = input("Enter marks: ")

file.write("Name: " + name + "\n")
file.write("Roll No: " + roll + "\n")
file.write("Marks: " + marks)

file.close()

print("Student details saved successfully.")

#9. Reading data from a text file

file = open("student.txt", "r")

data = file.read()

print("Student Details:")
print(data)

file.close()

#10.Handle division by zero using exception handling

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

#11.Create a student class with name and marks 

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


# User Input
name = input("Enter student name: ")
marks = int(input("Enter marks: "))

s1 = Student(name, marks)

s1.display()