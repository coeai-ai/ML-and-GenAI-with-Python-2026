# 1.Aim-Find area of rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area of rectangle =", area)


# 2.Aim-Find simple interest
p = float(input("Enter Principal: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time(in years): "))
simple_interest = (p * r * t) / 100
print("Simple Interest =", simple_interest)


# 3.Aim-Convert temperature from Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit =", fahrenheit)


# 4.Aim-Calculate average of 3 numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
average = (a + b + c) / 3
print("Average =", average)


# 5.Aim-Find square and cube of a number
num = float(input("Enter a number: "))
square = num ** 2
cube = num ** 3
print("Square =", square)
print("Cube =", cube)


# 6.Aim-Swap two numbers without third variable
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
# Swapping
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)


# 7.Aim-Create a Student Report Program that take student details using input(), Store marks in variables, Calculate total and percentage , Use comments, Use proper indentation
#Student details
print("Enter Student Details ")
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Input marks of Student
print("Enter marks (out of 100) ")
m1 = float(input("Enter marks in Subject 1: "))
m2 = float(input("Enter marks in Subject 2: "))
m3 = float(input("Enter marks in Subject 3: "))

# Calculating total and percentage
TotalMarks = m1 + m2 + m3
MaxMarks=300
percentage = (TotalMarks / MaxMarks) * 100

# Displaying report
print("\n----- Student Report -----")
print("Name:", name)
print("\nSubject Scores")
print("Subject 1: ",m1)
print("Subject 2: ",m2)
print("Subject 3: ",m3)
print("Roll No:", roll_no)
print("Total Marks:",TotalMarks ,"/",MaxMarks)
print("Percentage:", percentage, "%")