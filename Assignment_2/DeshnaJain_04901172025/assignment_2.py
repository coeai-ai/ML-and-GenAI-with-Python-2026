# Find sum of first 10 natural numbers.

s = 0
for i in range(1, 11):
    s=s+i
print("Sum =",s)


# Find factorial of a number.

n=int(input("Enter number:"))
f=1
for i in range(1, n+1):
    f=f*i

print("Factorial=",f)


# Print Fibonacci Series.

n=int(input("Enter number of terms: "))

a=0
b=1
for i in range(n):
    print(a,end=" ")
    c = a+b
    a = b
    b = c

print()


# Find largest among 3 numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest =",a)
elif b >= a and b >= c:
    print("Largest =",b)
else:
    print("Largest =",c)


# Create Student Result System
# Input student details
# Input marks
# Calculate percentage
# Display grade
# Use:
# if-elif-else
# loops

name=input("Enter student name: ")
roll=input("Enter roll number: ")
total = 0

for i in range(5):
    marks = float(input("Enter marks: "))
    total = total + marks

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

print("Student Name:", name)
print("Roll Number:", roll)
print("Percentage:", percentage)
print("Grade:", grade)