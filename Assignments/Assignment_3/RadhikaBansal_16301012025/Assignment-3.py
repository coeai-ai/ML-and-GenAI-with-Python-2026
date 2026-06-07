
# 1. Create a function to print first 10 natural numbers
def print_first_10_natural_numbers():
    for i in range(1, 11):
        print(i)
print("First 10 Natural Numbers:")
print_first_10_natural_numbers()

# 2. Create a function to calculate sum of first N natural numbers
def sum_of_n_natural_numbers(n):
    return n * (n + 1) // 2
n = int(input("\nEnter N for sum of natural numbers: "))
print("Sum =", sum_of_n_natural_numbers(n))

# 3. Create a function to reverse a number
def reverse_number(num):
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10
    return reverse
num = int(input("\nEnter a number to reverse: "))
print("Reversed Number =", reverse_number(num))

# 4. Create a function to count digits in a number
def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count
num = int(input("\nEnter a number to count digits: "))
print("Number of Digits =", count_digits(num))

# 5. Create a function to check palindrome number
def is_palindrome(num):
    return num == reverse_number(num)
num = int(input("\nEnter a number to check palindrome: "))
if is_palindrome(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

# 6. Create a function to generate Fibonacci series
def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
n = int(input("\nEnter number of terms for Fibonacci Series: "))
print("Fibonacci Series:")
fibonacci_series(n)

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
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice (1-4): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result =", add(num1, num2))
elif choice == 2:
    print("Result =", subtract(num1, num2))
elif choice == 3:
    print("Result =", multiply(num1, num2))
elif choice == 4:
    if num2 != 0:
        print("Result =", divide(num1, num2))
    else:
        print("Division by zero is not allowed")
else:
    print("Invalid Choice")

# 8. Create a text file and store student details
with open("student_details.txt", "w") as file:
    name = input("\nEnter Student Name: ")
    marks = input("Enter Student Marks: ")
    file.write(f"Name: {name}\nMarks: {marks}\n")
print("Student details saved to file.")

# 9. Read data from a file
print("\nReading Student Details:")
with open("student_details.txt", "r") as file:
    print(file.read())

# 10. Handle division by zero using exception handling
try:
    a = int(input("\nEnter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result =", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# 11. Create a Student class with name and marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Marks:", self.marks)

name = input("\nEnter student name: ")
marks = float(input("Enter student marks: "))

student = Student(name, marks)
student.display()
