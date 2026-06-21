"""ASSIGNMENT 2"""

# Find sum of first 10 natural numbers
sum = 0
for i in range(1, 11):
    sum += i
print("Sum =", sum)

# Find factorial of a number
num = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is", factorial)

# Print Fibonacci series up to n terms
n = int(input("Enter the number of terms for Fibonacci series: "))
a, b = 0, 1
print("Fibonacci series:")
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
print()

# Find largest of three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))    
num3 = float(input("Enter third number: "))
largest = max(num1, num2, num3)
print("The largest number is:", largest)

# Create Student Result System
name = input("Enter student's name: ")
marks = float(input("Enter student's marks: "))
if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade = 'F'
print("Student Name:", name)
print("Marks:", marks)
print("Grade:", grade)
