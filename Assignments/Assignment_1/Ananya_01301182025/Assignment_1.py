# ============================================================
# Python Assignment Solutions
# ============================================================


# 1. Find Area of Rectangle
print("=" * 40)
print("1. Area of Rectangle")
print("=" * 40)
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print(f"Area of Rectangle = {area}")


# 2. Find Simple Interest
print("\n" + "=" * 40)
print("2. Simple Interest")
print("=" * 40)
principal = float(input("Enter Principal amount: "))
rate = float(input("Enter Rate of interest (%): "))
time = float(input("Enter Time (years): "))
simple_interest = (principal * rate * time) / 100
print(f"Simple Interest = {simple_interest}")


# 3. Convert Temperature from Celsius to Fahrenheit
print("\n" + "=" * 40)
print("3. Celsius to Fahrenheit")
print("=" * 40)
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")


# 4. Calculate Average of 3 Numbers
print("\n" + "=" * 40)
print("4. Average of 3 Numbers")
print("=" * 40)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print(f"Average = {average}")


# 5. Find Square and Cube of a Number
print("\n" + "=" * 40)
print("5. Square and Cube of a Number")
print("=" * 40)
num = float(input("Enter a number: "))
square = num ** 2
cube = num ** 3
print(f"Square of {num} = {square}")
print(f"Cube of {num} = {cube}")


# 6. Swap Two Numbers Without Third Variable
print("\n" + "=" * 40)
print("6. Swap Two Numbers (No Third Variable)")
print("=" * 40)
a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
print(f"Before Swap: a = {a}, b = {b}")
a = a + b
b = a - b
a = a - b
print(f"After Swap:  a = {a}, b = {b}")


# 7. Student Report Program
print("\n" + "=" * 40)
print("7. Student Report Program")
print("=" * 40)

# Taking student details using input()
student_name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")

# Store marks in variables
marks_english = float(input("Enter marks in English (out of 100): "))
marks_math = float(input("Enter marks in Maths (out of 100): "))
marks_science = float(input("Enter marks in Science (out of 100): "))
marks_hindi = float(input("Enter marks in Hindi (out of 100): "))
marks_computer = float(input("Enter marks in Computer (out of 100): "))

# Calculate total and percentage
total_marks = marks_english + marks_math + marks_science + marks_hindi + marks_computer
max_marks = 500
percentage = (total_marks / max_marks) * 100

# Determine grade
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

# Display Student Report with proper indentation
print("\n" + "=" * 40)
print("        STUDENT REPORT CARD")
print("=" * 40)
print(f"  Name        : {student_name}")
print(f"  Roll Number : {roll_number}")
print("-" * 40)
print(f"  English     : {marks_english}")
print(f"  Maths       : {marks_math}")
print(f"  Science     : {marks_science}")
print(f"  Hindi       : {marks_hindi}")
print(f"  Computer    : {marks_computer}")
print("-" * 40)
print(f"  Total Marks : {total_marks} / {max_marks}")
print(f"  Percentage  : {percentage:.2f}%")
print(f"  Grade       : {grade}")
print("=" * 40)