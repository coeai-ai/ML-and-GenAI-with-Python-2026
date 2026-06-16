"""Assignment 3: Basic Python programs covering loops, numbers, a calculator,
a Student class, and file read/write operations."""


# 1. Function to print first 10 natural numbers
def print_natural():
    """Print the first 10 natural numbers."""
    for i in range(1, 11):
        print(i, end=" ")
    print()


# 2. Function to calculate sum of first N natural numbers
def sum_natural(n):
    """Return the sum of the first n natural numbers."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


# 3. Function to reverse a number
def reverse_number(n):
    """Return the digits of n reversed."""
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev


# 4. Function to count digits in a number
def count_digits(n):
    """Return the number of digits in n."""
    count = 0
    if n == 0:
        return 1
    while n > 0:
        count += 1
        n //= 10
    return count


# 5. Function to check palindrome number
def is_palindrome(n):
    """Return True if n reads the same reversed."""
    return n == reverse_number(n)


# 6. Function to generate Fibonacci series
def fibonacci(terms):
    """Print the Fibonacci series up to the given number of terms."""
    a, b = 0, 1
    for _ in range(terms):
        print(a, end=" ")
        a, b = b, a + b
    print()


# 7. Calculator using functions
def add(a, b):
    """Return a + b."""
    return a + b


def subtract(a, b):
    """Return a - b."""
    return a - b


def multiply(a, b):
    """Return a * b."""
    return a * b


def divide(a, b):
    """Return a / b, handling division by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"


def calculator():
    """Run a simple interactive calculator."""
    print("\n--- Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Select operation (1-4): ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if choice == "1":
        result = add(a, b)
    elif choice == "2":
        result = subtract(a, b)
    elif choice == "3":
        result = multiply(a, b)
    elif choice == "4":
        result = divide(a, b)
    else:
        result = "Invalid choice"
    print("Result:", result)


# 8. Student class with name and marks
class Student:
    """Represent a student with a name and marks."""

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        """Print the student's name and marks."""
        print("Name:", self.name)
        print("Marks:", self.marks)


# 9. Create a text file and store student details
def write_student_file():
    """Prompt for student details and write them to student.txt."""
    name = input("Enter student name: ")
    marks = input("Enter student marks: ")
    with open("student.txt", "w", encoding="utf-8") as f:
        f.write("Name: " + name + "\n")
        f.write("Marks: " + marks + "\n")
    print("Details stored in student.txt")


# 10. Read data from a file
def read_student_file():
    """Read and print the contents of student.txt."""
    try:
        with open("student.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found. Please create it first.")


def main():
    """Driver code demonstrating each function."""
    print("\n=== First 10 Natural Numbers ===")
    print_natural()

    print("\n=== Sum of First N Natural Numbers ===")
    num = int(input("Enter N: "))
    print("Sum:", sum_natural(num))

    print("\n=== Reverse a Number ===")
    num = int(input("Enter a number to reverse: "))
    print("Reversed:", reverse_number(num))

    print("\n=== Count Digits ===")
    num = int(input("Enter a number: "))
    print("Number of digits:", count_digits(num))

    print("\n=== Palindrome Check ===")
    num = int(input("Enter a number: "))
    if is_palindrome(num):
        print(num, "is a palindrome")
    else:
        print(num, "is not a palindrome")

    print("\n=== Fibonacci Series ===")
    terms = int(input("Enter number of terms: "))
    fibonacci(terms)

    calculator()

    print("\n=== Store Student Details in File ===")
    write_student_file()

    print("\n=== Read Student Details from File ===")
    read_student_file()

    print("\n=== Student Class ===")
    name = input("Enter student name: ")
    marks = float(input("Enter student marks: "))
    s1 = Student(name, marks)
    s1.display()


if __name__ == "__main__":
    main()
