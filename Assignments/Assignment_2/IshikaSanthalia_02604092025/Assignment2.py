# Sum of first 10 natural numbers

sum = 0
for i in range(1, 11):
    sum += i

print("Sum of first 10 natural numbers =", sum)

# Factorial of a number

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial of", num, "=", factorial)

# Fibonacci Series

n = int(input("Enter number of terms: "))
a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

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

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

subjects = int(input("Enter number of subjects: "))

total = 0
for i in range(1, subjects + 1):
    marks = float(input(f"Enter marks for Subject {i}: "))
    total += marks

percentage = total / subjects
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"
print("\n STUDENT RESULT ")
print("Name       :", name)
print("Roll No    :", roll_no)
print("Total Marks:", total)
print("Percentage :", round(percentage, 2), "%")
print("Grade      :", grade)
