# 1. Find Area of Rectangle

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print("Area of Rectangle =", area)


# 2. Find Simple Interest

p = float(input("\nEnter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))
si = (p * r * t) / 100
print("Simple Interest =", si)


# 3. Convert Celsius to Fahrenheit

celsius = float(input("\nEnter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit =", fahrenheit)


# 4. Calculate Average of 3 Numbers

a = float(input("\nEnter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
average = (a + b + c) / 3
print("Average =", average)


# 5. Find Square and Cube of a Number

num = int(input("\nEnter a number: "))
square = num ** 2
cube = num ** 3
print("Square =", square)
print("Cube =", cube)


# 6. Swap Two Numbers Without Third Variable

x = int(input("\nEnter first number: "))
y = int(input("Enter second number: "))
x, y = y, x
print("After swapping:")
print("x =", x)
print("y =", y)


# 7. Student Report Program

name = input("\nEnter Student Name: ")
roll_no = input("Enter Roll Number: ")

m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))

total = m1 + m2 + m3
percentage = total / 3

print("\n----- STUDENT REPORT -----")
print("Name :", name)
print("Roll No :", roll_no)
print("Total Marks :", total)
print("Percentage :", percentage, "%")