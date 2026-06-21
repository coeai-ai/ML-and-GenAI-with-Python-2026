# 1. Find Area of Rectangle

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth

print("Area of Rectangle =", area)


# 2. Find Simple Interest

P = float(input("\nEnter Principal Amount: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time (years): "))

SI = (P * R * T) / 100

print("Simple Interest =", SI)


# 3. Convert Celsius to Fahrenheit

celsius = float(input("\nEnter Temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit =", fahrenheit)


# 4. Calculate Average of 3 Numbers

num1 = float(input("\nEnter First Number: "))
num2 = float(input("Enter Second Number: "))
num3 = float(input("Enter Third Number: "))

average = (num1 + num2 + num3) / 3

print("Average =", average)


# 5. Find Square and Cube of a Number

number = float(input("\nEnter a Number: "))

square = number ** 2
cube = number ** 3

print("Square =", square)
print("Cube =", cube)


# 6. Swap Two Numbers Without Third Variable

a = int(input("\nEnter First Number: "))
b = int(input("Enter Second Number: "))

a, b = b, a

print("After Swapping:")
print("a =", a)
print("b =", b)


# 7. Student Report Program

print("\n----- Student Report -----")

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

marks1 = float(input("Enter Marks in Subject 1: "))
marks2 = float(input("Enter Marks in Subject 2: "))
marks3 = float(input("Enter Marks in Subject 3: "))

total = marks1 + marks2 + marks3
percentage = (total / 300) * 100

print("\n----- Report Card -----")
print("Name:", name)
print("Roll Number:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage, "%")