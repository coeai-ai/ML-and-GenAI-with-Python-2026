# 1. Sum of first 10 Natural Numbers
total = 0
for i in range(1, 11):
    total += i
print("Sum of first 10 natural numbers is:", total)

# 2. Factorial of a Number
num = int(input("Enter a number: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("Factorial of 0 is: 1")
else:
    result = 1
    for i in range(1, num + 1):
        result = result * i
    print("Factorial of", num, "is:", result)

# 3. Fibonacci Series
n = int(input("Number of terms: "))
a = 0
b = 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    next_term = a + b
    a = b
    b = next_term
    
print()

# 4. Largest Among 3 Numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("Largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest number is:", num2)
else:
    print("Largest number is:", num3)

# 5.Student Result System

#Student details
student_name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")

total_marks = 0
for subject in range(1, 6):
    marks = float(input(f"Enter marks for Subject {subject}: "))
    total_marks += marks

# Calculating percentage
percentage = (total_marks / 500) * 100

# Calculating grade
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

# Pass/Fail status
status = "Pass" if grade != "F" else "Fail"

# Displaying result
print("\n----- STUDENT RESULT -----")
print("Student Name :", student_name)
print("Roll Number  :", roll_number)
print("Total Marks  :", total_marks)
print("Percentage   :", percentage, "%")
print("Grade        :", grade)
print("Status       :", status)