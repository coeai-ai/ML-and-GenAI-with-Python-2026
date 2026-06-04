# Assignment 1 

# 1. Find area of rectangle
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
area = length * breadth
print("Area of rectangle =", area)

# 2. Find simple interest
principal = float(input("\nEnter Principal amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (in years): "))
simple_interest = (principal * rate * time) / 100
print("Simple Interest =", simple_interest)

# 3. Convert temperature from Celsius to Fahrenheit
celsius = float(input("\nEnter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit =", fahrenheit)

# 4. Calculate average of 3 numbers
num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print("Average of three numbers =", average)

# 5. Find square and cube of a number
number = int(input("\nEnter a number: "))
square = number ** 2
cube = number ** 3
print("Square =", square)
print("Cube =", cube)

# 6. Swap two numbers without third variable
a = int(input("\nEnter first number (a): "))
b = int(input("Enter second number (b): "))
print("Before swapping: a =", a, "b =", b)
a, b = b, a
print("After swapping: a =", a, "b =", b)

# 7. Student Report Program
# Taking student details and marks, calculating total and percentage

print("\n--- Student Report Program ---")
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Storing marks in variables
maths = float(input("Enter marks in Maths: "))
science = float(input("Enter marks in Science: "))
english = float(input("Enter marks in English: "))

# Calculating total and percentage
total_marks = maths + science + english
percentage = (total_marks / 300) * 100  # Assuming each subject is out of 100

# Displaying report
print("\n--- Student Report ---")
print("Name:", name)
print("Roll Number:", roll_no)
print("Maths:", maths)
print("Science:", science)
print("English:", english)
print("Total Marks:", total_marks)
print("Percentage:", percentage, "%")
