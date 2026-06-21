# Create a function to print first 10 natural numbers
def print_natural_numbers(n):
    for i in range(1, n + 1):
        print(i)
print("First 10 natural numbers:")
print_natural_numbers(10)

# Create a function to calculate sum of first N natural numbers
def sum_natural_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
print("Sum of first 10 natural numbers:")
print(sum_natural_numbers(10))

# Create a function to reverse a number
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num
number = int(input("Enter a number to reverse: "))
print("Reversed number:", reverse_number(number))

# Create a function to count digits in a number
def count_digits(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count
number = int(input("Enter a number to count digits: "))
print("Number of digits:", count_digits(number))

# Create a function to check palindrome number
def is_palindrome(num):
    original_num = num
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return original_num == reversed_num
number = int(input("Enter a number to check palindrome: "))
if is_palindrome(number):
    print(number, "is a palindrome.")
else:
    print(number, "is not a palindrome.")

# Create a function to generate Fibonacci Series
def fibonacci_series(n_terms):
    n1, n2 = 0, 1
    count = 0
    series = []
    while count < n_terms:
        series.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    return series
n_terms = int(input("Enter the number of terms for Fibonacci series: "))
print("Fibonacci sequence:")
print(fibonacci_series(n_terms))

# Calculator Using Functions that contains the following features: User selects operation, Program performs calculation, Display result
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter choice (1/2/3/4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        result = num1 + num2
        print("Result:", result)
    elif choice == '2':
        result = num1 - num2
        print("Result:", result)
    elif choice == '3':
        result = num1 * num2
        print("Result:", result)
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid input.")

# Create a text fille and store student details in it using functions and user input
def store_student_details():
    num_students = int(input("Enter the number of students: "))
    with open("student_details.txt", "w") as file:
        for i in range(num_students):
            name = input("Enter the name of student {}: ".format(i + 1))
            marks = float(input("Enter the marks of {}: ".format(name)))
            file.write("Name: {}, Marks: {}\n".format(name, marks))
    print("Student details have been stored in 'student_details.txt'.")
store_student_details()

# Read data from a file
def read_student_details():
    try:
        with open("student_details.txt", "r") as file:
            print("Student Details:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("The file 'student_details.txt' does not exist.")
read_student_details()

# Handle division by zero using exception handling
def safe_division():
    try:
        num1 = float(input("Enter numerator: "))
        num2 = float(input("Enter denominator: "))
        result = num1 / num2
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
safe_division()

# Create a Student class with name and marks as attributes and a method to display student details
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display_details(self):
        print("Name: {}, Marks: {}".format(self.name, self.marks))
student_name = input("Enter student name: ")
student_marks = float(input("Enter student marks: "))
student = Student(student_name, student_marks)
student.display_details()

