#1. sum of first 10 natural numbers
sum_numbers = 0
for i in range(1, 11):
    sum_numbers += i
print("Sum of first 10 natural numbers =", sum_numbers)

#2. factorial of a number
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial =", factorial)

#3. fibonacci series
n = int(input("Enter number of terms: "))
a = 0
b = 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#4. largest among 3 numbers
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

# 5. Student Result System

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

total_marks = 0
subjects = 5

for i in range(1, subjects + 1):
    marks = float(input(f"Enter marks for Subject {i}: "))
    total_marks += marks

percentage = total_marks / subjects

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

print("\n----- STUDENT RESULT -----")
print("Name:", name)
print("Roll Number:", roll_no)
print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Grade:", grade)