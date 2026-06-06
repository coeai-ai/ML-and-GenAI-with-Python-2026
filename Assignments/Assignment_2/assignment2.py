#ASSIGNMENT 2

# Q1: Find sum of first 10 natural numbers
sum = 0
for i in range(1, 11):
    sum += i
print("Sum of first 10 natural numbers is:", sum)

# Q2: Find factorial of a number
n=int(input("enter a number:"))
factorial = 1
for i in range(1,n+1):
    factorial*=i
print("factorial of the number is:", factorial)

#Q3: Print fibonnacci series up to n terms
n=int(input("enter number of terms:"))
a, b = 0, 1
print("Fibonacci series up to", n, "terms:")
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b

# Q4: Find largest among 3 numbers
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print("largest among three numbers is:", largest)

# Q5:  Student Result System

# Input student details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Input number of subjects
n = int(input("Enter Number of Subjects: "))

total = 0

# Loop to input marks
for i in range(1, n + 1):
    marks = float(input(f"Enter marks for Subject {i}: "))
    total += marks

# Calculate percentage
percentage = total / n

# Display grade using if-elif-else
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

# Display result
print("\n===== STUDENT RESULT =====")
print("Name       :", name)
print("Roll No.   :", roll_no)
print("Total Marks:", total)
print("Percentage :", percentage, "%")
print("Grade      :", grade)