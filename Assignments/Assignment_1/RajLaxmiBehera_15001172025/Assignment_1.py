"""ASSIGNMENT 1"""

# Find area of rectangle
length=20
breadth=10
area=length*breadth
print("Area of rectangle with length 20 and breadth 10 is:",area)

# Find simple interest
P=100 #principle amount
R=2 # rate in percentage
T=2 #time in years
SI=(P*R*T)/100
print("Simple interest calculated is:",SI)

# Convert tempreture from Celsius to Fahrenheit
C = 35 # temperature in Celsius
F = (C * 9/5) + 32
print("Temperature in Fahrenheit is: ", F)

# Calculate average of three numbers
num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
num3=int(input("Enter 3rd number:"))
avg=(num1+num2+num3)/3
print("Average of entered number is:",avg)

# Find Square and cube of a number
num = int(input("Enter a number: "))    
square = num ** 2
cube = num ** 3
print("Square of the number is: ", square)
print("Cube of the number is: ", cube)

# Swap two numbers without using third variable
a = 10
b = 20
a = a + b
b = a - b
a = a - b
print("After swapping, first number is: ", a)
print("After swapping, second number is: ", b)

# Create a Student Report Program, Store marks in variables, Calculate total and percentage
name=input("Enter student name:")
roll=int(input("Enter student's roll number:"))
print("Enter marks out of 100\n")
marks1=float(input("Enter marks of first subject:"))
marks2=float(input("Enter marks of second subject:"))
marks3=float(input("Enter marks of third subject"))
total=marks1+marks2+marks3
perc=(total/300)*100
print("Total marks are:",total)
print("Percentage is:",perc)