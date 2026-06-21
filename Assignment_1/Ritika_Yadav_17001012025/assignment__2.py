# Program to find sum of first 10 natural numbers

sum = 0

for i in range(1, 11):
    sum += i

print("Sum of first 10 natural numbers =", sum)


# Program to find factorial of a number

num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial of", num, "=", factorial)


# Program to print Fibonacci Series

n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    
    next_term = a + b
    a = b
    b = next_term

    
# Program to find the largest among three numbers

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



# Student Result System

# Input student details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

total_marks = 0

# Input marks of 5 subjects using loop
for i in range(1, 6):
    marks = float(input(f"Enter marks of Subject {i}: "))
    total_marks += marks

# Calculate percentage
percentage = (total_marks / 500) * 100

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
print("Roll No    :", roll_no)
print("Total Marks:", total_marks)
print("Percentage :", round(percentage, 2), "%")
print("Grade      :", grade)




