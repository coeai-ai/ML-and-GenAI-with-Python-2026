# Question 1: Sum of First 10 Natural Numbers

sum = 0
for i in range(1, 11):
    sum += i

print("Q1: Sum of first 10 natural numbers =", sum)


# Question 2: Factorial of a Number

num = int(input("\nQ2: Enter a number to find factorial: "))

fact = 1
for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)


# Question 3: Fibonacci Series

n = int(input("\nQ3: Enter number of terms for Fibonacci Series: "))

a = 0
b = 1

print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

print()


# Question 4: Largest Among 3 Numbers

a = int(input("\nQ4: Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)


# Question 5: Student Result System

print("\nQ5: Student Result System")

name = input("Enter Student Name: ")

m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))

total = m1 + m2 + m3
percentage = total / 3

print("\nStudent Name:", name)
print("Percentage:", percentage)

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"

print("Grade:", grade)