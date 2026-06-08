# ASSIGNMENT - 1
# Find the area of rectangle
len = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

Area = len*width
print("Area of Rectangle: ", Area)

#Find simple interest
P = float(input("Enter the Principal amount: "))
R = float(input("Enter the Rate of interest: "))
T = float(input("Enter the Time in years: "))

SI = (P * R * T) / 100

print("Simple Interest: ", SI)

# Convert temperature from Celcuis to Fahrenheit
C = float(input("Enter temperature in Celsius: "))
F = (C * 9/5) + 32

print(f"{C}°C is equal to {F}°F")

# Calculate average of 3 numbers
a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))

avg = (a + b + c) / 3

print(f"Average of {a}, {b} and {c} = {avg}")

# Find square and cube of a number
num=float(input("Enter the number: "))

square = num ** 2
cube = num ** 3

print(f"Square of {num} = {square}")
print(f"Cube of {num} = {cube}")

# Swap two numbers without third variable
n1 = float(input("Enter 1st number: "))
n2 = float(input("Enter 2nd number: "))

print(f"Original numbers: a = {n1}, b = {n2}")

n1, n2 = n2, n1

print(f"Swapped numbers: a = {n1}, b = {n2}")

'''Create a Student Report Program that takes student details using input(). Store marks in 
variables, calculate total and percentage. Use comments, Use proper indentation'''
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
course = input("Enter Course Name: ")

maths = float(input("Enter marks in Mathematics: "))
science = float(input("Enter marks in Science: "))
data_sturucture = float(input("Enter marks in Data Stuructures: "))

total = maths + science + data_sturucture
percentage = (total / 300) * 100  

print("\n---- Student Report ----")
print(f"Name: {name}")
print(f"Roll Number: {roll_no}")
print(f"Course: {course}")
print(f"Marks: Maths = {maths}, Science = {science}, English = {data_sturucture}")
print(f"Total Marks = {total}")
print(f"Percentage = {percentage}%")
