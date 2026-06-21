# Program to find area of rectangle

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth

print("Area of Rectangle =", area)

# Program to calculate Simple Interest

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (years): "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)

# Celsius to Fahrenheit conversion

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (9/5) * celsius + 32

print("Temperature in Fahrenheit =", fahrenheit)

# Program to calculate average

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print("Average =", average)

# Program to find square and cube

num = int(input("Enter a number: "))

square = num ** 2
cube = num ** 3

print("Square =", square)
print("Cube =", cube)

# Program to swap two numbers without third variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)

# Student Report Program

# Taking student details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Taking marks of 5 subjects
m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
m5 = float(input("Enter marks of Subject 5: "))

# Calculating total marks
total = m1 + m2 + m3 + m4 + m5

# Calculating percentage
percentage = total / 5

# Displaying report
print("\n----- STUDENT REPORT -----")
print("Student Name :", name)
print("Roll Number  :", roll_no)

print("Total Marks  :", total)
print("Percentage   :", percentage, "%")

if percentage >= 40:
    print("Result       : Pass")
else:
    print("Result       : Fail")

