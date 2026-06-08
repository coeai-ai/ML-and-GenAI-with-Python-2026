# ASSIGNMENT - 3
# Create a function to print first 10 natural numbers
def print_natural_numbers():
    for i in range(1, 11):
        print(i, end=" ")

print_natural_numbers()

# Create a function to calculate sum of first N natural numbers
def calculate_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum+=i
    return sum

print(calculate_sum(5))
print(calculate_sum(10))

# Create a function to reverse a number
def reverse_num(n):
    return int(str(n)[::-1])   

print(reverse_num(1234))       
print(reverse_num(516382)) 

# Create a function to count digits in a number
def count_digits(n):
    return len(str(abs(n)))

print(count_digits(1234))        
print(count_digits(-98765))      

# Create a function to check pallindrome number
def check_pallindrome(n):
    return n == int(str(n)[::-1])
    
print(check_pallindrome(13431))
print(check_pallindrome(542))

# Create a function to generate Fibonacci series
def fibonacci_series(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci_series(10)  

''' 
Calculator using functions that constains the following features:
    - User selects operations
    - Program performs calculations
    - Display result
'''
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("---- Calulator ----")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid input")

calculator()

# Create a text file and store student details
with open("students.txt", "w") as file:
    file.write("----- Student Details -----\n")
    file.write("Name: Dorain Smith, Age: 20, Course: Computer Science\n")
    file.write("Name: Jane Austen, Age: 22, Course: Mathematics\n")
    file.write("Name: Alex Brown, Age: 19, Course: Physics\n")

# # Read data from a file
with open("students.txt", "r") as file:
    data = file.read()

print("\nReading data from file:")
print(data)

# Handle division by zero using exception handling
def division_by_zero(x, y):
    try:
        result = x / y
        print("Result:", result)
    except ZeroDivisionError:
        print("Error! Division by zero is not allowed.")

division_by_zero(10, 2)
division_by_zero(10, 0)

# Create a Student class with name and marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name} \nMarks: {self.marks}\n")

s1 = Student("Harry", 100)
s2 = Student("Rose", 98)

s1.display()
s2.display()
