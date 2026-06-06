# Q1. Find sum of first 10 natural numbers.
sum = 0
for i in range(1, 11):
    sum += i

print("Sum of first 10 natural numbers =", sum)


# Q2. Find factorial of a number.
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)


# Q3. Print Fibonacci Series.
n = int(input("How many terms? "))
a, b = 0, 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# Q4. Find largest among 3 numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest number is", a)
elif b >= a and b >= c:
    print("Largest number is", b)
else:
    print("Largest number is", c)


# Q5. Create Student Result System - Input student details - Input marks - Calculate percentage - Display grade - Use: if-elif-else loops user input

# Input student details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Input marks
m1 = float(input("Enter marks in Subject 1: "))
m2 = float(input("Enter marks in Subject 2: "))
m3 = float(input("Enter marks in Subject 3: "))
m4 = float(input("Enter marks in Subject 4: "))
m5 = float(input("Enter marks in Subject 5: "))

# Calculate percentage
total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

# Display grade
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
    grade = "F"

# Display result
print("\n STUDENT RESULT ")
print("Name       :", name)
print("Roll No    :", roll_no)
print("Total Marks:", total)
print("Percentage :", percentage, "%")
print("Grade      :", grade)