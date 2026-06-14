# Question 1 : Function to print first 10 natural numbers
def print_natural_numbers():
    print("First 10 Natural Numbers:")
    for i in range(1, 11):
        print(i, end=" ")
    print()
print_natural_numbers()


# Question 2: Function to calculate sum of first N natural numbers
def sum_natural_numbers(n):
    return n * (n + 1) // 2
n = int(input("\nEnter N: "))
print("Sum =", sum_natural_numbers(n))

# Question 3: Function to reverse a number
def reverse_number(num):
    return int(str(num)[::-1])

num = int(input("\nEnter a number to reverse: "))
print("Reversed Number =", reverse_number(num))

# Question 4: Function to count digits in a number
def count_digits(num):
    return len(str(abs(num)))
num = int(input("\nEnter a number: "))
print("Number of Digits =", count_digits(num))

# Question 5:  Function to check palindrome number
def is_palindrome(num):
    return str(num) == str(num)[::-1]

num = int(input("\nEnter a number: "))

if is_palindrome(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

# Question 6: Function to generate Fibonacci series

def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci Series:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

terms = int(input("\nEnter number of terms: "))
fibonacci(terms)

# Question 7: Calculator Using Functions
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

print("\nCalculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice (1-4): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result =", add(num1, num2))

elif choice == 2:
    print("Result =", subtract(num1, num2))

elif choice == 3:
    print("Result =", multiply(num1, num2))

elif choice == 4:
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print("Result =", divide(num1, num2))

else:
    print("Invalid Choice")

# Question 8: Create a text file and store student details
file = open("student.txt", "w")

name = input("\nEnter Student Name: ")
roll = input("Enter Roll Number: ")

file.write("Name: " + name + "\n")
file.write("Roll Number: " + roll + "\n")

file.close()

print("Student details saved in student.txt")

# Question 9: Read data from a file
file = open("student.txt", "r")
print("\nContents of student.txt:")
print(file.read())
file.close()

# Question 10: Handle division by zero using exception handling
try:
    a = int(input("\nEnter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result =", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Question 11: Create a Student class with name and marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Marks:", self.marks)
student_name = input("\nEnter Student Name: ")
student_marks = float(input("Enter Marks: "))

student = Student(student_name, student_marks)

student.display()