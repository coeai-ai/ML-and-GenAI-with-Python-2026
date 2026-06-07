# 1) Find Sum of First 10 Natural Numbers

sum = 0

for i in range(1, 11):
    sum += i

print("Sum =", sum)


# 2) Find Factorial of a Number

num = int(input("Enter a Number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial =", factorial)


# 3) Print Fibonacci Series

n = int(input("Enter Number of Terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# 4) Find Largest Among 3 Numbers

a = int(input("\nEnter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if a >= b and a >= c:
    print("Largest Number =", a)
elif b >= a and b >= c:
    print("Largest Number =", b)
else:
    print("Largest Number =", c)


# 5) Student Result System

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

subjects = int(input("Enter Number of Subjects: "))

total = 0

for i in range(subjects):
    marks = float(input(f"Enter Marks of Subject {i+1}: "))
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

print("\n----- STUDENT RESULT -----")
print("Name:", name)
print("Roll Number:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)