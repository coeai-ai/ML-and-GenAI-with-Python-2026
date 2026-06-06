# 1. Function to print first 10 natural numbers

def print_natural_numbers():
    for i in range(1, 11):
        print(i)


print("First 10 Natural Numbers:")
print_natural_numbers()


# 2. Function to calculate sum of first N natural numbers

def sum_natural_numbers(n):
    sum = 0

    for i in range(1, n + 1):
        sum = sum + i

    print("Sum =", sum)


n = int(input("\nEnter N: "))
sum_natural_numbers(n)


# 3. Function to reverse a number

def reverse_number(num):
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    print("Reverse number =", rev)


num = int(input("\nEnter a number to reverse: "))
reverse_number(num)


# 4. Function to count digits in a number

def count_digits(num):
    count = 0

    while num > 0:
        count = count + 1
        num = num // 10

    print("Number of digits =", count)


num = int(input("\nEnter a number to count digits: "))
count_digits(num)


# 5. Function to check palindrome number

def check_palindrome(num):
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


num = int(input("\nEnter a number to check palindrome: "))
check_palindrome(num)


# 6. Function to generate Fibonacci series

def fibonacci_series(n):
    a = 0
    b = 1

    print("Fibonacci Series:")

    for i in range(n):
        print(a)
        c = a + b
        a = b
        b = c


n = int(input("\nEnter number of terms for Fibonacci series: "))
fibonacci_series(n)


# 7. Calculator using Functions

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

choice = int(input("Enter your choice: "))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

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

name = input("\nEnter student name: ")
roll_no = input("Enter roll number: ")
marks = input("Enter marks: ")

file.write("Name: " + name + "\n")
file.write("Roll Number: " + roll_no + "\n")
file.write("Marks: " + marks + "\n")

file.close()

print("Student details stored successfully.")


# 9. Read data from a file

file = open("student.txt", "r")

data = file.read()

print("\nData from file:")
print(data)

file.close()


# 10. Handle division by zero using exception handling

try:
    a = int(input("\nEnter first number for division: "))
    b = int(input("Enter second number for division: "))

    result = a / b

    print("Result =", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")



# 11. Create a Student class with name and marks

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


name = input("\nEnter student name for class: ")
marks = int(input("Enter marks: "))

s1 = Student(name, marks)

print("\nStudent Details using Class:")
s1.display()