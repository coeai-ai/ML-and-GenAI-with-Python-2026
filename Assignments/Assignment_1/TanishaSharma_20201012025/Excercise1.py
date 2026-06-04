# 1 Find area of rectangle.
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth

print("Area of rectangle =", area)


# 2 Find simple interest.
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (%): "))
time = float(input("Enter Time (years): "))
si = (principal * rate * time) / 100

print("Simple Interest =", si)


# 3 Convert temperature from Celsius to Fahrenheit.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32;
print("Temperature in Fahrenheit =", fahrenheit)


# 4 Calculate average of 3 numbers.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
avg = (num1 + num2 + num3) / 3

print("Average =", avg)


# 5 Find square and cube of a number.
num = float(input("Enter a number: "))
square = num ** 2
cube = num ** 3

print("Square =", square)
print("Cube =", cube)


# 6 Swap two numbers without third variable.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)


# 7 Create a Student Report Program that take student details using input(), Store marks in variables, Calculate total and percentage , Use comments, Use proper indentation

# Input student details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Input marks of 3 subjects
marks1 = float(input("Enter marks in Subject 1: "))
marks2 = float(input("Enter marks in Subject 2: "))
marks3 = float(input("Enter marks in Subject 3: "))

# Calculate total marks
total = marks1 + marks2 + marks3

# Calculate percentage
percentage = (total / 300) * 100

# Display report
print("\n STUDENT REPORT")
print("Student Name :", name)
print("Roll Number  :", roll_no)
print("Marks Subject 1 :", marks1)
print("Marks Subject 2 :", marks2)
print("Marks Subject 3 :", marks3)
print("Total Marks :", total)
print("Percentage :", percentage, "%")