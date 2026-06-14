## Function to print first 10 natural numbers
def print_numbers():
    for i in range(1, 11):
        print(i)
print_numbers()

#Create a function to calculate sum of first N natural numbers.
def find_sum(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    print("Sum =", total)

n = int(input("Enter a number: "))
find_sum(n)

#Create a function to reverse a number.
#method 1 
def reverse_number(num):
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return reverse
num = int(input("Enter a number: "))
print("Reversed Number =", reverse_number(num))

#method 2 
def reverse_number(num):
    return str(num)[::-1]

num = input("Enter a number: ")
print("Reversed Number =", reverse_number(num))

#Create a function to count digits in a number
def count_digits(num):
    count = 0

    while num > 0:
        count = count + 1
        num = num // 10

    return count
num = int(input("Enter a number: "))
print("Number of digits =", count_digits(num))

#Create a function to check palindrome number.
def check_palindrome(num):
    if str(num) == str(num)[::-1]:
        print("Palindrome Number")
    else:
        print("Not a Palindrome Number")

num = int(input("Enter a number: "))
check_palindrome(num)

#Create a function to generate Fibonacci series
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
n = int(input("Enter number of terms: "))
fibonacci(n)

#Calculator
def calculator(num1, num2, operator):

    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/":
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2

    else:
        return "Invalid Operation"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operation (+, -, *, /): ")
result = calculator(num1, num2, operator)
print("Result =", result)

#Create a text file and store student details.
name = input("Enter student name: ")
marks = input("Enter marks: ")

file = open("student.txt", "w")
file.write("Name: " + name + "\n")
file.write("Marks: " + marks)
file.close()

print("Data saved successfully.")

#Read data from a file. 
file = open("student.txt", "r")
data = file.read()
print(data)
file.close()

#Handle division by zero using exception handling. 
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result =", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

#Create a Student class with name and marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
name = input("Enter student name: ")
marks = float(input("Enter marks: "))

s1 = Student(name, marks)
s1.display()