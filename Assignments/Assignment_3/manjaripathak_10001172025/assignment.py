

# 1. Print first 10 natural numbers
def first_10_natural():
    for i in range(1, 11):
        print(i, end=" ")
    print()


# 2. Sum of first N natural numbers
def sum_n(n):
    return n * (n + 1) // 2


# 3. Reverse a number
def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev


# 4. Count digits in a number
def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count


# 5. Check palindrome number
def palindrome(num):
    return num == reverse_number(num)


# 6. Generate Fibonacci series
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
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
    return a / b


# 8. Create text file and store student details
def write_student():
    with open("student.txt", "w") as file:
        name = input("Enter student name: ")
        marks = input("Enter marks: ")
        file.write("Name: " + name + "\n")
        file.write("Marks: " + marks)


# 9. Read data from file
def read_student():
    with open("student.txt", "r") as file:
        print(file.read())


# 10. Exception handling (division by zero)
def safe_division():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        print("Result =", a / b)
    except ZeroDivisionError:
        print("Cannot divide by zero!")


# 11. Student class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


# ---------------- MAIN ----------------

print("First 10 Natural Numbers:")
first_10_natural()

n = int(input("\nEnter N for sum: "))
print("Sum =", sum_n(n))

num = int(input("\nEnter a number: "))
print("Reverse =", reverse_number(num))
print("Digit Count =", count_digits(num))

if palindrome(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

terms = int(input("\nEnter Fibonacci terms: "))
print("Fibonacci Series:")
fibonacci(terms)

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
print("Addition =", add(a, b))
print("Subtraction =", subtract(a, b))
print("Multiplication =", multiply(a, b))

if b != 0:
    print("Division =", divide(a, b))
else:
    print("Division by zero not allowed")

write_student()

print("\nStudent File Data:")
read_student()

safe_division()

name = input("\nEnter student name: ")
marks = int(input("Enter student marks: "))

s1 = Student(name, marks)
print("\nStudent Details:")
s1.display()