# Create a function to print first 10 natural numbers.
def first_naturalnums(n):
    for i in range(1,n+1):
        print(i)
first_naturalnums(10)        

# Create a function to calculate sum of first N natural numbers.
n = int(input("enter the number: "))
def natural_num(n):
    return (n*(n+1))/2
sum = natural_num(n)
print("sum of first 10 natural numbers: ",sum)

# Create a function to reverse a number.
def reverse(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev
num = int(input("enter the number: "))
print("reverse of the number: ",reverse(num))

# Create a function to count digits in a number.
def count(n):
    count_num = 0
    while n>0:
        count_num = count_num + 1
        n//10
    return count_num
num1 = int(input("enter the number: "))
print("count of digits: ",count(num1))

# Create a function to check palindrome number.
def ispalindrome(n):
    temp = n
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    if temp == rev:
        return True
    else:
        return False
num2 = int(input("enter the number: "))    
if ispalindrome(num2):
    print("given number is a palindrome")
else:
    print("given number is not a palindrome") 

# Create a function to generate Fibonacci series.
def fibonacci(n):
    a = 0
    b = 1
    print(a, b, end=" ")
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c
num3 = int(input("Enter number of terms: "))
fibonacci(num3)

# Calculator Using Functions that contains the following features;
# 	-	User selects operation 
# 	-	Program performs calculation 
# 	-	Display result
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice: "))
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

# Create a text file and store student details. 
file = open("student.txt", "w")
name = input("Enter student name: ")
marks = input("Enter marks: ")
file.write("Name: " + name + "\n")
file.write("Marks: " + marks)
file.close()

# Read data from a file. 
file = open("student.txt", "r")
data = file.read()
print(data)
file.close()

# Handle division by zero using exception handling.
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Division by zero is not allowed.") 

# Create a Student class with name and marks. 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)
name = input("Enter student name: ")
marks = int(input("Enter marks: "))
s1 = Student(name, marks)
s1.display()