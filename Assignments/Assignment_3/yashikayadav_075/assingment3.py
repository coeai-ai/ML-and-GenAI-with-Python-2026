# 1. Function to print first 10 natural numbers
def print_numbers():
    for i in range(1, 11):
        print(i)

print("First 10 Natural Numbers:")
print_numbers()


# 2. Function to calculate sum of first N natural numbers
def sum_n(n):
    return n * (n + 1) // 2

n = int(input("\nEnter N: "))
print("Sum =", sum_n(n))


# 3. Function to reverse a number
def reverse_num(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev

num = int(input("\nEnter a number: "))
print("Reverse =", reverse_num(num))


# 4. Function to count digits
def count_digits(num):
    return len(str(num))

num = int(input("\nEnter a number: "))
print("Digits =", count_digits(num))


# 5. Function to check palindrome
def palindrome(num):
    return str(num) == str(num)[::-1]

num = int(input("\nEnter a number: "))
if palindrome(num):
    print("Palindrome")
else:
    print("Not Palindrome")


# 6. Function to generate Fibonacci series
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("\nEnter number of terms: "))
fibonacci(n)


# 7. Calculator using functions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

print("\nCalculator")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+,-,*,/): ")

if op == "+":
    print("Result =", add(a, b))
elif op == "-":
    print("Result =", sub(a, b))
elif op == "*":
    print("Result =", mul(a, b))
elif op == "/":
    print("Result =", div(a, b))
else:
    print("Invalid operation")


# 8. Create and read a text file
file = open("student.txt", "w")
file.write("Name: Yashika Yadav\n")
file.write("Enrollment: 07501192025\n")
file.close()

file = open("student.txt", "r")
print("\nStudent File Data:")
print(file.read())
file.close()


# 9. Exception handling for division by zero
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print("Result =", a / b)
except ZeroDivisionError:
    print("Division by zero is not allowed")


# 10. Student class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("\nStudent Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Yashika Yadav", 95)
s1.display()