# 1. Area of rectangle
print("=== Area of Rectangle ===")
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
print("Area of rectangle:", length * breadth)


# 2. Simple interest
print("\n=== Simple Interest ===")
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time (years): "))
print("Simple Interest:", (p * r * t) / 100)


# 3. Celsius to Fahrenheit
print("\n=== Celsius to Fahrenheit ===")
celsius = float(input("Enter temperature in Celsius: "))
print("Fahrenheit:", (celsius * 9 / 5) + 32)


# 4. Average of 3 numbers
print("\n=== Average of 3 Numbers ===")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
print("Average:", (a + b + c) / 3)


# 5. Square and cube of a number
print("\n=== Square and Cube ===")
n = float(input("Enter a number: "))
print("Square:", n ** 2)
print("Cube:", n ** 3)


# 6. Swap two numbers without third variable
print("\n=== Swap Two Numbers ===")
x = int(input("Enter x: "))
y = int(input("Enter y: "))
x, y = y, x
print("After swap: x =", x, ", y =", y)


# 7. Student Report Program
print("\n=== Student Report ===")
# Take student details
name = input("Enter student name: ")
roll = input("Enter roll number: ")

# Store marks in variables
marks1 = float(input("Enter marks in subject 1: "))
marks2 = float(input("Enter marks in subject 2: "))
marks3 = float(input("Enter marks in subject 3: "))

# Calculate total and percentage
total = marks1 + marks2 + marks3
percentage = total / 3

# Display report
print("\n--- Student Report ---")
print("Name:", name)
print("Roll Number:", roll)
print("Total Marks:", total)
print("Percentage:", percentage, "%")