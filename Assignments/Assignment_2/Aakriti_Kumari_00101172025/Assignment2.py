# Assignment 2


# 1. Find Sum of First 10 Natural Numbers
sum_n = 0
for i in range(1, 11):
    sum_n += i
print("Sum =", sum_n)


# 2. Find Factorial of a Number
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial of", num, "=", fact)


# 3. Print Fibonacci Series
terms = int(input("Enter number of terms: "))
a, b = 0, 1
print("Fibonacci Series:")
for i in range(terms):
    print(a, end=" ")
    a, b = b, a + b
print()


# 4. Find Largest Among 3 Numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print("Largest number is:", largest)


# 5. Student Result System
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
subjects = int(input("Enter number of subjects: "))
total_marks = 0
for i in range(1, subjects + 1):
    marks = float(input(f"Enter marks for Subject {i}: "))
    total_marks += marks
percentage = total_marks / subjects

# Grade Calculation
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

print("\n----- RESULT -----")
print("Student Name :", name)
print("Roll Number  :", roll_no)
print("Total Marks  :", total_marks)
print("Percentage   :", round(percentage, 2), "%")
print("Grade        :", grade)