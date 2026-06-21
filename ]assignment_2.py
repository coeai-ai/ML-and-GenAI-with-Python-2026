#1. Sum of First 10 Natural Numbers
sum = 0
for i in range(1, 11):
    sum += i
print("Sum =", sum)

#factorial of a number
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial =", fact)

#Fibonacci Series
n = int(input("How many terms? "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c


#Largest Among 3 Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)

# Student Result System
name = input("Enter student name: ")

total = 0

for i in range(1, 6):
    marks = int(input(f"Enter marks of subject {i}: "))
    total += marks

percentage = total / 5

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

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
    grade = "Fail"

print("Grade:", grade)