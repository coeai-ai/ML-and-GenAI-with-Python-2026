#1- Area of Rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area of Rectangle =", area)

# 2- Find Simple Interest 

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (years): "))

simple_interest = (principal * rate * time) / 100
print("Simple Interest =", simple_interest)

# Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit =", fahrenheit)

# Average of 3 Numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print("Average =", average)

# Square and Cube of a Number

number = float(input("Enter a number: "))
square = number ** 2
cube = number ** 3
print("Square =", square)
print("Cube =", cube)

# Swap Two Numbers Without Third Variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before Swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After Swapping:")
print("a =", a)
print("b =", b)


# Student Report Program
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

english = float(input("Enter English Marks: "))
maths = float(input("Enter Maths Marks: "))
science = float(input("Enter Science Marks: "))
computer = float(input("Enter Computer Marks: "))
hindi = float(input("Enter Hindi Marks: "))

total = english + maths + science + computer + hindi

percentage = (total / 500) * 100

print("\n STUDENT REPORT-")
print("Name       :", name)
print("Roll No    :", roll_no)
print("English    :", english)
print("Maths      :", maths)
print("Science    :", science)
print("Computer   :", computer)
print("Hindi      :", hindi)
print("Total Marks:", total)
print("Percentage :", percentage, "%")
