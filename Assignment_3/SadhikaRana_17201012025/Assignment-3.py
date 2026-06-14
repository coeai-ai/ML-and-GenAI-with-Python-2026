# 1. Create a function to print first 10 natural numbers.
def natural_numbers():
    for i in range(1,11):
        print(i)
natural_numbers()

# 2. Create a function to calculate sum of first N natural numbers.
def natural_numbers_Sum(n):
    sum = 0
    for i in range(1,n + 1):
        sum += i
    return sum
n = int(input("Enter a number: "))
print("sum of first", n, "natural numbers is:", natural_numbers_Sum(n))

# 3. Create a function to reverse a number.
def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev
num = int(input("Enter a number: "))
print("Reverse of", num, "is:", reverse_number(num))

# 4. Create a function to count digits in a number.
def count_digits(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count
num = int(input("Enter a number: "))
print("Number of digits in", num, "is:", count_digits(num))

# 5. Create a function to check palindrome number.
def is_palindrome(num):
    rev = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10
    return num == rev
num = int(input("Enter a number: "))
if is_palindrome(num):
    print(num, "is a palindrome number.")
else:    
    print(num, "is not a palindrome number.")

# 6. Create a function to generate Fibonacci series.
def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
n = int(input("Enter the number of terms: "))
print("Fibonacci series:")
fibonacci_series(n)

# 7. Calculator Using Functions that contains the following features;
#-	User selects operation 
#-	Program performs calculation 
#-	Display result

# Calculator Using Functions

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Division by zero is not possible."
    return a / b
print("CALCULATOR")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
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
    print("Result =", divide(num1, num2))
else:
    print("Invalid choice.")


# 8. Create a text file and store student details. 
def store_student_details(name, age, grade):
    with open("student_details.txt", "a") as file:
        file.write(f"Name: {name}, Age: {age}, Grade: {grade}\n")
name = input("Enter student name: ")
age = input("Enter student age: ")
grade = input("Enter student grade: ")
store_student_details(name, age, grade)
print("Student details stored in student_details.txt")

# 9. Read data from a file. 
def read_file(filename):
    with open(filename, "r") as file:
        data = file.read()
    return data
print("Student details from file:")
print(read_file("student_details.txt"))

# 10. Handle division by zero using exception handling. 
def safe_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero is not possible."
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Result =", safe_division(num1, num2))

# 11. Create a Student class with name and marks. 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display_details(self):
        print(f"Name: {self.name}, Marks: {self.marks}")
name = input("Enter student name: ")
marks = float(input("Enter student marks: "))
student = Student(name, marks)
student.display_details()

