# Sum of first 10 natural numbers

total = 0

for i in range(1, 11):
    total += i

print("Sum of first 10 natural numbers =", total)

# Factorial of a number

num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial =", factorial)

# Fibonacci Series

n = int(input("How many terms do you want? "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    
    next_num = a + b
    a = b
    b = next_num

# Largest among three numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1

elif num2 >= num1 and num2 >= num3:
    largest = num2

else:
    largest = num3

print("Largest number =", largest)

# Student Result System

print("===== STUDENT RESULT SYSTEM =====")

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

total = 0

# Taking marks of 5 subjects using loop
for i in range(1, 6):
    marks = float(input(f"Enter marks of Subject {i}: "))
    total += marks

percentage = total / 5

# Grade Calculation
if percentage >= 90:
    grade = "A"

elif percentage >= 75:
    grade = "B"

elif percentage >= 60:
    grade = "C"

elif percentage >= 40:
    grade = "D"

else:
    grade = "F"

print("\n===== RESULT =====")
print("Name       :", name)
print("Roll No    :", roll_no)
print("Total Marks:", total)
print("Percentage :", percentage, "%")
print("Grade      :", grade)

if percentage >= 40:
    print("Status     : PASS")
else:
    print("Status     : FAIL")

