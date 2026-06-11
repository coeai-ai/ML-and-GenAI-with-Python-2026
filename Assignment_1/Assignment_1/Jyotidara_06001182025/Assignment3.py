#  Function to print 10 natural number


def print_number(n):
    for i in range(n):
        print(i+1)
print_number(10) 


# Funtion to print sum of natural number
def Sum_natural(n):
    sum = 0
    for i in range(n):
        sum = sum + i
    return sum
sum_of = Sum_natural(11)
print(sum_of)

# To revers a number
num = int(input("number = "))

def reverse_number(num):
    reverse = 0
    while num > 0:
     digit = num % 10
     reverse = reverse * 10 + digit
     num = num // 10
    return reverse
revers_num = reverse_number(num)
print(revers_num)





# To count Digit in a number
num = int(input("the number is:"))
def count_digit(n):
    count = 0
    while n > 0:
        n = n//10
        count += 1
    return count

digits = count_digit(num)
print(digits)    

# To check Palindrome number
def is_palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return original == reverse

num = int(input("Enter a number: "))

if is_palindrome(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

# To create Fibonacci series
n = int(input("Enter the number of terms: "))
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
       sum = a+b
       a = b
       b = sum
       print(sum)
 
fibonacci(n)

# to create a calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return "Division by zero is not allowed"

print("Calculator")
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
    print("Invalid Choice")

# Create and write student details to a text file

name = input("Enter student name: ")
roll = input("Enter roll number: ")
marks = input("Enter marks: ")

file = open("student.txt", "w")
file.write(f"Name: {name}\n")
file.write(f"Roll No: {roll}\n")
file.write(f"Marks: {marks}\n")
file.close()

print("Student details saved successfully.")

# Read data from student.txt

file = open("student.txt", "r")
data = file.read()
print("File Contents:")
print(data)
file.close()


# Exception handdling 
try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))

    result = num1 / num2
    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")



# Create Student class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)

# Create object
s1 = Student("Jyoti", 90)

# Display details
s1.display()




