
# Print first 10 natural numbers
def print_natural_numbers():
    for i in range(1, 11):
        print(i, end=" ")
    print()

#  Sum of first N natural numbers
def sum_natural_numbers():
    n = int(input("Enter N: "))
    total = sum(range(1, n + 1))
    print("Sum =", total)

#  Reverse a number
def reverse_number():
    num = int(input("Enter a number: "))
    rev = 0
    temp = num
    while temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10
    print("Reversed number =", rev)

#  Count digits in a number
def count_digits():
    num = int(input("Enter a number: "))
    count = 0
    temp = num
    while temp > 0:
        temp //= 10
        count += 1
    print("Number of digits =", count)

# Check palindrome
def check_palindrome():
    num = int(input("Enter a number: "))
    if num == int(str(num)[::-1]):
        print(num, "is a palindrome")
    else:
        print(num, "is not a palindrome")

# Generate Fibonacci series
def fibonacci_series():
    n = int(input("Enter number of terms: "))
    a, b = 0, 1
    print("Fibonacci Series:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

# Calculator using functions
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero!"

def calculator():
    print("Select operation: +, -, *, /")
    op = input("Enter operator: ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if op == '+':
        print("Result =", add(a, b))
    elif op == '-':
        print("Result =", subtract(a, b))
    elif op == '*':
        print("Result =", multiply(a, b))
    elif op == '/':
        print("Result =", divide(a, b))
    else:
        print("Invalid operator!")

# Read and write student details to a file
def file_handling():
    name = input("Enter student name: ")
    marks = input("Enter marks: ")
    with open("student.txt", "w") as f:
        f.write(f"Name: {name}\nMarks: {marks}\n")
    print("Data written to student.txt")

    with open("student.txt", "r") as f:
        print("\nFile contents:\n", f.read())

# Handle division by zero
def division_handling():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        print("Result =", a / b)
    except ZeroDivisionError:
        print("Cannot divide by zero!")

# Student class with name and marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

def student_class_demo():
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    s = Student(name, marks)
    s.display()

# -------------------------------
# Menu-driven main program
# -------------------------------
def main():
    while True:
        print("\n--- Python Practice Menu ---")
        print("1. Print first 10 natural numbers")
        print("2. Sum of first N natural numbers")
        print("3. Reverse a number")
        print("4. Count digits in a number")
        print("5. Check palindrome")
        print("6. Generate Fibonacci series")
        print("7. Calculator")
        print("8. File handling (student details)")
        print("9. Division handling (exception)")
        print("10. Student class demo")
        print("11. Exit")

        choice = input("Enter your choice (1-11): ")

        if choice == '1': print_natural_numbers()
        elif choice == '2': sum_natural_numbers()
        elif choice == '3': reverse_number()
        elif choice == '4': count_digits()
        elif choice == '5': check_palindrome()
        elif choice == '6': fibonacci_series()
        elif choice == '7': calculator()
        elif choice == '8': file_handling()
        elif choice == '9': division_handling()
        elif choice == '10': student_class_demo()
        elif choice == '11':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

# Run the program
if __name__ == "__main__":
    main()
