#Create a function to print first 10 natural numbers
def print_natural_numbers():
    for i in range(1, 11):
        print(i)

print_natural_numbers()

#Create a function to calculate sum of first N natural numbers
def sum_natural_numbers(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    return total_sum

#Create a function to reverse a number
def reverse_number(number):
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    return reversed_number

#Create a function to count digits in a number
def count_digits(number):
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count

#Create a function to check palindrome number
def is_palindrome(number):
    original_number = number
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    return original_number == reversed_number

#Create a function to generate Fibonacci series
def fibonacci_series(n):
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print("Fibonacci sequence:")
        print(0)
    else:
        print("Fibonacci sequence:")
        n1, n2 = 0, 1
        count = 0
        while count < n:
            print(n1, end=" ")
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        print()

#Calculator Using Functions that contains the following features; User selects operation, Program performs calculation, Display result
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a % b

def power(a, b):
    return a ** b

print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Power")

choice = input("Enter your choice (1-6): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == '1':
    result = add(num1, num2)
    operator = "+"
elif choice == '2':
    result = subtract(num1, num2)
    operator = "-"
elif choice == '3':
    result = multiply(num1, num2)
    operator = "*"
elif choice == '4':
    result = divide(num1, num2)
    operator = "/"
elif choice == '5':
    result = modulus(num1, num2)
    operator = "%"
elif choice == '6':
    result = power(num1, num2)
    operator = "**"
else:
    result = None
    print("Invalid choice")

if result is not None:
    print(f"Result: {num1} {operator} {num2} = {result}")

#Create a text file and store student details
with open("student_details.txt", "w") as file:
    file.write("Name: Rishika\n")
    file.write("Roll Number: 2440140204\n")
    file.write("Grade: A\n")
    file.write("Total Marks: 450\n")
    file.write("Percentage: 90%\n")

#Read data from a file
with open("student_details.txt", "r") as file:
    data = file.read()
    print(data)

#Handle division by zero using exception handling
try:
    result = divide(num1, num2)
    print(f"Result: {num1} / {num2} = {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

#Create a Student class with name and marks
class Student:
    def __init__(self, name, rollno, grade, total_marks, percentage):
        self.name = name
        self.rollno = rollno
        self.grade = grade
        self.total_marks = total_marks
        self.percentage = percentage

    def display_details(self):
        print("Name: ", self.name)
        print("Roll Number: ", self.rollno)
        print("Grade: ", self.grade)
        print("Total Marks: ", self.total_marks)
        print("Percentage: ", self.percentage, "%")

#Create a student object
student = Student("Rishika", 2440140204, "A", 450, 90)

#Display student details
student.display_details()
