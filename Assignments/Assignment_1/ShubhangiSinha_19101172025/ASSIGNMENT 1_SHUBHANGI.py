19101172025
SHUBHANGI SINHA

#QUESTION 1
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print("Area of rectangle =", area)

#QUESTION 2
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time: "))
simple_interest = (principal * rate * time) / 100
print("Simple Interest =", simple_interest)

#QUESTION 3
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit =", fahrenheit)

#QUESTION 4
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print("Average =", average)

#QUESTION 5
number = float(input("Enter a number: "))
square = number ** 2
cube = number ** 3
print("Square =", square)
print("Cube =", cube)

#QUESTION 6
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a = a + b
b = a - b
a = a - b
print("After swapping:")
print("a =", a)
print("b =", b)

#QUESTION 7
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
mark1 = float(input("Enter marks of Subject 1: "))
mark2 = float(input("Enter marks of Subject 2: "))
mark3 = float(input("Enter marks of Subject 3: "))
total = mark1 + mark2 + mark3
percentage = total / 3
print("Student Name:", name)
print("Roll Number:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage)