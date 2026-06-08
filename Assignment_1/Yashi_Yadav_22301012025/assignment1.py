
#Assignment 1 by Yashi Yadav 22301012025
# Program to find area of rectangle

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth

print("Area of rectangle =", area)

# Program to calculate average of 3 numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print("Average =", average)

# Program to calculate Simple Interest

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time: "))

si = (p * r * t) / 100

print("Simple Interest =", si)

# Program to find square and cube of a number

num = float(input("Enter a number: "))

square = num ** 2
cube = num ** 3

print("Square =", square)
print("Cube =", cube)

# Program to create a student report

# Taking student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Taking marks of three subjects
marks1 = float(input("Enter marks in Subject 1: "))
marks2 = float(input("Enter marks in Subject 2: "))
marks3 = float(input("Enter marks in Subject 3: "))

# Calculating total marks
total = marks1 + marks2 + marks3

# Calculating percentage
percentage = total / 3

# Displaying student report
print("\n----- Student Report -----")
print("Student Name:", name)
print("Roll Number:", roll_no)
print("Subject 1 Marks:", marks1)
print("Subject 2 Marks:", marks2)
print("Subject 3 Marks:", marks3)
print("Total Marks:", total)
print("Percentage:", percentage, "%")


# Program to swap two numbers without third variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)

# Program to convert Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit =", fahrenheit)

