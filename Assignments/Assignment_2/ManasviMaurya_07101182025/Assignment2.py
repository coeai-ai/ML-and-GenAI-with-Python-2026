#Find sum of first 10 natural numbers
n = 10
sum_natural = n * (n + 1) // 2
print(f"The sum of the first {n} natural numbers is: {sum_natural}")

#Find factorial of a number
def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers."
    elif num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

# Example
num = 5
print(f"The factorial of {num} is: {factorial(num)}")

#Print the Fibonacci series
def fibonacci(n):
    fibonacci_series = []
    a, b = 0, 1
    for i in range(n):
        fibonacci_series.append(a)
        a, b = b, a + b
    return fibonacci_series
n = 10
print(f"The first {n} numbers in the Fibonacci series are: {fibonacci(n)}")

#Find the largest among three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
largest = max(num1, num2, num3)
print(f"The largest number among {num1}, {num2}, and {num3} is: {largest}")

'''Create student result system
-input student details
-input marks
-calculate percentage
-display grade
use: if-elif-else and loops'''
#Student result system
#Details
student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")
class_name = input("Enter class/section: ")
#Storing marks
math_marks = float(input("Enter marks for Mathematics: "))
science_marks = float(input("Enter marks for Science: "))
english_marks = float(input("Enter marks for English: "))
total_marks = math_marks + science_marks + english_marks
percentage = (total_marks / 300) * 100
# Determine grade
if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
else:
    grade = 'F'
# Display report card
print("          REPORT CARD          ")
print("--------------------------------")
print(f"Name: {student_name}")
print(f"Roll Number: {roll_number}")
print(f"Class/Section: {class_name}")
print(f"Mathematics Marks: {math_marks}")
print(f"Science Marks: {science_marks}")
print(f"English Marks: {english_marks}")
print("--------------------------------")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")
