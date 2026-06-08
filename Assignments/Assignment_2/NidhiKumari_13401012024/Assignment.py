# -------------------------------
# Python Assignment - 2 Solution
# -------------------------------

# Q1. Find Sum of First 10 Natural Numbers
print("Q1. Sum of First 10 Natural Numbers")
sum_num = 0
for i in range(1, 11):
    sum_num += i
print("Sum =", sum_num)

# Q2. Find Factorial of a Number
print("\nQ2. Factorial of a Number")
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial =", factorial)

# Q3. Print Fibonacci Series
print("\nQ3. Fibonacci Series")
n = int(input("How many terms? "))
a = 0
b = 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Q4. Find Largest Among 3 Numbers
print("\n\nQ4. Largest Among 3 Numbers")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("Largest Number =", largest)

# Q5. Student Result System
print("\nQ5. Student Result System")
name = input("Enter Student Name: ")
rollno = input("Enter Roll Number: ")

english = float(input("Enter English Marks: "))
maths = float(input("Enter Maths Marks: "))
science = float(input("Enter Science Marks: "))
hindi = float(input("Enter Hindi Marks: "))
computer = float(input("Enter Computer Marks: "))

total = english + maths + science + hindi + computer
percentage = (total / 500) * 100

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
    grade = "F (Fail)"

print("\nSTUDENT RESULT")
print("Name       :", name)
print("Roll No.   :", rollno)
print("English    :", english)
print("Maths      :", maths)
print("Science    :", science)
print("Hindi      :", hindi)
print("Computer   :", computer)
print("Total      :", total, "/ 500")
print("Percentage :", round(percentage, 2), "%")
print("Grade      :", grade)
