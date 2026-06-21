
# 1. FIND SUM OF FIRST 10 NATURAL NUMBERS

sum = 0

for i in range(1, 11):
    sum = sum + i

print("Sum of first 10 natural numbers =", sum)


# 2. FIND FACTORIAL OF A NUMBER

num = int(input("\nEnter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial =", factorial)


# 3. PRINT FIBONACCI SERIES

n = int(input("\nEnter number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

print()


# 4. FIND LARGEST AMONG 3 NUMBERS

num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("Largest Number =", largest)


# 5. STUDENT RESULT SYSTEM

# Input student details
name = input("\nEnter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Input number of subjects
n = int(input("Enter Number of Subjects: "))

total = 0

# Input marks using loop
for i in range(1, n + 1):
    marks = float(input(f"Enter Marks for Subject {i}: "))
    total = total + marks

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
print("\nSTUDENT RESULT")
print("Student Name :", name)
print("Roll Number  :", roll_no)
print("Total Marks  :", total)
print("Percentage   :", percentage)
print("Grade        :", grade)