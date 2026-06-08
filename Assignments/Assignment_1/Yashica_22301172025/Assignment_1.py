Name: Yashica 
enrollment number:22301172025
college: IGDTUW 


# 1. Find Area of Rectangle

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth

print("Area of Rectangle =", area)


# 2. Find Simple Interest

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (in years): "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)


# 3. Convert Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit =", fahrenheit)


# 4. Calculate Average of 3 Numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print("Average =", average)


# 5. Find Square and Cube of a Number

number = int(input("Enter a number: "))

square = number ** 2
cube = number ** 3

print("Square =", square)
print("Cube =", cube)


# 6. Swap Two Numbers Without Third Variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before Swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After Swapping:")
print("a =", a)
print("b =", b)


# 7. Student Report Program

# Taking student details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Taking marks
mark1 = float(input("Enter marks in Subject 1: "))
mark2 = float(input("Enter marks in Subject 2: "))
mark3 = float(input("Enter marks in Subject 3: "))

# Calculating total marks
total = mark1 + mark2 + mark3

# Calculating percentage
percentage = total / 3

# Displaying report
print("\n------ STUDENT REPORT ------")
print("Student Name :", name)
print("Roll Number  :", roll_no)
print("Subject 1 Marks :", mark1)
print("Subject 2 Marks :", mark2)
print("Subject 3 Marks :", mark3)
print("Total Marks :", total)
print("Percentage :", percentage, "%")
print("----------------------------")
