# Find area of rectangle
length = int(input("Enter length of rectangle: "))
breadth = int(input("Enter breadth of rectangle: "))
area = length * breadth
print(f"Area of rectangle is: {area} square units")

# Find simple interest
principal = float(input("Enter principal amount (P): "))
rate = float(input("Enter rate of interest (R in %): "))
time = float(input("Enter time in years (T): "))
simple_interest = (principal * rate * time) / 100
print(f"Simple interest is: {simple_interest}")

# Convert temprature from celsius to fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit is: {fahrenheit} °F")

# Calculate average of 3 numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print(f"Average of the three numbers is: {average}")

# Find square and cube of a number
number = float(input("Enter a number: "))
square = number ** 2
cube = number ** 3
print(f"Square of {number} is: {square}")
print(f"Cube of {number} is: {cube}")       

# Swap two numbers without using a third variable
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
print(f"Before swapping: a = {a}, b = {b}")
a,b = b,a
print(f"After swapping: a = {a}, b = {b}")

#  Create a Student Report Program that takes student details using input(), stores marks in variables,
# calculate total and percentage, use comments, use proper indentation

# Taking student details
student_name = input("Enter name: ")
student_age = int(input("Enter age: "))
student_grade = input("Enter grade: ")

#Taking marks for 5 subjects
phy_marks = int(input("Enter Physics marks: "))
math_marks = int(input("Enter Math marks: "))
chemistry_marks = int(input("Enter Chemistry marks: "))
english_marks = int(input("Enter English marks: "))
computer_marks = int(input("Enter Computer marks: "))

# Calculating total marks and percentage
total_marks = phy_marks + math_marks + chemistry_marks + english_marks + computer_marks
percentage = (total_marks / 500) * 100

# Printing student report

print("\n--- Student Report ---")
print(f"Student Name: {student_name}")
print(f"Age: {student_age}")
print(f"Grade: {student_grade}")
print(f"Total Marks: {total_marks} / 500")
print(f"Percentage: {percentage:.2f}%")
print("----------------------")


