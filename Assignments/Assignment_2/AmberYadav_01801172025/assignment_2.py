# Find sum of first 10 natural numbers
sum_natural = sum(range(1, 11))
print(f"Sum of first 10 natural numbers is: {sum_natural}")

# Find factorial of a number
num = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is: {factorial}")

# Print Fibonacci series 
n_terms = int(input("Enter the number of terms for Fibonacci series: "))
a, b = 0, 1
print("Fibonacci series:")
for _ in range(n_terms):
    print(a, end=' ')
    a, b = b, a + b
print()  # for new line after the series

# Find largest among three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
largest = max(num1, num2, num3)
print(f"The largest number among {num1}, {num2}, and {num3} is: {largest}")

# Create student result system
# - input student details and marks
# - calculate percentage
# - display grade
# use if-elif-else loops

# Taking student details
student_name = input("Enter student name: ")
student_age = int(input("Enter student age: "))
student_grade = input("Enter student grade: ")

# Taking marks for 3 subjects
phy_marks = int(input("Enter Physics marks: "))
math_marks = int(input("Enter Math marks: "))
chem_marks = int(input("Enter Chemistry marks: "))

# Calculating total marks and percentage
total_marks = phy_marks + math_marks + chem_marks
percentage = (total_marks / 300) * 100

# Determining grade based on percentage
if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
else:    grade = 'F'

# Printing student result
print("\n--- Student Result ---")
print(f"Name: {student_name}")
print(f"Age: {student_age}")
print(f"Grade: {student_grade}")
print(f"Total Marks: {total_marks} / 300")
print(f"Percentage: {percentage:.2f}%")
print(f"Final Grade: {grade}")
print("----------------------")



