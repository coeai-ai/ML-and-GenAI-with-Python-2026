# Assignment 3

# Question 1

# Function to print first 10 natural numbers
def print_natural_numbers(): 
# Loop to iterate from 1 to 10
    for i in range(1, 11): 
        print(i)
# Calling the function to print natural numbers
print_natural_numbers() 

# Question 2

# Function to calculate the sum of first n natural numbers
def sum_natural_numbers(n): 
    return n * (n + 1) // 2
# Calling the function to calculate the sum of first 10 natural numbers
print(sum_natural_numbers(10)) 

# Question 3

# Function to reverse a number
def reverse_number(num): 
    # Variable to store the reversed number
    rev = 0 
    # Loop to reverse the number
    while num > 0: 
        rev = rev * 10 + num % 10
        num //= 10
    # Returning the reversed number
    return rev 
# Calling the function to reverse the number 1234
print(reverse_number(1234)) 


# Question 4

# Variable to count the number of digits
def count_digits(num): 
    # Loop to count the digits
    count = 0 
    # Incrementing the count for each digit
    while num > 0: 
        count += 1
        num //= 10
    # Calling the function to count the digits in the number 12345
    return count 
print(count_digits(12345)) # Output: 5

# Question 5

# Store the original number for comparison
def is_palindrome(num): 
    # Variable to store the reversed number
    original = num 
    # Loop to reverse the number
    rev = 0 
    # Update the reversed number
    while num > 0: 
        rev = rev * 10 + num % 10
        num //= 10
    # Check if the original number is equal to the reversed number
    return original == rev 
print(is_palindrome(121)) # Output: True
print(is_palindrome(123)) # Output: False

# Question 6

# Function to print the first n Fibonacci numbers
def fibonacci(n): 
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1 
    # Loop to generate Fibonacci numbers
    for i in range(n): 
        # Print the current Fibonacci number
        print(a, end=" ") 
        # Update a and b to the next two Fibonacci numbers
        a, b = b, a + b 

# Question 7

# Class to represent a student
class Student: 
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
# Function to add two numbers
def add(a, b): 
    return a + b
# Function to subtract two numbers
def subtract(a, b): 
    return a - b
# Function to multiply two numbers
def multiply(a, b): 
    return a * b
# Function to divide two numbers with error handling for division by zero
def divide(a, b): 
    try: # Attempt to perform division
        return a / b
    except ZeroDivisionError: # Handle division by zero error
        return "Division by zero is not allowed."
# Displaying the menu for the calculator
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
# Taking user input for the choice of operation and the two numbers
choice = int(input("Enter choice: ")) 
# Validating the user's choice and performing the corresponding operation
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
# Performing the selected operation based on the user's choice and displaying the result
if choice == 1:
    print("Result =", add(a, b))
elif choice == 2:
    print("Result =", subtract(a, b))
elif choice == 3:
    print("Result =", multiply(a, b))
elif choice == 4:
    print("Result =", divide(a, b))
# Writing student details to a file
with open("students.txt", "w") as file: 
    file.write("Rahul,85\n")
    file.write("Priya,90\n")
# Reading and displaying student details from the file
with open("students.txt", "r") as file: 
    print("\nStudent Details:")
    print(file.read())
# Creating an instance of the Student class and displaying the details
s1 = Student("Rahul", 85) 
s1.display() # Output: Name: Rahul, Marks: 85

