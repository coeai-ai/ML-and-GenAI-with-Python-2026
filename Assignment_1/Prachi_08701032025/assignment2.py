#ASSIGNMENT 2

#1.Sum of frst 10 natural numbers
sum=0

for i in range(1,11):
    sum=sum+i

print("Sum of first 10 natural numbers is:", sum)

#2.Factorial of a number
num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial of", num, "is:", factorial)

#3.Fibonacci Series
n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

#4.Largest among 3 numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Largest number is:", a)

elif b > a and b > c:
    print("Largest number is:", b)

else:
    print("Largest number is:", c)

#5.Student Result System
name = input("Enter student name: ")
roll = input("Enter roll number: ")

total = 0

for i in range(1, 6):
    marks = int(input("Enter marks of subject " + str(i) + ": "))
    total = total + marks

percentage = total / 5

print("Student Name:", name)
print("Roll Number:", roll)
print("Total Marks:", total)
print("Percentage:", percentage)

# Grade Calculation

if percentage >= 90:
    grade = "A+"

elif percentage >= 75:
    grade = "A"

elif percentage >= 60:
    grade = "B"

elif percentage >= 40:
    grade = "C"

else:
    grade = "Fail"

print("Grade:", grade)