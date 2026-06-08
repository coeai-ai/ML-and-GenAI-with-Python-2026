# ==========================================
# Assignment 2
# Name: Divija Tewari
# ==========================================

# 1. Sum of first 10 natural numbers

print("1. Sum of First 10 Natural Numbers")

sum_of_numbers = 0

for i in range(1, 11):
    sum_of_numbers += i

print("Sum =", sum_of_numbers)

print("\n-----------------------------------\n")


# 2. Factorial of a Number

print("2. Factorial of a Number")

num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial =", factorial)

print("\n-----------------------------------\n")


# 3. Fibonacci Series

print("3. Fibonacci Series")

n = int(input("How many terms do you want? "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

print("\n")
print("\n-----------------------------------\n")


# 4. Largest Among Three Numbers

print("4. Largest Among Three Numbers")

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

print("\n-----------------------------------\n")


# 5. Student Result System

print("5. Student Result System")

student_name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")

total_marks = 0

for i in range(1, 6):
    marks = float(input(f"Enter marks for Subject {i}: "))
    total_marks += marks

percentage = total_marks / 5

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

print("\n========== STUDENT RESULT ==========")
print("Student Name :", student_name)
print("Roll Number  :", roll_number)
print("Total Marks  :", total_marks)
print("Percentage   :", round(percentage, 2), "%")
print("Grade        :", grade)
print("====================================")
