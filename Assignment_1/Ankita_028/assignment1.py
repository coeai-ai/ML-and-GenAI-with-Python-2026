# Find area of rectangle
length = float(input("Enter the length of the rectangle:"))
breadth = float(input("Enter the breadth of the rcetangle:"))
area = length * breadth
print("The area of rectangle (in m^2) is: ",area)

#Find simple interest
principal = float(input("Enter principal amount: "))
rate = float(input("Enter the annual interest rate(in %): "))
time = float(input("Enter the time(in years): "))
simple_interest = (principal * rate * time)/100
print("The required simple interest is ",simple_interest)

#Convert temperature from Celcius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")

#Calculate average of 3 numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
average = (a + b + c)/3
print("the averag eof the three numbers is ",average)

#Find square and cube of a number
num = float(input("Enter a number: "))
square = num ** 2
cube = num ** 3
print("Square of number is ",square)
print("Cube of number is ",cube)

#Swap two numbers without third variable
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print(f"Befire swapping: a = {a}, b = {b} ")
a,b = b,a
print(f"After swapping: a = {a}, b = {b} ")

#Student Report Program
student_name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")
class_name = input("Enter Class: ")
print("Enter marks for 3 subjects!(out of 100)")
math = float(input("Mathematics: "))
science = float(input("Science: "))
english = float(input("English: "))
total_marks = math + science + english
percentage = total_marks/300

print(".           REPORT CARD           ")
print("Name: ",student_name)
print("Roll No: ",roll_number)
print("Class: ",class_name)
print("Total Marks: ",total_marks)
print("Percentage(in %): ",percentage)

