# Program to find area of rectangle

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth

print("Area of Rectangle =", area)

# Program to calculate Simple Interest

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (in years): "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)

# Program to convert Celsius into Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit =", fahrenheit)
# Program to calculate average of 3 numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print("Average =", average)
# Program to find square and cube

number = int(input("Enter a number: "))

square = number ** 2
cube = number ** 3

print("Square =", square)
print("Cube =", cube)
# Program to swap two numbers without third variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before Swapping:")
print("a =", a)
print("b =", b)

a = a + b
b = a - b
a = a - b

print("After Swapping:")
print("a =", a)
print("b =", b)
# Student Report Program

# Taking student details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Taking marks of 5 subjects
marks1 = float(input("Enter marks in Subject 1: "))
marks2 = float(input("Enter marks in Subject 2: "))
marks3 = float(input("Enter marks in Subject 3: "))
marks4 = float(input("Enter marks in Subject 4: "))
marks5 = float(input("Enter marks in Subject 5: "))

# Calculating total marks
total = marks1 + marks2 + marks3 + marks4 + marks5

# Calculating percentage
percentage = total / 5

# Displaying report
print("\n----- STUDENT REPORT -----")
print("Student Name :", name)
print("Roll Number  :", roll_no)
print("Total Marks  :", total)
print("Percentage   :", percentage, "%")
