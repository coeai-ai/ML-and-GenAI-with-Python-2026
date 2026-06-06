# 1. Find sum of first 10 natural numbers

sum = 0

for i in range(1, 11):
    sum = sum + i

print("Sum of first 10 natural numbers =", sum)


# 2. Find factorial of a number

num = int(input("\nEnter a number for factorial: "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)


# 3. Print Fibonacci Series

n = int(input("\nEnter number of terms for Fibonacci Series: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c


# 4. Find largest among 3 numbers

x = int(input("\nEnter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if x >= y and x >= z:
    print("Largest number =", x)
elif y >= x and y >= z:
    print("Largest number =", y)
else:
    print("Largest number =", z)


# 5. Create Student Result System

name = input("\nEnter student name: ")
roll_no = int(input("Enter roll number: "))

marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks of subject 3: "))

total = marks1 + marks2 + marks3
percentage = total / 3

print("\n----- Student Result -----")
print("Name:", name)
print("Roll Number:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 90:
    print("Grade: A")
elif percentage >= 75:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 40:
    print("Grade: D")
else:
    print("Grade: Fail")