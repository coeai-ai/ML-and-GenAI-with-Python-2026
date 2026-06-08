# Student Name: Prachi Bhardwaj
# Enrollment Number: 09301182025
# College Name: IGDTUW

# ASSIGNMENT 2

## 1. Find Sum of First 10 Natural Numbers

sum = 0
for i in range(1, 11):
    sum += i
print("Sum of first 10 natural numbers =", sum)


## 2. Find Factorial of a Number


num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial =", factorial)



## 3. Print Fibonacci Series


n = int(input("Enter number of terms: "))
a = 0
b = 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c



## 4. Find Largest Among 3 Numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("Largest number =", largest)


## 5. Student Result System

# Input Student Details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Input Marks
maths = float(input("Enter Maths Marks: "))
science = float(input("Enter Science Marks: "))
english = float(input("Enter English Marks: "))

# Calculate Total and Percentage
total = maths + science + english
percentage = (total / 300) * 100

# Display Grade using if-elif-else
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

# Display Result
print("\n----- STUDENT RESULT -----")
print("Name:", name)
print("Roll Number:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)







