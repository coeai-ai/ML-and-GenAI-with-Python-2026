#area of a rectangle 
length=int(input("enter length: "))
breadth=int(input("enter breadth: "))
area = length*breadth
print(area)

#simple interest
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))#in percentage
time = float(input("Enter Time : "))#in years

simple_interest = (principal * rate * time) / 100
print("Simple Interest =", simple_interest)

#celsius to fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit =", fahrenheit)

#average of 3 numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print("Average =", average)

#square and cube of a number 
num = int(input("Enter a number: "))
square = num ** 2
cube = num ** 3
print("Square =", square)
print("Cube =", cube)

#Swap two numbers without third variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)

#Create a Student Report Program that take student details using input(), Store marks in variables, Calculate total and percentage , Use comments, Use proper indentation
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

m1 = float(input("Enter marks in Subject 1: "))
m2 = float(input("Enter marks in Subject 2: "))
m3 = float(input("Enter marks in Subject 3: "))
# total marks
total = m1 + m2 + m3
# percentage
percentage = total / 3
# report
print("Name:", name)
print("Roll Number:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage, "%")