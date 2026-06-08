# Question 1
def print_natural_numbers():
    """Prints the first 10 natural numbers."""
    print("First 10 Natural Numbers:")
    for i in range(1, 11):   # Loop from 1 to 10
        print(i, end=" ")
    print()  # New line
# Call the function
print_natural_numbers()


# Question 2
def sum_of_n(n):
    """Returns the sum of first n natural numbers."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
# Take input from user
n = int(input("Enter value of N: "))
result = sum_of_n(n)
print(f"Sum of first {n} natural numbers = {result}")


# Question 3
def reverse_number(num):
    """Returns the reverse of the given number."""
    reversed_num = int(str(num)[::-1])  # Convert to string, reverse, convert back
    return reversed_num
# Take input from user
num = int(input("Enter a number to reverse: "))
print(f"Reverse of {num} = {reverse_number(num)}")


# Question 4
def count_digits(num):
    """Returns the count of digits in the given number."""
    count = len(str(abs(num)))  # abs() handles negative numbers
    return count
# Take input from user
num = int(input("Enter a number: "))
print(f"Number of digits in {num} = {count_digits(num)}")


# Question 5
# A palindrome number reads the same forwards and backwards
# Example: 121, 1331, 12321
def is_palindrome(num):
    """Returns True if the number is a palindrome, else False."""
    original = str(num)
    reversed_str = original[::-1]  # Reverse the string
    return original == reversed_str

# Take input from user
num = int(input("Enter a number to check palindrome: "))

if is_palindrome(num):
    print(f"{num} is a Palindrome number.")
else:
    print(f"{num} is NOT a Palindrome number.")


# Question 6
# Fibonacci Sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
# Each term = sum of previous two terms
def fibonacci_series(n):
    """Prints Fibonacci series up to n terms."""
    a, b = 0, 1
    print(f"Fibonacci Series ({n} terms):", end=" ")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b  # Update both values at once
    print()
# Take input from user
n = int(input("Enter number of terms for Fibonacci series: "))
fibonacci_series(n)


# Question 7
# ---- operation functions ----
def add(a, b):
    """Returns sum of a and b."""
    return a + b
def subtract(a, b):
    """Returns difference of a and b."""
    return a - b
def multiply(a, b):
    """Returns product of a and b."""
    return a * b
def divide(a, b):
    """Returns division of a by b."""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b
# ---- Display menu ----
print("========== CALCULATOR ==========")
print("Select operation:")
print("  1. Addition       (+)")
print("  2. Subtraction    (-)")
print("  3. Multiplication (*)")
print("  4. Division       (/)")
print("================================")
# ---- User selects operation ----
choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
# ---- Perform calculation and display result ----
if choice == '1':
    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"Result: {num1} × {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"Result: {num1} ÷ {num2} = {divide(num1, num2)}")
else:
    print("Invalid choice! Please select 1, 2, 3, or 4.")


# Question 8
# We write student data into 'students.txt'
# Open file in write mode ('w') — creates the file if it doesn't exist
with open("students.txt", "w") as file:
    file.write("Name,Roll No,Class,Marks\n")           # Header line
    file.write("Aarav Sharma,101,10A,88\n")
    file.write("Priya Singh,102,10A,92\n")
    file.write("Rohit Verma,103,10B,75\n")
    file.write("Sneha Gupta,104,10B,68\n")
    file.write("Karan Mehta,105,10C,55\n")
print("Student details have been saved to 'students.txt'")


# Question 9
# Open file in read mode ('r')
print("Reading data from 'students.txt':\n")
with open("students.txt", "r") as file:
    lines = file.readlines()  # Read all lines into a list
# Print each line
for line in lines:
    print(line.strip())  # strip() removes the trailing newline '\n'


# Question 10
# try     → code that might cause an error
# except  → what to do if an error occurs
# finally → always runs, error or not
try:
    numerator   = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))
    result = numerator / denominator  # This may cause ZeroDivisionError
    print(f"Result: {numerator} / {denominator} = {result}")
except ZeroDivisionError:
    # This block runs only if denominator is 0
    print("Error: Division by zero is not allowed!")
except ValueError:
    # This block runs if user enters a non-numeric value
    print("Error: Please enter valid numbers only!")
finally:
    # This block always runs regardless of error
    print("Program completed.")


# Question 11
class Student:
    """A class to represent a Student."""
    def __init__(self, name, marks):
        """Constructor to initialize name and marks."""
        self.name  = name    # Student name
        self.marks = marks   # List of marks for 5 subjects
    def calculate_total(self):
        """Returns total marks."""
        return sum(self.marks)
    def calculate_percentage(self):
        """Returns percentage out of 500."""
        return (self.calculate_total() / 500) * 100
    def get_grade(self):
        """Returns grade based on percentage."""
        percent = self.calculate_percentage()
        if percent >= 90:
            return "A+"
        elif percent >= 80:
            return "A"
        elif percent >= 70:
            return "B"
        elif percent >= 60:
            return "C"
        elif percent >= 40:
            return "D"
        else:
            return "F"
    def display_report(self):
        """Displays the student report card."""
        print("\n" + "="*40)
        print("        STUDENT REPORT CARD")
        print("="*40)
        print(f"  Name       : {self.name}")
        print(f"  Marks      : {self.marks}")
        print(f"  Total      : {self.calculate_total()} / 500")
        print(f"  Percentage : {self.calculate_percentage():.2f}%")
        print(f"  Grade      : {self.get_grade()}")
        print("="*40)
# ---- Create Student objects ----
s1 = Student("Aarav Sharma", [88, 92, 76, 85, 90])
s2 = Student("Priya Singh",  [70, 65, 80, 55, 60])
# ---- Display reports ----
s1.display_report()
s2.display_report()
# ---- Create a student from user input ----
print("\n--- Enter your details ---")
uname = input("Enter your name: ")
umarks = []
subjects = ["Maths", "Science", "English", "Hindi", "Computer"]
for sub in subjects:
    m = float(input(f"Enter {sub} marks (out of 100): "))
    umarks.append(m)
user_student = Student(uname, umarks)
user_student.display_report()