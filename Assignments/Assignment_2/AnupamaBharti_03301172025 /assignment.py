# Question 1

# Initializing sum variable
sum = 0
# Looping from 1 to 10 and adding numbers
for i in range(1, 11):
    sum += i
    # Displaying result
print("Sum of first 10 natural numbers =", sum)

#Question2

# Taking input from the user for which we need to find factorial
num = int(input("Enter a number: "))
# Initializing factorial with 1 (since multiplication starts from 1)
factorial = 1
# Loop to multiply numbers from 1 to num
for i in range(1, num + 1):
    factorial *= i
# Displaying the final result
print("Factorial =", factorial)

#Question3

# Taking number of terms from user
n = int(input("Enter number of terms: "))
# First two numbers of Fibonacci series
a = 0
b = 1
# Printing Fibonacci series
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

#Question4

# Taking three numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
# Finding largest number using conditions
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
# Displaying result
print("Largest number =", largest)

#Question5

# Taking student details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
# Taking marks input
maths = float(input("Enter Maths Marks: "))
science = float(input("Enter Science Marks: "))
english = float(input("Enter English Marks: "))
# Calculating total and percentage
total = maths + science + english
percentage = total / 3
# Assigning grade based on percentage
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
# Displaying final result
print()
print("----- Student Result -----")
print("Name:", name)
print("Roll No:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
