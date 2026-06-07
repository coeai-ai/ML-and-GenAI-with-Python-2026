# 1. Find Area of Rectangle

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth
print("Area of Rectangle =", area)



# 2. Find Simple Interest

p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time (years): "))

sim = (p * r * t) / 100
print("Simple Interest =", sim)


# 3. Convert Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit =", fahrenheit)



# 4. Calculate Average of 3 Numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

average = (a + b + c) / 3

print("Average =", average)



# 5. Find Square and Cube of a Number

num = int(input("Enter a number: "))

square = num ** 2
cube = num ** 3

print("Square =", square)
print("Cube =", cube)


# 6. Swap Two Numbers Without Third Variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before Swapping")
print("a =", a)
print("b =", b)

a, b = b, a

print("After Swapping")
print("a =", a)
print("b =", b)



# 7. Student Report Program

# Taking Student Details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Taking Marks
marks1 = float(input("Enter marks of Subject 1: "))
marks2 = float(input("Enter marks of Subject 2: "))
marks3 = float(input("Enter marks of Subject 3: "))

# Calculating Total and Percentage
total = marks1 + marks2 + marks3
percentage = (total / 300) * 100

# Displaying Report
print("\nSTUDENT REPORT")
print("Name:", name)
print("Roll Number:", roll_no)
print("Subject 1 Marks:", marks1)
print("Subject 2 Marks:", marks2)
print("Subject 3 Marks:", marks3)
print("Total Marks:", total)
print("Percentage:", percentage, "%")





