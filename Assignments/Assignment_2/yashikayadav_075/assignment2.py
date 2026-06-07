# 1. Sum of First 10 Natural Numbers

sum = 0
for i in range(1, 11):
    sum += i
print("Sum of first 10 natural numbers =", sum)


# 2. Factorial of a Number

n = int(input("\nEnter a number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)


# 3. Fibonacci Series

terms = int(input("\nEnter number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")
for i in range(terms):
    print(a, end=" ")
    c = a + b
    a = b
    b = c


# 4. Largest Among 3 Numbers

a = int(input("\n\nEnter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number =", largest)


# 5. Student Result System

name = input("\nEnter Student Name: ")
roll = input("Enter Roll Number: ")

subjects = int(input("Enter number of subjects: "))

total = 0

for i in range(subjects):
    marks = float(input(f"Enter marks for Subject {i+1}: "))
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
print("Roll Number:", roll)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)