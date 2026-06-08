# 1) Find Area of Rectangle

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth
print("Area of Rectangle =", area)


# 2) Find Simple Interest

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time: "))

si = (principal * rate * time) / 100
print("Simple Interest =", si)


# 3) Convert Celsius to Fahrenheit

celsius = float(input("Enter Temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit =", fahrenheit)


# 4) Calculate Average of 3 Numbers

a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))
c = float(input("Enter Third Number: "))

average = (a + b + c) / 3
print("Average =", average)


# 5) Find Square and Cube of a Number

num = float(input("Enter a Number: "))

square = num ** 2
cube = num ** 3

print("Square =", square)
print("Cube =", cube)


# 6) Swap Two Numbers Without Third Variable

x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))

x, y = y, x

print("After Swapping:")
print("First Number =", x)
print("Second Number =", y)


# 7) Student Report 

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

english = float(input("Enter English Marks: "))
maths = float(input("Enter Maths Marks: "))
science = float(input("Enter Science Marks: "))

total = english + maths + science

percentage = (total / 300) * 100

print("\n----- STUDENT REPORT -----")
print("Name:", name)
print("Roll Number:", roll_no)
print("English:", english)
print("Maths:", maths)
print("Science:", science)
print("Total Marks:", total)
print("Percentage:", percentage, "%")