# Area of Rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
print("Area of rectangle:", area)

# Simple Interest: SI = (P * R * T) / 100
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (in years): "))

simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest)

# Temperature Conversion: F = (C * 9/5) + 32
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# Average of 3 numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

average = (a + b + c) / 3
print("Average:", average)

# Square and Cube of a number
num = float(input("Enter a number: "))

square = num ** 2
cube = num ** 3

print("Square:", square)
print("Cube:", cube)

# Swap two numbers without using a third variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swap -> a:", a, "b:", b)

a = a + b
b = a - b
a = a - b

print("After swap  -> a:", a, "b:", b)

# Student Report Program
# Takes student details, stores marks, calculates total and percentage

# ---------- Student Details ----------
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# ---------- Marks Input ----------
marks_maths = float(input("Enter marks in Maths (out of 100): "))
marks_science = float(input("Enter marks in Science (out of 100): "))
marks_english = float(input("Enter marks in English (out of 100): "))
marks_history = float(input("Enter marks in History (out of 100): "))
marks_computer = float(input("Enter marks in Computer (out of 100): "))

# ---------- Calculations ----------
total_marks = marks_maths + marks_science + marks_english + marks_history + marks_computer
max_marks = 500  # 5 subjects x 100
percentage = (total_marks / max_marks) * 100

# ---------- Result ----------
print("\n========== STUDENT REPORT CARD ==========")
print("Name      :", name)
print("Roll No.  :", roll_no)
print("-----------------------------------------")
print("Maths     :", marks_maths)
print("Science   :", marks_science)
print("English   :", marks_english)
print("History   :", marks_history)
print("Computer  :", marks_computer)
print("-----------------------------------------")
print("Total     :", total_marks, "/ 500")
print("Percentage: {:.2f}%".format(percentage))
print("=========================================")

