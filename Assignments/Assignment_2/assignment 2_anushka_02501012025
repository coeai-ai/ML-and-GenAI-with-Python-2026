# Assignment 2

# 1. Sum of First 10 Natural Numbers

sum_num = 0

for i in range(1, 11):
    sum_num += i

print("1. Sum of first 10 natural numbers =", sum_num)

# -----------------------------------------

# 2. Factorial of a Number

num = int(input("\n2. Enter a number to find factorial: "))

fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)

# -----------------------------------------

# 3. Fibonacci Series

n = int(input("\n3. Enter number of terms for Fibonacci Series: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

print()

# -----------------------------------------

# 4. Largest Among 3 Numbers

a = int(input("\n4. Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number is:", largest)

# -----------------------------------------

# 5. Student Result System

print("\n5. STUDENT RESULT SYSTEM")

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

m1 = float(input("Enter Marks in Subject 1: "))
m2 = float(input("Enter Marks in Subject 2: "))
m3 = float(input("Enter Marks in Subject 3: "))
m4 = float(input("Enter Marks in Subject 4: "))
m5 = float(input("Enter Marks in Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

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
print("Roll Number:", roll)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
