#1.Create a function to print first 10 natural numbers
def print_natural_numbers():
    for i in range(1, 11):
        print(i)
print_natural_numbers()


#2.Create a function to calculate sum of first N natural numbers
def sum_n_numbers(n):
    return n * (n + 1) // 2
n = int(input("Enter N: "))
print("Sum =", sum_n_numbers(n))


#3. Create a function to reverse a number
def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev
num = int(input("Enter a number: "))
print("Reverse =", reverse_number(num))


#4. Create a function to count digits in a number
def count_digits(num):
    count = 0

    while num > 0:
        count += 1
        num //= 10

    return count

num = int(input("Enter a number: "))
print("Digits =", count_digits(num))


#5. Create a function to check palindrome number
def is_palindrome(num):
    temp = num
    rev = 0

    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10

    return num == rev

num = int(input("Enter a number: "))

if is_palindrome(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")


#6. Create a function to generate Fibonacci series
def fibonacci(n):
    a, b = 0, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter number of terms: "))
fibonacci(n)


#7. Calculator using functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter choice: "))

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


#Create a text file and store student details
file = open("student.txt", "w")

name = input("Enter Name: ")
marks = input("Enter Marks: ")

file.write("Name: " + name + "\n")
file.write("Marks: " + marks)

file.close()

print("Data Saved Successfully")


#Read data from a file
file = open("student.txt", "r")

data = file.read()
print(data)

file.close()


#Handle division by zero using exception handling
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Result =", a / b)

except ZeroDivisionError:
    print("Division by zero is not allowed")


#Create a Student class with name and marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s = Student("Deepanshi", 95)
s.display()