# 1. Find the sum of the first 10 natural numbers.
sum = 0

for i in range(1, 11):
    sum = sum + i

print("Sum =", sum)

# 2. Find the factorial of a given number.
num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial =", factorial)

# 3. Print the Fibonacci series up to N terms.
n = int(input("How many terms? "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

# 4. Find the largest among three numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number is:", largest)

# 5. Create a Student Result System that:
    # Takes student details as input.
    # Takes marks of subjects as input.
    # Calculates total marks and percentage.
    # Displays the grade based on the percentage.
    # Uses if-elif-else statements.
    # Uses loops wherever required.

# Student Result System

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

total = 0

# Input marks of 5 subjects
for i in range(1, 6):
    marks = float(input(f"Enter marks of Subject {i}: "))
    total += marks

percentage = total / 5

# Display grade
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

print("\n----- Student Result -----")
print("Name:", name)
print("Roll No:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)