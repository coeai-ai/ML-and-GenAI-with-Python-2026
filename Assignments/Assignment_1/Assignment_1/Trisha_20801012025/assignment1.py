# Question 1: Find area of rectangle

print("\\nQuestion 1: Area of Rectangle")

length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))

area = length * breadth

print("Area of rectangle =", area)


# Question 2: Find simple interest

print("\\nQuestion 2: Simple Interest")

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)


# Question 3: Convert temperature from Celsius to Fahrenheit

print("\\nQuestion 3: Celsius to Fahrenheit")

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit =", fahrenheit)


# Question 4: Calculate average of 3 numbers

print("\\nQuestion 4: Average of Three Numbers")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print("Average of three numbers =", average)


# Question 5: Find square and cube of a number

print("\\nQuestion 5: Square and Cube")

num = float(input("Enter a number: "))
square = num ** 2
cube = num ** 3

print("Square of the number =", square)
print("Cube of the number =", cube)


# Question 6: Swap two numbers without third variable

print("\\nQuestion 6: Swap Two Numbers Without Third Variable")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping:")
print("a =", a)
print("b =", b)

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)


# Question 7: Student Report Program

print("\\nQuestion 7: Student Report Program")

# Taking student details as input
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
course = input("Enter course name: ")

# Taking marks of five subjects
marks1 = float(input("Enter marks of Subject 1: "))
marks2 = float(input("Enter marks of Subject 2: "))
marks3 = float(input("Enter marks of Subject 3: "))
marks4 = float(input("Enter marks of Subject 4: "))
marks5 = float(input("Enter marks of Subject 5: "))

# Calculating total marks and percentage
total = marks1 + marks2 + marks3 + marks4 + marks5
percentage = (total / 500) * 100

# Displaying student report
print("\\n----- Student Report -----")
print("Name:", name)
print("Roll Number:", roll_no)
print("Course:", course)
print("Total Marks:", total)
print("Percentage:", percentage, "%")

