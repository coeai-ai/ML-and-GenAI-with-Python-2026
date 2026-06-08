#ASSIGNMENT2
# Sum of first 10 natural numbers
sum = 0
for i in range(1, 11):
    sum += i
print("Sum =", sum)

# Factorial of a number
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print("Factorial =", fact)

# Fibonacci Series
n = int(input("How many terms? "))
a = 0
b = 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
print()

# Largest among 3 numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b and a > c:
    print("Largest =", a)
elif b > c:
    print("Largest =", b)
else:
    print("Largest =", c)

# Student Result System
name = input("Enter name: ")
roll = input("Enter roll number: ")
total = 0
for i in range(1, 6):
    marks = float(input(f"Enter marks of subject {i}: "))
    total += marks
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
print("\n----- Result -----")
print("Name:", name)
print("Roll No:", roll)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
if percentage >= 40:
    print("Status: Pass")
else:
    print("Status: Fail")