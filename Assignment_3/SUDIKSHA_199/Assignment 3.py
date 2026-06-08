
# Assignment 3

# 1. Function to print first 10 natural numbers
def print_natural_numbers():
    print("First 10 Natural Numbers:")
    for i in range(1, 11):
        print(i, end=" ")
    print()


# 2. Function to calculate sum of first N natural numbers
def sum_natural_numbers(n):
    return n * (n + 1) // 2


# 3. Function to reverse a number
     #Let num be the number of letters in the word
def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev


# 4. Function to count digits in a number
def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count


# 5. Function to check palindrome number
def is_palindrome(num):
    return num == reverse_number(num)


# 6. Function to generate Fibonacci series
def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci Series:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


# 7. Calculator using functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


print("\nCalculator")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Result:", add(a, b))
elif choice == 2:
    print("Result:", subtract(a, b))
elif choice == 3:
    print("Result:", multiply(a, b))
elif choice == 4:
    print("Result:", divide(a, b))
else:
    print("Invalid Choice")


# 8. Create a text file and store student details
with open("student.txt", "w") as file:
    file.write("Name: Sudiksha\n")
    file.write("Roll No: 199\n")
    file.write("Marks: 95\n")

print("Student details written to file.")


# 9. Read data from a file
with open("student.txt", "r") as file:
    print("\nReading Student File:")
    print(file.read())


# 10. Handle division by zero using exception handling
try:
    x = int(input("\nEnter numerator: "))
    y = int(input("Enter denominator: "))
    print("Result =", x / y)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


# 11. Student class with name and marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Marks:", self.marks)


s1 = Student("Sudiksha", 95)
s1.display()


# Function Calls for testing
print_natural_numbers()

n = int(input("\nEnter N for sum of natural numbers: "))
print("Sum =", sum_natural_numbers(n))

num = int(input("\nEnter a number: "))
print("Reverse =", reverse_number(num))
print("Digit Count =", count_digits(num))

if is_palindrome(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

terms = int(input("\nEnter number of Fibonacci terms: "))
fibonacci(terms)